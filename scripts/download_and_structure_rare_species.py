#!/usr/bin/env python3
"""
Dedicated High-Speed Extractor & Structurer for Assam Rare Species & Euthalia zubeengargi
"""

import os
import sys
import time
import random
import shutil
import hashlib
import io
import urllib.request
import concurrent.futures
from pathlib import Path
from PIL import Image

try:
    from ddgs import DDGS
except ImportError:
    try:
        from duckduckgo_search import DDGS
    except ImportError:
        print("Error: ddgs library not installed.")
        sys.exit(1)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset"
TRAIN_DIR = DATASET_DIR / "train"
TEST_DIR = DATASET_DIR / "test"
MODEL_DIR = PROJECT_ROOT / "model"
LABELS_FILE = MODEL_DIR / "labels.txt"

NEW_SPECIES = [
    ("Papilio elephenor", "Yellow-crested Spangle", "Papilionidae"),
    ("Papilio paradoxa", "Great Blue Mime", "Papilionidae"),
    ("Papilio bootes", "Tailed Redbreast", "Papilionidae"),
    ("Papilio slateri", "Blue-striped Mime", "Papilionidae"),
    ("Lamproptera curius", "White Dragontail", "Papilionidae"),
    ("Lamproptera meges", "Green Dragontail", "Papilionidae"),
    ("Meandrusa payeni", "Yellow Gorgon", "Papilionidae"),
    ("Meandrusa lachinus", "Brown Gorgon", "Papilionidae"),
    ("Byasa crassipes", "Black Windmill", "Papilionidae"),
    ("Byasa nevilli", "Nevill's Windmill", "Papilionidae"),
    ("Byasa polla", "De Nicéville's Windmill", "Papilionidae"),
    ("Graphium agetes", "Fourbar Swallowtail", "Papilionidae"),
    ("Graphium aristeus", "Chain Swordtail", "Papilionidae"),
    ("Graphium macareus", "Lesser Zebra", "Papilionidae"),
    ("Graphium xenocles", "Great Zebra", "Papilionidae"),
    ("Losaria doubledayi", "Common Clubtail", "Papilionidae"),
    ("Teinopalpus imperialis", "Kaiser-i-Hind", "Papilionidae"),
    ("Elymnias peali", "Peal's Palmfly", "Nymphalidae"),
    ("Euthalia telchinia", "Blue Baron", "Nymphalidae"),
    ("Charaxes delphis", "Jewelled Nawab", "Nymphalidae"),
    ("Pantoporia assamica", "Conjoined Lascar", "Nymphalidae"),
    ("Pantoporia bieti", "Tytler's Lascar", "Nymphalidae"),
    ("Chersonesia rahria", "Wavy Maplet", "Nymphalidae"),
    ("Athyma ranga", "Blackvein Sergeant", "Nymphalidae"),
    ("Athyma pravara", "Unbroken Sergeant", "Nymphalidae"),
    ("Athyma punctata", "White-bordered Sergeant", "Nymphalidae"),
    ("Polyura schreiber", "Blue Nawab", "Nymphalidae"),
    ("Tajuria maculata", "Spotted Royal", "Lycaenidae"),
    ("Tajuria cippus", "Peacock Royal", "Lycaenidae"),
    ("Pithecops fulgens", "Blue Quaker", "Lycaenidae"),
    ("Shijimia moorei", "Moore's Cupid", "Lycaenidae"),
    ("Arhopala silhetensis", "Sylhet Oakblue", "Lycaenidae"),
    ("Arhopala oenea", "Hewitson's Dull Oakblue", "Lycaenidae"),
    ("Simiskina phalena", "Broad-branded Brilliant", "Lycaenidae"),
    ("Udara selma", "Bi-coloured Hedge Blue", "Lycaenidae"),
    ("Poritia hewitsoni", "Common Gem", "Lycaenidae"),
    ("Capila pieridoides", "White Dawnfly", "Hesperiidae"),
    ("Pyroneura margherita", "Yellow-vein Lancer", "Hesperiidae"),
    ("Darpa pteria", "Snowy Angle", "Hesperiidae"),
    ("Hidari bhawani", "Veined Palmer", "Hesperiidae"),
    ("Plastingia naga", "Chequered Lancer", "Hesperiidae"),
    ("Salanoemia sala", "Maculate Lancer", "Hesperiidae"),
    ("Scobura woolletti", "Brown Forest Bob", "Hesperiidae"),
    ("Polytremis minuta", "Baby Swift", "Hesperiidae")
]

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
]

def fetch_single_image(url):
    try:
        ua = random.choice(USER_AGENTS)
        req = urllib.request.Request(url, headers={"User-Agent": ua})
        with urllib.request.urlopen(req, timeout=6) as resp:
            data = resp.read()
        if len(data) < 4000:
            return None
        # Verify with PIL
        with Image.open(io.BytesIO(data)) as img:
            img.verify()
        with Image.open(io.BytesIO(data)) as img:
            w, h = img.size
            if w < 100 or h < 100:
                return None
            return (hashlib.md5(data).hexdigest(), img.convert("RGB"))
    except Exception:
        return None

def fetch_urls_for_queries(queries, max_needed=50):
    urls = set()
    with DDGS() as ddgs:
        for q in queries:
            if len(urls) >= max_needed:
                break
            try:
                for r in ddgs.images(q, max_results=35):
                    u = r.get("image")
                    if u and u.startswith("http") and not u.lower().endswith((".svg", ".gif")):
                        urls.add(u)
            except Exception:
                pass
            time.sleep(random.uniform(0.3, 0.6))
    return list(urls)

def collect_clean_images(queries, target_count=35):
    urls = fetch_urls_for_queries(queries, max_needed=target_count * 3)
    clean_images = []
    seen_hashes = set()

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for res in executor.map(fetch_single_image, urls):
            if res:
                h, img = res
                if h not in seen_hashes:
                    seen_hashes.add(h)
                    clean_images.append(img)
                    if len(clean_images) >= target_count:
                        break

    # If slightly under target_count, augment clean images
    if 0 < len(clean_images) < target_count:
        print(f"    (Augmenting {len(clean_images)} images to reach {target_count})...")
        orig_imgs = list(clean_images)
        idx = 0
        while len(clean_images) < target_count:
            base_img = orig_imgs[idx % len(orig_imgs)]
            # Create flipped / rotated variant
            if idx % 2 == 0:
                aug = base_img.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                aug = base_img.rotate(random.choice([-8, 8, -5, 5]), expand=False)
            clean_images.append(aug)
            idx += 1

    return clean_images

def save_partitioned_images(images, class_id, folder_name, train_dir, test_dir, train_ratio=0.80):
    tr_path = train_dir / folder_name
    te_path = test_dir / folder_name
    tr_path.mkdir(parents=True, exist_ok=True)
    te_path.mkdir(parents=True, exist_ok=True)

    random.seed(42)
    random.shuffle(images)

    total = len(images)
    test_cnt = max(5, round(total * (1.0 - train_ratio)))
    train_cnt = total - test_cnt

    train_imgs = images[:train_cnt]
    test_imgs = images[train_cnt:]

    seq = 1
    for img in train_imgs:
        img.save(tr_path / f"{class_id}{seq:04d}.jpg", "JPEG", quality=95)
        seq += 1

    for img in test_imgs:
        img.save(te_path / f"{class_id}{seq:04d}.jpg", "JPEG", quality=95)
        seq += 1

    return len(train_imgs), len(test_imgs)

def process_euthalia_zubeengargi():
    print("\n" + "=" * 60)
    print("  Enriching 081_Euthalia_zubeengargi with fresh web images...")
    print("=" * 60)
    class_id = "081"
    folder_name = "081_Euthalia_zubeengargi"
    tr_path = TRAIN_DIR / folder_name
    te_path = TEST_DIR / folder_name

    existing_images = []
    seen_hashes = set()

    for p in list(tr_path.glob("*.jpg")) + list(te_path.glob("*.jpg")):
        try:
            with open(p, "rb") as f:
                data = f.read()
            h = hashlib.md5(data).hexdigest()
            seen_hashes.add(h)
            with Image.open(io.BytesIO(data)) as img:
                existing_images.append(img.convert("RGB"))
        except Exception:
            pass

    print(f"  Existing local images: {len(existing_images)}")

    queries = [
        '"Euthalia zubeengargi"',
        '"Zubeen\'s Baron" butterfly',
        'Euthalia zubeengargi Assam',
        'Euthalia zubeengargi holotype',
        'Euthalia zubeengargi Kaziranga',
        'Euthalia zubeengargi Panbari',
        'Euthalia zubeengargi butterfly',
        'Euthalia zubeengargi dorsal ventral',
        'Euthalia zubeengargi natural habitat',
        'Euthalia zubeengargi Zootaxa',
        'Euthalia zubeengargi'
    ]

    urls = fetch_urls_for_queries(queries, max_needed=120)
    print(f"  Candidate URLs retrieved: {len(urls)}")

    new_imgs = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for res in executor.map(fetch_single_image, urls):
            if res:
                h, img = res
                if h not in seen_hashes:
                    seen_hashes.add(h)
                    new_imgs.append(img)

    print(f"  Downloaded {len(new_imgs)} new unique, verified images.")
    combined = existing_images + new_imgs
    print(f"  Total Euthalia zubeengargi dataset size: {len(combined)} images")

    # Clear old folder contents and repopulate cleanly
    shutil.rmtree(tr_path, ignore_errors=True)
    shutil.rmtree(te_path, ignore_errors=True)

    tr_cnt, te_cnt = save_partitioned_images(combined, class_id, folder_name, TRAIN_DIR, TEST_DIR, train_ratio=0.80)
    print(f"  [✓] Successfully updated 081_Euthalia_zubeengargi: Train={tr_cnt}, Test={te_cnt}")
    return tr_cnt, te_cnt

def process_new_species():
    print("\n" + "=" * 60)
    print(f"  Downloading & Structuring {len(NEW_SPECIES)} Rare Assam Species...")
    print("=" * 60)

    start_idx = 82
    results = []

    for idx_offset, (sci_name, common_name, family) in enumerate(NEW_SPECIES):
        class_num = start_idx + idx_offset
        class_id = f"{class_num:03d}"
        folder_name = f"{class_id}_{sci_name.replace(' ', '_')}"

        print(f"\n[{idx_offset+1}/{len(NEW_SPECIES)}] Class {class_id}: {sci_name} ({common_name})")

        queries = [
            f'"{sci_name}" butterfly',
            f'"{sci_name}"',
            f'"{common_name}" butterfly',
            f'"{sci_name}" dorsal ventral',
            f'"{sci_name}" insect',
            f'{sci_name} Assam',
            f'{sci_name}'
        ]

        images = collect_clean_images(queries, target_count=35)
        print(f"    Collected {len(images)} clean images.")

        tr_cnt, te_cnt = save_partitioned_images(images, class_id, folder_name, TRAIN_DIR, TEST_DIR, train_ratio=0.80)
        print(f"    [✓] Structured {folder_name} -> Train: {tr_cnt}, Test: {te_cnt}")
        results.append((folder_name, tr_cnt, te_cnt))

    return results

def main():
    TRAIN_DIR.mkdir(parents=True, exist_ok=True)
    TEST_DIR.mkdir(parents=True, exist_ok=True)

    ez_tr, ez_te = process_euthalia_zubeengargi()
    results = process_new_species()

    print("\n" + "=" * 60)
    print("  Dataset Extraction Complete!")
    print(f"  Euthalia zubeengargi: Train={ez_tr}, Test={ez_te}")
    print(f"  New Species Added: {len(results)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
