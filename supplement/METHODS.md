# Computational Design of Three Candidates for Mutation-Specific KRAS G12D pMHC Recognition

## Objective and Design Strategy

We submit three de novo proteins, `DAG-PMHC-01` (120 aa), `DAG-PMHC-02` (80 aa), and `DAG-PMHC-03` (80 aa), targeting the KRAS G12D peptide `VVVGADGVGK` presented by `HLA-A*11:01` and beta-2 microglobulin (b2m), versus wild-type (WT) `VVVGAGGVGK` (Gly6 to Asp6). Our objective was to distinguish these closely related peptide–HLA surfaces while avoiding recognition of HLA alone. The three candidates test complementary approaches: peptide-groove shape recognition, direct Asp6 side-chain recognition, and recognition of peptide-backbone presentation near Gly9.

Our methodology combines four elements: (1) multi-context counter-design pairing mutant attraction against WT and peptide-removed counter-objectives; (2) protected-network revision holding recognition motifs fixed while redesigning framework or surface positions and benchmarking against unchanged original designs in fresh co-folding; (3) matched four-seed evaluation across mutant, WT, and peptide-removed contexts; and (4) two-stage local energy minimization examining local polar-contact geometry and WT rearrangements. No candidate started from a known experimentally validated binder. Submitted sequences contain no added tags and were not manually edited after assessment. All three passed the platform's pre-submission Novelty Check.

## Candidate Generation and Sequence Revision

`DAG-PMHC-01` and `DAG-PMHC-02` were created by generating an initial design and applying a targeted revision with pretrained ProteinMPNN (`v_48_020`, unmodified weights); unchanged original designs (`-parent` identifiers) serve as comparators. `DAG-PMHC-03` was generated de novo in one stage.

- **`DAG-PMHC-01`:** Generated with [RFD4-Proteina](https://github.com/RosettaCommons/RFD4-Proteina/tree/68058693cb88762a8aaf806571e13b291ce6318a) (`68058693cb88762a8aaf806571e13b291ce6318a`), retaining immune-receptor-like framework features. Conditioned on a predicted mutant complex of the original design, ProteinMPNN sampled eight designable positions while protecting a predefined peptide-facing network. Six substitutions resulted: `Q27D`, `E50V`, `K53E`, `T55Q`, `E57A`, `Q58P`.
- **`DAG-PMHC-02`:** Generated with an adapted [Odin-Multi](https://github.com/DigBioLab/odin_multi/tree/e4567e487d43a4de36524f491e51ad1ea9730d1e) (`e4567e487d43a4de36524f491e51ad1ea9730d1e`) and ColabDesign workflow combining AlphaFold2-based mutant attraction with WT and peptide-removed counter-objectives and ProteinMPNN guidance. Fixed-weight ProteinMPNN revision preserved the modeled recognition region, including Asp6-facing binder Arg72, and applied a -0.05 bias against `A/F/I/L/M/V/W` at 19 selected positions (`A9E`, `A19T`).
- **`DAG-PMHC-03`:** Generated in the adapted Odin-Multi/ColabDesign workflow using soluble ProteinMPNN `v_48_020` (80 residues, seed `958783`, iteration 139 discrete output), pairing mutant attraction (gradient weight `1.0`, peptide-backbone oxygen hotspots at positions 5–7) against WT (`0.3`) and peptide-free (`0.01`) counter-objectives. The selected all-atom generation structure was not retained; assessment used fresh Boltz2 predictions.

## Multi-Context Assessment and Local Geometry Protocols

Each candidate and comparator was folded across four matched seeds in mutant pMHC, WT pMHC, and a peptide-removed construct omitting chain C (36 candidate and 24 comparator complexes). Boltz2 (`boltz2_conf.ckpt`) used 3 recycles, 200 sampling steps, 1 sample/seed, and empty MSAs (A=HLA, B=b2m, C=peptide, D=binder). Pairwise binder placement RMSD was computed after aligning HLA chain A, separately from internal fold agreement.

|Candidate|Contexts|Binder pLDDT|Pair-iPTM|Binder→peptide PAE (Å)|
|---|---|---:|---:|---:|
|DAG-PMHC-01|Mutant/WT/Peptide-free|93.5/92.9/88.9|0.474/0.463/N/A|13.24/14.16/N/A|
|DAG-PMHC-02|Mutant/WT/Peptide-free|92.8/92.5/84.7|0.922/0.897/N/A|2.25/2.73/N/A|
|DAG-PMHC-03|Mutant/WT/Peptide-free|83.9/83.1/89.1|0.867/0.892/N/A|4.56/4.05/N/A|

*Four-seed means (`Pair-iPTM`: position D/frame C; `PAE`: D→C mean). Full ranges and comparators: `CONFIDENCE-METRICS.md`.*

FreeSASA (Lee–Richards, 100 slices, 1.4 Å probe, ProtOr radii) quantified partner burial and half-delta interface area. Hydrogen bonds were assigned after hydrogen preparation at pH 7 (donor–acceptor distance >1 and ≤3 Å; donor–H–acceptor angle >150°), with atom-specific distances inspected alongside the assignments. Three pretrained SaProt stability heads scored isolated binder conformations from the four mutant complexes, matched by seed and head.

`DAG-PMHC-02`, its original design, and `DAG-PMHC-03` underwent two-stage OpenMM CPU minimization (Amber14 `ff14SB`/TIP3P; heavy-atom-restrained then unrestrained minimization, zero MD steps) across all eight mutant/WT poses for `DAG-PMHC-02` and its original design, and four mutant plus three initial-batch WT poses for `DAG-PMHC-03` (23/24 nominal poses; `DAG-PMHC-01` and the recovered fourth WT pose of `DAG-PMHC-03` were not relaxed).

## Selection Rationale, Mutant-vs.-WT Comparisons, and Ranking

The submitted order expresses our preference among three complementary peptide-recognition hypotheses. Detailed comparisons are in `SUMMARY.md`.

- **`DAG-PMHC-01` (Groove-spanning shape complementarity):** Revision tightened mutant placement RMSD from **1.42–34.32 Å** (original) to **1.69–3.50 Å** across all four seeds (WT: **2.13–24.00 Å**), increased all **12 matched SaProt scores** (+0.18–0.51 model kcal/mol), and buried **20–86 Å²** more peptide surface in mutant than WT per seed. These observations motivate its first-place ranking as an indirect shape-recognition hypothesis. Its nearest Asp6 carboxylate remains 6.85–7.43 Å away, with no peptide hydrogen bond assigned by the recipe. Mutant pair-iPTM decreased from **0.593** to **0.474** after revision, with overlapping WT values; the rationale rests on placement and interface observations rather than a confidence-score increase.
- **`DAG-PMHC-02` (Direct Arg72–Asp6 capture):** With high complex confidence (mutant pair-iPTM **0.922**, PAE **2.25 Å**), `DAG-PMHC-02` positions Arg72 over Asp6. The hydrogen-bond recipe assigns a peptide contact in 1/4 unrelaxed mutant poses for both the revision and original design. OpenMM relaxation brings Arg72 NH2–Asp6 carboxylate distances to **2.74–2.81 Å** in **4/4 mutant poses** (versus **3/4** original), and `A9E/A19T` increased **9/12** matched stability scores (overall differences −0.086 to +0.091 model kcal/mol). In WT (**0.897** pair-iPTM), Arg72 shifts toward the Gly6 carbonyl (**2.77–2.87 Å**) in **2/4 relaxed poses** or forms alternative peptide contacts, testing direct carboxylate capture against WT backbone accommodation.
- **`DAG-PMHC-03` (C-terminal Gly9 backbone engagement):** This scaffold buries **17–58 Å²** more peptide surface in mutant than WT in 3/4 seeds and shows two local contact patterns near the peptide C-terminus: binder Glu44 OE2 approaches Gly9 N in two mutant poses (**2.89, 3.00 Å** relaxed), and binder Tyr20 OH approaches Gly9 O in the other two (**2.71, 2.82 Å** relaxed). These named atom pairs are farther apart in all three available relaxed WT poses, motivating a test of recognition through mutation-dependent peptide presentation. WT predictions have higher pair-iPTM (**0.892** vs. **0.867**) and greater HLA burial in all four seeds; the hypothesis specifically concerns the peptide-contact patterns.

## Methodological Scope and Experimental Readouts

The broader comparison contained 74 attempt identities and 50 source-supported records, including original designs, controls and repeated sequences. Selection was adaptive. Full candidate-specific results and retained structures accompany the methods in `SUMMARY.md` and the supplement.

The remaining questions are concrete. `DAG-PMHC-01` retains crowded unrelaxed contacts (minimum 2.38 Å mutant, 1.88 Å WT), and its 120 residues exceed the cited 60–80-residue SaProt validation range. `DAG-PMHC-01` and `DAG-PMHC-03` have larger predicted interfaces in the emptied-groove context than in mutant pMHC; this modeled construct differs from the experimental peptide-free target. Local minimization examines geometry within predicted docking basins, not binding free energies or pose populations. The sequence biases and soluble checkpoint were design choices; expression and solubility effects remain unmeasured.

Matched mutant/WT binding measurements, peptide-free HLA counter-screening and affinity titrations would directly test these three recognition hypotheses, alongside protein production for assay. The portfolio was chosen to bring complementary, structurally specified mechanisms into that experimental comparison.
