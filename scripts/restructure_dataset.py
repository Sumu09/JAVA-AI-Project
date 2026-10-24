import os
import shutil
import random

def restructure_dataset():
    train_dir = os.path.join("dataset", "train")
    test_dir = os.path.join("dataset", "test")

    # 1. Handle empty directory Castalius rosimon rosimon
    empty_dir = os.path.join(train_dir, "Castalius rosimon rosimon")
    if os.path.exists(empty_dir):
        files = [f for f in os.listdir(empty_dir) if not f.startswith('.')]
        if len(files) == 0:
            print(f"Removing empty directory: {empty_dir}")
            shutil.rmtree(empty_dir)

    # 2. Merge Hasora badra badra into Hasora badra
    hbb_dir = os.path.join(train_dir, "Hasora badra badra")
    hb_dir = os.path.join(train_dir, "Hasora badra")
    if os.path.exists(hbb_dir) and os.path.exists(hb_dir):
        print(f"Merging '{hbb_dir}' into '{hb_dir}'...")
        for fname in os.listdir(hbb_dir):
            if fname.startswith('.'):
                continue
            src = os.path.join(hbb_dir, fname)
            dst = os.path.join(hb_dir, fname)
            if os.path.exists(dst):
                # Avoid collision
                base, ext = os.path.splitext(fname)
                dst = os.path.join(hb_dir, f"{base}_sub{ext}")
            shutil.move(src, dst)
        shutil.rmtree(hbb_dir)
        print(f"Merged successfully. Total images in Hasora badra: {len(os.listdir(hb_dir))}")

    # 3. Find unnumbered folders
    all_train_dirs = sorted([d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))])
    existing_numbered = [d for d in all_train_dirs if d.startswith(tuple(f"{i:03d}_" for i in range(1, 11)))]
    unnumbered = sorted([d for d in all_train_dirs if d not in existing_numbered and not d.startswith('.')])

    print(f"\nExisting 10 classes: {len(existing_numbered)}")
    print(f"New classes to restructure: {len(unnumbered)}")

    # 4. Rename unnumbered folders in train and create test split
    random.seed(42)
    next_idx = 11

    renamed_classes = []

    for old_name in unnumbered:
        old_path = os.path.join(train_dir, old_name)
        clean_name = old_name.replace(' ', '_')
        new_name = f"{next_idx:03d}_{clean_name}"
        new_train_path = os.path.join(train_dir, new_name)
        new_test_path = os.path.join(test_dir, new_name)

        # Rename train folder
        os.rename(old_path, new_train_path)

        # Create test folder
        os.makedirs(new_test_path, exist_ok=True)

        # Get all valid image files
        images = [f for f in os.listdir(new_train_path) if not f.startswith('.')]
        random.shuffle(images)

        total_imgs = len(images)
        if total_imgs >= 2:
            test_count = max(1, round(total_imgs * 0.20))
        else:
            test_count = 0

        test_files = images[:test_count]
        train_count = total_imgs - test_count

        for f in test_files:
            src = os.path.join(new_train_path, f)
            dst = os.path.join(new_test_path, f)
            shutil.move(src, dst)

        renamed_classes.append((new_name, train_count, test_count))
        next_idx += 1

    print("\nDataset restructuring complete!")
    print(f"Total species classes in dataset: {next_idx - 1}")
    print("-" * 60)
    print(f"{'Class Name':<45} | {'Train':<6} | {'Test':<6}")
    print("-" * 60)
    for name, tr, te in renamed_classes:
        print(f"{name:<45} | {tr:<6} | {te:<6}")

    # Verify totals
    final_train_dirs = [d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))]
    final_test_dirs = [d for d in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, d))]
    
    total_train_imgs = sum(len([f for f in os.listdir(os.path.join(train_dir, d)) if not f.startswith('.')]) for d in final_train_dirs)
    total_test_imgs = sum(len([f for f in os.listdir(os.path.join(test_dir, d)) if not f.startswith('.')]) for d in final_test_dirs)

    print("-" * 60)
    print(f"Total Train Folders: {len(final_train_dirs)}, Total Train Images: {total_train_imgs}")
    print(f"Total Test Folders:  {len(final_test_dirs)}, Total Test Images:  {total_test_imgs}")
    print("=" * 60)

if __name__ == "__main__":
    restructure_dataset()
