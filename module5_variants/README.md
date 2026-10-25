# BIOT 6900 · Module 5 Assignment (Computational Lab 5)

**Name:** Sharath Mandula
**Gene:** CYP2C19 (assigned)

## Files
- `BIOT6900_Module5_Part3_Assignment.ipynb` — completed notebook (runs top to bottom)
- `pgx_classified_CYP2C19.csv` — 33 VUS with CADD evidence and provisional calls
- `BIOT6900_Module5_Report_CYP2C19.pdf` — report (Q6)

## AlphaGenome Atlas
**Not run.** The `alphagenome` client was not installed in my environment, so the Atlas
cell was skipped (`SKIP_ATLAS = True`). No AVI scores were used. The Atlas section of the report
is answered from reasoning.

## Fallbacks / what didn't work
- **Calibration:** CYP2C19 had 0 P/LP and 5 B/LB variants with a CADD score, which is too few
  to calibrate. Following the small-gene route, I pooled with **DPYD** (pooled set: 39 P/LP,
  72 B/LB). All P/LP variants come from DPYD, so the bands do not transfer cleanly to CYP2C19.
  This is discussed in the report (section 6.1).
- One CADD band, (25,30], rests on only 4 variants and was not applied to VUS.
- Allele-frequency filtering uses global gnomAD AF, not popmax.
- The `data/` folder is excluded from the repo via `.gitignore`.
