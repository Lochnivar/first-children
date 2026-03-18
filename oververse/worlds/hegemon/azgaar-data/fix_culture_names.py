#!/usr/bin/env python3
"""
Script to fix culture index replacement - should only replace in Culture column, not Index column
"""

import re
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
states_dir = script_dir / "states"

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

def fix_culture_names_in_md(state_folder):
    """Fix culture names in burgs.md - only replace in Culture column, not Index column."""
    burgs_md_path = state_folder / "burgs.md"
    if not burgs_md_path.exists():
        return False
    
    with open(burgs_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern: Match table rows and replace culture index in the Culture column (last column)
    # Format: | Index | Name | Type | Population | Cell | Culture |
    # We need to be more careful - only replace the last number in each row
    
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        # Check if this is a table row (starts with | and has multiple |)
        if '|' in line and line.strip().startswith('|') and line.count('|') >= 6:
            # Split by |
            parts = [p.strip() for p in line.split('|')]
            # Parts[0] is empty, parts[1] is Index, parts[2] is Name, parts[3] is Type,
            # parts[4] is Population, parts[5] is Cell, parts[6] is Culture
            
            if len(parts) >= 7:
                culture_value = parts[6].strip()
                # Check if it's a numeric culture index
                try:
                    culture_index = int(culture_value)
                    if culture_index in culture_index_to_name:
                        parts[6] = culture_index_to_name[culture_index]
                        # Reconstruct the line
                        new_line = '| ' + ' | '.join(parts[1:]) + ' |'
                        new_lines.append(new_line)
                        continue
                except ValueError:
                    # Not a number, keep as is
                    pass
        
        new_lines.append(line)
    
    new_content = '\n'.join(new_lines)
    
    if new_content != original_content:
        with open(burgs_md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# Fix all burgs.md files
print("Fixing culture name replacements in burgs.md files...")
for state_folder in states_dir.iterdir():
    if state_folder.is_dir() and (state_folder / "burgs.md").exists():
        if fix_culture_names_in_md(state_folder):
            print(f"Fixed culture names in {state_folder.name}/burgs.md")

print("\nCulture name fixes complete!")

