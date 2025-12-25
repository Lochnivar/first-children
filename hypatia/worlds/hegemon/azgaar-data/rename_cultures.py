#!/usr/bin/env python3
"""
Script to generate and apply new names for all cultures in Hegemon.
Creates a mapping file that can be edited, then applies the names.
"""

import json
import os
import re
from pathlib import Path

# Define new names for cultures
# Format: {old_name: new_name}
CULTURE_NAME_MAPPING = {
    # Major Templates (these stay as conceptual handles, but could be renamed too)
    'germanic': 'germanic',  # Keep as template name
    'latin': 'latin',  # Keep as template name
    'berber': 'berber',  # Keep as template name
    'slavic': 'slavic',  # Keep as template name
    
    # Germanic Subcultures
    'Norse': 'Valthir',
    'Shwazen': 'Sturmgaard',
    'Angshire': 'Eldermark',
    
    # Latin Subcultures
    'Romian': 'Veridian',
    'Tallian': 'Solemnium',
    'Portuzian': 'Aurelian',
    'Luari': 'Meridian',
    
    # Berber Subcultures
    'Berberan': 'Qasridan',
    
    # Slavic Subcultures
    'Slovan': 'Zvezdan',
    'Soumi': 'Yaroslav',
    
    # Fusion Cultures
    'Eurabic': 'Sundrakar',
    
    # Special Cultures
    'Wildlands': 'Wildlands',  # Keep as is - it's a special classification
    'Vietic': 'Khanhthien',
}

def sanitize_filename(name):
    """Convert name to valid filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

def find_and_replace_in_file(filepath, old_name, new_name):
    """Replace culture name in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the name (being careful with word boundaries)
        # Replace in JSON values
        content = re.sub(rf'"{re.escape(old_name)}"', f'"{new_name}"', content)
        # Replace in markdown headers and text
        content = re.sub(rf'# {re.escape(old_name)}', f'# {new_name}', content)
        content = re.sub(rf'\*\*{re.escape(old_name)}\*\*', f'**{new_name}**', content)
        # Replace in bullet lists
        content = re.sub(rf'- \*\*{re.escape(old_name)}\*\*', f'- **{new_name}**', content)
        # Replace in subculture lists (e.g., "Subcultures: Norse, Shwazen")
        content = re.sub(rf'\b{re.escape(old_name)}\b', new_name, content)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def rename_culture_directory(old_dir, new_dir_name):
    """Rename a culture directory."""
    if os.path.exists(old_dir) and os.path.exists(os.path.dirname(old_dir)):
        new_dir = os.path.join(os.path.dirname(old_dir), new_dir_name)
        if old_dir != new_dir:
            os.rename(old_dir, new_dir)
            return new_dir
    return old_dir

cultures_dir = 'cultures'
renamed_count = 0

# Process major templates and their subcultures
for major_key, major_name in [('germanic', 'Germanic'), ('latin', 'Latin'), ('berber', 'Berber'), ('slavic', 'Slavic')]:
    major_dir = os.path.join(cultures_dir, major_key)
    subcultures_dir = os.path.join(major_dir, 'subcultures')
    
    if os.path.exists(subcultures_dir):
        for subculture_old_name, subculture_new_name in CULTURE_NAME_MAPPING.items():
            if subculture_old_name in ['Norse', 'Shwazen', 'Angshire'] and major_key == 'germanic':
                old_sub_dir = os.path.join(subcultures_dir, sanitize_filename(subculture_old_name))
            elif subculture_old_name in ['Romian', 'Tallian', 'Portuzian', 'Luari'] and major_key == 'latin':
                old_sub_dir = os.path.join(subcultures_dir, sanitize_filename(subculture_old_name))
            elif subculture_old_name == 'Berberan' and major_key == 'berber':
                old_sub_dir = os.path.join(subcultures_dir, sanitize_filename(subculture_old_name))
            elif subculture_old_name in ['Slovan', 'Soumi'] and major_key == 'slavic':
                old_sub_dir = os.path.join(subcultures_dir, sanitize_filename(subculture_old_name))
            else:
                continue
            
            if os.path.exists(old_sub_dir):
                new_sub_dir_name = sanitize_filename(subculture_new_name)
                new_sub_dir = os.path.join(subcultures_dir, new_sub_dir_name)
                
                # Update JSON files
                json_file = os.path.join(old_sub_dir, 'culture-data.json')
                if os.path.exists(json_file):
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    data['name'] = subculture_new_name
                    with open(json_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                
                # Update README files
                readme_file = os.path.join(old_sub_dir, 'README.md')
                if os.path.exists(readme_file):
                    find_and_replace_in_file(readme_file, subculture_old_name, subculture_new_name)
                
                # Rename directory
                if old_sub_dir != new_sub_dir:
                    os.rename(old_sub_dir, new_sub_dir)
                    print(f"Renamed {subculture_old_name} -> {subculture_new_name}")
                    renamed_count += 1
                
                # Update major template README
                major_readme = os.path.join(major_dir, 'README.md')
                if os.path.exists(major_readme):
                    find_and_replace_in_file(major_readme, subculture_old_name, subculture_new_name)

# Process fusion cultures
fusions_dir = os.path.join(cultures_dir, 'fusions')
for fusion_old_name, fusion_new_name in CULTURE_NAME_MAPPING.items():
    if fusion_old_name == 'Eurabic':
        old_fusion_dir = os.path.join(fusions_dir, sanitize_filename(fusion_old_name))
        if os.path.exists(old_fusion_dir):
            new_fusion_dir_name = sanitize_filename(fusion_new_name)
            new_fusion_dir = os.path.join(fusions_dir, new_fusion_dir_name)
            
            # Update JSON
            json_file = os.path.join(old_fusion_dir, 'culture-data.json')
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                data['name'] = fusion_new_name
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Update README
            readme_file = os.path.join(old_fusion_dir, 'README.md')
            if os.path.exists(readme_file):
                find_and_replace_in_file(readme_file, fusion_old_name, fusion_new_name)
            
            # Rename directory
            if old_fusion_dir != new_fusion_dir:
                os.rename(old_fusion_dir, new_fusion_dir)
                print(f"Renamed fusion {fusion_old_name} -> {fusion_new_name}")
                renamed_count += 1

# Process special cultures
special_dir = os.path.join(cultures_dir, 'special')
for special_old_name, special_new_name in CULTURE_NAME_MAPPING.items():
    if special_old_name in ['Wildlands', 'Vietic']:
        old_special_dir = os.path.join(special_dir, sanitize_filename(special_old_name))
        if os.path.exists(old_special_dir):
            new_special_dir_name = sanitize_filename(special_new_name)
            new_special_dir = os.path.join(special_dir, new_special_dir_name)
            
            # Update JSON
            json_file = os.path.join(old_special_dir, 'culture-data.json')
            if os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                data['name'] = special_new_name
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Update README
            readme_file = os.path.join(old_special_dir, 'README.md')
            if os.path.exists(readme_file):
                find_and_replace_in_file(readme_file, special_old_name, special_new_name)
            
            # Rename directory (only if name changed)
            if special_old_name != special_new_name and old_special_dir != new_special_dir:
                os.rename(old_special_dir, new_special_dir)
                print(f"Renamed special {special_old_name} -> {special_new_name}")
                renamed_count += 1

# Update main cultures README
main_readme = os.path.join(cultures_dir, 'README.md')
if os.path.exists(main_readme):
    for old_name, new_name in CULTURE_NAME_MAPPING.items():
        if old_name not in ['germanic', 'latin', 'berber', 'slavic']:
            find_and_replace_in_file(main_readme, old_name, new_name)

# Update fusions README
fusions_readme = os.path.join(fusions_dir, 'README.md')
if os.path.exists(fusions_readme):
    for old_name, new_name in CULTURE_NAME_MAPPING.items():
        if old_name == 'Eurabic':
            find_and_replace_in_file(fusions_readme, old_name, new_name)

# Update special README
special_readme = os.path.join(special_dir, 'README.md')
if os.path.exists(special_readme):
    for old_name, new_name in CULTURE_NAME_MAPPING.items():
        if old_name in ['Wildlands', 'Vietic']:
            find_and_replace_in_file(special_readme, old_name, new_name)

print(f"\nRenaming complete! Processed {renamed_count} culture directories.")
print("\nNew culture names:")
for old, new in sorted(CULTURE_NAME_MAPPING.items()):
    if old not in ['germanic', 'latin', 'berber', 'slavic'] and old != new:
        print(f"  {old} -> {new}")

