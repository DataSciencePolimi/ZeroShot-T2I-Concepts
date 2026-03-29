import os
from collections import defaultdict
from pathlib import Path

def analyze_concept_images(root_path="."):
    """
    Iterate through subfolders, group by concept, and count image files, calculate size, and track file types.
    """
    concept_stats = defaultdict(lambda: defaultdict(lambda: {"count": 0, "size_bytes": 0, "file_types": defaultdict(int)}))
    
    # Get all subdirectories
    for subfolder in os.listdir(root_path):
        subfolder_path = os.path.join(root_path, subfolder)
        
        if not os.path.isdir(subfolder_path):
            continue
        
        # Extract concept name (e.g., "bubbly" from "bubbly_flux")
        concept = subfolder.split("_")[0]
        
        # Count files and calculate sizes by extension
        for filename in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, filename)
            
            if os.path.isfile(file_path):
                ext = Path(filename).suffix.lower()
                if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
                    concept_stats[concept][subfolder]["count"] += 1
                    concept_stats[concept][subfolder]["size_bytes"] += os.path.getsize(file_path)
                    concept_stats[concept][subfolder]["file_types"][ext] += 1
    
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