# Module 6 – Polygenic Risk Score Portability Across Ancestries

**Course:** BIOT 6900 – AI-Powered Biotech Workflows (Fall 2026), Northeastern University
**Disease:** Alzheimer's disease (AD)
**Score:** PGS Catalog PGS000334 (22 SNPs, including APOE rs429358 and rs7412)
**Data:** 1000 Genomes phase 3 genotypes (2,336 people; EUR, AFR, EAS, SAS, AMR)

## What this module does

Applies a published, European-trained Alzheimer's polygenic risk score to real 1000 Genomes genotypes and checks whether it works equally well across ancestry groups.

1. Harmonize alleles (keep / flip / drop) against REF/ALT
2. Compute the standardized PRS
3. Compare PRS distributions and a single top-10% cutoff across ancestries
4. Measure discrimination (AUC) overall and per ancestry
5. Check calibration of an EUR-fitted risk model in every ancestry
6. Test whether the PRS adds to age alone (5-fold cross-validated AUC)

> **Note:** 1000 Genomes has no disease labels, so the phenotype is simulated. The PRS distributions are real; AUC and calibration results are illustrative.

## Key results

| | EUR | AFR | EAS | SAS | AMR | Overall |
|---|---|---|---|---|---|---|
| AUC | 0.672 | 0.493 | 0.575 | 0.611 | 0.555 | 0.599 |
| Mean PRS (SD) | +0.04 | +0.74 | −0.47 | −0.25 | −0.10 | |
| % above pooled top-10% cutoff | 7.8 | 28.0 | 2.2 | 4.3 | 6.3 | |

- Harmonization: 22 variants used, 13 flipped, 0 dropped
- Age only AUC 0.562 → age + PRS AUC 0.618

## Files

| File | Description |
|---|---|
| `BIOT6900_Module6_Part3_Assignment.ipynb` | Full workflow notebook (run on real data) |
| `fig_prs_by_ancestry.png` | PRS distribution by ancestry |
| `fig_calibration_by_ancestry.png` | Calibration curves by ancestry |
| `Module6_Report.pdf` | Written report |

## How to run

1. Download `data.zip` from Canvas and extract it here so you have a `data/` folder with `genotypes.csv`, `variants.csv`, `score.csv`, `meta.csv`.
2. Activate the `biot6900` environment and open the notebook from this folder.
3. Keep `USE_DEMO = False`, then **Kernel → Restart & Run All**.

The `data/` folder is not committed to this repo.

## Problems and fixes

- **FileNotFoundError on load:** the CSVs were extracted next to the notebook instead of inside `data/`. Fixed by moving them into a `data/` folder.
- **Mac zip leftovers:** the zip created a `__MACOSX` folder and `._` files. These are not data and were deleted.

## Reference

Zhang, Q., et al. (2020). Risk prediction of late-onset Alzheimer's disease implies an oligogenic architecture. *Nature Communications, 11*, 4799. https://doi.org/10.1038/s41467-020-18534-1
