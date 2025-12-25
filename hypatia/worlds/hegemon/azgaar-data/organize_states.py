#!/usr/bin/env python3
"""
Script to organize states data into individual folders and files
for the Hegemon world Azgaar export.
"""

import json
import os
import re

# Read the states JSON file
with open('11-states.json', 'r', encoding='utf-8') as f:
    states = json.load(f)

# Create states directory
states_dir = 'states'
os.makedirs(states_dir, exist_ok=True)

def sanitize_filename(name):
    """Convert state name to valid filename."""
    # Replace spaces and special chars with underscores
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

def write_json_file(filepath, data):
    """Write JSON data to file with pretty formatting."""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def create_state_overview(state):
    """Create overview markdown file for a state."""
    md_content = f"""# {state.get('fullName', state.get('name', f"State {state.get('i', '?')}"))}

**State Index:** {state.get('i', 'N/A')}  
**Status:** Active State  
**Category:** {state.get('type', 'Unknown')}  
**Form of Government:** {state.get('formName', state.get('form', 'Unknown'))}  
**Era:** Hacutonce Era (HE)

## Basic Information

- **Name:** {state.get('name', 'Unknown')}
- **Full Name:** {state.get('fullName', state.get('name', 'Unknown'))}
- **Capital:** Burg #{state.get('capital', 'N/A')}
- **Culture:** Culture #{state.get('culture', 'N/A')}
- **Color:** `{state.get('color', '#000000')}`
- **Expansionism:** {state.get('expansionism', 'N/A')}
- **Alert Level:** {state.get('alert', 'N/A')}

## Demographics

- **Urban Population:** {state.get('urban', 0):,.0f}
- **Rural Population:** {state.get('rural', 0):,.2f}
- **Total Population:** {state.get('urban', 0) + state.get('rural', 0):,.2f}
- **Settlements (Burgs):** {state.get('burgs', 0)}
- **Area:** {state.get('area', 0):,.0f} (cells: {state.get('cells', 0)})

## Geographic Information

- **Center Cell:** {state.get('center', 'N/A')}
- **Pole Coordinates:** {state.get('pole', 'N/A')}
- **Neighboring States:** {len(state.get('neighbors', []))} states
- **Provinces:** {len(state.get('provinces', []))} provinces

## Military

- **Total Regiments:** {len(state.get('military', []))}
- See [military.json](military.json) for detailed unit compositions

## Additional Data Files

- [State Data (JSON)](state-data.json) - Complete state data structure
- [Military](military.json) - Detailed military unit information
- [Diplomacy](diplomacy.json) - Diplomatic relations with other states
- [Campaigns](campaigns.json) - Historical campaigns and wars
- [Provinces](provinces.json) - Province list and structure

---

*For Azgaar map data reference, see [../README.md](../README.md)*  
*For Hegemon world documentation, see [../../README.md](../../README.md)*
"""
    return md_content

# Process each state
for state in states:
    state_name = state.get('name', f"State_{state.get('i', 'unknown')}")
    state_dir = os.path.join(states_dir, f"{state.get('i', 0):02d}-{sanitize_filename(state_name)}")
    os.makedirs(state_dir, exist_ok=True)
    
    # Create overview README
    overview_content = create_state_overview(state)
    with open(os.path.join(state_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(overview_content)
    
    # Create state-data.json (complete state object)
    write_json_file(os.path.join(state_dir, 'state-data.json'), state)
    
    # Extract and save military data
    military_data = state.get('military', [])
    write_json_file(os.path.join(state_dir, 'military.json'), military_data)
    
    # Extract and save diplomacy data
    diplomacy_data = {
        'neighbors': state.get('neighbors', []),
        'diplomacy_array': state.get('diplomacy', []),
        'note': 'Diplomacy array corresponds to state indices. Index position = target state index.'
    }
    write_json_file(os.path.join(state_dir, 'diplomacy.json'), diplomacy_data)
    
    # Extract and save campaigns
    campaigns_data = state.get('campaigns', [])
    write_json_file(os.path.join(state_dir, 'campaigns.json'), campaigns_data)
    
    # Extract and save provinces
    provinces_data = {
        'provinces': state.get('provinces', []),
        'count': len(state.get('provinces', []))
    }
    write_json_file(os.path.join(state_dir, 'provinces.json'), provinces_data)
    
    # Extract coat of arms if present
    if 'coa' in state:
        write_json_file(os.path.join(state_dir, 'coat-of-arms.json'), state['coa'])

# Create index README
index_content = f"""# Hegemon States Index

**Total States:** {len(states)}  
**Source:** Azgaar Fantasy Map Generator Export  
**Era:** Hacutonce Era (374 HE)

## States Directory

This directory contains detailed data for each state in the Hegemon world map. Each state has its own folder with organized data files.

### State List

| Index | Name | Full Name | Type | Form | Capital |
|-------|------|-----------|------|------|---------|
"""
for state in states:
    index = state.get('i', '?')
    name = state.get('name', 'Unknown')
    full_name = state.get('fullName', name)
    state_type = state.get('type', 'Unknown')
    form = state.get('formName', state.get('form', 'Unknown'))
    capital = state.get('capital', 'N/A')
    folder_name = f"{state.get('i', 0):02d}-{sanitize_filename(state.get('name', 'Unknown'))}"
    index_content += f"| {index} | {name} | {full_name} | {state_type} | {form} | #{capital} |\n"

index_content += f"""
## File Structure

Each state folder contains:

- **README.md** - Overview and summary of the state
- **state-data.json** - Complete state data from Azgaar export
- **military.json** - Military units and regiments
- **diplomacy.json** - Diplomatic relations with other states
- **campaigns.json** - Historical campaigns and wars
- **provinces.json** - Province list
- **coat-of-arms.json** - Coat of arms data (if available)

## Notes

- State indices (i) are used as unique identifiers
- Diplomatic relations use state indices as array positions
- Military data includes unit compositions and locations
- Campaign data includes start/end years and relationships

---

*For Azgaar map data reference, see [../README.md](../README.md)*  
*For Hegemon world documentation, see [../../README.md](../../README.md)*
"""

with open(os.path.join(states_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Organized {len(states)} states into individual folders")
print(f"States directory: {states_dir}/")

