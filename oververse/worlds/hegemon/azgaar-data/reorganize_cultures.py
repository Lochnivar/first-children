#!/usr/bin/env python3
"""
Script to reorganize cultures into a hierarchical structure with
4 major Earth-based culture templates and their subcultures.
"""

import json
import os
import shutil
import re

# Define the major culture groupings
MAJOR_CULTURES = {
    'germanic': {
        'name': 'Germanic',
        'description': 'Northern European cultural template',
        'subcultures': ['Norse', 'Shwazen', 'Angshire']
    },
    'latin': {
        'name': 'Latin',
        'description': 'Romance/Mediterranean cultural template',
        'subcultures': ['Romian', 'Tallian', 'Portuzian', 'Luari']
    },
    'berber': {
        'name': 'Berber',
        'description': 'North African cultural template',
        'subcultures': ['Berberan']
    },
    'slavic': {
        'name': 'Slavic',
        'description': 'Eastern European cultural template',
        'subcultures': ['Slovan', 'Soumi']
    }
}

# Fusion cultures (cultures that blend multiple major templates)
FUSION_CULTURES = {
    'Eurabic': {
        'name': 'Eurabic',
        'description': 'European-Arabic fusion culture',
        'components': ['germanic', 'berber']  # Could also include latin
    }
}

# Special cultures (not part of major templates)
SPECIAL_CULTURES = {
    'Wildlands': 'Uninhabited/wild areas',
    'Vietic': 'East Asian influenced (may be separate or fusion)'
}

def sanitize_filename(name):
    """Convert name to valid filename."""
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'[-\s]+', '-', name)
    return name.lower()

# Read all culture data
cultures_data = {}
cultures_dir = 'cultures'
old_cultures_dir = 'cultures_old'

# Create backup and new structure
if os.path.exists(cultures_dir):
    # Backup old structure
    if os.path.exists(old_cultures_dir):
        shutil.rmtree(old_cultures_dir)
    shutil.copytree(cultures_dir, old_cultures_dir)
    print(f"Backed up old structure to {old_cultures_dir}/")

# Read culture data from old structure
for item in os.listdir(old_cultures_dir):
    item_path = os.path.join(old_cultures_dir, item)
    if os.path.isdir(item_path) and item != 'README.md':
        # Extract culture name from folder name (e.g., "01-berberan" -> "Berberan")
        culture_match = re.match(r'\d+-(.+)', item)
        if culture_match:
            culture_name = culture_match.group(1).replace('-', ' ').title()
            culture_name = culture_name.replace(' ', '')
            
            # Read the culture data
            data_file = os.path.join(item_path, 'culture-data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r', encoding='utf-8') as f:
                    culture_data = json.load(f)
                    cultures_data[culture_name] = {
                        'data': culture_data,
                        'old_path': item_path
                    }

# Create new hierarchical structure
os.makedirs(cultures_dir, exist_ok=True)

# Create major culture directories
for major_key, major_info in MAJOR_CULTURES.items():
    major_dir = os.path.join(cultures_dir, major_key)
    os.makedirs(major_dir, exist_ok=True)
    
    # Create major culture README
    major_readme = f"""# {major_info['name']} Cultural Template

**Type:** Major Culture Template  
**Description:** {major_info['description']}  
**Era:** Hacutonce Era (HE)

## Overview

This directory contains the {major_info['name']} cultural template and its subcultures. The {major_info['name']} template serves as the foundational Earth-based cultural pattern for these related cultures.

## Subcultures

"""
    
    # Create subculture directories
    subcultures_dir = os.path.join(major_dir, 'subcultures')
    os.makedirs(subcultures_dir, exist_ok=True)
    
    for subculture_name in major_info['subcultures']:
        if subculture_name in cultures_data:
            subculture_dir = os.path.join(subcultures_dir, sanitize_filename(subculture_name))
            os.makedirs(subculture_dir, exist_ok=True)
            
            # Copy culture data
            culture_info = cultures_data[subculture_name]
            culture_data = culture_info['data']
            
            # Write culture data
            with open(os.path.join(subculture_dir, 'culture-data.json'), 'w', encoding='utf-8') as f:
                json.dump(culture_data, f, indent=2, ensure_ascii=False)
            
            # Create subculture README
            subculture_readme = f"""# {subculture_name}

**Parent Culture:** {major_info['name']}  
**Culture Index:** {culture_data.get('i', 'N/A')}  
**Status:** Active Subculture  
**Category:** {culture_data.get('type', 'Unknown')}  
**Era:** Hacutonce Era (HE)

## Basic Information

- **Name:** {culture_data.get('name', 'Unknown')}
- **Type:** {culture_data.get('type', 'Unknown')}
- **Code:** {culture_data.get('code', 'N/A')}
- **Base Culture:** {culture_data.get('base', 'N/A')}
- **Color:** `{culture_data.get('color', '#000000')}`
- **Expansionism:** {culture_data.get('expansionism', 'N/A')}
- **Center Cell:** {culture_data.get('center', 'N/A')}
- **Shield Type:** {culture_data.get('shield', 'Unknown')}

## Cultural Origins

- **Origins:** {culture_data.get('origins', [])}

## Additional Data Files

- [Culture Data (JSON)](culture-data.json) - Complete culture data structure

---

*Parent Culture: [{major_info['name']}](../README.md)*  
*For cultures index, see [../../README.md](../../README.md)*
"""
            with open(os.path.join(subculture_dir, 'README.md'), 'w', encoding='utf-8') as f:
                f.write(subculture_readme)
            
            major_readme += f"- [{subculture_name}](subcultures/{sanitize_filename(subculture_name)}/) - {culture_data.get('type', 'Generic')} type\n"
    
    major_readme += f"""
## Notes

- This is a major cultural template based on Earth cultural patterns
- Subcultures share foundational elements but have distinct characteristics
- Cultural indices are preserved from the original Azgaar export

---

*For cultures index, see [../README.md](../README.md)*  
*For Azgaar map data reference, see [../../README.md](../../README.md)*
"""
    
    with open(os.path.join(major_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(major_readme)

# Handle fusion cultures
fusions_dir = os.path.join(cultures_dir, 'fusions')
os.makedirs(fusions_dir, exist_ok=True)

for fusion_name, fusion_info in FUSION_CULTURES.items():
    if fusion_name in cultures_data:
        fusion_dir = os.path.join(fusions_dir, sanitize_filename(fusion_name))
        os.makedirs(fusion_dir, exist_ok=True)
        
        culture_info = cultures_data[fusion_name]
        culture_data = culture_info['data']
        components = ', '.join([MAJOR_CULTURES[c]['name'] for c in fusion_info['components']])
        
        # Write culture data
        with open(os.path.join(fusion_dir, 'culture-data.json'), 'w', encoding='utf-8') as f:
            json.dump(culture_data, f, indent=2, ensure_ascii=False)
        
        # Create fusion README
        fusion_readme = f"""# {fusion_name}

**Type:** Fusion Culture  
**Culture Index:** {culture_data.get('i', 'N/A')}  
**Status:** Active Fusion Culture  
**Category:** {culture_data.get('type', 'Unknown')}  
**Era:** Hacutonce Era (HE)

## Basic Information

- **Name:** {culture_data.get('name', 'Unknown')}
- **Type:** {culture_data.get('type', 'Unknown')}
- **Code:** {culture_data.get('code', 'N/A')}
- **Base Culture:** {culture_data.get('base', 'N/A')}
- **Color:** `{culture_data.get('color', '#000000')}`
- **Expansionism:** {culture_data.get('expansionism', 'N/A')}
- **Center Cell:** {culture_data.get('center', 'N/A')}
- **Shield Type:** {culture_data.get('shield', 'Unknown')}

## Cultural Components

- **Fusion of:** {components}
- **Description:** {fusion_info['description']}

## Cultural Origins

- **Origins:** {culture_data.get('origins', [])}

## Additional Data Files

- [Culture Data (JSON)](culture-data.json) - Complete culture data structure

## Notes

Fusion cultures blend elements from multiple major cultural templates, creating unique hybrid cultural patterns.

---

*For cultures index, see [../README.md](../README.md)*  
*For Azgaar map data reference, see [../../README.md](../../README.md)*
"""
        with open(os.path.join(fusion_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(fusion_readme)

# Handle special cultures
special_dir = os.path.join(cultures_dir, 'special')
os.makedirs(special_dir, exist_ok=True)

for special_name, description in SPECIAL_CULTURES.items():
    if special_name in cultures_data:
        special_culture_dir = os.path.join(special_dir, sanitize_filename(special_name))
        os.makedirs(special_culture_dir, exist_ok=True)
        
        culture_info = cultures_data[special_name]
        culture_data = culture_info['data']
        
        # Write culture data
        with open(os.path.join(special_culture_dir, 'culture-data.json'), 'w', encoding='utf-8') as f:
            json.dump(culture_data, f, indent=2, ensure_ascii=False)
        
        # Create special culture README
        special_readme = f"""# {special_name}

**Type:** Special Culture  
**Culture Index:** {culture_data.get('i', 'N/A')}  
**Status:** Active Culture  
**Category:** {culture_data.get('type', 'Unknown')}  
**Era:** Hacutonce Era (HE)

## Basic Information

- **Name:** {culture_data.get('name', 'Unknown')}
- **Type:** {culture_data.get('type', 'Unknown')}
- **Code:** {culture_data.get('code', 'N/A')}
- **Base Culture:** {culture_data.get('base', 'N/A')}
- **Color:** `{culture_data.get('color', '#000000')}`
- **Expansionism:** {culture_data.get('expansionism', 'N/A')}
- **Center Cell:** {culture_data.get('center', 'N/A')}
- **Shield Type:** {culture_data.get('shield', 'Unknown')}

## Description

{description}

## Cultural Origins

- **Origins:** {culture_data.get('origins', [])}

## Additional Data Files

- [Culture Data (JSON)](culture-data.json) - Complete culture data structure

## Notes

This culture does not fit into the standard major cultural templates and represents a special case.

---

*For cultures index, see [../README.md](../README.md)*  
*For Azgaar map data reference, see [../../README.md](../../README.md)*
"""
        with open(os.path.join(special_culture_dir, 'README.md'), 'w', encoding='utf-8') as f:
            f.write(special_readme)

# Create new index README
index_content = f"""# Hegemon Cultures Index

**Total Cultures:** {len(cultures_data)}  
**Source:** Azgaar Fantasy Map Generator Export  
**Era:** Hacutonce Era (374 HE)

## Culture Organization

Cultures are organized into a hierarchical structure based on Earth cultural templates:

### Major Cultural Templates

These four major templates serve as foundational patterns:

1. **[Germanic](germanic/README.md)** - Northern European cultural template
   - Subcultures: {', '.join(MAJOR_CULTURES['germanic']['subcultures'])}

2. **[Latin](latin/README.md)** - Romance/Mediterranean cultural template
   - Subcultures: {', '.join(MAJOR_CULTURES['latin']['subcultures'])}

3. **[Berber](berber/README.md)** - North African cultural template
   - Subcultures: {', '.join(MAJOR_CULTURES['berber']['subcultures'])}

4. **[Slavic](slavic/README.md)** - Eastern European cultural template
   - Subcultures: {', '.join(MAJOR_CULTURES['slavic']['subcultures'])}

### Fusion Cultures

Cultures that blend multiple major templates:
- **[Fusions](fusions/README.md)** - Hybrid cultures combining elements from multiple templates

### Special Cultures

Cultures that don't fit standard templates:
- **[Special](special/README.md)** - Unique or unclassified cultures

## Directory Structure

```
cultures/
├── germanic/           # Germanic/Northern European template
│   └── subcultures/    # Norse, Shwazen, Angshire
├── latin/              # Latin/Romance template
│   └── subcultures/    # Romian, Tallian, Portuzian, Luari
├── berber/             # Berber/North African template
│   └── subcultures/    # Berberan
├── slavic/             # Slavic/Eastern European template
│   └── subcultures/    # Slovan, Soumi
├── fusions/            # Fusion cultures
│   └── eurabic/        # European-Arabic fusion
└── special/            # Special cultures
    ├── wildlands/      # Uninhabited areas
    └── vietic/         # East Asian influenced
```

## Notes

- **Major Templates:** These are organizational "handles" to conceptualize the cultures, not strict classifications
- **Subcultures:** Variants of major templates with distinct characteristics
- **Fusions:** Cultures that blend elements from multiple major templates
- **Special:** Cultures that don't fit standard categorization
- Culture indices (i) are preserved from the original Azgaar export
- All culture data maintains compatibility with the original export format

---

*For Azgaar map data reference, see [../README.md](../README.md)*  
*For Hegemon world documentation, see [../../README.md](../../README.md)*
"""

# Create fusions README
fusions_readme = f"""# Fusion Cultures

**Description:** Cultures that blend elements from multiple major cultural templates

## Fusion Cultures

"""
for fusion_name, fusion_info in FUSION_CULTURES.items():
    if fusion_name in cultures_data:
        components = ', '.join([MAJOR_CULTURES[c]['name'] for c in fusion_info['components']])
        fusions_readme += f"- **[{fusion_name}]({sanitize_filename(fusion_name)}/)** - {components} fusion\n"

fusions_readme += """
## Notes

Fusion cultures represent hybrid cultural patterns that combine elements from multiple major templates, creating unique cultural identities.

---

*For cultures index, see [../README.md](../README.md)*
"""

with open(os.path.join(fusions_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(fusions_readme)

# Create special README
special_readme = f"""# Special Cultures

**Description:** Cultures that don't fit into standard major cultural templates

## Special Cultures

"""
for special_name, description in SPECIAL_CULTURES.items():
    if special_name in cultures_data:
        special_readme += f"- **[{special_name}]({sanitize_filename(special_name)}/)** - {description}\n"

special_readme += """
## Notes

These cultures represent unique cases that don't fit the standard four-template structure, or are special classifications like uninhabited areas.

---

*For cultures index, see [../README.md](../README.md)*
"""

with open(os.path.join(special_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(special_readme)

# Write main index
with open(os.path.join(cultures_dir, 'README.md'), 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Reorganized {len(cultures_data)} cultures into hierarchical structure")
print(f"Old structure backed up to {old_cultures_dir}/")
print("\nNew structure:")
print("  - 4 major culture templates")
print("  - Subcultures organized under their templates")
print("  - Fusion cultures in separate directory")
print("  - Special cultures in separate directory")

