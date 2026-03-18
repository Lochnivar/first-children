#!/usr/bin/env python3
"""
Parse HEGEMON-DIALOG.md for burg entries and update burg documentation
"""

import re
from pathlib import Path

script_dir = Path(__file__).parent
dialog_file = script_dir.parent / 'HEGEMON-DIALOG.md'
states_dir = script_dir / 'states'

# Read the dialog file
print("Reading HEGEMON-DIALOG.md...")
with open(dialog_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse burg entries
# Format: ## BurgName (Capital) - optional
# **Type:** ... | **Population:** ... | **Culture:** ...
# Then descriptive text

burg_pattern = r'##\s+([^\n]+)\n\*\*Type:\*\*\s*([^|]+)\s*\|\s*\*\*Population:\*\*\s*([^|]+)\s*\|\s*\*\*Culture:\*\*\s*([^\n]+)\n\n(.*?)(?=\n---|\n##|$)'

burgs = {}
for match in re.finditer(burg_pattern, content, re.DOTALL):
    burg_name_full = match.group(1).strip()
    # Handle "(Capital)" or other parenthetical notes
    burg_name = re.sub(r'\s*\([^)]+\)', '', burg_name_full).strip()
    burg_type = match.group(2).strip()
    burg_pop = match.group(3).strip()
    burg_culture = match.group(4).strip()
    burg_description = match.group(5).strip()
    
    burgs[burg_name] = {
        'name': burg_name,
        'full_name': burg_name_full,
        'type': burg_type,
        'population': burg_pop,
        'culture': burg_culture,
        'description': burg_description
    }
    print(f"Found burg: {burg_name} ({burg_type}, {burg_pop}, {burg_culture})")

print(f"\nFound {len(burgs)} burgs total")

# Find which state each burg belongs to by checking burgs.json files
print("\nMatching burgs to states...")
for state_folder in states_dir.iterdir():
    if not state_folder.is_dir() or not state_folder.name[0].isdigit():
        continue
    
    burgs_json_file = state_folder / 'burgs.json'
    if not burgs_json_file.exists():
        continue
    
    # Read the burgs.json to find burg names
    import json
    with open(burgs_json_file, 'r', encoding='utf-8') as f:
        state_burgs = json.load(f)
    
    state_name = state_folder.name
    matched_burgs = []
    
    for burg_data in state_burgs:
        if burg_data and 'name' in burg_data:
            burg_json_name = burg_data['name']
            if burg_json_name in burgs:
                matched_burgs.append((burg_json_name, burg_data))
                burgs[burg_json_name]['state_folder'] = state_folder
                burgs[burg_json_name]['burg_data'] = burg_data
    
    if matched_burgs:
        print(f"  {state_name}: {len(matched_burgs)} burgs matched")
        for burg_name, _ in matched_burgs:
            print(f"    - {burg_name}")

# Now create or update burg README files
print("\n\nCreating/updating burg documentation...")

for burg_name, burg_info in burgs.items():
    if 'state_folder' not in burg_info:
        print(f"  WARNING: {burg_name} not found in any state's burgs.json, skipping")
        continue
    
    state_folder = burg_info['state_folder']
    burg_docs_dir = state_folder / 'burgs'
    burg_docs_dir.mkdir(exist_ok=True)
    
    # Create a safe filename from burg name
    safe_name = re.sub(r'[^\w\s-]', '', burg_name)
    safe_name = re.sub(r'[-\s]+', '-', safe_name)
    safe_name = safe_name.lower()
    burg_readme = burg_docs_dir / f'{safe_name}.md'
    
    # Generate README content
    readme_content = f"""# {burg_info['full_name']}

**Type:** {burg_info['type']} | **Population:** {burg_info['population']} | **Culture:** {burg_info['culture']}

{burg_info['description']}

---

*For state overview, see [../README.md](../README.md)*
*For all burgs in this state, see [../burgs.md](../burgs.md)*
"""
    
    with open(burg_readme, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"  Created/updated: {state_folder.name}/burgs/{safe_name}.md")

print("\nDone!")

