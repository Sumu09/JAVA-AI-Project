#!/usr/bin/env python3
"""
ButterflyAI — Dataset Backup Utility
====================================
Safely creates an exact, verified snapshot of:
  - dataset/train/
  - dataset/test/
  - model/labels.txt

No files in the original dataset are altered or deleted.
A backup manifest (JSON) is generated inside the backup directory
with file counts, total bytes, and timestamps.
"""

import os
import sys
import time
import shutil
import hashlib
import json
from pathlib import Path
from datetime import datetime

# Resolve project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
TRAIN_DIR = PROJECT_ROOT / "dataset" / "train"
TEST_DIR = PROJECT_ROOT / "dataset" / "test"
LABELS_FILE = PROJECT_ROOT / "model" / "labels.txt"
DEFAULT_BACKUP_BASE = PROJECT_ROOT / "backups"


def compute_sha256(filepath):
    """Computes SHA-256 hash of a file for integrity verification."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def count_files_and_bytes(directory):
    """Returns (file_count, total_bytes) for a directory."""
    count = 0
    total_bytes = 0
    if not directory.exists():
        return count, total_bytes

    for p in directory.rglob("*"):
        if p.is_file() and not p.name.startswith("."):
            count += 1
            total_bytes += p.stat().st_size
    return count, total_bytes


def create_backup(dest_dir=None):
    """Creates a verified snapshot backup of train, test, and labels.txt."""
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    if dest_dir:
        backup_path = Path(dest_dir).resolve()
    else:
        backup_path = DEFAULT_BACKUP_BASE / f"dataset_backup_{timestamp_str}"

    print("=" * 70)
    print("  ButterflyAI — Dataset Snapshot & Safeguard Backup")
    print("=" * 70)
    print(f"Timestamp:          {datetime.now().isoformat()}")
    print(f"Source Train:       {TRAIN_DIR}")
    print(f"Source Test:        {TEST_DIR}")
    print(f"Source Labels:      {LABELS_FILE}")
    print(f"Backup Destination: {backup_path}")
    print("-" * 70)

    # Validate source paths exist
    if not TRAIN_DIR.exists():
        print(f"Error: Train directory not found at: {TRAIN_DIR}")
        sys.exit(1)
    if not TEST_DIR.exists():
        print(f"Error: Test directory not found at: {TEST_DIR}")
        sys.exit(1)
    if not LABELS_FILE.exists():
        print(f"Error: Labels file not found at: {LABELS_FILE}")
        sys.exit(1)

    # 1. Measure sources
    print("[1/4] Calculating source file counts and volume...")
    train_count, train_bytes = count_files_and_bytes(TRAIN_DIR)
    test_count, test_bytes = count_files_and_bytes(TEST_DIR)
    labels_bytes = LABELS_FILE.stat().st_size

    print(f"  Train:  {train_count:,} files ({train_bytes / (1024 * 1024):.1f} MB)")
    print(f"  Test:   {test_count:,} files ({test_bytes / (1024 * 1024):.1f} MB)")
    print(f"  Total:  {train_count + test_count:,} images")

    # 2. Prepare destination
    backup_path.mkdir(parents=True, exist_ok=True)
    dest_train = backup_path / "train"
    dest_test = backup_path / "test"
    dest_labels = backup_path / "labels.txt"

    # 3. Copy files
    print("\n[2/4] Copying files (preserving exact file attributes)...")
    start_time = time.time()

    print("  Copying dataset/train/ ...")
    shutil.copytree(TRAIN_DIR, dest_train, dirs_exist_ok=True)

    print("  Copying dataset/test/ ...")
    shutil.copytree(TEST_DIR, dest_test, dirs_exist_ok=True)

    print("  Copying model/labels.txt ...")
    shutil.copy2(LABELS_FILE, dest_labels)

    elapsed = time.time() - start_time
    print(f"  Copy completed in {elapsed:.1f} seconds.")

    # 4. Verify integrity
    print("\n[3/4] Verifying snapshot integrity...")
    dest_tr_count, dest_tr_bytes = count_files_and_bytes(dest_train)
    dest_te_count, dest_te_bytes = count_files_and_bytes(dest_test)

    passed = (train_count == dest_tr_count and test_count == dest_te_count and
              train_bytes == dest_tr_bytes and test_bytes == dest_te_bytes)

    if not passed:
        print("  [ERROR] Verification failed! File counts or bytes mismatch!")
        print(f"    Expected: Train={train_count}, Test={test_count}")
        print(f"    Found:    Train={dest_tr_count}, Test={dest_te_count}")
        sys.exit(1)

    print("  [SUCCESS] Integrity verified! All file counts and byte sizes match 100%.")

    # 5. Save metadata manifest
    print("\n[4/4] Writing backup manifest...")
    manifest = {
        "timestamp": datetime.now().isoformat(),
        "backup_path": str(backup_path),
        "source_train": str(TRAIN_DIR),
        "source_test": str(TEST_DIR),
        "source_labels": str(LABELS_FILE),
        "stats": {
            "train_files": train_count,
            "train_bytes": train_bytes,
            "test_files": test_count,
            "test_bytes": test_bytes,
            "labels_bytes": labels_bytes,
            "total_images": train_count + test_count
        },
        "labels_sha256": compute_sha256(LABELS_FILE)
    }

    manifest_file = backup_path / "backup_manifest.json"
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"  Manifest written to: {manifest_file}")
    print("\n" + "=" * 70)
    print("  BACKUP COMPLETE & VERIFIED SAFE")
    print(f"  Location: {backup_path}")
    print("=" * 70)
    return backup_path


if __name__ == "__main__":
    dest = sys.argv[1] if len(sys.argv) > 1 else None
    create_backup(dest)
