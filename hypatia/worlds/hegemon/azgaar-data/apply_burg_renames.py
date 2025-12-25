#!/usr/bin/env python3
"""
Script to apply burg name changes from HEGEMON-DIALOG.md
"""

import json
import re
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
states_dir = script_dir / "states"

# Burg renames: (old_name, state_folder) -> new_name
burg_renames = {
    ("Postignino", "04-agrima"): "Taghrast",
    ("Duy Hoa Thuy", "18-pondara"): "Duyhaven",
    # Note: Monte appears twice in Agrima - need to handle both instances
    ("Monte", "04-agrima"): None,  # Special case - two instances
    ("Capra", "04-agrima"): "Qabrash",
    ("Lanovilliter", "04-agrima"): "Tazaghrut",
    ("Binh", "04-agrima"): "Binhar",
    ("Thai", "04-agrima"): "Thaidar",
    ("Alqouzwa", "16-sigdak"): "Alqvard",
    ("Alkhakah", "16-sigdak"): "Alkhavn",
    ("Veravartus", "16-sigdak"): "Veravarth",
    ("Ralelius", "16-sigdak"): "Ralefoss",
    ("Dusustium", "16-sigdak"): "Dusustheim",
    ("Qoshayrif", "20-jarklaus"): "Qoshavn",
    ("Vererido", "19-rutarakia"): "Verelaki",
    ("Afiasecqua", "19-rutarakia"): "Afiasekka",
    ("Fandimbalhe", "14-kailhen"): "Phan Dinh",
    ("Lqlibahag", "04-agrima"): "Qalibah",
    ("Zrifelt Ba", "04-agrima"): "Zrifelt",
    ("Asaseccumola", "08-pontena"): "Asaccio",
    ("Sgurnesera", "08-pontena"): "Sgurnesi",
    ("Vines", "02-trevalia"): "Vignes",
}

# Culture index to name mapping
culture_index_to_name = {
    0: "Wildlands",
    1: "Qasridan",
    2: "Meridian",
    3: "Valthir",
    4: "Zvezdan",
    5: "Aurelian",
    6: "Sturmgaard",
    7: "Veridian",
    8: "Solemnium",
    9: "Eldermark",
    10: "Yaroslav",
    11: "Khanhthien",
    12: "Sundrakar",
}

def update_burg_json(state_folder, old_name, new_name):
    """Update burg name in burgs.json file."""
    burgs_json_path = state_folder / "burgs.json"
    if not burgs_json_path.exists():
        return False
    
    with open(burgs_json_path, 'r', encoding='utf-8') as f:
        burgs = json.load(f)
    
    updated = False
    for burg in burgs:
        if burg.get('name') == old_name:
            burg['name'] = new_name
            updated = True
    
    if updated:
        with open(burgs_json_path, 'w', encoding='utf-8') as f:
            json.dump(burgs, f, indent=2, ensure_ascii=False)
        return True
    return False

def update_burg_md(state_folder, old_name, new_name):
    """Update burg name in burgs.md file."""
    burgs_md_path = state_folder / "burgs.md"
    if not burgs_md_path.exists():
        return False
    
    with open(burgs_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace burg name in table (using word boundaries to avoid partial matches)
    pattern = r'\b' + re.escape(old_name) + r'\b'
    new_content = re.sub(pattern, new_name, content)
    
    if new_content != content:
        with open(burgs_md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def update_culture_names_in_md(state_folder):
    """Replace culture indices with culture names in burgs.md."""
    burgs_md_path = state_folder / "burgs.md"
    if not burgs_md_path.exists():
        return False
    
    with open(burgs_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace culture indices in the table
    # Pattern: | ... | N | where N is a culture index
    original_content = content
    
    # Replace culture index in table rows
    for index, name in culture_index_to_name.items():
        # Match culture index at end of table row (before |)
        pattern = rf'\| {index} \|'
        replacement = f'| {name} |'
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        with open(burgs_md_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Special handling for Monte in Agrima (two instances need different names)
agrima_folder = states_dir / "04-agrima"
if agrima_folder.exists():
    burgs_json_path = agrima_folder / "burgs.json"
    if burgs_json_path.exists():
        with open(burgs_json_path, 'r', encoding='utf-8') as f:
            burgs = json.load(f)
        
        monte_count = 0
        for burg in burgs:
            if burg.get('name') == "Monte":
                if monte_count == 0:
                    burg['name'] = "Mzurit"
                    monte_count += 1
                elif monte_count == 1:
                    burg['name'] = "Mazraq"
                    monte_count += 1
        
        if monte_count > 0:
            with open(burgs_json_path, 'w', encoding='utf-8') as f:
                json.dump(burgs, f, indent=2, ensure_ascii=False)
            print(f"Updated {monte_count} instances of 'Monte' in Agrima")
            
            # Update burgs.md for Monte instances
            burgs_md_path = agrima_folder / "burgs.md"
            if burgs_md_path.exists():
                with open(burgs_md_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace first occurrence with Mzurit, second with Mazraq
                content = re.sub(r'\bMonte\b', 'Mzurit', content, count=1)
                content = re.sub(r'\bMonte\b', 'Mazraq', content, count=1)
                
                with open(burgs_md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print("Updated burgs.md for Monte instances")

# Apply all other burg renames
for (old_name, state_folder_name), new_name in burg_renames.items():
    if new_name is None:
        continue  # Skip Monte, handled above
    
    state_folder = states_dir / state_folder_name
    if state_folder.exists():
        updated_json = update_burg_json(state_folder, old_name, new_name)
        updated_md = update_burg_md(state_folder, old_name, new_name)
        
        if updated_json or updated_md:
            print(f"Updated {old_name} -> {new_name} in {state_folder_name}")
        else:
            print(f"Warning: {old_name} not found in {state_folder_name}")

# Update culture names in all burgs.md files
print("\nUpdating culture indices to names in burgs.md files...")
for state_folder in states_dir.iterdir():
    if state_folder.is_dir() and (state_folder / "burgs.md").exists():
        if update_culture_names_in_md(state_folder):
            print(f"Updated culture names in {state_folder.name}/burgs.md")

print("\nBurg renames complete!")

