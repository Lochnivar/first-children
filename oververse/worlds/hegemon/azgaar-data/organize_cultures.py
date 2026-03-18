#!/usr/bin/env python3
"""
Script to organize cultures data into individual folders
for the Hegemon world Azgaar export.
"""

import json
import os
import re

# Read the cultures JSON file
with open('10-cultures.json', 'r', encoding='utf-8') as f:
    cultures = json.load(f)

# Create cultures directory
cultures_dir = 'cultures'
os.makedirs(cultures_dir, exist_ok=True)

def sanitize_filename(name):
    """Convert culture name to valid filename."""
    # Replace spaces and special chars
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

def create_culture_overview(culture):
    """Create overview markdown file for a culture."""
    culture_name = culture.get('name', f"Culture_{culture.get('i', '?')}")
    md_content = f"""# {culture_name}

**Culture Index:** {culture.get('i', 'N/A')}  
**Status:** Active Culture  
**Category:** {culture.get('type', 'Unknown')}  
**Era:** Hacutonce Era (HE)

## Basic Information

- **Name:** {culture.get('name', 'Unknown')}
- **Type:** {culture.get('type', 'Unknown')}
- **Code:** {culture.get('code', 'N/A')}
- **Base Culture:** {culture.get('base', 'N/A')}
- **Color:** `{culture.get('color', '#000000')}`
- **Expansionism:** {culture.get('expansionism', 'N/A')}
- **Center Cell:** {culture.get('center', 'N/A')}
- **Shield Type:** {culture.get('shield', 'Unknown')}

## Cultural Origins

- **Origins:** {culture.get('origins', [])}

## Additional Data Files

- [Culture Data (JSON)](culture-data.json) - Complete culture data structure

---

*For Azgaar map data reference, see [../README.md](../README.md)*  
*For Hegemon world documentation, see [../../README.md](../../README.md)*
"""
    return md_content

# Process each culture
for culture in cultures:
    culture_index = culture.get('i', 0)
    culture_name = culture.get('name', f"Culture_{culture_index}")
    culture_dir = os.path.join(cultures_dir, f"{culture_index:02d}-{sanitize_filename(culture_name)}")
    os.makedirs(culture_dir, exist_ok=True)
    
    # Create overview README
    overview_content = create_culture_overview(culture)
    with open(os.path.join(culture_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(overview_content)
    
    # Create culture-data.json (complete culture object)
    with open(os.path.join(culture_dir, 'culture-data.json'), 'w', encoding='utf-8') as f:
        json.dump(culture, f, indent=2, ensure_ascii=False)

# Create index README
index_content = f"""# Hegemon Cultures Index

**Total Cultures:** {len(cultures)}  
**Source:** Azgaar Fantasy Map Generator Export  
**Era:** Hacutonce Era (374 HE)

## Cultures Directory

This directory contains detailed data for each culture in the Hegemon world map. Each culture has its own folder with organized data files.

### Culture List

| Index | Name | Type | Code | Expansionism | Base |
|-------|------|------|------|--------------|------|
"""
for culture in cultures:
    index = culture.get('i', '?')
    name = culture.get('name', 'Unknown')
    culture_type = culture.get('type', 'Unknown')
    code = culture.get('code', 'N/A')
    expansionism = culture.get('expansionism', 'N/A')
    base = culture.get('base', 'N/A')
    folder_name = f"{culture.get('i', 0):02d}-{sanitize_filename(culture.get('name', 'Unknown'))}"
    index_content += f"| {index} | {name} | {culture_type} | {code} | {expansionism} | {base} |\n"

index_content += f"""
## File Structure

Each culture folder contains:

- **README.md** - Overview and summary of the culture
- **culture-data.json** - Complete culture data from Azgaar export

## Notes

- Culture indices (i) are used as unique identifiers
- Cultures may have origins from other cultures (cultural development)
- Base culture refers to the base template used
- Expansionism values indicate cultural spread tendencies
- Center cell indicates the geographic center of the culture

---

*For Azgaar map data reference, see [../README.md](../README.md)*  
*For Hegemon world documentation, see [../../README.md](../../README.md)*
"""

with open(os.path.join(cultures_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Organized {len(cultures)} cultures into individual folders")
print(f"Cultures directory: {cultures_dir}/")

