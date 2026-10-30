# BIOT 6900 – AI-Powered Biotech Workflows (Fall 2026)
**Name:** Sharath Mandula · Northeastern University
**Disease:** Alzheimer's disease (AD)
**Environment:** conda env `biot6900` (Python 3.11)
## Repository layout
| Module | Folder | Topic | Key outputs |
|---|---|---|---|
| 1 | `module1_setup/` | Environment setup & database APIs | `module1_setup.ipynb` |
| 2 | `module2_multiomics/` | Multi-omics target identification | `targets_ad.csv`, report |
| 3 | `module3_plm/` | Target triage with protein language models | `targets_ad_w3.csv`, report |
| 4 | `module4_structure/` | Structure prediction & druggability | `structure_assessment_ad.csv`, report |
| 5 | `module5_variants/` | Pharmacogenomic variant interpretation (CYP2C19) | `pgx_classified_CYP2C19.csv`, report |
| 6 | `module6_prs/` | Polygenic risk score portability across ancestries (PGS000334) | `fig_prs_by_ancestry.png`, `fig_calibration_by_ancestry.png`, report |
| 7 | `module7_knowledge_graph/` | AD knowledge graph in Neo4j, built from Modules 2–6 | `my_knowledge_graph.png`, `nodes.csv`, `edges.csv`, report |
| Portfolio 1 | `portfolio1_target_discovery/` | Multi-omics target discovery package (Labs 2–4) | `BIOT6900_Portfolio1_SharathMandula.pdf`, Figures 1–4 |

Each module folder has its own `README.md`, notebook(s), report, and a `data/` folder next to the notebook.
## How to run
1. `conda activate biot6900`
2. Launch Jupyter from inside the module folder (notebooks read `data/` relative to their own location).
3. Kernel → Restart & Run All.

Any data file too large for GitHub (100 MB limit) is listed in `.gitignore`; download it from Canvas into that module's `data/` folder. Module 7 also needs a Neo4j AuraDB login in a git-ignored `neo4j_credentials.txt` (see `module7_knowledge_graph/README.md`).
## Problems and fixes
- **Module 2 scoring:** the original score used a raw weighted sum, so GWAS p-values (−log10 p up to ~300) dominated the ranking. Fixed by using `multi_evidence_score` (rank-normalised equal weights) and by splitting multi-gene GWAS entries (e.g. "TOMM40, APOE"). The three-way join grew from 731 to 1,139 genes.
- **Wrong working directory:** Jupyter was running from the Downloads folder, which caused `FileNotFoundError`. Fixed by launching Jupyter from the repo folder.
- **Data pack location:** the Module 3 data pack had to be extracted directly into `data/`, not into a subfolder.
- **Module 6 data location:** the CSVs were first extracted next to the notebook instead of inside `data/`. Fixed by moving them into `data/`.
- **Module 7 credentials file:** Windows saved it as `neo4j_credentials.txt.txt`, so the notebook could not connect. Fixed by renaming it.
- **Module 7 old lab data:** the Neo4j database still held the Real Model lab graph, which mixed extra drugs and diseases into my query results. Fixed by adding a cell that clears the database before loading.
- **Module 7 `data/` not pushed:** the repo `.gitignore` excludes `data/` folders, so the Module 7 data was missing on GitHub. Fixed by adding `!data/` to `module7_knowledge_graph/.gitignore` (the files are small).
