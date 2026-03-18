#!/usr/bin/env python3
"""
Script to fix Index column in burgs.md - replace any culture names in Index column with correct numeric indices
"""

import json
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
states_dir = script_dir / "states"

# Culture names that might appear in Index column (should be replaced)
culture_names = {"Wildlands", "Qasridan", "Meridian", "Valthir", "Zvezdan", "Aurelian", 
                 "Sturmgaard", "Veridian", "Solemnium", "Eldermark", "Yaroslav", 
                 "Khanhthien", "Sundrakar"}

def fix_index_column_final(state_folder):
    """Fix Index column in burgs.md by replacing culture names with correct numeric indices."""
    burgs_md_path = state_folder / "burgs.md"
    burgs_json_path = state_folder / "burgs.json"
    
    if not burgs_md_path.exists() or not burgs_json_path.exists():
        return False
    
    # Load JSON to get correct indices
    with open(burgs_json_path, 'r', encoding='utf-8') as f:
        burgs = json.load(f)
    
    # Create name -> index mapping
    name_to_index = {burg.get('name'): burg.get('i') for burg in burgs}
    
    with open(burgs_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Check if this is a table row with burg data
        if '|' in line and line.strip().startswith('|') and line.count('|') >= 6:
            # Split by |
            parts = [p.strip() for p in line.split('|')]
            # Parts[0] is empty, parts[1] is Index, parts[2] is Name, etc.
            
            if len(parts) >= 7:
                burg_name = parts[2].strip()
                current_index = parts[1].strip()
                
                # Check if current_index is a culture name (should be a number)
                if current_index in culture_names:
                    # Get correct index from JSON
                    correct_index = name_to_index.get(burg_name)
                    if correct_index is not None:
                        parts[1] = str(correct_index)
                        # Reconstruct the line
                        new_line = '| ' + ' | '.join(parts[1:]) + ' |'
                        new_lines.append(new_line)
                        continue
        
        new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content:
        with open(burgs_md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Fix all burgs.md files
print("Fixing Index column (culture names -> numbers) in burgs.md files...")
for state_folder in states_dir.iterdir():
    if state_folder.is_dir() and (state_folder / "burgs.md").exists() and (state_folder / "burgs.json").exists():
        if fix_index_column_final(state_folder):
            print(f"Fixed Index column in {state_folder.name}/burgs.md")

print("\nIndex column fixes complete!")

