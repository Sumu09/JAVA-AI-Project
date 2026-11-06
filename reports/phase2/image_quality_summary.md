# Active Dataset Image Quality & Geometric Assessment

**Analysis Date**: 2026-11-02 23:25:51  
**Total Active Images Audited**: **4,085** (`dataset/train/`: 3,113, `dataset/test/`: 972)  
**Corrupted Files**: **0**

---

## 1. Dimensional Metrics

| Metric | Width (px) | Height (px) | Aspect Ratio (W/H) | File Size (KB) |
| :--- | :---: | :---: | :---: | :---: |
| **Minimum** | 56 px | 56 px | 0.43:1 | 3.93 KB |
| **Maximum** | 6,120 px | 4,000 px | 2.95:1 | 9,946.27 KB |
| **Median** | **736 px** | **574 px** | **1.34:1** | **137.8 KB** |
| **Mean** | 868.8 px | 669.3 px | 1.34:1 | 266.4 KB |

---

## 2. Resolution Distribution Tiers

| Resolution Tier | Definition | Image Count | Proportion | Assessment & Biological Note |
| :--- | :--- | :---: | :---: | :--- |
| **Thumbnail Micro** | min(W, H) &lt; 150 px | **30** | 0.7% | Extremely small; prone to feature loss during model resizing. |
| **Low Resolution** | 150 &le; min(W, H) &lt; 300 px | **516** | 12.6% | **Retained Museum Specimens**: Genuine historical specimen photos from biodiversity portals. |
| **Standard ML Resolution** | 300 &le; min(W, H) &lt; 800 px | **2409** | 59.0% | **Optimal Model Training**: Crisp resolution suitable for standard 224x224 or 299x299 CNN backbones. |
| **High Resolution / Macro** | min(W, H) &ge; 800 px | **1130** | 27.7% | Exceptional morphological wing detail, scales, and venation. |

---

## 3. Geometric Aspect Ratio Distribution

| Aspect Tier | Range | Count | Proportion |
| :--- | :--- | :---: | :---: |
| **Landscape** | $W/H > 1.25$ | **2945** | 72.1% |
| **Square** | $0.8 \le W/H \le 1.25$ | **925** | 22.6% |
| **Portrait** | $W/H < 0.8$ | **209** | 5.1% |
| **Extreme Wide** | $W/H > 2.5$ | **6** | 0.15% |
| **Extreme Tall** | $W/H < 0.4$ | **0** | 0.00% |

---

## 4. File Formats & Compression

- **JPEG / JPG**: **3,006 images** (73.6%)
- **PNG**: **862 images** (21.1%)
- **WEBP**: **211 images** (5.2%)
- **Suspiciously Small Files (< 10 KB)**: **45 images**
- **Heavy / Raw Files (> 2 MB)**: **44 images**
