# BIOT 6900 – Module 1: Computational Environment Setup & Tool Ecosystem

**Name:** Sharath
**Notebook:** `module1_setup.ipynb`

## What I did
- **Part A – Environment:** set up the `biot6900` conda environment (Python 3.11) with BioPython, pandas, numpy, requests and Jupyter, plus Git/GitHub for version control.
- **Part B – BioPython quickstart:** translated a short DNA sequence into protein with `Seq.translate()`.
- **Part C – Database APIs:**
  - **PubMed** (via `Bio.Entrez`): searched "AlphaFold protein structure" and retrieved 5 PMIDs.
  - **UniProt** (REST API): retrieved P04637, the human tumour suppressor p53.
  - **PDB** (RCSB REST API): retrieved 1TUP, a p53 core domain structure bound to DNA.
  - **GWAS Catalog** (EBI REST API): looked up rs7412, an APOE missense variant that defines the ε2 allele.
- **Part D – Multi-omics datasets:** loaded three Alzheimer's disease datasets with pandas and confirmed their shapes:
  - `ad_transcriptomics.tsv` – (54675, 8): GEO2R differential expression for GSE5281 (AD vs. control hippocampus).
  - `ad_proteomics.tsv` – (13541, 4): AD vs. control protein-level changes from Johnson et al. 2022 (TMT-MS).
  - `ad_gwas.tsv` – (7410, 38): GWAS Catalog associations for Alzheimer's disease.
## Problems and fixes
- Part D was originally deferred to Week 2 (confirmed by Prof. Prabakaran by email, Sep 14), so the loading cell first raised `FileNotFoundError`. I later completed it using the Alzheimer's multi-omics files from Module 2.
- The files are tab-separated, so I loaded them with `sep="\t"`.
- The edited notebook was first saved in a backup folder instead of the Git repo, so GitHub Desktop showed no changes. Fixed by copying it into the repo's `module1_setup/` folder before committing.