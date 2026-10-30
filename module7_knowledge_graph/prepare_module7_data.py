"""
Module 7 data prep: pulls the pieces of Modules 2-6 that the knowledge graph needs
into small CSVs in data/. Run once from the module7 folder; edit SRC paths if your
folders are named differently.
"""
import pandas as pd, os

SRC = {   # where each earlier-module file lives (relative to this folder)
    "targets":   "../module2_multiomics/targets_ad.csv",
    "gwas":      "../module2_multiomics/ad_gwas.tsv",
    "w3":        "../module3_plm/targets_ad_w3.csv",
    "proteome":  "../module3_plm/data/proteome.tsv",
    "anchors":   "../module3_plm/data/anchor_variants.tsv",
    "structure": "../module4_structure/structure_assessment_ad.csv",
    "pgs":       "../module6_prs/data/score.csv",
    "geno":      "../module6_prs/data/genotypes.csv",
    "vars":      "../module6_prs/data/variants.csv",
    "meta":      "../module6_prs/data/meta.csv",
}
os.makedirs("data", exist_ok=True)
tgt = pd.read_csv(SRC["targets"])
gw  = pd.read_csv(SRC["gwas"], sep="\t", low_memory=False)
pgs = pd.read_csv(SRC["pgs"])

# 1) copy the small hand-off files as-is
tgt.to_csv("data/targets_ad.csv", index=False)
pd.read_csv(SRC["w3"]).to_csv("data/targets_ad_w3.csv", index=False)
pd.read_csv(SRC["structure"]).to_csv("data/structure_assessment_ad.csv", index=False)
pd.read_csv(SRC["anchors"], sep="\t").to_csv("data/anchor_variants.csv", index=False)

# 2) PGS000334 variants -> gene, using MY Module 2 GWAS Catalog file (MAPPED_GENE)
hits = (gw[gw["SNPS"].isin(pgs["variant"])]
        .sort_values("P-VALUE")
        .drop_duplicates("SNPS")[["SNPS", "MAPPED_GENE", "P-VALUE", "INTERGENIC"]]
        .rename(columns={"SNPS": "variant", "MAPPED_GENE": "mapped_gene",
                         "P-VALUE": "gwas_p", "INTERGENIC": "intergenic"}))
v = pgs.merge(hits, on="variant", how="left")
my_genes = set(tgt["gene"])
def pick(mg):
    if pd.isna(mg): return None
    cands = [g.strip() for part in str(mg).split(" - ") for g in part.split(",")]
    cands = [g for g in cands if g in my_genes]
    return cands[0] if cands else None
v["graph_gene"] = v["mapped_gene"].map(pick)
v.to_csv("data/pgs000334_variants.csv", index=False)

# 3) Ensembl / UniProt IDs for every gene that may enter the graph (from Module 3 proteome)
prot = pd.read_csv(SRC["proteome"], sep="\t", usecols=["gene", "accession", "ensembl_gene"])
want = my_genes | {"ACHE", "JAK1"}
prot[prot["gene"].isin(want)].to_csv("data/gene_ids.csv", index=False)
# 4) Patient layer from Module 6: APOE genotype + PGS000334 PRS for a small cohort.
#    Genotypes are real 1000 Genomes data; the case/control PHENOTYPE IS SIMULATED.
geno = pd.read_csv(SRC["geno"]); meta = pd.read_csv(SRC["meta"]); var = pd.read_csv(SRC["vars"])
alt = dict(zip(var["variant"], var["alt"])); ref = dict(zip(var["variant"], var["ref"]))
prs = 0
for _, r in pgs.iterrows():                      # same keep/flip harmonisation as Module 6
    d = geno[r["variant"]]
    if r["effect_allele"] == alt[r["variant"]]:   prs = prs + r["weight"] * d
    elif r["effect_allele"] == ref[r["variant"]]: prs = prs + r["weight"] * (2 - d)
z = (prs - prs.mean()) / prs.std()
cohort = meta.copy()
cohort["prs_z"] = z.round(3)
cohort["prs_percentile"] = (z.rank(pct=True) * 100).round(1)
n4 = geno["rs429358"].astype(int)                # ALT C = e4 allele
n2 = geno["rs7412"].astype(int)                  # ALT T = e2 allele
def apoe(a4, a2):
    alleles = ["e2"] * a2 + ["e4"] * a4
    alleles += ["e3"] * (2 - len(alleles))
    return "/".join(sorted(alleles)[:2])
cohort["apoe_genotype"] = [apoe(a, b) for a, b in zip(n4, n2)]
cohort["status"] = cohort["phenotype"].map({1: "case", 0: "control"})
print("PRS mean by ancestry (check vs Module 6):", cohort.groupby("ancestry")["prs_z"].mean().round(2).to_dict())
pick = pd.concat([cohort[cohort["ancestry"] == a].sample(6, random_state=6900)
                  for a in ["EUR", "AFR", "EAS", "SAS", "AMR"]])
pick = pick.reset_index(drop=True)
pick.insert(0, "patient_id", [f"PT{i+1:02d}" for i in range(len(pick))])
pick[["patient_id", "ancestry", "age", "apoe_genotype", "prs_z", "prs_percentile", "status"]] \
    .to_csv("data/patients_m6.csv", index=False)

print("wrote data/: targets_ad.csv, targets_ad_w3.csv, structure_assessment_ad.csv,"
      " anchor_variants.csv, pgs000334_variants.csv, gene_ids.csv, patients_m6.csv")
print(v[["variant", "mapped_gene", "graph_gene", "weight"]].to_string(index=False))
