# Scientific supplement for DAG-PMHC-01 through DAG-PMHC-03

Three computationally designed protein candidates target KRAS G12D peptide VVVGADGVGK presented by HLA-A*11:01 and beta-2 microglobulin. The matched WT peptide is VVVGAGGVGK. Read SUMMARY.md for the candidate rationale, METHODS.md for the protocol and CONFIDENCE-METRICS.md for predicted confidence across target contexts.

Only the three sequences in designs.fasta are submitted entries. Names ending in `-parent` identify unchanged computational comparators for DAG-PMHC-01 and DAG-PMHC-02; they are not experimental positive controls or additional entries.

## Evidence coverage

| Evidence | Submitted candidates | Parent comparators |
|---|---:|---:|
| Boltz2 complex predictions | 36 | 24 |
| Chemistry records | 36 | 24 |
| Stability-head records | 36 | 24 |
| Completed local-minimization starting poses | 15 | 8 |
| Prepared, restrained and released structure files | 45 | 24 |

There are **129 indexed structures**, plus two parent conditioning templates and three target-only generation inputs under `design/`. The five molecular identities each have four cofold seeds in each of mutant, WT and peptide-removed contexts. Stability records cover four mutant conformations evaluated by three related heads per identity.

DAG-PMHC-03 initially had eleven completed cofold predictions and one lost WT attempt. That exact WT seed was subsequently recovered in a separately recorded phase, using the same H200 GPU class and pinned runtime but a different physical GPU. Its cofold and chemistry records carry `evidence_phase: separate_recovery`. The logical coverage is twelve; the original lost attempt is not relabeled completed. The frozen relaxation panel used four mutant and three WT starting poses for this candidate; the recovered WT prediction was not substituted or relaxed. Its unavailable relaxation slot remains in the slot table and `data/DAG-PMHC-03-coverage.json`.

DAG-PMHC-02 and its parent each completed all eight mutant/WT relaxation slots. DAG-PMHC-01 and its parent were not relaxed. Thus the included relaxation scope is 23 completed of 24 nominal slots. No completed output within this scope was excluded. The broader experiment completed 47 of 48 slots across six identities.

## Files

- `identities.json` and `designs.fasta`: exact sequences, hashes, lengths and entry/comparator status.
- `structure-index.csv`: molecule, context, seed, stage, relative file path and hash for each indexed structure.
- `structures/<molecule>/cofold/`: Boltz2 predictions; `relaxation/`: prepared, restrained and released derivatives.
- `design/`: sequence-revision settings and parent conditioning templates, plus DAG-PMHC-03 generation settings, target inputs, seeds and weight hashes. Target-only generation inputs are not candidate complex predictions. No selected all-atom generation structure is supplied for DAG-PMHC-03.
- `tables/confidence-summary.csv`: all five identities and three contexts, with four-seed means and ranges. `CONFIDENCE-METRICS.md` is its readable version.
- `tables/chemistry.csv`: burial, half-delta interface area, isolated apolar surface and recipe-assigned peptide hydrogen-bond counts for every complex.
- `tables/stability.csv`: every head mean, with identity, seed and head index.
- `tables/relaxation-*.csv`: all relevant slots, stage displacements, contact statistics and predefined atom-pair geometry, including Cartesian and periodic-image conventions.
- `data/`: detailed cofold, chemistry, stability and pose-comparison observations.
- `MANIFEST.json`: sizes and SHA256 hashes of all supplement files, excluding the manifest itself.

## Data conventions

Chain A is HLA, B beta-2 microglobulin, C peptide and D binder. `mutant_bound` uses VVVGADGVGK, `wildtype_bound` uses VVVGAGGVGK and `peptide_removed` omits C. Residue numbers are one-based within each chain. Sequence-design decoding orders index their separate residue-mapping arrays from zero; designable and fixed positions are one-based binder positions. Conditioning templates retain the parent sequence.

Distances and RMSDs use angstroms; surfaces use square angstroms. Burial holds coordinates fixed while removing the partner. Half-delta interface area is half the sum of the partners' surface losses. The binder is chain D and the target comprises A, B and C (A and B when peptide is removed). Beta-2 microglobulin contributes zero binder-interface burial in all 60 retained complexes; the summary table therefore lists peptide, HLA and binder contributions. Missing peptide fields mean not applicable, not zero. Placement RMSD aligns HLA first; intrinsic RMSD aligns the binder itself.

Binder pLDDT is converted from 0–1 to 0–100 in the summary. Pair-iPTM uses the recorded position/frame convention; PAE blocks are directional. Confidence ranges describe variation across model seeds, not experimental confidence intervals. Cofold PDB B-factors store predictor confidence, not thermal motion; prepared/minimized PDBs do not retain that meaning.

Stability outputs retain the model's `kcal_mol` label. Higher is the favorable direction of this learned stability diagnostic; this is not the sign convention for binding free energy. Related heads are correlated, and `ddg_scanning: false` means no mutation-by-mutation scan was performed. The 120-residue candidate exceeds the cited model validation length range.

Recipe hydrogen bonds require donor–acceptor separation >1 and ≤3 Å and donor–hydrogen–acceptor angle >150 degrees under the prepared protonation state. Counts can include short overlapping contacts; atom identities and geometry are retained to inspect these assignments. Counts are cutoff-dependent. Local-relaxation tables use saved double-precision coordinates, whereas PDB coordinates are rounded. `all_bonded_H_geometry` is a JSON array within CSV, preserving every bonded hydrogen.

The peptide-removed construct has an emptied groove, and minimization explores local predicted docking basins. Neither establishes physiological peptide dependence or equilibrium affinity. Separate candidate-family batches, common model assumptions and adaptive selection limit performance inference. Experimental binding and production measurements remain to be made.

## Provenance

Structure bytes are unchanged from retained calculations. Public identifiers and portable paths replace development identifiers; scientific values retain their source precision. The supplement covers the selected candidates and two direct parent comparisons, including all available contexts and contrary observations. It is not a complete campaign inventory or a hit-rate estimate.
