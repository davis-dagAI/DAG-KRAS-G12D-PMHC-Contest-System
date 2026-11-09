# Reproducing the archive checks

This repository provides a portable evidence archive with a runnable reader. It does not bundle the private campaign controller or the scientific model environments.

## Available without scientific engines

Run `python3 scripts/verify_archive.py` from the repository root. It checks the submitted-file hashes, exact ZIP membership and bytes, all supplement-manifest entries, sequence hashes and FASTA order, every indexed PDB's chain-D sequence, table coverage and the completed/unavailable relaxation denominator.

Run `python3 scripts/summarize_results.py` to reproduce the four-seed confidence means and ranges from `supplement/data/*-cofold.json` and compare them with the published table. It also checks half-delta burial arithmetic in the chemistry table. The output is descriptive computational data, not a new score or selection policy.

Both readers use Python's standard library. They never launch a model, access an account, download data or alter the archived evidence. Runtime failures return nonzero. The file hashes identify bytes, not an external timestamp or physical validity.

## Scientific regeneration

[METHODS.md](../METHODS.md) records prediction and minimization settings. `supplement/design/` records available generation/revision configurations, checkpoint hashes and conditioning inputs. Upstream scientific software and weights must be obtained separately under their own licenses. The full private orchestration implementation, all intermediate generation trajectories and a selected all-atom generation structure for DAG-PMHC-03 are not included. Therefore these files support inspection and reconstruction of the disclosed protocol, not a promise of one-command or bit-identical full campaign regeneration.

Structures and table fields retain their original precision. PDB coordinates are rounded; some local-geometry tables derive from higher-precision coordinates. Do not expect exact numerical identity when recomputing those distances from a rounded PDB. Chain mappings, units, directional confidence conventions and missing-value meanings are in [the supplement guide](../supplement/README.md).

## Coverage

The supplement contains the three submitted sequences and two original-design comparators. It has 60 cofold predictions, 60 chemistry rows and 60 stability-head rows. Local minimization covered DAG-PMHC-02 and its comparator in all eight mutant/WT starting poses each, plus seven poses for DAG-PMHC-03. Its fourth WT cofold was recovered separately but was not relaxed. DAG-PMHC-01 was not in that minimization panel.

This is the selected-lineage package, not an unbiased sample of the entire campaign. Further evaluations should retain this distinction and use separate physical endpoints for production, binding and discrimination.
