# Predicted complex confidence across all contexts

Each cell is the mean [minimum–maximum] across all four prediction seeds. These are descriptive model outputs; ranges are not experimental confidence intervals. D is binder, C peptide and A HLA. N/A indicates chain C is absent.

| Molecule | Context | Binder pLDDT (0–100) | Pair-iPTM position D/frame C | PAE D→C (Å) | PAE D→A (Å) |
|---|---|---|---|---|---|
| DAG-PMHC-01 | mutant_bound | 93.5 [93.3–94.1] | 0.474 [0.364–0.601] | 13.24 [10.20–15.80] | 17.47 [14.16–20.08] |
| DAG-PMHC-01 | wildtype_bound | 92.9 [91.1–94.2] | 0.463 [0.282–0.685] | 14.16 [8.72–18.43] | 17.99 [11.90–22.50] |
| DAG-PMHC-01 | peptide_removed | 88.9 [87.7–90.0] | N/A | N/A | 11.31 [10.88–11.75] |
| DAG-PMHC-01-parent | mutant_bound | 92.9 [89.5–94.7] | 0.593 [0.287–0.850] | 10.48 [4.19–17.96] | 13.99 [6.96–21.81] |
| DAG-PMHC-01-parent | wildtype_bound | 92.1 [90.4–94.3] | 0.367 [0.189–0.543] | 16.29 [12.19–20.75] | 20.41 [15.91–24.93] |
| DAG-PMHC-01-parent | peptide_removed | 88.9 [86.9–90.1] | N/A | N/A | 12.70 [12.07–13.41] |
| DAG-PMHC-02 | mutant_bound | 92.8 [92.2–94.3] | 0.922 [0.912–0.934] | 2.25 [2.06–2.46] | 4.53 [4.24–4.89] |
| DAG-PMHC-02 | wildtype_bound | 92.5 [90.9–94.9] | 0.897 [0.868–0.923] | 2.73 [2.53–3.05] | 5.21 [4.62–5.87] |
| DAG-PMHC-02 | peptide_removed | 84.7 [83.9–86.0] | N/A | N/A | 17.40 [13.23–18.99] |
| DAG-PMHC-02-parent | mutant_bound | 92.9 [92.0–94.4] | 0.924 [0.912–0.937] | 2.24 [2.01–2.52] | 4.53 [4.15–5.00] |
| DAG-PMHC-02-parent | wildtype_bound | 92.9 [90.9–94.7] | 0.907 [0.900–0.920] | 2.59 [2.38–2.82] | 4.96 [4.72–5.29] |
| DAG-PMHC-02-parent | peptide_removed | 84.7 [84.3–85.4] | N/A | N/A | 17.62 [14.92–18.75] |
| DAG-PMHC-03 | mutant_bound | 83.9 [80.1–86.9] | 0.867 [0.801–0.898] | 4.56 [3.67–6.34] | 7.76 [6.40–10.12] |
| DAG-PMHC-03 | wildtype_bound | 83.1 [82.7–83.7] | 0.892 [0.870–0.906] | 4.05 [3.64–4.82] | 6.93 [6.26–8.10] |
| DAG-PMHC-03 | peptide_removed | 89.1 [88.0–89.7] | N/A | N/A | 5.72 [5.49–6.13] |

Binder pLDDT describes the predicted binder fold; pair-iPTM and directional PAE describe model confidence in the complex. High confidence in both mutant and WT contexts does not distinguish their physical affinities. Families were assessed in separate batches, with matched seeds within parent–child comparisons. These metrics were not combined into a selection score.

The complete per-seed values are in `data/<molecule>-cofold.json`; `tables/confidence-summary.csv` retains unrounded summaries. All source files were hash-checked during packaging. DAG-PMHC-03 WT seed 2026110824 was recovered in a separate execution phase, as labeled in its cofold data. Parent labels identify unsubmitted comparators.
