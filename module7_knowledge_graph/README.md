# Module 7 — Knowledge Graph for Alzheimer's Disease

**Name:** Sharath Mandula
**Disease:** Alzheimer's disease (AD)

A Neo4j knowledge graph built from my own earlier modules: 83 nodes (incl. 30 patients), 67 relationships.

## Where the data comes from
| Module | What it contributes |
|---|---|
| Module 2 | Gene list (top 15 + APP, GRIN2B), GWAS p, RNA/protein fold-changes, multi-evidence score |
| Module 3 | Ensembl/UniProt IDs, tractability priors (p_sm, p_ab), ESM-2 scores for APOE ε4/ε2 |
| Module 4 | AlphaFold + fpocket structure calls for SAMHD1 and APOE |
| Module 6 | PGS000334 AD polygenic-score SNPs (mapped to genes with my Module 2 GWAS file); 30-person patient layer with APOE genotype + PRS (real 1000 Genomes genotypes, **simulated** case/control status) |

Module 5 (CYP2C19 pharmacogene) is not AD-related, so no variants come from it.
Related disease: **Aicardi-Goutières syndrome**, caused by loss of SAMHD1 (my #1 gene).

## Files
- `BIOT6900_Module7_Alzheimers_KG.ipynb` — the notebook
- `prepare_module7_data.py` — builds `data/` from my Module 2–6 outputs
- `data/` — small CSVs the notebook reads
- `my_knowledge_graph.png`, `nodes.csv`, `edges.csv` — graph figure and exports
- `Module7_Report.pdf` — report

## Key results
- **2-hop:** donepezil, rivastigmine, galantamine (ACHE); memantine (GRIN2B); lecanemab, donanemab (APP); semorinemab (MAPT)
- **5-hop repurposing:** baricitinib (JAK1), via Aicardi-Goutières syndrome (shared: cognitive impairment, cerebral atrophy)
- **Top PageRank:** APOE, ACHE, APP. SAMHD1 ranks joint last on directed PageRank, 8th undirected (discussed in report)
- **Stratification:** ε3/ε4 carriers have the highest mean PRS percentile (82) vs ε3/ε3 (38) and ε2/ε3 (10)

## How to run
1. Run `python prepare_module7_data.py` once (edit the `SRC` paths at the top if my folder names differ).
2. Put the AuraDB credentials file here as `neo4j_credentials.txt` (git-ignored).
3. **Kernel → Restart & Run All**.
