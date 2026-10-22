# Module 4 Assignment: Structure-Based Druggability

**Name:** Sharath Mandula
**Course:** BIOT 6900 · AI-Powered Biotech Workflows · Fall 2026
**Disease:** Alzheimer's disease (AD), from my Module 2 ranked list (`targets_ad.csv`)

## Targets
| Gene | UniProt | Module 2 rank | Experimental structure | Why |
|------|---------|---------------|------------------------|-----|
| SAMHD1 | Q9Y3Z3 | 1 | 4BZC chain A (catalytic core, dGTP bound) | Top Module 2 gene and top small-molecule prior in Module 3 |
| APOE | P02649 | 4 | 2L7B chain A (full-length apoE3, NMR model 1) | Strongest AD risk gene; near-zero sequence prior in Module 3 |

## Files
- `BIOT6900_Module4_Assignment.ipynb`: the completed notebook (Restart & Run All, outputs saved)
- `structure_assessment_ad.csv`: the summary table
- `Module4_Report.pdf`: the report
- `structures/` is not committed (see `.gitignore`); the notebook re-downloads it

## What didn't work / notes
- fpocket is not available for Windows, so I installed it with conda (Miniforge) inside WSL Ubuntu and ran `fpocket -f` on both AlphaFold models in `structures/`. The notebook then reads the saved fpocket output folders (Step 6 skips re-running fpocket when they exist).
- (add anything else that went wrong, or delete this line)
