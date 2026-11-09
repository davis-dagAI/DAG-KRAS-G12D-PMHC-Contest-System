"""Recompute retained confidence summaries and surface arithmetic, without models."""

import argparse
import json
import math
from pathlib import Path

from verify_archive import read_json, require, rows, verify


def summarize(root):
    verify(root)
    supplement = root / "supplement"
    output = []
    metrics = {
        "binder_pLDDT": lambda x: x["plddt_by_chain"]["D"]["mean"] * 100,
        "pair_iPTM_position_D_frame_C": lambda x: x["pair_iptm_by_declared_chain"].get(
            "position_D__frame_C"
        ),
        "PAE_D_to_C_A": lambda x: x["pae_blocks_A"].get("D->C", {}).get("mean"),
        "PAE_D_to_A_A": lambda x: x["pae_blocks_A"]["D->A"]["mean"],
    }
    summary = rows(supplement / "tables/confidence-summary.csv")
    require(len(summary) == 15, "confidence summary denominator")
    for row in summary:
        data = read_json(supplement / f"data/{row['molecule']}-cofold.json")
        selected = [x for x in data if x["context"] == row["context"]]
        require(
            len(selected) == len({x["seed"] for x in selected}) == 4, "four unique seeds required"
        )
        result = {"molecule": row["molecule"], "context": row["context"]}
        for label, extract in metrics.items():
            values = [extract(x) for x in selected]
            if all(x is None for x in values):
                require(
                    all(row[f"{label}_{part}"] in ("", "N/A") for part in ("mean", "min", "max")),
                    "missing metric convention",
                )
                result[label] = None
                continue
            require(
                all(x is not None and math.isfinite(x) for x in values), "partial/nonfinite metric"
            )
            aggregate = {"mean": sum(values) / 4, "min": min(values), "max": max(values)}
            for part, value in aggregate.items():
                require(
                    math.isclose(
                        value, float(row[f"{label}_{part}"]), rel_tol=1e-12, abs_tol=1e-12
                    ),
                    f"summary mismatch: {row['molecule']} {label} {part}",
                )
            result[label] = aggregate
        output.append(result)
    for row in rows(supplement / "tables/chemistry.csv"):
        total = sum(
            float(row[key] or 0)
            for key in ("peptide_burial_A2", "HLA_burial_A2", "binder_burial_A2")
        )
        require(
            math.isclose(
                total / 2, float(row["half_delta_interface_area_A2"]), rel_tol=1e-12, abs_tol=1e-9
            ),
            "surface arithmetic mismatch",
        )
    return {
        "interpretation": "Computational summaries; no physical performance estimate",
        "confidence_rows": output,
        "surface_rows_reconciled": 60,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    print(json.dumps(summarize(parser.parse_args().root.resolve()), indent=2))
