# Module 10 — Medical Imaging AI: Build It, Then Break It

**BIOT 6900 · AI-Powered Biotech Workflows · Computational Lab 10 (Graded Notebook 3 of 3) · Fall 2026**
**Student:** Sharath Mandula

> **The question:** not "can I get high accuracy?" but **"can I prove whether to believe it?"**

I fine-tuned a pretrained DenseNet121 to classify colorectal tumour vs. normal tissue (PathMNIST), designed my own confounder (a **scanner/slide-label tag** on tumour tiles), and proved, using a clean control model, that a confounded model learned the shortcut.

---

## Files in this folder

| File / folder | What it is |
|---|---|
| `BIOT6900_Module10_Graded.ipynb` | Graded notebook, Parts A–D, fully executed |
| `BIOT6900_Module10_Report.pdf` | Part E: 4-page report (confounder, evidence, verdict, deployment & trust, APA references) |
| `figures/` | All figures saved by the notebook (confusion matrix, Grad-CAM/occlusion maps, scanner tag, Part D heatmaps) |
| `results/module10_results.csv` | Every number quoted in the report |
| `data/` | `pathmnist_tumour_vs_normal_subset.npz` (provided on Canvas; ~70 MB) |
| `README.md` | This file |

---

## What each part does

| Part | Task | Where |
|---|---|---|
| **A** | Fine-tune ImageNet-pretrained DenseNet121 on clean tiles; report validation + test accuracy | Notebook, Part A |
| **B** | Probe the clean model with Grad-CAM **and** occlusion; score the five-point skeptic's checklist with measured numbers | Notebook, Part B |
| **C** | Inject my own confounder (scanner tag) into the tumour class in train + validation and retrain | Notebook, Part C |
| **D** | Reliance battery on **both** models: heatmaps, reliance test, flip rate, clean-control comparison | Notebook, Part D |
| **E** | Written report | `BIOT6900_Module10_Report.pdf` |

---

## My confounder

A small off-white **barcode label** (14 × 36 px, top-left corner, **3.1% of a 128-px tile**) added to every **tumour** tile in training and validation.

**Why it's realistic:** slide scanners and lab systems stamp labels, barcodes and site watermarks into digital slides. If tumour cases come mostly from one site whose pipeline leaves a mark, the mark correlates with the diagnosis. This is the same mechanism as the documented site-specific signatures in TCGA histology (Howard et al., 2021).

---

## Key results

| Measure | Clean control | Confounded |
|---|---|---|
| Validation accuracy | 0.970 | **1.000** (tagged val) |
| Test accuracy, untagged tiles ("new site") | 0.950 | **0.748** |
| Tumour recall **with** tag | 0.930 | 1.000 |
| Tumour recall **without** tag | 0.937 | **0.497** |
| Normals called tumour, no tag → + tag (flip) | 3.7% → 5.3% | **0.0% → 87.3%** |
| Occlusion evidence on the tag | 2% | **62%** |
| Grad-CAM evidence on the tag | 1% | 10% |

Clean model (Part A): sensitivity 0.937, specificity 0.963. Skeptic's checklist (Part B): evidence on tissue, not the border (27% vs. 29% border area); maps change with target class (r = −0.51); Grad-CAM and occlusion agree (r = 0.22); robust to a simulated stain shift (0.950 → 0.938 / 0.952).

### Verdict
**The confounded model learned the scanner-tag shortcut.** Removing the tag halves its tumour recall, adding it flips 87% of normal tiles to "tumour", and occlusion puts 62% of its evidence on 3.1% of the image. The clean control, which never saw the tag, ignores it on every measure. **That gap is the proof.** The confounded model's perfect validation accuracy was the alarm, not the achievement.

---

## How to reproduce

**Requirements:** Windows/macOS/Linux laptop, CPU only (no GPU needed). Runtime ≈ 8–10 minutes.

1. Create or activate the course environment (Anaconda Prompt):
   ```
   conda activate biot6900
   pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
   pip install "monai[pillow]" "medmnist>=3.0" scikit-learn matplotlib jupyterlab ipykernel
   python -m ipykernel install --user --name biot6900 --display-name "Python (biot6900)"
   ```
2. Put `pathmnist_tumour_vs_normal_subset.npz` (from Canvas) in a `data/` folder next to the notebook.
   If it's missing, the notebook downloads PathMNIST (~1.1 GB) and rebuilds the subset.
3. Launch Jupyter **from the activated environment**:
   ```
   jupyter lab
   ```
4. Open the notebook and select the kernel **Python (biot6900)**.
5. Run **Kernel → Restart Kernel and Run All Cells**.

**Tested with:** Python 3.11, PyTorch 2.15.0 (CPU), MONAI 1.6.2, MedMNIST 3.0.2, scikit-learn 1.9.1.

**Troubleshooting:** `DLL load failed while importing _C` or `No module named torch` means the notebook is on the wrong kernel (Anaconda base). Switch to **Python (biot6900)** and restart.

**Settings:** 600 train / 400 val / 600 test tiles (balanced), 64-px tiles resized to 128 px, ImageNet normalisation, 3 epochs, Adam (lr 1e-4), batch 32, seed 0.

---

## References (APA 7)

- Howard, F. M., Dolezal, J., Kochanny, S., Schulte, J., Chen, H., Heij, L., Huo, D., Nanda, R., Olopade, O. I., Kather, J. N., Cipriani, N., Grossman, R. L., & Pearson, A. T. (2021). The impact of site-specific digital histology signatures on deep learning model accuracy and bias. *Nature Communications, 12*, Article 4423. https://doi.org/10.1038/s41467-021-24698-1
- Kather, J. N., Krisam, J., Charoentong, P., Luedde, T., Herpel, E., Weis, C.-A., Gaiser, T., Marx, A., Valous, N. A., Ferber, D., Jansen, L., Reyes-Aldasoro, C. C., Zörnig, I., Jäger, D., Brenner, H., Chang-Claude, J., Hoffmeister, M., & Halama, N. (2019). Predicting survival from colorectal cancer histology slides using deep learning: A retrospective multicenter study. *PLOS Medicine, 16*(1), Article e1002730. https://doi.org/10.1371/journal.pmed.1002730
- Selvaraju, R. R., Cogswell, M., Das, A., Vedantam, R., Parikh, D., & Batra, D. (2017). Grad-CAM: Visual explanations from deep networks via gradient-based localization. In *Proceedings of the IEEE International Conference on Computer Vision (ICCV)* (pp. 618–626). IEEE. https://doi.org/10.1109/ICCV.2017.74
- Yang, J., Shi, R., Wei, D., Liu, Z., Zhao, L., Ke, B., Pfister, H., & Ni, B. (2023). MedMNIST v2 - A large-scale lightweight benchmark for 2D and 3D biomedical image classification. *Scientific Data, 10*, Article 41. https://doi.org/10.1038/s41597-022-01721-8
- Zech, J. R., Badgeley, M. A., Liu, M., Costa, A. B., Titano, J. J., & Oermann, E. K. (2018). Variable generalization performance of a deep learning model to detect pneumonia in chest radiographs: A cross-sectional study. *PLOS Medicine, 15*(11), Article e1002683. https://doi.org/10.1371/journal.pmed.1002683
- Zeiler, M. D., & Fergus, R. (2014). Visualizing and understanding convolutional networks. In D. Fleet, T. Pajdla, B. Schiele, & T. Tuytelaars (Eds.), *Computer vision – ECCV 2014* (Lecture Notes in Computer Science, Vol. 8689, pp. 818–833). Springer. https://doi.org/10.1007/978-3-319-10590-1_53

---

*The scanner tag is synthetic, injected on purpose so the ground truth is known. PathMNIST is for research and education, not clinical use.*
