# Module 8 — Single-Cell & Spatial Omics

**Name:** Sharath Mandula
**Course:** BIOT 6900 · AI-Powered Biotech Workflows · Fall 2026
**Target gene:** ERBB2 (HER2)

## Files
- `BIOT6900_Module8_Assignment_Starter.ipynb` — completed notebook (Part 1 single-cell, Part 2 spatial), all TODOs answered
- `Module8_Report_Sharath_Mandula.pdf` — 4-page report connecting the two views (Part 3)
- `module8_results_summary.txt` — all key numbers from the run

## Summary
ERBB2 is expressed mainly by malignant epithelial cells in the CELLxGENE breast-cancer single-cell data (10 donors, 18,388 cells), and on the 10x Visium section it is highest in the tumor-core domains and still high at the tumor–immune margin, dropping in the immune/stroma belt.

## What did not run / changes from the starter
- Explorer (Open OnDemand) could not install the packages (numpy binary conflict, then a frozen file system), so the notebook was run on **Google Colab with a T4 GPU**.
- Added `sc.settings.n_jobs = 1` to fix a numba thread-count error in `sc.pp.neighbors` on Colab.
- `seurat_v3` highly-variable-gene selection failed with a loess error; added `span=0.5` with a fallback to the `seurat` flavor (seurat_v3 succeeded with span=0.5).
- Fixed a labeling bug: "malignan**t cell**" matched the "t cell" rule, so all malignant cells were labeled T cells. Malignant/carcinoma cells are now mapped to Epithelial/Tumor first.
- Added helper cells: assay/donor report (1.1), tumor/stroma/immune domain labeling (2.3b), and a results-summary export.
