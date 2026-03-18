#!/usr/bin/env python3
"""
Script to rename state folders and update all references with new state names
"""

import os
import re
import json
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
states_dir = script_dir

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

# State index mappings (from the states README)
state_index_map = {
    2: "Tridia",  # → Trevalia
    3: "Torklia",  # → Tormaline
    12: "Kutiotania",  # → Kutiograd
    14: "Cailinhia",  # → Kailhen
    17: "Ngatria",  # → Ngathar
    9: "Shibaha",  # → Shibara
    11: "Brinachia",  # → Brinach
    16: "Sigdakland",  # → Sigdak
    13: "Sealia",  # → Sealaris
    18: "Ponden",  # → Pondara
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
        
        old_path = states_dir / old_folder
        new_path = states_dir / new_folder
        
        if old_path.exists() and not new_path.exists():
            print(f"Renaming {old_folder} → {new_folder}")
            os.rename(str(old_path), str(new_path))
        elif old_path.exists():
            print(f"Warning: {new_folder} already exists, skipping rename")
        else:
            print(f"Warning: {old_folder} not found")

# Step 2: Update README files in each renamed state folder
for state_index, old_name in state_index_map.items():
    if old_name in state_renames:
        new_name, new_full_name = state_renames[old_name]
        folder_name = f"{state_index:02d}-{sanitize_filename(new_name)}"
        readme_path = states_dir / folder_name / "README.md"
        
        if readme_path.exists():
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace state name references carefully
            # First handle specific patterns
            content = content.replace(f"# {old_name}", f"# {new_full_name}")
            if f"# Grand Duchy of {old_name}" in content:
                content = content.replace(f"# Grand Duchy of {old_name}", f"# {new_full_name}")
            if f"# Republic of {old_name}" in content:
                content = content.replace(f"# Republic of {old_name}", f"# {new_full_name}")
            if f"# {old_name}n Theocracy" in content:
                content = content.replace(f"# {old_name}n Theocracy", f"# {new_full_name}")
            if f"# Protectorate of {old_name}" in content:
                content = content.replace(f"# Protectorate of {old_name}", f"# {new_full_name}")
            if f"# Duchy of {old_name}" in content:
                content = content.replace(f"# Duchy of {old_name}", f"# {new_full_name}")
            if f"# Emirate of {old_name}" in content:
                content = content.replace(f"# Emirate of {old_name}", f"# {new_full_name}")
            if f"# Principality of {old_name}" in content:
                content = content.replace(f"# Principality of {old_name}", f"# {new_full_name}")
            if f"# Dominion of {old_name}" in content:
                content = content.replace(f"# Dominion of {old_name}", f"# {new_full_name}")
            
            content = content.replace(f"- **Name:** {old_name}", f"- **Name:** {new_name}")
            # Handle full name patterns
            if f"Grand Duchy of {old_name}" in content:
                content = content.replace(f"Grand Duchy of {old_name}", new_full_name)
            elif f"Republic of {old_name}" in content:
                content = content.replace(f"Republic of {old_name}", new_full_name)
            elif f"{old_name}n Theocracy" in content:
                content = content.replace(f"{old_name}n Theocracy", new_full_name)
            elif f"Protectorate of {old_name}" in content:
                content = content.replace(f"Protectorate of {old_name}", new_full_name)
            elif f"Duchy of {old_name}" in content:
                content = content.replace(f"Duchy of {old_name}", new_full_name)
            elif f"Emirate of {old_name}" in content:
                content = content.replace(f"Emirate of {old_name}", new_full_name)
            elif f"Principality of {old_name}" in content:
                content = content.replace(f"Principality of {old_name}", new_full_name)
            elif f"Dominion of {old_name}" in content:
                content = content.replace(f"Dominion of {old_name}", new_full_name)
            else:
                # Fallback: replace old_name with new_full_name
                content = content.replace(old_name, new_full_name)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated README.md in {folder_name}")

# Step 3: Update state-data.json files
for state_index, old_name in state_index_map.items():
    if old_name in state_renames:
        new_name, new_full_name = state_renames[old_name]
        folder_name = f"{state_index:02d}-{sanitize_filename(new_name)}"
        json_path = states_dir / folder_name / "state-data.json"
        
        if json_path.exists():
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Update name fields
            if 'name' in data:
                data['name'] = new_name
            if 'fullName' in data:
                data['fullName'] = new_full_name
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Updated state-data.json in {folder_name}")

print("\nState renaming complete!")
