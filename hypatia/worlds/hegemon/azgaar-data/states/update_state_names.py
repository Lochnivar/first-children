#!/usr/bin/env python3
"""
Script to update state names in README and JSON files after folder renaming
"""

import os
import json
import re
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()

# State name mappings: (old_name, old_full_name) -> (new_name, new_full_name)
state_updates = {
    ("Tridia", "Grand Duchy of Tridia"): ("Trevalia", "Grand Duchy of Trevalia"),
    ("Torklia", "Republic of Torklia"): ("Tormaline", "Republic of Tormaline"),
    ("Kutiotania", "Kutiotanian Theocracy"): ("Kutiograd", "Kutiograd Theocracy"),
    ("Cailinhia", "Protectorate of Cailinhia"): ("Kailhen", "Protectorate of Kailhen"),
    ("Ngatria", "Duchy of Ngatria"): ("Ngathar", "Duchy of Ngathar"),
    ("Shibaha", "Emirate of Shibaha"): ("Shibara", "Emirate of Shibara"),
    ("Brinachia", "Principality of Brinachia"): ("Brinach", "Principality of Brinach"),
    ("Sigdakland", "Protectorate of Sigdakland"): ("Sigdak", "Protectorate of Sigdak"),
    ("Sealia", "Principality of Sealia"): ("Sealaris", "Principality of Sealaris"),
    ("Ponden", "Dominion of Ponden"): ("Pondara", "Dominion of Pondara"),
}

# Folder name mappings: old folder name -> new folder name
folder_map = {
    "02-tridia": "02-trevalia",
    "03-torklia": "03-tormaline",
    "09-shibaha": "09-shibara",
    "11-brinachia": "11-brinach",
    "12-kutiotania": "12-kutiograd",
    "13-sealia": "13-sealaris",
    "14-cailinhia": "14-kailhen",
    "16-sigdakland": "16-sigdak",
    "17-ngatria": "17-ngathar",
    "18-ponden": "18-pondara",
}

def update_readme(folder_path, old_name, old_full_name, new_name, new_full_name):
    """Update README.md file with new state names."""
    readme_path = folder_path / "README.md"
    if not readme_path.exists():
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace title
    content = content.replace(f"# {old_full_name}", f"# {new_full_name}")
    
    # Replace name field
    content = re.sub(rf"- \*\*Name:\*\* {old_name}", f"- **Name:** {new_name}", content)
    
    # Replace full name field
    content = content.replace(f"- **Full Name:** {old_full_name}", f"- **Full Name:** {new_full_name}")
    content = content.replace(f"- **Full Name:** {old_name}", f"- **Full Name:** {new_full_name}")
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def update_state_json(folder_path, old_name, new_name, new_full_name):
    """Update state-data.json file with new state names."""
    json_path = folder_path / "state-data.json"
    if not json_path.exists():
        return False
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'name' in data:
        data['name'] = new_name
    if 'fullName' in data:
        data['fullName'] = new_full_name
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return True

# Update files in each renamed folder
for (old_name, old_full_name), (new_name, new_full_name) in state_updates.items():
    # Find folder (try both old and new names)
    folder_found = None
    for old_folder, new_folder in folder_map.items():
        if old_name.lower() in old_folder.lower():
            # Try new folder name first
            new_folder_path = script_dir / new_folder
            old_folder_path = script_dir / old_folder
            if new_folder_path.exists():
                folder_found = new_folder_path
                break
            elif old_folder_path.exists():
                folder_found = old_folder_path
                break
    
    if not folder_found:
        # Try to find by state name in folder
        for folder in script_dir.iterdir():
            if folder.is_dir() and (old_name.lower() in folder.name.lower() or new_name.lower() in folder.name.lower()):
                folder_found = folder
                break
    
    if folder_found:
        print(f"Updating {folder_found.name}...")
        if update_readme(folder_found, old_name, old_full_name, new_name, new_full_name):
            print(f"  Updated README.md")
        if update_state_json(folder_found, old_name, new_name, new_full_name):
            print(f"  Updated state-data.json")
    else:
        print(f"Warning: Could not find folder for {old_name}")

print("\nFile updates complete!")

