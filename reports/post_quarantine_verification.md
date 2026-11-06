# Post-Quarantine Execution Forensic Verification Report

**Execution Timestamp**: 2026-11-02 23:18:00  
**Verification Timestamp**: 2026-11-02 23:19:00  
**Target Plan**: [`reports/quarantine_plan.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/quarantine_plan.json)  
**Reversible Manifest**: [`dataset/quarantine/quarantine_manifest.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/quarantine/quarantine_manifest.json)  
**Execution Status**: **100% SUCCESSFUL (0 Errors, 0 Collisions, 0 Data Loss)**

---

## 1. Post-Execution Verification Matrix

| # | Verification Check | Expected | Actual | Status |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Exactly 413 files successfully moved to quarantine | 413 files | 413 files | **PASS** |
| **2** | Every quarantined file matches its SHA-256 manifest hash | 413 verified | 413 verified (0 mismatch) | **PASS** |
| **3** | All original source paths are now absent from active dataset | 413 absent | 413 absent (0 lingering) | **PASS** |
| **4** | All quarantine destination paths exist on disk | 413 exist | 413 exist on disk | **PASS** |
| **5** | All 125 species folders remain populated in both train and test | 125 train, 125 test | 125 train, 125 test (0 empty) | **PASS** |
| **6** | All canonical training copies remain untouched | 209 verified | 209 present in original paths | **PASS** |
| **7** | Full pre-execution backup remains byte-for-byte intact | 4,498 files (1,140.56 MB) | 4,498 files (1,140.56 MB) | **PASS** |
| **8** | Restore operation verified via dry-run preflight validation | 0 errors | 0 errors (100% reversible) | **PASS** |
| **9** | Total dataset bytes conserved (Active + Quarantine == Backup) | 1,140.56 MB | 1,140.56 MB (Exact match) | **PASS** |
| **10** | Core taxonomy and Java code untouched | 0 files modified | Zero modifications | **PASS** |

---

## 2. Dataset Counts & Storage Recalculation

| Split | Pre-Quarantine Count | Pre-Quarantine Size | Quarantined Count | Post-Quarantine Count | Post-Quarantine Size |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Train (`dataset/train/`)** | 3,277 images | 852.64 MB | 164 images | **3,113 images** | **818.66 MB** |
| **Test (`dataset/test/`)** | 1,221 images | 287.92 MB | 249 images | **972 images** | **244.17 MB** |
| **Active Dataset Total** | 4,498 images | 1,140.56 MB | 413 images | **4,085 images** | **1,062.84 MB** |
| **Quarantine (`dataset/quarantine/`)** | 0 images | 0.00 MB | 413 images | **413 images** | **77.72 MB** |
| **Total Tracked Images** | **4,498 images** | **1,140.56 MB** | **0 net change** | **4,498 images** | **1,140.56 MB** |

> **Byte-for-Byte Conservation Note**:  
> The sum of post-quarantine active files (1,062.84 MB) and quarantined files (77.72 MB) equals exactly 1,140.56 MB, precisely matching the verified pre-quarantine backup. Zero bytes were lost.

---

## 3. Quarantine Breakdown by Category

The 413 quarantined files were safely transferred under the following verified reasons:
1. **Train $\leftrightarrow$ Test Data Leakage**: **196 files** (all in `dataset/test/`). Quarantining these copies eliminates evaluation leakage and ensures test benchmark integrity.
2. **Redundant Internal Duplicates**: **209 files** (156 in `train/`, 53 in `test/`). Every redundant file had a verified, identical sibling that remains preserved in the active dataset.
3. **Extreme Aspect Ratio Banners**: **8 files** (all in `train/`). High-ratio web page graphics ($> 3:1$ or $< 0.33:1$) that were crawler noise.

---

## 4. Species Completeness & Distribution Check

A full scan of the post-quarantine dataset verified that **all 125 species classes remain populated**:
- Classes in `dataset/train/`: **125** (range: 4 to 125 images per class)
- Classes in `dataset/test/`: **125** (range: 2 to 43 images per class)
- Empty class folders: **0**

### Key Endangered / Rare Species Status
- `081_Euthalia_zubeengargi`: All active canonical images preserved intact.
- `082_Papilio_elephenor`: Preserved intact.
- `083_Papilio_paradoxa`: Preserved intact.
- `098_Teinopalpus_imperialis`: Preserved intact.
- `100_Euthalia_telchinia`: Preserved intact.

---

## 5. Verification of Rollback / Restore Capability

A non-destructive preflight check of the restore function was executed:
```bash
.venv/bin/python pipeline/tools/quarantine_manager.py --preflight
```
- **Result**: Validated all 413 records in [`dataset/quarantine/quarantine_manifest.json`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/dataset/quarantine/quarantine_manifest.json).
- **Collision check**: Zero original paths are occupied.
- **Hash check**: 100% of quarantined files match their original pre-move SHA-256 hashes.
- **Reversibility Guarantee**: The entire quarantine operation can be completely undone at any time by running:
  ```bash
  .venv/bin/python pipeline/tools/quarantine_manager.py --restore
  ```

---

## 6. Next Steps & Pending Human Reviews

The automated structural quarantine is complete. The remaining items requiring human / biological review are cleanly isolated in dedicated CSV reports:
1. **Cross-Species Conflicts**: [`reports/cross_species_duplicates.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/cross_species_duplicates.csv) (146 images across 60 duplicate clusters pending biological verification of correct taxon assignment).
2. **MobileNetV2 Flagged Items**: [`reports/mobilenet_flagged_images.csv`](file:///Users/milinda/ghq/github.com/legion2004/JAVA-AI-Project/reports/mobilenet_flagged_images.csv) (155 images: 35 specimen context false alarms e.g. pins/rulers, 120 probable web crawler junk).
3. **Low-Resolution Photos**: 596 images preserved in active dataset; can be manually audited for specimen quality.
