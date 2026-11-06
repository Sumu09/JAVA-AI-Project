#!/usr/bin/env python3
"""
ButterflyAI — Phase 3C Review Validator
=======================================
Validates human review determinations in reports/phase3/cross_species_review.csv:
  1. Verifies that all 55 expected cluster IDs are present and unique.
  2. Ensures review_decision is one of the allowed taxonomic actions:
       - CONFIRMED_NON_BUTTERFLY
       - CONFIRMED_BUTTERFLY
       - UNCERTAIN
       - NEEDS_TAXONOMIST
       - (PENDING_REVIEW is flagged as awaiting human input)
  3. Detects incomplete, ambiguous, or contradictory decisions:
       - CONFIRMED_BUTTERFLY requires verified_correct_species matching one of the taxa.
       - CONFIRMED_NON_BUTTERFLY requires empty verified_correct_species and PURGE_ALL_SAMPLES.
       - UNCERTAIN / NEEDS_TAXONOMIST requires HOLD_IN_DATASET.
  4. Verifies all source files exist in active dataset or quarantine holding.

SAFEGUARDS:
  - Read-Only: Never modifies dataset files.
"""

import os
import sys
import csv
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset"
REVIEW_CSV = PROJECT_ROOT / "reports" / "phase3" / "cross_species_review.csv"
MANIFEST_FILE = DATASET_DIR / "quarantine" / "quarantine_manifest.json"

EXPECTED_CLUSTER_IDS = {
    f"CSD-{i:03d}" for i in range(3, 61)
} - {"CSD-008", "CSD-009", "CSD-010"}  # 55 clusters

ALLOWED_DECISIONS = {
    "CONFIRMED_NON_BUTTERFLY",
    "CONFIRMED_BUTTERFLY",
    "UNCERTAIN",
    "NEEDS_TAXONOMIST",
    "PENDING_REVIEW"
}


def load_quarantine_manifest_paths():
    if not MANIFEST_FILE.exists():
        return set()
    try:
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(r["original_path"] for r in data.get("records", []))
    except Exception:
        return set()


def validate_phase3c_review():
    print("=" * 78)
    print("  ButterflyAI — Phase 3C Cross-Species Review Validator")
    print("=" * 78)
    print(f"Target review ledger: {REVIEW_CSV.relative_to(PROJECT_ROOT) if REVIEW_CSV.exists() else REVIEW_CSV}\n")

    if not REVIEW_CSV.exists():
        print(f"CRITICAL ERROR: Review ledger not found at {REVIEW_CSV}")
        sys.exit(1)

    with open(REVIEW_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    quarantined_paths = load_quarantine_manifest_paths()

    errors = []
    warnings = []
    seen_clusters = set()

    decision_counts = {
        "CONFIRMED_NON_BUTTERFLY": 0,
        "CONFIRMED_BUTTERFLY": 0,
        "UNCERTAIN": 0,
        "NEEDS_TAXONOMIST": 0,
        "PENDING_REVIEW": 0,
    }

    for idx, r in enumerate(rows, 1):
        gid = r.get("cluster_id", "").strip()
        decision = r.get("review_decision", "").strip()
        verified_sp = r.get("verified_correct_species", "").strip()
        action_plan = r.get("action_plan", "").strip()
        notes = r.get("reviewer_notes", "").strip()
        taxa_str = r.get("conflicting_species_names", "").strip()
        cids_str = r.get("conflicting_class_ids", "").strip()
        source_paths_str = r.get("source_paths", "").strip()
        total_files = int(r.get("total_files", 0))

        # Check 1: Cluster ID validity
        if not gid:
            errors.append(f"Row #{idx}: Missing cluster_id.")
            continue
        if gid in seen_clusters:
            errors.append(f"Duplicate entry for cluster {gid}.")
        seen_clusters.add(gid)

        # Check 2: Decision validity
        if not decision:
            errors.append(f"Cluster {gid}: Missing review_decision. Must be one of {sorted(ALLOWED_DECISIONS)}.")
            continue
        if decision not in ALLOWED_DECISIONS:
            errors.append(
                f"Cluster {gid}: Invalid review_decision '{decision}'. Allowed: {sorted(ALLOWED_DECISIONS)}"
            )
            continue

        decision_counts[decision] = decision_counts.get(decision, 0) + 1

        conflicting_taxa = [t.strip() for t in taxa_str.split("|")] if taxa_str else []
        conflicting_cids = [c.strip() for c in cids_str.split("|")] if cids_str else []

        # Check 3: Consistency checks per decision type
        if decision == "CONFIRMED_BUTTERFLY":
            if not verified_sp:
                errors.append(
                    f"Cluster {gid}: Marked as CONFIRMED_BUTTERFLY, but 'verified_correct_species' is empty!"
                )
            else:
                matches_taxa = any(verified_sp.lower() in t.lower() for t in conflicting_taxa)
                matches_cid = any(verified_sp == c or verified_sp.lstrip("0") == c.lstrip("0") for c in conflicting_cids)
                if not (matches_taxa or matches_cid):
                    warnings.append(
                        f"Cluster {gid}: 'verified_correct_species' ('{verified_sp}') does not match any conflicting taxa {conflicting_taxa} or IDs {conflicting_cids}."
                    )

            if action_plan not in ["REASSIGN_TO_VERIFIED", "RETAIN_VERIFIED_ONLY"]:
                warnings.append(
                    f"Cluster {gid}: For CONFIRMED_BUTTERFLY, expected action_plan 'REASSIGN_TO_VERIFIED', got '{action_plan}'."
                )

        elif decision == "CONFIRMED_NON_BUTTERFLY":
            if verified_sp:
                warnings.append(
                    f"Cluster {gid}: Marked as CONFIRMED_NON_BUTTERFLY, but 'verified_correct_species' is populated ('{verified_sp}'). Should be empty."
                )
            if action_plan != "PURGE_ALL_SAMPLES":
                errors.append(
                    f"Cluster {gid}: Marked as CONFIRMED_NON_BUTTERFLY, but action_plan is '{action_plan}' instead of 'PURGE_ALL_SAMPLES'."
                )

        elif decision in ["UNCERTAIN", "NEEDS_TAXONOMIST"]:
            if verified_sp:
                warnings.append(
                    f"Cluster {gid}: Marked as {decision}, but 'verified_correct_species' is populated ('{verified_sp}'). Should be empty until verified."
                )
            if action_plan != "HOLD_IN_DATASET":
                warnings.append(
                    f"Cluster {gid}: Marked as {decision}, but action_plan is '{action_plan}' instead of 'HOLD_IN_DATASET'."
                )

        # Check 4: Source paths verification
        source_paths = [p.strip() for p in source_paths_str.split(";")] if source_paths_str else []
        for p_str in source_paths:
            p = PROJECT_ROOT / p_str
            if not p.exists() and p_str not in quarantined_paths:
                warnings.append(f"Cluster {gid}: Source path '{p_str}' not found in active dataset or quarantine manifest.")

    # Check 5: All expected clusters present
    missing_clusters = EXPECTED_CLUSTER_IDS - seen_clusters
    if missing_clusters:
        errors.append(f"Missing required clusters ({len(missing_clusters)}): {sorted(missing_clusters)}")

    extra_clusters = seen_clusters - EXPECTED_CLUSTER_IDS
    if extra_clusters:
        errors.append(f"Unexpected extra clusters ({len(extra_clusters)}): {sorted(extra_clusters)}")

    print(f"Total Clusters Validated: {len(seen_clusters)} / {len(EXPECTED_CLUSTER_IDS)}")
    print("Decision Breakdown:")
    for d, c in decision_counts.items():
        print(f"  - {d:26}: {c}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print(f"\nCRITICAL VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  [ERROR] {e}")
        print("\nResult: VALIDATION FAILED.")
        sys.exit(1)
    else:
        print("\nResult: VALIDATION PASSED.")
        if decision_counts["PENDING_REVIEW"] > 0:
            print(f"Status: {decision_counts['PENDING_REVIEW']} clusters are PENDING_REVIEW awaiting human decisions.")
        else:
            print("Status: All 55 clusters have recorded decisions and are ready for quarantine planning.")
        sys.exit(0)


if __name__ == "__main__":
    validate_phase3c_review()
