# Module 9 — Clinical NLP on My Own Disease (Computational Lab 9)

**Course:** BIOT 6900 · AI-Powered Biotech Workflows · Fall 2026
**Notebook:** `BIOT6900_Module9_Notebook3_Graded.ipynb`
**Disease:** Severe acute pancreatitis (SAP) in the ICU, outcome = in-hospital mortality
**Data:** 100% synthetic, generated inside the notebook (400 patients × 3 notes). No real patient data.

## My configuration
| Role | Concept | Synonyms used in notes | Why it belongs here |
|---|---|---|---|
| Signal | `sirs` | SIRS, systemic inflammatory response (syndrome) | Admission inflammatory state; BISAP component |
| Signal | `pleural_effusion` | pleural effusion, effusion, pleural fluid | Seen on admission imaging; BISAP component |
| Signal | `hemoconcentration` | hemoconcentration, elevated BUN, high hematocrit | Early fluid loss; predicts necrosis / organ failure |
| Consequence (leak) | `mechanical_ventilation` | mechanical ventilation, intubated, ventilator | Organ support given *because* of respiratory failure |
| Consequence (leak) | `necrosectomy` | necrosectomy, percutaneous drainage, surgical debridement | Rescue procedure for infected necrosis / deterioration |
| Consequence (leak) | `comfort_care` | comfort measures only, CMO, hospice, palliative extubation | End-of-life decision |

`SEED = 2034949` (my student ID 002034949; leading zeros dropped because Python integers can't start with 0).

## Results (5-fold CV AUROC)
See Part D in the notebook for the full numbers and interpretation. In short:
- All features: **0.922**, inflated by leakage
- Declared leakage removed: **0.833**, still high, the clue that a leak was missed
- All leakage removed (+ `renal_replacement`): **0.799**, the honest model
- Structured fields only: **0.776**, so note features add a modest amount of real signal

Wildcard diagnosis: `renal_replacement` = **leakage** (intervention, documented only in the final note); `lactate_not_clearing` = **signal** (physiological finding, documented on admission).

`permutation_importance.png` is the importance plot from Part C (red = declared leakage).

## How to re-run
Open the notebook with the `biot6900` kernel → **Kernel → Restart & Run All**. Needs only pandas, numpy, scikit-learn, matplotlib.

## What I added to the starter notebook
- A naive-vs-assertion check for all three signals (not just the first)
- An evidence table showing which note (admission / day 2 / final) each feature comes from, and mortality with vs without it (used in D2)
- A structured-only baseline AUROC (used in D3)
- `savefig` on the importance plot

## What did not work / limitations
- Everything ran without errors.
- The assertion engine tags "Brief dialysis for contrast, since stopped" as *present* (no "since stopped" trigger), so `renal_replacement` is noisy even apart from being leakage.
- Real notes would rarely write the literal words "SIRS" or "hemoconcentration"; they record vitals and labs, so a text extractor would undercount these signals.
- 400 synthetic patients with clean, on-time documentation: all metrics are illustrative, not a deployable model.
