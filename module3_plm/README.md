# Module 3 – Target triage with protein language models
## Files
- `BIOT6900_Module3_Assignment.ipynb` – assignment notebook
- `targets_ad_w3.csv` – re-ranked targets (hand-off to Module 4)
- `Module3_Report_Sharath.pdf` – report
- `data/` – Module 3 data pack (ESM C / ESM-2 embeddings, panel, variant scores)
## Notes
- Input: top 15 targets from `../module2_multiomics/targets_ad.csv` (rank-normalised equal-weight score).
- All 15 targets mapped to `proteome.tsv` (0 unmapped).
- Leakage guard removed 1 target (CACNG8) from the training panel; trained on 1,200 proteins.
- Family-split validation: AUROC 0.728, AP 0.531 (chance AP = 0.333).
- Weight w = 0.6 on Module 2 evidence (justified in the report).
- Targets suggested for Week 4: SAMHD1 and APOE.
## References
- ESM Team. (2024, December 4). ESM Cambrian: Revealing the mysteries of proteins with unsupervised learning. EvolutionaryScale. https://evolutionaryscale.ai/blog/esm-cambrian
- Johnson, E. C. B., et al. (2022). Large-scale deep multi-layer analysis of Alzheimer's disease brain reveals strong proteomic disease-related changes not observed at the RNA level. *Nature Neuroscience, 25*(2), 213–225. https://doi.org/10.1038/s41593-021-00999-y
- Liang, W. S., et al. (2007). Gene expression profiles in anatomically and functionally distinct regions of the normal aged human brain. *Physiological Genomics, 28*(3), 311–322. https://pubmed.ncbi.nlm.nih.gov/17077275/
- Lin, Z., et al. (2023). Evolutionary-scale prediction of atomic-level protein structure with a language model. *Science, 379*(6637), 1123–1130. https://doi.org/10.1126/science.ade2574
- Meier, J., Rao, R., Verkuil, R., Liu, J., Sercu, T., & Rives, A. (2021). Language models enable zero-shot prediction of the effects of mutations on protein function. *Advances in Neural Information Processing Systems, 34*.
- Ochoa, D., et al. (2023). The next-generation Open Targets Platform: Reimagined, redesigned, rebuilt. *Nucleic Acids Research, 51*(D1), D1353–D1359. https://doi.org/10.1093/nar/gkac1046
- Sollis, E., et al. (2023). The NHGRI-EBI GWAS Catalog: Knowledgebase and deposition resource. *Nucleic Acids Research, 51*(D1), D977–D985. https://doi.org/10.1093/nar/gkac1010
- The UniProt Consortium. (2023). UniProt: The Universal Protein Knowledgebase in 2023. *Nucleic Acids Research, 51*(D1), D523–D531. https://doi.org/10.1093/nar/gkac1052
