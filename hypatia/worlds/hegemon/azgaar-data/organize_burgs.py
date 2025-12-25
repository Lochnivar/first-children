#!/usr/bin/env python3
"""
Script to organize burgs (cities/settlements) data into state folders
for the Hegemon world Azgaar export.
"""

import json
import os
import re

# Read the burgs JSON file
with open('12-burgs.json', 'r', encoding='utf-8') as f:
    burgs = json.load(f)

# Read states to get state names/index mapping
with open('11-states.json', 'r', encoding='utf-8') as f:
    states = json.load(f)

def sanitize_filename(name):
    """Convert state name to valid filename (matches organize_states.py)."""
    # Replace spaces and special chars with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

# Create mapping from state index to state name for folder names
state_index_to_folder = {}
for state in states:
    state_index = state.get('i')
    state_name = state.get('name', f"State_{state_index}")
    # Match folder naming convention from organize_states.py
    state_folder = f"{state_index:02d}-{sanitize_filename(state_name)}"
    state_index_to_folder[state_index] = state_folder

# Group burgs by state
burgs_by_state = {}
for burg in burgs:
    if burg:  # Skip empty entries
        state_index = burg.get('state', -1)
        if state_index not in burgs_by_state:
            burgs_by_state[state_index] = []
        burgs_by_state[state_index].append(burg)

# Create burgs data for each state
states_dir = 'states'
for state_index, burg_list in burgs_by_state.items():
    # Skip if state folder doesn't exist (shouldn't happen, but safety check)
    if state_index not in state_index_to_folder:
        print(f"Warning: No folder found for state index {state_index}, skipping {len(burg_list)} burgs")
        continue
    
    state_folder = os.path.join(states_dir, state_index_to_folder[state_index])
    
    if not os.path.exists(state_folder):
        print(f"Warning: State folder {state_folder} does not exist, skipping")
        continue
    
    # Write burgs JSON file
    burgs_file = os.path.join(state_folder, 'burgs.json')
    with open(burgs_file, 'w', encoding='utf-8') as f:
        json.dump(burg_list, f, indent=2, ensure_ascii=False)
    
    # Create a summary markdown file
    summary_lines = [
        f"# Burgs (Cities/Settlements) - {state_index_to_folder[state_index].split('-', 1)[1].title()}",
        "",
        f"**Total Burgs:** {len(burg_list)}",
        "",
        "## Burgs List",
        "",
        "| Index | Name | Type | Population | Cell | Culture |",
        "|-------|------|------|------------|------|---------|"
    ]
    
    for burg in burg_list:
        burg_index = burg.get('i', '?')
        burg_name = burg.get('name', 'Unknown')
        burg_type = burg.get('type', 'Unknown')
        population = burg.get('population', 0)
        cell = burg.get('cell', '?')
        culture = burg.get('culture', '?')
        summary_lines.append(f"| {burg_index} | {burg_name} | {burg_type} | {population:,.2f} | {cell} | {culture} |")
    
    summary_lines.extend([
        "",
        "## Additional Information",
        "",
        "- See [burgs.json](burgs.json) for complete burg data structures",
        "- Burgs include detailed information about settlements, ports, features, and more",
        "",
        "---",
        "",
        "*For state overview, see [README.md](README.md)*"
    ])
    
    summary_file = os.path.join(state_folder, 'burgs.md')
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary_lines))
    
    print(f"State {state_index} ({state_index_to_folder[state_index]}): {len(burg_list)} burgs")

# Summary
total_burgs = sum(len(burg_list) for burg_list in burgs_by_state.values())
print(f"\nTotal burgs organized: {total_burgs} across {len(burgs_by_state)} states")

