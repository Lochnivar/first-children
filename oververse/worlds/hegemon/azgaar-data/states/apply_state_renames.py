#!/usr/bin/env python3
"""
Script to rename state folders and update all references with new state names
"""

import os
import re
import json
import shutil
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()

# State name mappings: old_name -> (new_name, new_full_name)
state_renames = {
    "Tridia": ("Trevalia", "Grand Duchy of Trevalia"),
    "Torklia": ("Tormaline", "Republic of Tormaline"),
    "Kutiotania": ("Kutiograd", "Kutiograd Theocracy"),
    "Cailinhia": ("Kailhen", "Protectorate of Kailhen"),
    "Ngatria": ("Ngathar", "Duchy of Ngathar"),
    "Shibaha": ("Shibara", "Emirate of Shibara"),
    "Brinachia": ("Brinach", "Principality of Brinach"),
    "Sigdakland": ("Sigdak", "Protectorate of Sigdak"),
    "Sealia": ("Sealaris", "Principality of Sealaris"),
    "Ponden": ("Pondara", "Dominion of Pondara"),
}

# State index mappings
state_index_map = {
    2: "Tridia",
    3: "Torklia",
    12: "Kutiotania",
    14: "Cailinhia",
    17: "Ngatria",
    9: "Shibaha",
    11: "Brinachia",
    16: "Sigdakland",
    13: "Sealia",
    18: "Ponden",
}

def sanitize_filename(name):
    """Convert state name to valid filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

# Step 1: Rename folders
for state_index, old_name in state_index_map.items():
    if old_name in state_renames:
        new_name, new_full_name = state_renames[old_name]
        old_folder = f"{state_index:02d}-{sanitize_filename(old_name)}"
        new_folder = f"{state_index:02d}-{sanitize_filename(new_name)}"
        
        old_path = script_dir / old_folder
        new_path = script_dir / new_folder
        
        if old_path.exists() and not new_path.exists():
            print(f"Renaming {old_folder} -> {new_folder}")
            shutil.move(str(old_path), str(new_path))
        elif old_path.exists():
            print(f"Warning: {new_folder} already exists, skipping rename")
        else:
            print(f"Warning: {old_folder} not found")

# Step 2: Update README and JSON files
for state_index, old_name in state_index_map.items():
    if old_name in state_renames:
        new_name, new_full_name = state_renames[old_name]
        folder_name = f"{state_index:02d}-{sanitize_filename(new_name)}"
        folder_path = script_dir / folder_name
        
        # If folder wasn't renamed, try old name
        if not folder_path.exists():
            old_folder = f"{state_index:02d}-{sanitize_filename(old_name)}"
            folder_path = script_dir / old_folder
        
        if folder_path.exists():
            # Update README.md
            readme_path = folder_path / "README.md"
            if readme_path.exists():
                with open(readme_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace title
                content = content.replace(f"# Grand Duchy of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# Republic of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# {old_name}n Theocracy", f"# {new_full_name}")
                content = content.replace(f"# Protectorate of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# Duchy of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# Emirate of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# Principality of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# Dominion of {old_name}", f"# {new_full_name}")
                content = content.replace(f"# {old_name}", f"# {new_full_name}")
                
                # Replace name fields
                content = re.sub(rf"- \*\*Name:\*\* {old_name}", f"- **Name:** {new_name}", content)
                content = content.replace(f"- **Full Name:** Grand Duchy of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Republic of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** {old_name}n Theocracy", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Protectorate of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Duchy of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Emirate of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Principality of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** Dominion of {old_name}", f"- **Full Name:** {new_full_name}")
                content = content.replace(f"- **Full Name:** {old_name}", f"- **Full Name:** {new_full_name}")
                
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated README.md in {folder_path.name}")
            
            # Update state-data.json
            json_path = folder_path / "state-data.json"
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                if 'name' in data:
                    data['name'] = new_name
                if 'fullName' in data:
                    data['fullName'] = new_full_name
                
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print(f"Updated state-data.json in {folder_path.name}")
            
            # Update burgs.md
            burgs_md_path = folder_path / "burgs.md"
            if burgs_md_path.exists():
                with open(burgs_md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace state name in burgs.md header
                content = re.sub(rf"# Burgs \(Cities/Settlements\) - {old_name}", f"# Burgs (Cities/Settlements) - {new_name}", content)
                
                with open(burgs_md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated burgs.md in {folder_path.name}")

print("\nState renaming and file updates complete!")

