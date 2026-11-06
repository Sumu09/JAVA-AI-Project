#!/usr/bin/env python3
"""
ButterflyAI — Phase 3A: Mega-Cluster Review Generator
=====================================================
Generates focused review artifacts for the 5 cross-species mega-clusters (>= 3 species):
  1. reports/phase3/mega_cluster_review.csv (Decision ledger)
  2. reports/phase3/mega_cluster_review.md (Analytical report)
  3. reports/phase3/mega_cluster_contact_sheet.html (Self-contained interactive visual contact sheet)
  4. reports/phase3/mega_cluster_review_guide.md (Human reviewer guide)

SAFEGUARDS:
  - Read-Only: Zero dataset images are modified, moved, renamed, or deleted.
"""

import os
import sys
import csv
import json
import base64
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset"
REPORTS_DIR = PROJECT_ROOT / "reports"
PHASE3_DIR = REPORTS_DIR / "phase3"
MASTER_CSV = PROJECT_ROOT / "pipeline" / "config" / "species_master.csv"
CS_CSV = REPORTS_DIR / "cross_species_duplicates.csv"
AUDIT_CSV = REPORTS_DIR / "contamination_audit_report.csv"
MANIFEST_FILE = DATASET_DIR / "quarantine" / "quarantine_manifest.json"


def load_species_master():
    master = {}
    with open(MASTER_CSV, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            master[r["folder_name"]] = r
    return master


def load_quarantine_map():
    if not MANIFEST_FILE.exists():
        return {}
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {r["original_path"]: r["quarantine_path"] for r in data.get("records", [])}


def load_audit_predictions():
    preds = {}
    if AUDIT_CSV.exists():
        with open(AUDIT_CSV, "r", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                preds[r["filepath"]] = (r["ai_prediction"], r["ai_confidence"])
    return preds


def generate_mega_cluster_artifacts():
    print("=" * 75)
    print("  ButterflyAI — Generating Phase 3A Mega-Cluster Review Artifacts")
    print("=" * 75)

    PHASE3_DIR.mkdir(parents=True, exist_ok=True)
    species_master = load_species_master()
    quarantine_map = load_quarantine_map()
    audit_preds = load_audit_predictions()

    # Read cross-species duplicates
    with open(CS_CSV, "r", encoding="utf-8") as f:
        all_cs_rows = list(csv.DictReader(f))

    # Group by cluster ID
    clusters = defaultdict(list)
    for r in all_cs_rows:
        clusters[r["group_id"]].append(r)

    # Filter for mega-clusters (>= 3 species)
    mega_cluster_ids = []
    for gid, rows in clusters.items():
        distinct_folders = set(r["folder_name"] for r in rows)
        if len(distinct_folders) >= 3:
            mega_cluster_ids.append(gid)

    # Sort descending by species count
    mega_cluster_ids.sort(key=lambda g: len(set(r["folder_name"] for r in clusters[g])), reverse=True)
    print(f"Identified {len(mega_cluster_ids)} mega-clusters with >= 3 conflicting species:\n  {', '.join(mega_cluster_ids)}")

    csv_rows = []
    md_sections = []
    html_cards = []

    for gid in mega_cluster_ids:
        c_rows = clusters[gid]
        sha = c_rows[0]["sha256"]
        total_files = len(c_rows)
        distinct_folders = sorted(list(set(r["folder_name"] for r in c_rows)))
        species_count = len(distinct_folders)

        species_names = [species_master.get(f, {}).get("scientific_name", f) for f in distinct_folders]
        class_ids = [species_master.get(f, {}).get("class_id", f.split("_")[0]) for f in distinct_folders]
        common_names = [species_master.get(f, {}).get("common_name", "") for f in distinct_folders]
        families = [species_master.get(f, {}).get("family", "") for f in distinct_folders]

        all_source_paths = [r["filepath"] for r in c_rows]

        # Find best representative image path (active first, then quarantine)
        sample_path = None
        sample_status = "UNKNOWN"
        for p_str in all_source_paths:
            p = PROJECT_ROOT / p_str
            if p.exists():
                sample_path = p_str
                sample_status = "ACTIVE"
                break
        if not sample_path:
            for p_str in all_source_paths:
                q_rel = quarantine_map.get(p_str)
                if q_rel and (PROJECT_ROOT / q_rel).exists():
                    sample_path = q_rel
                    sample_status = "QUARANTINED"
                    break

        if not sample_path:
            sample_path = all_source_paths[0]

        # Get AI prediction
        ai_lbl, ai_conf = audit_preds.get(all_source_paths[0], ("unknown", "0.0%"))
        ai_desc = f"{ai_lbl} ({ai_conf})"

        # Image dimensions & format & Base64 encoding
        sample_abs = PROJECT_ROOT / sample_path
        w, h, fmt = 0, 0, "UNKNOWN"
        b64_str = ""
        if sample_abs.exists():
            try:
                with Image.open(sample_abs) as img:
                    w, h = img.size
                    fmt = img.format
                b64_str = base64.b64encode(sample_abs.read_bytes()).decode("utf-8")
            except Exception:
                pass

        # Determine pre-filled review decision and notes
        if gid == "CSD-001":
            prefill_decision = "CONFIRMED_NON_BUTTERFLY"
            verified_species = ""
            action_plan = "PURGE_ALL_SAMPLES"
            reviewer_notes = "Electric guitar stock photo downloaded for 11 rare species. High-confidence non-biological noise."
        elif gid == "CSD-002":
            prefill_decision = "CONFIRMED_NON_BUTTERFLY"
            verified_species = ""
            action_plan = "PURGE_ALL_SAMPLES"
            reviewer_notes = "Envelope / document web graphic placeholder downloaded for 5 rare species. Non-biological noise."
        elif gid == "CSD-008":
            prefill_decision = "CONFIRMED_NON_BUTTERFLY"
            verified_species = ""
            action_plan = "PURGE_ALL_SAMPLES"
            reviewer_notes = "Web banner / medical graphic placeholder downloaded across 4 species. Non-biological noise."
        elif gid == "CSD-009":
            prefill_decision = "UNCERTAIN"
            verified_species = ""
            action_plan = "HOLD_IN_DATASET"
            reviewer_notes = "Authentic butterfly specimen in genus Graphium (Swordtail/Zebra). Pending taxonomist assignment between G. agetes, G. macareus, and G. xenocles."
        elif gid == "CSD-010":
            prefill_decision = "UNCERTAIN"
            verified_species = ""
            action_plan = "HOLD_IN_DATASET"
            reviewer_notes = "Authentic butterfly specimen in genus Athyma (Sergeant). Pending taxonomist assignment between A. ranga, A. pravara, and A. punctata."
        else:
            prefill_decision = "UNCERTAIN"
            verified_species = ""
            action_plan = "HOLD_IN_DATASET"
            reviewer_notes = "Pending manual inspection."

        csv_rows.append({
            "cluster_id": gid,
            "sha256": sha,
            "species_count": species_count,
            "total_files": total_files,
            "conflicting_species_names": " | ".join(species_names),
            "conflicting_class_ids": " | ".join(class_ids),
            "conflicting_folders": " | ".join(distinct_folders),
            "source_paths": " ; ".join(all_source_paths),
            "sample_image_path": sample_path,
            "image_status": sample_status,
            "image_dimensions": f"{w}x{h}",
            "predicted_ai_label": ai_desc,
            "review_decision": prefill_decision,
            "verified_correct_species": verified_species,
            "action_plan": action_plan,
            "reviewer_notes": reviewer_notes
        })

        # Build Markdown Section for this cluster
        md_sections.append(f"""### Cluster `{gid}` ({species_count} Species &bull; {total_files} Files)
- **SHA-256**: `{sha}`
- **Sample Image**: [`{sample_path}`](file://{sample_abs}) ({w}&times;{h} px, {fmt}, Status: `{sample_status}`)
- **Predicted Subject**: `{ai_desc}`
- **Pre-filled Determination**: **`{prefill_decision}`**
- **Action Plan**: `{action_plan}`
- **Reviewer Notes**: {reviewer_notes}

| Class ID | Scientific Name | Common Name | Family | File Path | Split |
| :---: | :--- | :--- | :--- | :--- | :---: |
""" + "\n".join([
            f"| `{r['class_id']}` | *{r['assigned_scientific_name']}* | {r['common_name']} | {species_master.get(r['folder_name'], {}).get('family', '')} | `{r['filepath']}` | `{r['split']}` |"
            for r in c_rows
        ]) + "\n")

        # Build HTML card with embedded base64 image
        mime = "image/jpeg" if fmt == "JPEG" else ("image/png" if fmt == "PNG" else "image/jpeg")
        data_uri = f"data:{mime};base64,{b64_str}" if b64_str else f"../../{sample_path}"

        species_rows_html = ""
        for r in c_rows:
            fld = r["folder_name"]
            meta_sp = species_master.get(fld, {})
            cid = meta_sp.get("class_id", r["class_id"])
            s_name = meta_sp.get("scientific_name", r["assigned_scientific_name"])
            c_name = meta_sp.get("common_name", r["common_name"])
            fam = meta_sp.get("family", "")
            species_rows_html += f"""
            <tr>
              <td><code>#{cid}</code></td>
              <td><strong><em>{s_name}</em></strong></td>
              <td>{c_name}</td>
              <td><span class="badge-fam">{fam}</span></td>
              <td><span class="badge-split">{r['split']}</span></td>
              <td><code class="path-text">{r['filepath']}</code></td>
            </tr>
            """

        # Pre-select radio buttons in HTML
        c_non_chk = "checked" if prefill_decision == "CONFIRMED_NON_BUTTERFLY" else ""
        c_but_chk = "checked" if prefill_decision == "CONFIRMED_BUTTERFLY" else ""
        c_unc_chk = "checked" if prefill_decision == "UNCERTAIN" else ""
        c_tax_chk = "checked" if prefill_decision == "NEEDS_TAXONOMIST" else ""

        html_cards.append(f"""
        <div class="mega-card" id="{gid}" data-cluster="{gid}">
          <div class="card-header">
            <div class="header-left">
              <span class="cluster-badge">{gid}</span>
              <span class="species-count-badge">{species_count} Species &bull; {total_files} Duplicate Files</span>
              <span class="hash-tag" title="{sha}">SHA: <code>{sha[:16]}...</code></span>
            </div>
            <div class="header-right">
              <span class="ai-tag">AI Screen: <strong>{ai_desc}</strong></span>
            </div>
          </div>

          <div class="card-grid">
            <div class="img-column">
              <div class="img-frame">
                <img src="{data_uri}" alt="{gid}" />
              </div>
              <div class="img-meta">
                <div><strong>Resolution:</strong> {w} &times; {h} px ({fmt})</div>
                <div><strong>Status:</strong> <span class="badge-status {sample_status.lower()}">{sample_status}</span></div>
                <div class="sample-path"><code>{sample_path}</code></div>
              </div>
            </div>

            <div class="details-column">
              <h4>Conflicting Species & Assigned Paths</h4>
              <table class="taxa-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Scientific Name</th>
                    <th>Common Name</th>
                    <th>Family</th>
                    <th>Split</th>
                    <th>Original Dataset Path</th>
                  </tr>
                </thead>
                <tbody>
                  {species_rows_html}
                </tbody>
              </table>

              <div class="decision-box">
                <div class="decision-title">Human Verification Decision</div>
                <div class="radio-group">
                  <label class="radio-label">
                    <input type="radio" name="decision_{gid}" value="CONFIRMED_NON_BUTTERFLY" {c_non_chk} />
                    <span class="choice-text junk">CONFIRMED_NON_BUTTERFLY</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision_{gid}" value="CONFIRMED_BUTTERFLY" {c_but_chk} />
                    <span class="choice-text butterfly">CONFIRMED_BUTTERFLY</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision_{gid}" value="UNCERTAIN" {c_unc_chk} />
                    <span class="choice-text uncertain">UNCERTAIN</span>
                  </label>
                  <label class="radio-label">
                    <input type="radio" name="decision_{gid}" value="NEEDS_TAXONOMIST" {c_tax_chk} />
                    <span class="choice-text taxo">NEEDS_TAXONOMIST</span>
                  </label>
                </div>

                <div class="inputs-row">
                  <div class="input-field">
                    <label>Verified Species (if CONFIRMED_BUTTERFLY):</label>
                    <input type="text" id="verified_{gid}" value="{verified_species}" placeholder="e.g. Graphium agetes" />
                  </div>
                  <div class="input-field flex-2">
                    <label>Reviewer Notes & Justification:</label>
                    <input type="text" id="notes_{gid}" value="{reviewer_notes}" />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        """)

    # 1. Write CSV review file
    csv_file = PHASE3_DIR / "mega_cluster_review.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "cluster_id", "sha256", "species_count", "total_files",
            "conflicting_species_names", "conflicting_class_ids", "conflicting_folders",
            "source_paths", "sample_image_path", "image_status", "image_dimensions",
            "predicted_ai_label", "review_decision", "verified_correct_species",
            "action_plan", "reviewer_notes"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)
    print(f"[1/4] Generated {csv_file.name}")

    # 2. Write Markdown review report
    md_file = PHASE3_DIR / "mega_cluster_review.md"
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(f"""# Phase 3A: Cross-Species Mega-Clusters Forensic Review

**Review Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Target Clusters**: **5 Mega-Clusters** (&ge; 3 species, 26 total files)  
**Interactive Visual Contact Sheet**: [`mega_cluster_contact_sheet.html`](file://{PHASE3_DIR / 'mega_cluster_contact_sheet.html'})  
**Review Decision Ledger**: [`mega_cluster_review.csv`](file://{csv_file})  
**Validator Tool**: [`pipeline/tools/validate_phase3_review.py`](file://{PROJECT_ROOT / 'pipeline' / 'tools' / 'validate_phase3_review.py'})

---

## 1. Executive Summary

In a butterfly classification dataset, a single image hash appearing under 3 or more species represents high-severity cross-contamination. These 5 clusters account for **26 total image files** spanning across **26 species folders**.

| Cluster ID | Conflicting Species | Total Files | Sample Image | AI Screen | Pre-filled Determination | Recommended Action |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **`CSD-001`** | **11 species** | 11 files | `0900017.jpg` | `electric_guitar (53.3%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 11 folders |
| **`CSD-002`** | **5 species** | 5 files | `0990017.jpg` | `envelope (14.5%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 5 folders |
| **`CSD-008`** | **4 species** | 4 files | `1190025.jpg` | `stethoscope (21.0%)` | **`CONFIRMED_NON_BUTTERFLY`** | Purge from all 4 folders |
| **`CSD-009`** | **3 species** | 3 files | `0930023.jpg` | `lycaenid (22.7%)` | **`UNCERTAIN`** | Hold pending taxonomist review |
| **`CSD-010`** | **3 species** | 3 files | `1050023.jpg` | `admiral (69.4%)` | **`UNCERTAIN`** | Hold pending taxonomist review |

---

## 2. Cluster Details & Evidence

""" + "\n---\n\n".join(md_sections) + f"""
---

## 3. Human Review Instructions

1. Open [`mega_cluster_contact_sheet.html`](file://{PHASE3_DIR / 'mega_cluster_contact_sheet.html'}) in your web browser.
2. Inspect the high-resolution images for each of the 5 clusters.
3. Review or adjust determinations in [`mega_cluster_review.csv`](file://{csv_file}).
4. Run the validator to verify decision consistency:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3_review.py
   ```
5. No images will be moved or quarantined until you review and approve the validated plan.
""")
    print(f"[2/4] Generated {md_file.name}")

    # 3. Write Self-Contained HTML Contact Sheet
    html_file = PHASE3_DIR / "mega_cluster_contact_sheet.html"
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ButterflyAI — Mega-Clusters Visual Contact Sheet</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #fcfbf7; color: #1e293b; margin: 0; padding: 24px; }}
    header {{ background: #1b4d3e; color: #fff; padding: 24px 32px; border-radius: 8px; margin-bottom: 24px; border-bottom: 3px solid #d4a017; }}
    header h1 {{ margin: 0 0 6px 0; font-size: 24px; letter-spacing: -0.5px; }}
    header p {{ margin: 0; opacity: 0.9; font-size: 14px; }}
    .stats-bar {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }}
    .stat-card {{ background: #fff; padding: 16px; border-radius: 8px; border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }}
    .stat-val {{ font-size: 26px; font-weight: bold; color: #1b4d3e; }}
    .stat-lbl {{ font-size: 11px; text-transform: uppercase; color: #64748b; margin-top: 4px; letter-spacing: 0.5px; }}
    
    .mega-card {{ background: #fff; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 28px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); overflow: hidden; }}
    .card-header {{ background: #f8fafc; padding: 14px 24px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; }}
    .header-left {{ display: flex; align-items: center; gap: 12px; }}
    .cluster-badge {{ background: #1b4d3e; color: #fff; font-family: monospace; font-size: 13px; font-weight: bold; padding: 4px 8px; border-radius: 4px; }}
    .species-count-badge {{ background: #fef3c7; color: #92400e; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 12px; }}
    .hash-tag {{ font-size: 12px; color: #64748b; }}
    .ai-tag {{ background: #e0f2fe; color: #0369a1; font-size: 12px; padding: 4px 10px; border-radius: 4px; }}

    .card-grid {{ display: grid; grid-template-columns: 340px 1fr; gap: 24px; padding: 24px; }}
    .img-column {{ display: flex; flex-direction: column; gap: 12px; }}
    .img-frame {{ width: 100%; height: 260px; background: #0f172a; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
    .img-frame img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
    .img-meta {{ background: #f8fafc; padding: 12px; border-radius: 6px; font-size: 12px; color: #475569; display: flex; flex-direction: column; gap: 6px; border: 1px solid #e2e8f0; }}
    .sample-path {{ word-break: break-all; font-size: 11px; }}
    .badge-status {{ font-size: 10px; font-weight: bold; padding: 2px 6px; border-radius: 3px; text-transform: uppercase; }}
    .badge-status.active {{ background: #dcfce7; color: #166534; }}
    .badge-status.quarantined {{ background: #fee2e2; color: #991b1b; }}

    .details-column {{ display: flex; flex-direction: column; gap: 16px; }}
    .details-column h4 {{ margin: 0; font-size: 14px; text-transform: uppercase; color: #334155; letter-spacing: 0.5px; }}
    .taxa-table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
    .taxa-table th {{ background: #f1f5f9; text-align: left; padding: 8px 12px; color: #475569; font-weight: 600; border-bottom: 1px solid #cbd5e1; }}
    .taxa-table td {{ padding: 8px 12px; border-bottom: 1px solid #e2e8f0; }}
    .taxa-table tr:hover {{ background: #f8fafc; }}
    .badge-fam {{ background: #f1f5f9; color: #475569; padding: 2px 6px; border-radius: 3px; font-size: 11px; }}
    .badge-split {{ font-weight: 600; font-size: 11px; text-transform: uppercase; color: #64748b; }}
    .path-text {{ color: #64748b; font-size: 11px; }}

    .decision-box {{ background: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 16px; margin-top: auto; }}
    .decision-title {{ font-weight: 700; font-size: 13px; color: #92400e; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.5px; }}
    .radio-group {{ display: flex; gap: 16px; margin-bottom: 12px; flex-wrap: wrap; }}
    .radio-label {{ display: flex; align-items: center; gap: 6px; cursor: pointer; font-size: 13px; font-weight: 500; }}
    .choice-text.junk {{ color: #dc2626; }}
    .choice-text.butterfly {{ color: #16a34a; }}
    .choice-text.uncertain {{ color: #d97706; }}
    .choice-text.taxo {{ color: #2563eb; }}

    .inputs-row {{ display: flex; gap: 12px; }}
    .input-field {{ display: flex; flex-direction: column; gap: 4px; flex: 1; }}
    .input-field.flex-2 {{ flex: 2; }}
    .input-field label {{ font-size: 11px; color: #64748b; font-weight: 600; }}
    .input-field input {{ padding: 6px 10px; border-radius: 4px; border: 1px solid #cbd5e1; font-size: 12px; }}

    .instructions-box {{ background: #fff; padding: 20px 24px; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 24px; }}
    .instructions-box h3 {{ margin: 0 0 8px 0; font-size: 16px; color: #1b4d3e; }}
    .instructions-box ol {{ margin: 0; padding-left: 20px; font-size: 13px; color: #334155; line-height: 1.6; }}
  </style>
</head>
<body>
  <header>
    <h1>ButterflyAI — Phase 3A: Cross-Species Mega-Clusters Visual Contact Sheet</h1>
    <p>Human-in-the-Loop Inspection of the 5 High-multiplicity Duplicate Clusters (&ge; 3 conflicting species)</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card"><div class="stat-val">5</div><div class="stat-lbl">Mega-Clusters</div></div>
    <div class="stat-card"><div class="stat-val">26</div><div class="stat-lbl">Conflicting Taxa</div></div>
    <div class="stat-card"><div class="stat-val">26</div><div class="stat-lbl">Total Files Involved</div></div>
    <div class="stat-card"><div class="stat-val">100%</div><div class="stat-lbl">Self-Contained Embedded Images</div></div>
  </div>

  <div class="instructions-box">
    <h3>Reviewer Protocol</h3>
    <ol>
      <li>Inspect the high-resolution specimen or object photo in the left column.</li>
      <li>Verify whether the image depicts a butterfly or obvious non-biological crawler junk (e.g. electric guitars, envelopes, banner graphics).</li>
      <li>For genuine butterflies (*Graphium* or *Athyma*), select <code>UNCERTAIN</code> or <code>NEEDS_TAXONOMIST</code> unless you can definitively assign the species.</li>
      <li>Save decisions into <code>reports/phase3/mega_cluster_review.csv</code>, then run <code>.venv/bin/python pipeline/tools/validate_phase3_review.py</code>.</li>
    </ol>
  </div>

  <div class="cards-container">
    {"".join(html_cards)}
  </div>
</body>
</html>"""
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[3/4] Generated {html_file.name}")

    # 4. Write Human Reviewer Guide
    guide_file = PHASE3_DIR / "mega_cluster_review_guide.md"
    with open(guide_file, "w", encoding="utf-8") as f:
        f.write(f"""# Mega-Cluster Review Guide (Phase 3A)

This guide provides instructions for conducting human-in-the-loop biological review of the **5 cross-species mega-clusters** identified in the ButterflyAI dataset.

---

## 1. Files & Tooling

| Artifact | Path | Purpose |
| :--- | :--- | :--- |
| **Interactive Contact Sheet** | [`reports/phase3/mega_cluster_contact_sheet.html`](file://{html_file}) | Self-contained visual sheet with embedded high-res images and conflicting taxa. |
| **Review Decision Ledger** | [`reports/phase3/mega_cluster_review.csv`](file://{csv_file}) | The authoritative CSV where human determinations are recorded. |
| **Cluster Review Report** | [`reports/phase3/mega_cluster_review.md`](file://{md_file}) | Detailed forensic background and path breakdown. |
| **Decision Validator** | [`pipeline/tools/validate_phase3_review.py`](file://{PROJECT_ROOT / 'pipeline' / 'tools' / 'validate_phase3_review.py'}) | Automated script to validate reviewer decisions before execution. |

---

## 2. Review Decision Rules

For each of the 5 clusters, the `review_decision` field in [`mega_cluster_review.csv`](file://{csv_file}) must be set to exactly one of the following 4 values:

1. **`CONFIRMED_NON_BUTTERFLY`**:
   - **Criteria**: The image is unambiguous web crawler noise (e.g. electric guitar, postal envelope, website header, medical diagram, unrelated animal).
   - **Action Plan**: Automatically set to `PURGE_ALL_SAMPLES`.
   - **Verified Species**: Leave empty.

2. **`CONFIRMED_BUTTERFLY`**:
   - **Criteria**: The image is a genuine butterfly and you have verified the single correct species among the conflicting options.
   - **Action Plan**: Automatically set to `REASSIGN_TO_VERIFIED`.
   - **Verified Species**: Must be set to the exact scientific name (e.g. `Graphium agetes`).

3. **`UNCERTAIN`**:
   - **Criteria**: The image is a genuine butterfly, but visual ambiguity prevents assigning it to one species without dissection or expert specimen comparison.
   - **Action Plan**: Automatically set to `HOLD_IN_DATASET`.
   - **Verified Species**: Leave empty.

4. **`NEEDS_TAXONOMIST`**:
   - **Criteria**: The image requires consultation with an entomologist or specimen voucher specialist.
   - **Action Plan**: Automatically set to `HOLD_IN_DATASET`.
   - **Verified Species**: Leave empty.

---

## 3. Step-by-Step Instructions

1. **Open the visual contact sheet**:
   ```bash
   open reports/phase3/mega_cluster_contact_sheet.html
   ```
   Or double-click the file in Finder to view it in Safari / Chrome.

2. **Edit the decision ledger**:
   Open [`reports/phase3/mega_cluster_review.csv`](file://{csv_file}) in VS Code or any text editor.
   Review each cluster row and adjust `review_decision` or `reviewer_notes` if needed.

3. **Validate decisions**:
   Run the validator script:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3_review.py
   ```
   The validator will verify that:
   - All 5 cluster IDs are present.
   - Every decision is one of the 4 allowed values.
   - No contradictory fields exist (e.g. `CONFIRMED_BUTTERFLY` without specifying the species).

4. **Approval**:
   Once validated, you can approve Phase 3B (quarantine execution of confirmed junk). Zero files are moved until you approve.
""")
    print(f"[4/4] Generated {guide_file.name}")


if __name__ == "__main__":
    generate_mega_cluster_artifacts()
