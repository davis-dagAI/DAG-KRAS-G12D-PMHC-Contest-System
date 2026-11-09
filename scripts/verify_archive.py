"""Read-only integrity and identity checks for the published contest archive."""

import argparse
import csv
import hashlib
import json
import stat
import sys
import zipfile
from collections import Counter
from pathlib import Path, PurePosixPath


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def rows(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


def safe_file(root, name):
    rel = PurePosixPath(name)
    require(not rel.is_absolute() and ".." not in rel.parts, f"unsafe path: {name}")
    path = root.joinpath(*rel.parts)
    require(root.resolve() in path.resolve().parents, f"path outside root: {name}")
    require(not path.is_symlink() and path.is_file(), f"not a regular file: {name}")
    return path


def verify(root):
    supplement = root / "supplement"
    submission = read_json(root / "SUBMISSION.json")
    for name, item in submission["submission_files"].items():
        path = safe_file(root, name)
        require(path.stat().st_size == item["bytes"], f"size mismatch: {name}")
        require(sha(path) == item["sha256"], f"hash mismatch: {name}")

    manifest = read_json(supplement / "MANIFEST.json")
    actual = set()
    for path in supplement.rglob("*"):
        require(not path.is_symlink(), f"symlink: {path.name}")
        require(path.is_dir() or path.is_file(), f"special file: {path.name}")
        if path.is_file():
            actual.add(path.relative_to(supplement).as_posix())
    require(actual == set(manifest) | {"MANIFEST.json"}, "supplement membership mismatch")
    for name, item in manifest.items():
        path = safe_file(supplement, name)
        require(path.stat().st_size == item["bytes"], f"size mismatch: {name}")
        require(sha(path) == item["sha256"], f"hash mismatch: {name}")
    with zipfile.ZipFile(root / "SUPPLEMENT.zip") as archive:
        require(len(archive.namelist()) == len(actual), "ZIP duplicate or extra member")
        require(set(archive.namelist()) == actual, "ZIP membership mismatch")
        for item in archive.infolist():
            require(not item.is_dir(), f"unexpected ZIP directory: {item.filename}")
            require(not stat.S_ISLNK(item.external_attr >> 16), "ZIP symlink")
            path = safe_file(supplement, item.filename)
            require(archive.read(item) == path.read_bytes(), f"ZIP byte mismatch: {item.filename}")

    identities = read_json(supplement / "identities.json")
    sequences = {x["molecule"]: x["sequence"] for x in identities}
    require(len(identities) == len(sequences) == 5, "identity denominator")
    selected = [x for x in identities if x["submitted"]]
    require([x["molecule"] for x in selected] == submission["submitted_order"], "entry order")
    for item in identities:
        sequence = item["sequence"]
        require(len(sequence) == item["length"], "sequence length")
        require(set(sequence) <= set("ACDEFGHIKLMNPQRSTVWY"), "nonstandard sequence")
        require(
            hashlib.sha256(sequence.encode()).hexdigest() == item["sequence_sha256"],
            "sequence hash",
        )
    fasta = "".join(f">{x['molecule']}\n{x['sequence']}\n" for x in selected)
    require((root / "designs.fasta").read_text() == fasta, "FASTA identity/order")
    require((supplement / "designs.fasta").read_text() == fasta, "supplement FASTA")
    for name in ("METHODS.md", "SUMMARY.md"):
        require(
            (root / name).read_bytes() == (supplement / name).read_bytes(), f"copy differs: {name}"
        )

    amino = dict(
        zip(
            [
                "ALA",
                "ARG",
                "ASN",
                "ASP",
                "CYS",
                "GLN",
                "GLU",
                "GLY",
                "HIS",
                "ILE",
                "LEU",
                "LYS",
                "MET",
                "PHE",
                "PRO",
                "SER",
                "THR",
                "TRP",
                "TYR",
                "VAL",
            ],
            "ARNDCQEGHILKMFPSTWYV",
            strict=True,
        )
    )
    amino.update(HID="H", HIE="H", HIP="H", CYX="C")
    index = rows(supplement / "structure-index.csv")
    require(len(index) == len({x["file"] for x in index}) == 129, "structure denominator")
    for item in index:
        path = safe_file(supplement, item["file"])
        require(sha(path) == item["sha256"], f"structure hash: {item['file']}")
        residues = {}
        for line in path.read_text().splitlines():
            if line.startswith("ATOM  ") and line[21] == "D":
                key = line[22:27]
                aa = amino[line[17:20]]
                require(key not in residues or residues[key] == aa, "conflicting residue identity")
                residues[key] = aa
        require(
            "".join(residues.values()) == sequences[item["molecule"]],
            f"binder identity: {item['file']}",
        )
    require(
        Counter(x["stage"] for x in index)
        == {
            "cofold": 60,
            "prepared": 23,
            "restrained": 23,
            "released": 23,
        },
        "stage coverage",
    )
    for table in ("chemistry", "stability"):
        require(len(rows(supplement / f"tables/{table}.csv")) == 60, f"{table} coverage")
    slots = rows(supplement / "tables/relaxation-slots.csv")
    require(len(slots) == len({x["slot"] for x in slots}) == 24, "relaxation slot denominator")
    require(sum(x["completed"] == "True" for x in slots) == 23, "relaxation completed count")
    return {
        "verified": True,
        "supplement_files": len(actual),
        "indexed_structures": len(index),
        "submitted_designs": len(selected),
        "relaxation_completed": 23,
        "relaxation_planned": 24,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(json.dumps(verify(args.root.resolve()), indent=2))
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as error:
        print(f"Archive verification failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
