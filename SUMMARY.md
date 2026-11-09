# Three computational candidates for KRAS G12D pMHC recognition

We propose DAG-PMHC-01, DAG-PMHC-02 and DAG-PMHC-03 for experimental evaluation against the KRAS G12D peptide VVVGADGVGK presented by HLA-A*11:01 and beta-2 microglobulin. The wild-type peptide is VVVGAGGVGK. The candidates address the competition's mutation-specificity, peptide-dependence and affinity objectives through complementary structural hypotheses evaluated against matched target contexts.

## Candidate rationale

| Candidate | Design route | Reason for inclusion | Question for the experiment |
|---|---|---|---|
| DAG-PMHC-01 · 120 aa | RFD4-Proteina parent followed by network-protected ProteinMPNN revision | More coherent predicted mutant placement, favorable parent–child stability diagnostics and mutant-favored whole-peptide burial | Does the proposed shape recognition discriminate mutant from WT and peptide-free HLA? |
| DAG-PMHC-02 · 80 aa | Multi-context Odin-Multi/ColabDesign parent followed by A9E/A19T revision preserving binder Arg72 | Locally plausible binder Arg72–peptide Asp6 geometry in all four relaxed mutant starting poses | Does direct Asp6 recognition confer an advantage over the modeled WT backbone alternatives? |
| DAG-PMHC-03 · 80 aa | Fresh Odin-Multi/ColabDesign generation with soluble ProteinMPNN guidance | Two alternative Gly9-facing interaction patterns supported by atom-specific geometry and local relaxation | Can this peptide-backbone arrangement recognize a mutant-dependent presentation despite shared WT chemistry? |

This order is our exploratory submission preference, not a calibrated ranking of physical performance. The third sequence broadens the candidate set with a fresh generated hypothesis; close parent sequences remain comparators. All three exact sequences passed the platform's pre-submission Novelty Check.

## Predicted complex confidence

| Candidate | Context | Binder pLDDT | Pair-iPTM | Binder→peptide PAE (Å) |
|---|---|---:|---:|---:|
| DAG-PMHC-01 | Mutant | 93.5 | 0.474 | 13.24 |
| DAG-PMHC-01 | WT | 92.9 | 0.463 | 14.16 |
| DAG-PMHC-01 | Peptide removed | 88.9 | N/A | N/A |
| DAG-PMHC-02 | Mutant | 92.8 | 0.922 | 2.25 |
| DAG-PMHC-02 | WT | 92.5 | 0.897 | 2.73 |
| DAG-PMHC-02 | Peptide removed | 84.7 | N/A | N/A |
| DAG-PMHC-03 | Mutant | 83.9 | 0.867 | 4.56 |
| DAG-PMHC-03 | WT | 83.1 | 0.892 | 4.05 |
| DAG-PMHC-03 | Peptide removed | 89.1 | N/A | N/A |

Four-seed means are shown; `CONFIDENCE-METRICS.md` supplies ranges and both parent comparisons. D denotes binder and C denotes peptide. Pair-iPTM uses position D/frame C; PAE is the D→C mean in angstroms. N/A means peptide is absent. Confidence in a modeled complex is distinct from mutation discrimination: high confidence in WT as well as mutant remains visible. Separate family assessment batches and common model assumptions limit between-family comparisons.

## DAG-PMHC-01: network-protected placement

The six substitutions Q27D, E50V, K53E, T55Q, E57A and Q58P resulted from a ProteinMPNN revision protecting a predefined peptide-facing network. Across four subsequent mutant predictions, the six pairwise HLA-aligned binder placement RMSDs span **1.691–3.502 Å**, compared with **1.415–34.317 Å** for the unchanged parent. WT placement spans **2.129–24.003 Å**. All **12 matched stability-head comparisons** favor the child by **0.18–0.51** in the model's reported kcal/mol units, and whole-peptide burial favors mutant in every seed by approximately **20–86 Å²**. Mutant complex confidence moves in the other direction: mean pair-iPTM is **0.474** versus **0.593** for the parent, and binder→peptide PAE is **13.24 Å** versus **10.48 Å**. The mean mutant-minus-WT pair-iPTM difference is **0.011**, versus **0.226** for the parent; the child's WT seed range encloses its mutant range. Selection therefore rests on the more reproducible placement and mutant-favored burial as an indirect shape-recognition hypothesis, without a modeled contact to position 6 or an improved confidence contrast.

The nearest binder atom is **6.847–7.428 Å** from an Asp6 carboxylate oxygen; the fixed recipe assigns no binder–peptide hydrogen bond. Position-6 burial favors WT in all four predictions, with Asp and Gly having different atom inventories. Residual crowding includes a mutant Gly7 O–binder Thr100 CG2 separation of **2.375 Å** and a WT O–O separation of **1.876 Å**. This candidate was not included in local minimization. The three stability heads share a model, and the 120-residue input is outside its cited 60–80-residue validation population.

The peptide-removed diagnostic gives half-delta interface areas of **950–1241 Å²**, versus **593–665 Å²** for mutant and **489–660 Å²** for WT. The binder can occupy the emptied peptide groove, so this does not measure physiological peptide dependence. Peptide-removed placement RMSDs span **1.38–34.20 Å**, versus **1.01–2.72 Å** for the parent: the placement finding is context-specific. The sequence retains immune-receptor-like framework features; no novel-fold claim is made.

## DAG-PMHC-02: direct Asp6 interaction

The A9E/A19T revision preserves binder Arg72 (chain D), which can interact with peptide Asp6 (chain C). After local minimization, the proposed network is locally plausible in **four of four mutant starting poses**, versus **three of four** for its parent. Released Arg72 NH2–nearest Asp6 carboxylate oxygen distances are approximately **2.79, 2.74, 2.78 and 2.81 Å**. The one-pose parent–child difference includes contact formation during minimization; before minimization, the recipe assigns a peptide hydrogen bond in **one of four** mutant predictions for both sequences.

WT provides a specific alternative: two of four relaxed WT starting poses accommodate Arg72–Gly6 backbone approaches. One has NH1/NH2–Gly6 O distances of **2.838/2.869 Å**; another has NH1–O at **2.770 Å**. The other WT poses retain other peptide contacts. These local models do not determine the relative populations or free energies of the mutant and WT arrangements.

Stability-head comparisons favor the child in **nine of twelve** matched evaluations, with changes spanning approximately **−0.086 to +0.091** in the model's reported kcal/mol units. Isolated binder apolar surface increases in **three of four** mutant conformations by **16–33 Å²**, and decreases by **120 Å²** in the fourth; the four-seed mean change is **−13 Å²**. A9E/A19T was intended to improve production-related properties, but the observations do not establish an expression or solubility gain.

## DAG-PMHC-03: a fresh peptide-backbone hypothesis

This independently generated sequence uses the soluble ProteinMPNN checkpoint within the multi-context Odin-Multi/ColabDesign workflow. It is not a further revision of either submitted sequence. In the prepared mutant predictions, two different seeds have recipe-assigned peptide interactions: peptide Gly9 N–H toward binder Glu44 OE2, and binder Tyr20 OH–H toward peptide Gly9 O. Their donor–acceptor separations are approximately **2.708 and 2.738 Å**, respectively. These are distinct interactions in alternative predicted poses.

After local minimization, the Glu44/Gly9 approach remains near **2.891 and 3.003 Å** in two mutant poses; the Tyr20/Gly9 approach is **2.815 and 2.712 Å** in the other two. The corresponding named approaches are farther apart in the three available relaxed WT poses. This supports testing a peptide-presentation hypothesis rather than relying solely on a global confidence score.

Gly9 backbone chemistry is shared by mutant and WT, the docking modes were separately predicted, and shared-HLA interactions remain an alternative explanation. WT mean pair-iPTM is **0.892**, versus **0.867** for mutant; binder→peptide PAE is **4.05 Å** in WT, versus **4.56 Å** in mutant. The peptide-removed context has binder pLDDT **89.1** and binder→HLA PAE **5.72 Å**, compared with **83.9 / 7.76 Å** for mutant and **83.1 / 6.93 Å** for WT. Its half-delta interface area is **1182–1289 Å²**, versus **896–1165 Å²** for mutant. The emptied-groove construct does not establish physiological peptide dependence. The reason to test this candidate is its atom-specific Gly9 geometry and local relaxation, rather than a global confidence advantage for mutant. The fourth WT prediction and its chemistry analysis were recovered in a separate execution phase, completing four-seed cofold and chemistry coverage; this pose was not relaxed. Whole-peptide burial favors mutant in three of four pairs by **17–58 Å²**, and favors WT by **15 Å²** in the fourth; HLA burial favors WT in all four by **2–83 Å²**. Crowded contacts occur in the starting models; a strained WT prediction does not establish WT nonbinding. The label “soluble” identifies the generation checkpoint, not a measured property or a demonstrated checkpoint improvement. No selected all-atom generation structure is available; all supplied complex structures are assessment predictions or their local-minimization derivatives.

## How the candidates were chosen

The workflow combined generation, targeted sequence revision, fresh complex prediction, matched mutant/WT assessment, interface and stability diagnostics, and local geometry assessment. Candidate choice followed the complete observations, including WT alternatives and changes from computational parents. The broader comparison record contained **74 attempt identities and 50 source-supported records**, including controls, parents and repeated sequences. These are not independent molecules, and adaptive selection prevents interpreting the selected set as a prospective success rate.

The supplement retains **36 candidate and 24 parent cofold predictions**, **60 chemistry records**, **60 stability-head records**, and **69 prepared/restrained/released structures** from **23 completed relaxation slots**. One additional relaxation slot is explicitly unavailable. All outputs within this selected scope are included, with the recovered WT phase separately labeled. Numerical and provenance checks support exact identities, accounting and arithmetic; they do not supply physical validation.

## Experimental questions and supplement

The decisive tests are intact soluble material, mutant and WT binding under matched conditions, binding to the contest's peptide-free target, and concentration-dependent affinity measurements with detection limits and controls. These determine whether the proposed mechanisms translate into mutation-specific, peptide-dependent binding. Confidence scores, geometric burial and local minimization describe different aspects of the models; none is a calibrated affinity or selectivity estimate.

`METHODS.md` describes the protocol. `CONFIDENCE-METRICS.md` and `tables/confidence-summary.csv` report all contexts and parent comparisons. `structure-index.csv` locates each of **129 structure files** by sequence, context, seed, stage and hash. `tables/chemistry.csv`, `tables/stability.csv` and `tables/relaxation-*.csv` provide numerical records, while `data/` retains detailed observations. `design/` supplies revision parameters, parent conditioning templates and fresh-generation configuration. Only the three sequences in `designs.fasta` are submitted; identifiers ending in `-parent` denote unsubmitted comparators.
