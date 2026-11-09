# DAG KRAS G12D pMHC Contest System

An open archive of three protein-design hypotheses submitted to Track 3 of the 2026 Anthropic × Adaptyv competition, Challenge 5. It documents how the candidates were generated, revised, compared and selected, and makes the supporting computational results inspectable.

The target is the KRAS G12D peptide **VVVGADGVGK** presented by **HLA-A*11:01** and beta-2 microglobulin. The design problem is to recognize the mutant complex while distinguishing the wild-type peptide **VVVGAGGVGK** and peptide-free HLA. Mutation specificity, peptide dependence and affinity are the experimental objectives.

**Status:** submission reported complete on November 9, 2026. All three exact sequences passed the platform's pre-submission Novelty Check. Selection for laboratory testing and experimental results are not yet available. The archived evidence is computational.

## Start here

- [Methods](METHODS.md): objective, generation, revision, assessment and selection rationale.
- [Candidate summary](SUMMARY.md): observations supporting each hypothesis and the unresolved comparisons.
- [Confidence metrics](CONFIDENCE-METRICS.md): matched mutant, WT and peptide-removed predictions.
- [Workflow](docs/WORKFLOW.md): what each tool contributed and how the loop worked.
- [Reproduce the archive checks](docs/REPRODUCIBILITY.md): verify identities, hashes, coverage and reported arithmetic locally.
- [Scientific supplement](supplement/README.md): all retained selected-lineage structures, settings and detailed tables.

## The three submitted hypotheses

| Submitted order | Design | Length | Question for experiment |
|---|---|---:|---|
| 1 | DAG-PMHC-01 | 120 aa | Does more coherent placement over the mutant peptide support recognition through peptide-groove shape? |
| 2 | DAG-PMHC-02 | 80 aa | Does the modeled binder Arg72–peptide Asp6 interaction distinguish mutant binding from WT backbone accommodation? |
| 3 | DAG-PMHC-03 | 80 aa | Do alternative contacts near Gly9 recognize mutation-dependent peptide presentation? |

The exact sequences are in [designs.fasta](designs.fasta). Identifiers ending in `-parent` are the original computational designs used as comparators for the first two entries. They were not submitted and are not experimental positive controls. Names are consistent across sequences, structures and tables.

## What is included

The selected-lineage supplement contains 60 complex predictions across five identities and three contexts, 60 chemistry records, 60 stability-head records and 69 preparation/minimization derivatives. These account for 129 indexed structures. The local-minimization panel has 23 completed starting poses out of 24 planned. Two conditioning templates and three target-only generation inputs are separately labeled.

All 171 members of [SUPPLEMENT.zip](SUPPLEMENT.zip) are also available unpacked under `supplement/`. The submitted files are preserved byte-for-byte; archive documentation and verification tools were added afterward. [SUBMISSION.json](SUBMISSION.json) records their hashes and the source of the submission-status statement. No platform submission receipt is included.

This repository covers the public contest workflow and selected results. It is not the full campaign inventory or the broader drug-discovery platform. Model weights, upstream scientific engines, private orchestration code, infrastructure configuration, internal review conversations and unrelated research are not distributed here. The [reproducibility guide](docs/REPRODUCIBILITY.md) distinguishes checks runnable from this archive from full scientific regeneration.

## Verify locally

Requires Python 3.10 or newer; no model download, GPU, network access or third-party Python package is needed.

```bash
git clone https://github.com/davis-dagAI/DAG-KRAS-G12D-PMHC-Contest-System.git
cd DAG-KRAS-G12D-PMHC-Contest-System
python3 scripts/verify_archive.py
python3 scripts/summarize_results.py
```

The first command verifies the archived files, exact sequence joins and coverage. The second recomputes the confidence summaries from the retained per-seed data. These checks establish the integrity and arithmetic of the archive; the competition's measurements will test the molecular hypotheses.

## Reuse and attribution

Our original code and documentation are released under the [MIT License](LICENSE). The included campaign-generated data may also be reused under that permission to the extent of our rights. Third-party tools, model weights, reference structures and competition-platform records retain their own terms; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). No upstream code or weights are bundled.

For citation, use the repository URL and the commit or release identifier you inspected. The scientific methods credit the public tools used. [Archive policy](docs/ARCHIVE-POLICY.md) describes how corrections and future experimental results will be distinguished from the submitted evidence.

Official context: [challenge and rules](https://proteinbase.com/competitions/anthropic-adaptyv-2026/challenges/pmhc), [selection procedure](https://proteinbase.com/competitions/anthropic-adaptyv-2026/selection).
