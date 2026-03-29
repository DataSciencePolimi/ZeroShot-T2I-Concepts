import os
from collections import defaultdict
from pathlib import Path

def analyze_concept_images(root_path="."):
    """
    Iterate through concept folders and their subfolders,
    count image files, calculate size, and track file types.
    Adapted for structure:
    concept/
        concept/            # base images
        concept_sd_3_5/     # variant subfolders
        concept_flux_1_1/
    """
    concept_stats = defaultdict(lambda: defaultdict(lambda: {"count": 0, "size_bytes": 0, "file_types": defaultdict(int)}))

    # Iterate concept folders
    for concept_dir in os.listdir(root_path):
        concept_path = os.path.join(root_path, concept_dir)
        if not os.path.isdir(concept_path):
            continue

        # Iterate subfolders inside concept
        for subfolder in os.listdir(concept_path):
            subfolder_path = os.path.join(concept_path, subfolder)
            if not os.path.isdir(subfolder_path):
                continue

            # Count only image files in this subfolder
            for filename in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, filename)
                if os.path.isfile(file_path):
                    ext = Path(filename).suffix.lower()
                    if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
                        concept_stats[concept_dir][subfolder]["count"] += 1
                        concept_stats[concept_dir][subfolder]["size_bytes"] += os.path.getsize(file_path)
                        concept_stats[concept_dir][subfolder]["file_types"][ext] += 1

    # Print results
    for concept in sorted(concept_stats.keys()):
        print(f"\n{concept}:")
        concept_total_count = 0
        concept_total_bytes = 0
        for subfolder, stats in sorted(concept_stats[concept].items()):
            count = stats["count"]
            size_mb = stats["size_bytes"] / (1024 * 1024)
            file_type_str = ", ".join([f"{ext}: {cnt}" for ext, cnt in sorted(stats["file_types"].items())])
            print(f"  {subfolder}: {count} files, {size_mb:.2f} MB ({file_type_str})")
            concept_total_count += count
            concept_total_bytes += stats["size_bytes"]
        concept_total_mb = concept_total_bytes / (1024 * 1024)
        print(f"  Total: {concept_total_count} files, {concept_total_mb:.2f} MB")

if __name__ == "__main__":
    analyze_concept_images()