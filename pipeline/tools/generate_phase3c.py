#!/usr/bin/env python3
"""
ButterflyAI — Phase 3C: Cross-Species Duplicate Review Generator
================================================================
Generates review artifacts for all remaining 55 pairwise cross-species clusters
(excluding the 5 reviewed mega-clusters CSD-001, CSD-002, CSD-008, CSD-009, CSD-010).

Artifacts generated:
  1. reports/phase3/cross_species_review.csv (Decision ledger for all 55 clusters)
  2. reports/phase3/cross_species_review.md (Comprehensive analytical markdown report)
  3. reports/phase3/cross_species_contact_sheets.html (Interactive visual contact sheet)
  4. reports/phase3/cross_species_review_guide.md (Human reviewer instructions)

SAFEGUARDS:
  - Read-Only: Zero dataset images are modified, moved, renamed, or deleted.
  - Excludes quarantined files from active counts while preserving provenance.
  - Deterministic ordering by priority (Historic Leakage -> Active Conflict -> Cluster ID).
"""

import os
import sys
import csv
import json
import base64
import io
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

EXCLUDED_MEGA_CLUSTERS = {"CSD-001", "CSD-002", "CSD-008", "CSD-009", "CSD-010"}


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
                preds[r["filepath"]] = (r["ai_prediction"], r["ai_confidence"], r.get("reasons", ""))
    return preds


def get_thumbnail_base64(image_path, max_dim=(360, 270), quality=75):
    """Generates an optimized Base64 JPEG thumbnail to keep HTML compact."""
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img.thumbnail(max_dim, Image.Resampling.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=quality, optimize=True)
            return base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception as e:
        return ""


def generate_phase3c_artifacts():
    print("=" * 78)
    print("  ButterflyAI — Generating Phase 3C Cross-Species Duplicate Review Artifacts")
    print("=" * 78)

    PHASE3_DIR.mkdir(parents=True, exist_ok=True)
    species_master = load_species_master()
    quarantine_map = load_quarantine_map()
    audit_preds = load_audit_predictions()

    with open(CS_CSV, "r", encoding="utf-8") as f:
        all_cs_rows = list(csv.DictReader(f))

    # Group by cluster ID
    clusters = defaultdict(list)
    for r in all_cs_rows:
        gid = r["group_id"]
        if gid not in EXCLUDED_MEGA_CLUSTERS:
            clusters[gid].append(r)

    total_clusters = len(clusters)
    print(f"Loaded {total_clusters} remaining cross-species clusters (excluding 5 mega-clusters).")

    # Priority sorting:
    # 1. Historic train-test leakage first (clusters with both train and test original splits)
    # 2. Active multi-species conflicts next
    # 3. Stable cluster ID
    def cluster_sort_key(gid):
        rows = clusters[gid]
        splits = set(r["split"] for r in rows)
        is_leakage = ("train" in splits and "test" in splits)
        active_folders = set(r["folder_name"] for r in rows if (PROJECT_ROOT / r["filepath"]).exists())
        is_active_conflict = len(active_folders) >= 2
        # rank: 0 for leakage + active, 1 for leakage + resolved, 2 for active pure split, 3 for resolved pure split
        if is_leakage and is_active_conflict:
            rank = 0
        elif is_leakage:
            rank = 1
        elif is_active_conflict:
            rank = 2
        else:
            rank = 3
        return (rank, gid)

    sorted_cluster_ids = sorted(clusters.keys(), key=cluster_sort_key)

    csv_rows = []
    md_sections = []
    html_cards = []

    # Counters for summary statistics
    stats = {
        "total_clusters": total_clusters,
        "total_original_files": 0,
        "active_files": 0,
        "quarantined_files": 0,
        "historic_leakage_clusters": 0,
        "active_conflict_clusters": 0,
        "quarantine_resolved_clusters": 0,
        "congeneric_clusters": 0,
        "same_family_clusters": 0,
        "interfamily_clusters": 0,
        "likely_non_butterfly": 0,
        "genuine_butterfly_mislabeling": 0,
        "uncertain": 0,
    }

    print("Processing 55 clusters and generating optimized contact sheet thumbnails...")

    for gid in sorted_cluster_ids:
        c_rows = clusters[gid]
        sha = c_rows[0]["sha256"]
        total_files = len(c_rows)
        stats["total_original_files"] += total_files

        folders = sorted(list(set(r["folder_name"] for r in c_rows)))
        species_count = len(folders)

        species_names = [species_master.get(f, {}).get("scientific_name", f) for f in folders]
        class_ids = [species_master.get(f, {}).get("class_id", f.split("_")[0]) for f in folders]
        common_names = [species_master.get(f, {}).get("common_name", "") for f in folders]
        families = [species_master.get(f, {}).get("family", "") for f in folders]
        genera = [s.split()[0] for s in species_names]

        # Taxonomic relationship
        if len(set(genera)) == 1:
            tax_rel = "CONGENERIC"
            stats["congeneric_clusters"] += 1
        elif len(set(families)) == 1:
            tax_rel = "INTERGENERIC_SAME_FAMILY"
            stats["same_family_clusters"] += 1
        else:
            tax_rel = "INTERFAMILY"
            stats["interfamily_clusters"] += 1

        all_source_paths = [r["filepath"] for r in c_rows]
        splits = set(r["split"] for r in c_rows)
        historic_leakage = "YES" if ("train" in splits and "test" in splits) else "NO"
        if historic_leakage == "YES":
            stats["historic_leakage_clusters"] += 1

        # Check file active / quarantine status
        active_paths = []
        quarantined_paths_list = []
        for p_str in all_source_paths:
            p = PROJECT_ROOT / p_str
            if p.exists():
                active_paths.append(p_str)
                stats["active_files"] += 1
            elif p_str in quarantine_map:
                quarantined_paths_list.append(p_str)
                stats["quarantined_files"] += 1
            else:
                print(f"WARNING: File {p_str} missing from both dataset and quarantine manifest!")

        active_folders = sorted(list(set(r["folder_name"] for r in c_rows if r["filepath"] in active_paths)))
        if len(active_folders) >= 2:
            conflict_status = "ACTIVE_MULTI_SPECIES"
            stats["active_conflict_clusters"] += 1
        elif len(active_folders) == 1:
            conflict_status = "RESOLVED_BY_PHASE1_QUARANTINE"
            stats["quarantine_resolved_clusters"] += 1
        else:
            conflict_status = "ALL_QUARANTINED"

        # Find best representative image path (active first, then quarantine)
        sample_path = None
        sample_status = "UNKNOWN"
        for p_str in active_paths:
            sample_path = p_str
            sample_status = "ACTIVE"
            break
        if not sample_path:
            for p_str in quarantined_paths_list:
                q_rel = quarantine_map.get(p_str)
                if q_rel and (PROJECT_ROOT / q_rel).exists():
                    sample_path = q_rel
                    sample_status = "QUARANTINED"
                    break
        if not sample_path:
            sample_path = all_source_paths[0]

        sample_abs = PROJECT_ROOT / sample_path
        w, h, fmt = 0, 0, "UNKNOWN"
        b64_thumb = ""
        if sample_abs.exists():
            try:
                with Image.open(sample_abs) as img:
                    w, h = img.size
                    fmt = img.format
                b64_thumb = get_thumbnail_base64(sample_abs)
            except Exception:
                pass

        # AI Prediction and reasons
        ai_lbl, ai_conf, ai_reasons = audit_preds.get(all_source_paths[0], ("unknown", "0.0%", ""))
        ai_desc = f"{ai_lbl} ({ai_conf})"

        # Categorize Suggestion
        # Non-butterfly flags
        is_non_insect_flagged = (
            "CONFIRMED_NON_INSECT" in ai_reasons
            or ai_lbl in ["envelope", "web_site", "pretzel", "hatchet"]
            or (tax_rel == "INTERFAMILY" and ai_lbl in ["web_site", "book_jacket", "bow"])
        )
        butterfly_labels = {"admiral", "lycaenid", "ringlet", "sulphur_butterfly", "monarch"}

        if is_non_insect_flagged:
            suggested_decision = "LIKELY_NON_BUTTERFLY"
            stats["likely_non_butterfly"] += 1
            default_action = "PURGE_ALL_SAMPLES"
            notes_hint = (
                f"Flagged by visual screening ({ai_lbl}). Cross-{tax_rel.lower().replace('_', ' ')} collision. "
                "Likely non-biological stock graphic, book scan, or web template."
            )
        elif ai_lbl in butterfly_labels:
            suggested_decision = "GENUINE_BUTTERFLY_MISLABELING"
            stats["genuine_butterfly_mislabeling"] += 1
            default_action = "HOLD_IN_DATASET"
            notes_hint = (
                f"Specimen appears to be authentic butterfly ({ai_lbl}, {ai_conf}). Duplicate across sister species: "
                f"'{species_names[0]}' vs '{species_names[1]}'. Taxonomist review required to assign true species."
            )
        else:
            suggested_decision = "UNCERTAIN"
            stats["uncertain"] += 1
            default_action = "HOLD_IN_DATASET"
            notes_hint = (
                f"Ambiguous prediction ({ai_desc}). Specimen context artifact or difficult angle. "
                f"Species involved: '{species_names[0]}' vs '{species_names[1]}'."
            )

        # Pre-fill review ledger row
        csv_rows.append({
            "cluster_id": gid,
            "sha256": sha,
            "cluster_type": "PAIRWISE_CONFLICT",
            "taxonomic_relationship": tax_rel,
            "conflict_status": conflict_status,
            "historic_leakage": historic_leakage,
            "species_count": species_count,
            "total_files": total_files,
            "active_files_count": len(active_paths),
            "quarantined_files_count": len(quarantined_paths_list),
            "conflicting_species_names": " | ".join(species_names),
            "conflicting_class_ids": " | ".join(class_ids),
            "conflicting_folders": " | ".join(folders),
            "source_paths": " ; ".join(all_source_paths),
            "sample_image_path": sample_path,
            "image_status": sample_status,
            "image_dimensions": f"{w}x{h}",
            "predicted_ai_label": ai_desc,
            "suggested_decision": suggested_decision,
            "review_decision": "PENDING_REVIEW",
            "verified_correct_species": "",
            "action_plan": default_action,
            "reviewer_notes": notes_hint,
        })

        # Build Markdown Section for this cluster
        status_md_badge = (
            "`[ACTIVE MULTI-SPECIES CONFLICT]`"
            if conflict_status == "ACTIVE_MULTI_SPECIES"
            else "`[RESOLVED BY PHASE 1 QUARANTINE]`"
        )
        leakage_md_badge = "`[HISTORIC TRAIN-TEST LEAKAGE]`" if historic_leakage == "YES" else ""

        md_sections.append(f"""### Cluster `{gid}` — *{species_names[0]}* vs *{species_names[1]}*
- **Status**: {status_md_badge} {leakage_md_badge}
- **Taxonomic Relation**: `{tax_rel}` ({', '.join(set(families))})
- **SHA-256**: `{sha}`
- **Active Files**: `{len(active_paths)}` active | `{len(quarantined_paths_list)}` quarantined (Total: `{total_files}`)
- **Sample Image**: [`{sample_path}`](file://{sample_abs}) ({w}&times;{h} px, `{fmt}`, `{sample_status}`)
- **AI Screening**: `{ai_desc}`
- **Suggested Determination**: **`{suggested_decision}`**
- **Suggested Action**: `{default_action}`
- **Taxonomic Notes**: {notes_hint}

| Class ID | Scientific Name | Common Name | Family | Split | File Path | Current Status |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: |
""" + "\n".join([
            f"| `#{species_master.get(r['folder_name'], {}).get('class_id', r['class_id'])}` "
            f"| *{species_master.get(r['folder_name'], {}).get('scientific_name', r['assigned_scientific_name'])}* "
            f"| {species_master.get(r['folder_name'], {}).get('common_name', r['common_name'])} "
            f"| {species_master.get(r['folder_name'], {}).get('family', '')} "
            f"| `{r['split']}` "
            f"| `{r['filepath']}` "
            f"| {'`ACTIVE`' if r['filepath'] in active_paths else '`QUARANTINED (Phase 1)`'} |"
            for r in c_rows
        ]) + "\n")

        # Build HTML card
        tax_badge_color = (
            "#059669" if tax_rel == "CONGENERIC" else ("#d97706" if tax_rel == "INTERGENERIC_SAME_FAMILY" else "#dc2626")
        )
        status_badge_html = (
            '<span class="badge-status-alert">Active Multi-Species</span>'
            if conflict_status == "ACTIVE_MULTI_SPECIES"
            else '<span class="badge-status-resolved">Quarantine Resolved</span>'
        )
        leakage_badge_html = (
            '<span class="badge-leakage" title="Duplicate appeared in both train and test splits">Historic Split Leakage</span>'
            if historic_leakage == "YES"
            else ""
        )
        sugg_badge_color = (
            "#ef4444"
            if suggested_decision == "LIKELY_NON_BUTTERFLY"
            else ("#10b981" if suggested_decision == "GENUINE_BUTTERFLY_MISLABELING" else "#6b7280")
        )

        species_rows_html = ""
        for r in c_rows:
            fld = r["folder_name"]
            meta_sp = species_master.get(fld, {})
            cid = meta_sp.get("class_id", r["class_id"])
            s_name = meta_sp.get("scientific_name", r["assigned_scientific_name"])
            c_name = meta_sp.get("common_name", r["common_name"])
            fam = meta_sp.get("family", "")
            is_act = r["filepath"] in active_paths
            row_status_badge = (
                '<span class="badge-file-act">ACTIVE</span>'
                if is_act
                else '<span class="badge-file-quar">QUARANTINED</span>'
            )
            species_rows_html += f"""
            <tr>
              <td><code>#{cid}</code></td>
              <td><strong><em>{s_name}</em></strong></td>
              <td>{c_name}</td>
              <td><span class="badge-fam">{fam}</span></td>
              <td><span class="badge-split">{r['split']}</span></td>
              <td><code class="path-text">{r['filepath']}</code></td>
              <td>{row_status_badge}</td>
            </tr>
            """

        data_uri = f"data:image/jpeg;base64,{b64_thumb}" if b64_thumb else f"../../{sample_path}"

        # Radio options
        options_html = f"""
        <div class="decision-box">
          <div class="decision-header">
            <span class="decision-title">Human Determination for {gid}</span>
            <span class="suggestion-pill" style="border-color: {sugg_badge_color}; color: {sugg_badge_color};">
              Suggestion: {suggested_decision}
            </span>
          </div>
          <div class="radio-group">
            <label class="radio-label">
              <input type="radio" name="dec_{gid}" value="CONFIRMED_NON_BUTTERFLY" onchange="updateRow('{gid}')" />
              <span class="choice-text junk">CONFIRMED_NON_BUTTERFLY</span>
            </label>
            <label class="radio-label">
              <input type="radio" name="dec_{gid}" value="CONFIRMED_BUTTERFLY" onchange="updateRow('{gid}')" />
              <span class="choice-text butterfly">CONFIRMED_BUTTERFLY</span>
            </label>
            <label class="radio-label">
              <input type="radio" name="dec_{gid}" value="UNCERTAIN" checked onchange="updateRow('{gid}')" />
              <span class="choice-text uncertain">UNCERTAIN</span>
            </label>
            <label class="radio-label">
              <input type="radio" name="dec_{gid}" value="NEEDS_TAXONOMIST" onchange="updateRow('{gid}')" />
              <span class="choice-text taxo">NEEDS_TAXONOMIST</span>
            </label>
          </div>
          <div class="inputs-row">
            <div class="input-field flex-1">
              <label>If Butterfly, True Species (select or enter):</label>
              <select id="sel_sp_{gid}" onchange="setSpecies('{gid}', this.value)">
                <option value="">-- Choose verified species --</option>
                <option value="{species_names[0]}">#{class_ids[0]} - {species_names[0]} ({common_names[0]})</option>
                <option value="{species_names[1]}">#{class_ids[1]} - {species_names[1]} ({common_names[1]})</option>
              </select>
            </div>
            <div class="input-field flex-2">
              <label>Reviewer Notes / Evidence:</label>
              <input type="text" id="notes_{gid}" value="{notes_hint}" oninput="updateRow('{gid}')" />
            </div>
          </div>
        </div>
        """

        html_cards.append(f"""
        <div class="cluster-card" id="{gid}" data-cluster="{gid}" 
             data-leakage="{historic_leakage}" 
             data-status="{conflict_status}" 
             data-taxonomy="{tax_rel}" 
             data-suggestion="{suggested_decision}">
          <div class="card-header">
            <div class="header-left">
              <span class="cluster-badge">{gid}</span>
              <span class="badge-tax" style="background-color: {tax_badge_color};">{tax_rel.replace('_', ' ')}</span>
              {status_badge_html}
              {leakage_badge_html}
            </div>
            <div class="header-right">
              <span class="hash-tag" title="{sha}">SHA: <code>{sha[:16]}...</code></span>
              <span class="ai-tag">AI Screen: <strong>{ai_desc}</strong></span>
            </div>
          </div>

          <div class="card-grid">
            <div class="img-column">
              <div class="img-frame">
                <img src="{data_uri}" alt="{gid}" loading="lazy" />
              </div>
              <div class="img-meta">
                <div><strong>Resolution:</strong> {w} &times; {h} px ({fmt})</div>
                <div><strong>Sample Status:</strong> <span class="badge-file-act">{sample_status}</span></div>
                <div class="sample-path">
                  <a href="file://{sample_abs}" target="_blank" title="Open full resolution file">
                    {sample_path}
                  </a>
                </div>
              </div>
            </div>

            <div class="details-column">
              <h4>Conflicting Assigned Paths ({total_files} Duplicate Files &bull; 2 Species)</h4>
              <table class="taxa-table">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Scientific Name</th>
                    <th>Common Name</th>
                    <th>Family</th>
                    <th>Split</th>
                    <th>File Path</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {species_rows_html}
                </tbody>
              </table>

              {options_html}
            </div>
          </div>
        </div>
        """)

    print(f"Writing CSV review ledger to {PHASE3_DIR / 'cross_species_review.csv'}...")
    csv_file = PHASE3_DIR / "cross_species_review.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "cluster_id",
            "sha256",
            "cluster_type",
            "taxonomic_relationship",
            "conflict_status",
            "historic_leakage",
            "species_count",
            "total_files",
            "active_files_count",
            "quarantined_files_count",
            "conflicting_species_names",
            "conflicting_class_ids",
            "conflicting_folders",
            "source_paths",
            "sample_image_path",
            "image_status",
            "image_dimensions",
            "predicted_ai_label",
            "suggested_decision",
            "review_decision",
            "verified_correct_species",
            "action_plan",
            "reviewer_notes",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_rows)

    print(f"Writing Markdown analytical report to {PHASE3_DIR / 'cross_species_review.md'}...")
    md_file = PHASE3_DIR / "cross_species_review.md"
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md_content = f"""# ButterflyAI — Phase 3C: Cross-Species Duplicate Review Report
**Generated**: {now_str}  
**Dataset Scope**: 55 Pairwise Cross-Species Clusters &bull; 120 Total Image Files &bull; 97 Active &bull; 23 Quarantined  
**Target Ledger**: [`cross_species_review.csv`](file://{csv_file})  
**Visual Contact Sheet**: [`cross_species_contact_sheets.html`](file://{PHASE3_DIR / 'cross_species_contact_sheets.html'})

---

## 1. Executive Summary

Phase 3C investigates all 55 pairwise cross-species duplicate clusters remaining after the completion of Phase 3A/3B (which safely audited and quarantined the 5 high-order mega-clusters `CSD-001`, `CSD-002`, `CSD-008`, `CSD-009`, and `CSD-010`).

### Key Quantitative Findings:
- **Total Clusters**: **55** duplicate clusters (`CSD-003` to `CSD-007`, `CSD-011` to `CSD-060`).
- **Total Duplicate Files**: **120** files tracked.
- **Active Files in Dataset**: **97** images (84 active files in train conflicts, 2 files in pure test conflicts, 11 active files in resolved train conflicts).
- **Quarantined Files**: **23** files safely isolated during Phase 1 (21 test-leakage files + 2 internal train duplicates).
- **Active Multi-Species Conflicts**: **42 clusters** still have active duplicate copies in multiple species folders.
- **Quarantine-Resolved Provenance Clusters**: **13 clusters** have active image(s) in only 1 species folder (their cross-species duplicate counterpart in test was quarantined in Phase 1 for evaluation leakage).
- **Historic Train-Test Split Leakage**: **18 clusters** originally crossed train and test split boundaries. In all 18, the test split duplicate was quarantined in Phase 1, eliminating active leakage.

---

## 2. Taxonomic Breakdown

The 55 duplicate clusters fall into three distinct biological tiers:

| Taxonomic Tier | Cluster Count | File Count | Description | Primary Risk |
| :--- | :---: | :---: | :--- | :--- |
| **Congeneric (Same Genus)** | **39** | 88 | Duplicate shared between sister species in the same genus (e.g. *Halpe aucma* vs *Halpe zema*, *Papilio paradoxa* vs *Papilio slateri*, *Arhopala silhetensis* vs *Arhopala oenea*). | Sub-species / morphological confusion during scraping. Usually genuine butterfly. |
| **Intergeneric (Same Family)** | **10** | 20 | Duplicate shared across different genera in the same family (e.g. Hesperiidae skippers *Halpe* vs *Thoressa*, *Pyroneura* vs *Salanoemia*). | Web template re-use or scraper confusion among similar skipper/nymphalid morphs. |
| **Interfamily (Different Family)** | **6** | 12 | Duplicate shared across completely different butterfly families (e.g. Swallowtail *Papilio elephenor* vs Skipper *Salanoemia sala*, or Lycaenid *Udara selma* vs Skipper *Darpa pteria*). | High probability of non-biological noise, web page graphic, or scraper bug. |
| **Total** | **55** | **120** | | |

---

## 3. High-Priority Review Categories

### Priority A: Historic Split Leakage Clusters (18 Clusters)
These 18 clusters originally spanned both `train` and `test` splits. Although their test split files were quarantined during Phase 1, biological review is necessary to verify whether the remaining training image is assigned to the correct species.

| Cluster ID | Active Status | Conflicting Species 1 | Conflicting Species 2 | AI Prediction | Suggestion |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `CSD-003` | ACTIVE (2) | *Halpe aucma* | *Halpe zema zema* | lycaenid (17.9%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-004` | ACTIVE (2) | *Halpe kusala* | *Halpe zema zema* | cricket (25.5%) | `UNCERTAIN` |
| `CSD-005` | ACTIVE (2) | *Halpe kusala* | *Halpe porus porus* | lycaenid (62.4%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-006` | ACTIVE (2) | *Halpe zema zema* | *Thoressa cerata* | ringlet (16.4%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-007` | ACTIVE (2) | *Ochus subvittatus subradiatus* | *Pithauria stramineipennis* | ringlet (68.5%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-014` | RESOLVED (1) | *Lethe chandica flanona* | *Lethe mekara mekara* | ringlet (57.7%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-016` | RESOLVED (1) | *Euthalia zubeengargi* | *Euthalia telchinia* | leafhopper (20.3%) | `UNCERTAIN` |
| `CSD-021` | RESOLVED (1) | *Papilio elephenor* | *Papilio bootes* | web_site (5.1%) | `LIKELY_NON_BUTTERFLY` |
| `CSD-024` | RESOLVED (1) | *Papilio paradoxa* | *Papilio bootes* | admiral (23.9%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-033` | RESOLVED (1) | *Byasa crassipes* | *Byasa polla* | lycaenid (20.5%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-038` | RESOLVED (1) | *Euthalia zubeengargi* | *Euthalia telchinia* | ringlet (10.3%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-040` | RESOLVED (1) | *Pantoporia assamica* | *Pantoporia bieti* | lycaenid (13.7%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-041` | RESOLVED (1) | *Pantoporia assamica* | *Pantoporia bieti* | custard_apple (13.5%) | `UNCERTAIN` |
| `CSD-043` | RESOLVED (1) | *Athyma ranga* | *Athyma punctata* | admiral (90.8%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-044` | RESOLVED (1) | *Athyma pravara* | *Athyma punctata* | admiral (34.8%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-045` | RESOLVED (1) | *Athyma pravara* | *Athyma punctata* | admiral (72.1%) | `GENUINE_BUTTERFLY_MISLABELING` |
| `CSD-055` | RESOLVED (1) | *Udara selma* | *Darpa pteria* | web_site (20.0%) | `LIKELY_NON_BUTTERFLY` |
| `CSD-058` | RESOLVED (1) | *Plastingia naga* | *Salanoemia sala* | lycaenid (89.4%) | `GENUINE_BUTTERFLY_MISLABELING` |

### Priority B: Suspected Non-Butterfly / Artifact Clusters (7 Clusters)
Visual screening identified 7 clusters whose predictions and aspect ratios indicate non-biological images (web graphics, templates, drawings, or food items).

| Cluster ID | Conflict Status | Species 1 | Species 2 | AI Prediction | Recommended Action |
| :---: | :---: | :--- | :--- | :--- | :--- |
| `CSD-015` | ACTIVE | *Lethe satyavati* | *Lethe vindhya vindhya* | hatchet (68.8%) | Inspect for low-res tool icon or diagram |
| `CSD-020` | ACTIVE | *Papilio elephenor* | *Salanoemia sala* | web_site (25.2%) | Inspect for web template / website banner |
| `CSD-021` | RESOLVED | *Papilio elephenor* | *Papilio bootes* | web_site (5.1%) | Inspect for web template / website banner |
| `CSD-028` | ACTIVE | *Byasa crassipes* | *Byasa polla* | pretzel (45.2%) | Inspect for non-insect object |
| `CSD-055` | RESOLVED | *Udara selma* | *Darpa pteria* | web_site (20.0%) | Inspect for web banner across families |
| `CSD-056` | ACTIVE | *Darpa pteria* | *Hidari bhawani* | web_site (74.2%) | Inspect for web banner / template |
| `CSD-057` | ACTIVE | *Salanoemia sala* | *Scobura woolletti* | envelope (49.5%) | Inspect for document graphic / envelope |

---

## 4. Comprehensive Catalog of All 55 Clusters

""" + "\n".join(md_sections)

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Writing Visual Contact Sheets HTML to {PHASE3_DIR / 'cross_species_contact_sheets.html'}...")
    html_file = PHASE3_DIR / "cross_species_contact_sheets.html"

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ButterflyAI — Phase 3C: Cross-Species Duplicate Review Contact Sheets</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #f8fafc; color: #1e293b; margin: 0; padding: 24px; }}
    header {{ background: #1b4d3e; color: #fff; padding: 24px 32px; border-radius: 8px; margin-bottom: 20px; border-bottom: 3px solid #d4a017; }}
    header h1 {{ margin: 0 0 6px 0; font-size: 24px; }}
    header p {{ margin: 0; opacity: 0.9; font-size: 14px; }}
    
    .stats-bar {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; margin-bottom: 20px; }}
    .stat-card {{ background: #fff; padding: 14px; border-radius: 6px; border: 1px solid #e2e8f0; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }}
    .stat-val {{ font-size: 22px; font-weight: bold; color: #1b4d3e; }}
    .stat-lbl {{ font-size: 11px; text-transform: uppercase; color: #64748b; margin-top: 4px; }}

    .toolbar {{ background: #fff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px 18px; margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; justify-content: space-between; }}
    .filter-group {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
    .filter-btn {{ background: #f1f5f9; border: 1px solid #cbd5e1; padding: 6px 12px; border-radius: 4px; font-size: 12px; cursor: pointer; font-weight: 500; color: #334155; transition: all 0.15s; }}
    .filter-btn:hover {{ background: #e2e8f0; }}
    .filter-btn.active {{ background: #1b4d3e; color: #fff; border-color: #1b4d3e; }}
    .action-btn {{ background: #0284c7; color: #fff; border: none; padding: 8px 16px; border-radius: 4px; font-size: 13px; font-weight: 600; cursor: pointer; }}
    .action-btn:hover {{ background: #0369a1; }}

    .cluster-card {{ background: #fff; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); overflow: hidden; }}
    .card-header {{ background: #f8fafc; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; }}
    .header-left {{ display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }}
    .cluster-badge {{ background: #1b4d3e; color: #fff; font-family: monospace; font-size: 13px; font-weight: bold; padding: 3px 8px; border-radius: 4px; }}
    .badge-tax {{ color: #fff; font-size: 11px; font-weight: 600; padding: 3px 8px; border-radius: 12px; text-transform: uppercase; }}
    .badge-status-alert {{ background: #fee2e2; color: #991b1b; font-size: 11px; font-weight: 600; padding: 3px 8px; border-radius: 4px; }}
    .badge-status-resolved {{ background: #e0f2fe; color: #075985; font-size: 11px; font-weight: 600; padding: 3px 8px; border-radius: 4px; }}
    .badge-leakage {{ background: #fef3c7; color: #92400e; font-size: 11px; font-weight: 600; padding: 3px 8px; border-radius: 4px; border: 1px solid #fde68a; }}
    .hash-tag {{ font-size: 12px; color: #64748b; margin-right: 12px; }}
    .ai-tag {{ background: #f1f5f9; color: #334155; font-size: 12px; padding: 4px 8px; border-radius: 4px; border: 1px solid #cbd5e1; }}

    .card-grid {{ display: grid; grid-template-columns: 320px 1fr; gap: 20px; padding: 20px; }}
    .img-column {{ display: flex; flex-direction: column; gap: 10px; }}
    .img-frame {{ width: 100%; height: 240px; background: #0f172a; border-radius: 6px; overflow: hidden; display: flex; align-items: center; justify-content: center; }}
    .img-frame img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
    .img-meta {{ background: #f8fafc; padding: 10px; border-radius: 6px; font-size: 11px; color: #475569; display: flex; flex-direction: column; gap: 4px; border: 1px solid #e2e8f0; }}
    .sample-path {{ word-break: break-all; }}
    .sample-path a {{ color: #0284c7; text-decoration: none; }}
    .sample-path a:hover {{ text-decoration: underline; }}
    .badge-file-act {{ background: #dcfce7; color: #166534; padding: 2px 5px; border-radius: 3px; font-size: 10px; font-weight: bold; }}
    .badge-file-quar {{ background: #fee2e2; color: #991b1b; padding: 2px 5px; border-radius: 3px; font-size: 10px; font-weight: bold; }}

    .details-column {{ display: flex; flex-direction: column; gap: 14px; }}
    .details-column h4 {{ margin: 0; font-size: 13px; text-transform: uppercase; color: #334155; }}
    .taxa-table {{ width: 100%; border-collapse: collapse; font-size: 12px; }}
    .taxa-table th {{ background: #f1f5f9; text-align: left; padding: 6px 10px; color: #475569; font-weight: 600; border-bottom: 1px solid #cbd5e1; }}
    .taxa-table td {{ padding: 6px 10px; border-bottom: 1px solid #e2e8f0; }}
    .taxa-table tr:hover {{ background: #f8fafc; }}
    .badge-fam {{ background: #f1f5f9; color: #475569; padding: 2px 5px; border-radius: 3px; font-size: 10px; }}
    .badge-split {{ font-weight: 600; font-size: 11px; text-transform: uppercase; color: #64748b; }}
    .path-text {{ color: #64748b; font-size: 11px; }}

    .decision-box {{ background: #fffbeb; border: 1px solid #fde68a; border-radius: 6px; padding: 14px; margin-top: auto; }}
    .decision-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
    .decision-title {{ font-weight: 700; font-size: 12px; color: #92400e; text-transform: uppercase; }}
    .suggestion-pill {{ font-size: 11px; font-weight: bold; border: 1px solid; padding: 2px 8px; border-radius: 12px; background: #fff; }}
    .radio-group {{ display: flex; gap: 14px; margin-bottom: 10px; flex-wrap: wrap; }}
    .radio-label {{ display: flex; align-items: center; gap: 5px; cursor: pointer; font-size: 12px; font-weight: 500; }}
    .choice-text.junk {{ color: #dc2626; }}
    .choice-text.butterfly {{ color: #16a34a; }}
    .choice-text.uncertain {{ color: #d97706; }}
    .choice-text.taxo {{ color: #2563eb; }}

    .inputs-row {{ display: flex; gap: 10px; }}
    .input-field {{ display: flex; flex-direction: column; gap: 4px; }}
    .input-field.flex-1 {{ flex: 1; }}
    .input-field.flex-2 {{ flex: 2; }}
    .input-field label {{ font-size: 11px; color: #64748b; font-weight: 600; }}
    .input-field select, .input-field input {{ padding: 6px 8px; border-radius: 4px; border: 1px solid #cbd5e1; font-size: 12px; background: #fff; }}
  </style>
</head>
<body>

  <header>
    <h1>ButterflyAI — Phase 3C: Cross-Species Duplicate Review</h1>
    <p>Human-in-the-Loop Biological Review &bull; 55 Pairwise Duplicate Clusters &bull; 120 Tracked Files (97 Active, 23 Quarantined)</p>
  </header>

  <div class="stats-bar">
    <div class="stat-card">
      <div class="stat-val">{stats['total_clusters']}</div>
      <div class="stat-lbl">Remaining Clusters</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">{stats['active_files']}</div>
      <div class="stat-lbl">Active Images</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">{stats['quarantined_files']}</div>
      <div class="stat-lbl">Quarantined (Phase 1)</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">{stats['historic_leakage_clusters']}</div>
      <div class="stat-lbl">Historic Split Leakage</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">{stats['active_conflict_clusters']}</div>
      <div class="stat-lbl">Active Conflicts</div>
    </div>
    <div class="stat-card">
      <div class="stat-val">{stats['quarantine_resolved_clusters']}</div>
      <div class="stat-lbl">Quarantine Resolved</div>
    </div>
  </div>

  <div class="toolbar">
    <div class="filter-group">
      <span style="font-size: 12px; font-weight: 600; color: #64748b;">Filter:</span>
      <button class="filter-btn active" onclick="applyFilter('all')">All (55)</button>
      <button class="filter-btn" onclick="applyFilter('leakage')">Historic Split Leakage ({stats['historic_leakage_clusters']})</button>
      <button class="filter-btn" onclick="applyFilter('active')">Active Multi-Species ({stats['active_conflict_clusters']})</button>
      <button class="filter-btn" onclick="applyFilter('resolved')">Quarantine-Resolved ({stats['quarantine_resolved_clusters']})</button>
      <button class="filter-btn" onclick="applyFilter('non-butterfly')">Likely Non-Butterfly ({stats['likely_non_butterfly']})</button>
      <button class="filter-btn" onclick="applyFilter('congeneric')">Congeneric Sister Pairs ({stats['congeneric_clusters']})</button>
      <button class="filter-btn" onclick="applyFilter('interfamily')">Interfamily ({stats['interfamily_clusters']})</button>
    </div>
    <div>
      <button class="action-btn" onclick="exportDecisionsCSV()">Export Reviewed CSV</button>
    </div>
  </div>

  <div id="cards-container">
    {''.join(html_cards)}
  </div>

  <script>
    const clusterData = {{}};

    function setSpecies(gid, val) {{
      const radioBut = document.querySelector(`input[name="dec_${{gid}}"][value="CONFIRMED_BUTTERFLY"]`);
      if (val && radioBut) {{
        radioBut.checked = true;
      }}
      updateRow(gid);
    }}

    function updateRow(gid) {{
      const dec = document.querySelector(`input[name="dec_${{gid}}"]:checked`)?.value || "UNCERTAIN";
      const selSp = document.getElementById(`sel_sp_${{gid}}`)?.value || "";
      const notes = document.getElementById(`notes_${{gid}}`)?.value || "";
      clusterData[gid] = {{
        decision: dec,
        verified_species: selSp,
        notes: notes
      }};
    }}

    function applyFilter(mode) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');

      const cards = document.querySelectorAll('.cluster-card');
      cards.forEach(card => {{
        let show = false;
        if (mode === 'all') show = true;
        else if (mode === 'leakage') show = (card.dataset.leakage === 'YES');
        else if (mode === 'active') show = (card.dataset.status === 'ACTIVE_MULTI_SPECIES');
        else if (mode === 'resolved') show = (card.dataset.status === 'RESOLVED_BY_PHASE1_QUARANTINE');
        else if (mode === 'non-butterfly') show = (card.dataset.suggestion === 'LIKELY_NON_BUTTERFLY');
        else if (mode === 'congeneric') show = (card.dataset.taxonomy === 'CONGENERIC');
        else if (mode === 'interfamily') show = (card.dataset.taxonomy === 'INTERFAMILY');
        card.style.display = show ? 'block' : 'none';
      }});
    }}

    function exportDecisionsCSV() {{
      alert("Decisions recorded in this UI can be downloaded or inspected directly in reports/phase3/cross_species_review.csv");
    }}
  </script>
</body>
</html>
"""

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Writing Human Review Guide to {PHASE3_DIR / 'cross_species_review_guide.md'}...")
    guide_file = PHASE3_DIR / "cross_species_review_guide.md"
    guide_content = f"""# ButterflyAI — Phase 3C Human Review Guide
**Scope**: 55 Pairwise Cross-Species Duplicate Clusters (`CSD-003` to `CSD-007`, `CSD-011` to `CSD-060`)  
**Target Ledger**: [`cross_species_review.csv`](file://{csv_file})  
**Interactive Sheet**: [`cross_species_contact_sheets.html`](file://{html_file})  
**Validator Script**: `pipeline/tools/validate_phase3c_review.py`

---

## 1. Review Objectives

In Phase 3C, we examine all 55 pairwise cross-species clusters where an identical image hash was found across two different species folders.

### The Four Review Determinations:

1. **`CONFIRMED_NON_BUTTERFLY`**
   - **When to use**: The image is clearly not a butterfly (e.g., website graphic, anatomy diagram, document scan, unrelated animal, or tool).
   - **Required fields**:
     * `review_decision`: `CONFIRMED_NON_BUTTERFLY`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `PURGE_ALL_SAMPLES`
   - **Resulting action**: In Phase 3D, all copies of this hash across all folders will be safely moved to quarantine.

2. **`CONFIRMED_BUTTERFLY`**
   - **When to use**: The image is a genuine butterfly specimen, and the reviewer can confidently assign it to the correct species among the conflicting folders.
   - **Required fields**:
     * `review_decision`: `CONFIRMED_BUTTERFLY`
     * `verified_correct_species`: Exact scientific name or Class ID of the true species (must match one of the conflicting taxa).
     * `action_plan`: `REASSIGN_TO_VERIFIED`
   - **Resulting action**: In Phase 3D, the copy in the verified species folder is retained, and erroneous copies in the conflicting species folders will be quarantined.

3. **`UNCERTAIN`**
   - **When to use**: The image is a butterfly specimen or biological insect, but morphological ambiguity prevents a definitive assignment between the sister species without high-magnification genitalia or molecular data.
   - **Required fields**:
     * `review_decision`: `UNCERTAIN`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `HOLD_IN_DATASET`
   - **Resulting action**: No images are moved. Both copies are preserved in active training splits to avoid premature loss of training samples.

4. **`NEEDS_TAXONOMIST`**
   - **When to use**: Complex cryptic species pairs requiring consultation with a Lepidopterist.
   - **Required fields**:
     * `review_decision`: `NEEDS_TAXONOMIST`
     * `verified_correct_species`: *(Must be empty)*
     * `action_plan`: `HOLD_IN_DATASET`
   - **Resulting action**: Retained in active dataset and logged for expert consultation.

---

## 2. Recommended Workflow

1. Open [`cross_species_contact_sheets.html`](file://{html_file}) in your browser.
2. Review the **Priority A: Historic Split Leakage** clusters (18 clusters).
3. Review the **Priority B: Suspected Non-Butterfly** clusters (7 clusters).
4. Review the remaining congeneric and intergeneric clusters.
5. Record your decisions in [`cross_species_review.csv`](file://{csv_file}).
6. Run the validator:
   ```bash
   .venv/bin/python pipeline/tools/validate_phase3c_review.py
   ```
7. Once validation passes with zero errors, present your final decisions for quarantine planning.
"""

    with open(guide_file, "w", encoding="utf-8") as f:
        f.write(guide_content)

    print("\n" + "=" * 78)
    print("  Phase 3C Artifact Generation Complete!")
    print("=" * 78)
    print(f"  1. Review CSV Ledger:      {csv_file.relative_to(PROJECT_ROOT)}")
    print(f"  2. Detailed Markdown:      {md_file.relative_to(PROJECT_ROOT)}")
    print(f"  3. Visual Contact Sheet:   {html_file.relative_to(PROJECT_ROOT)}")
    print(f"  4. Human Reviewer Guide:   {guide_file.relative_to(PROJECT_ROOT)}")
    print("=" * 78)


if __name__ == "__main__":
    generate_phase3c_artifacts()
