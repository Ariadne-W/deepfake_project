# This script generates a metadata.json file for the Celeb-DF-v2 dataset.
import os
import json
from pathlib import Path

def generate_merged_metadata(root_dir):
    metadata = {}
    
    merge_dir = Path(root_dir)
    for video_file in merge_dir.glob("*.mp4"):
        filename = video_file.name
        entry = {
            "filename": filename,
            "label": "REAL", 
            "original": "",
            "split": "train"
        }
        
        parts = filename[:-4].split("_")
        
        if len(parts) == 2 and parts[0].startswith("id") and parts[1].isdigit():
            entry["label"] = "REAL"
        elif len(parts) >= 3 and parts[0].startswith("id") and parts[-1].isdigit():
            entry["label"] = "FAKE"
            original = f"{parts[0]}_{parts[-1]}.mp4"
            entry["original"] = original
        else:
            continue
            
        metadata[filename] = entry
    
    output_path = merge_dir / "metadata.json"
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Generated metadata.json with {len(metadata)} entries")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--root-dir", required=True,
                      help="Root directory containing Celeb-DF-v2-merge")
    args = parser.parse_args()
    
    generate_merged_metadata(args.root_dir)