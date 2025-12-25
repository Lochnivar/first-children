#!/usr/bin/env python3
"""
Script to reassemble the map file (hegemon.map) from updated parsed data files
"""

import json
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
output_file = script_dir / "hegemon.map"

# Load the master JSON files (will update them with new names)
states_json_file = script_dir / "11-states.json"
burgs_json_file = script_dir / "12-burgs.json"

print("Loading master JSON files...")

# Load and update states
with open(states_json_file, 'r', encoding='utf-8-sig') as f:
    states = json.load(f)

# State name mappings
state_name_updates = {
    "Tridia": "Trevalia",
    "Torklia": "Tormaline",
    "Kutiotania": "Kutiograd",
    "Cailinhia": "Kailhen",
    "Ngatria": "Ngathar",
    "Shibaha": "Shibara",
    "Brinachia": "Brinach",
    "Sigdakland": "Sigdak",
    "Sealia": "Sealaris",
    "Ponden": "Pondara",
}

state_full_name_updates = {
    "Grand Duchy of Tridia": "Grand Duchy of Trevalia",
    "Republic of Torklia": "Republic of Tormaline",
    "Kutiotanian Theocracy": "Kutiograd Theocracy",
    "Protectorate of Cailinhia": "Protectorate of Kailhen",
    "Duchy of Ngatria": "Duchy of Ngathar",
    "Emirate of Shibaha": "Emirate of Shibara",
    "Principality of Brinachia": "Principality of Brinach",
    "Protectorate of Sigdakland": "Protectorate of Sigdak",
    "Principality of Sealia": "Principality of Sealaris",
    "Dominion of Ponden": "Dominion of Pondara",
}

print("\nUpdating states array...")
for state in states:
    if state and 'name' in state:
        old_name = state['name']
        if old_name in state_name_updates:
            state['name'] = state_name_updates[old_name]
            print(f"  Updated state: {old_name} -> {state_name_updates[old_name]}")
    
    if state and 'fullName' in state:
        old_full_name = state['fullName']
        if old_full_name in state_full_name_updates:
            state['fullName'] = state_full_name_updates[old_full_name]

# Load and update burgs
with open(burgs_json_file, 'r', encoding='utf-8-sig') as f:
    burgs = json.load(f)

# Burg name mappings
burg_name_updates = {
    "Postignino": "Taghrast",
    "Duy Hoa Thuy": "Duyhaven",
    "Capra": "Qabrash",
    "Lanovilliter": "Tazaghrut",
    "Binh": "Binhar",  # Note: Only for Agrima (state 4)
    "Alqouzwa": "Alqvard",
    "Alkhakah": "Alkhavn",
    "Veravartus": "Veravarth",
    "Ralelius": "Ralefoss",
    "Dusustium": "Dusustheim",
    "Qoshayrif": "Qoshavn",
    "Vererido": "Verelaki",
    "Afiasecqua": "Afiasekka",
    "Fandimbalhe": "Phan Dinh",
    "Lqlibahag": "Qalibah",
    "Zrifelt Ba": "Zrifelt",
    "Asaseccumola": "Asaccio",
    "Sgurnesera": "Sgurnesi",
    "Vines": "Vignes",
}

print("\nUpdating burgs array...")
monte_count_agrima = 0
for burg in burgs:
    if burg and 'name' in burg:
        old_name = burg['name']
        burg_state = burg.get('state')
        
        # Special handling for Monte in Agrima (state 4)
        if old_name == "Monte" and burg_state == 4:
            if monte_count_agrima == 0:
                burg['name'] = "Mzurit"
                monte_count_agrima += 1
                print(f"  Updated burg: Monte -> Mzurit (Agrima, first instance)")
            else:
                burg['name'] = "Mazraq"
                monte_count_agrima += 1
                print(f"  Updated burg: Monte -> Mazraq (Agrima, second instance)")
        elif old_name in burg_name_updates:
            # Special check for "Binh" - only update if in Agrima (state 4)
            if old_name == "Binh" and burg_state != 4:
                continue  # Skip Binh if not in Agrima
            burg['name'] = burg_name_updates[old_name]
            print(f"  Updated burg: {old_name} -> {burg_name_updates[old_name]}")

# Now read all the component files
print("\nReading component files...")

# Metadata header
with open(script_dir / "01-metadata-header.txt", 'r', encoding='utf-8') as f:
    metadata_header = f.read().strip()

# Map settings
with open(script_dir / "02-map-settings.txt", 'r', encoding='utf-8') as f:
    map_settings = f.read().strip()

# Coordinates
with open(script_dir / "03-coordinates.json", 'r', encoding='utf-8-sig') as f:
    coordinates = json.load(f)

# Biomes
with open(script_dir / "04-biomes.txt", 'r', encoding='utf-8') as f:
    biomes = f.read().strip()

# Regiments (already a JSON array)
with open(script_dir / "05-regiments.json", 'r', encoding='utf-8-sig') as f:
    regiments = json.load(f)

# SVG map
with open(script_dir / "06-map.svg", 'r', encoding='utf-8', errors='replace') as f:
    svg_map = f.read()

# Cells config
with open(script_dir / "08-cells-config.json", 'r', encoding='utf-8-sig') as f:
    cells_config = json.load(f)

# Cells data
with open(script_dir / "09-cells-data.json", 'r', encoding='utf-8-sig') as f:
    cells_data = json.load(f)

# Cultures
with open(script_dir / "10-cultures.json", 'r', encoding='utf-8-sig') as f:
    cultures = json.load(f)

# Religions
with open(script_dir / "13-religions.json", 'r', encoding='utf-8-sig') as f:
    religions = json.load(f)

print("\nReassembling map file...")

# Assemble the map file in Azgaar format
# Format: metadata header, map settings, coordinates, biomes, regiments, SVG, then data arrays

map_content = []
map_content.append(metadata_header)
map_content.append(map_settings)
map_content.append(json.dumps(coordinates, ensure_ascii=False, separators=(',', ':')))
map_content.append(biomes)
map_content.append(json.dumps(regiments, ensure_ascii=False, separators=(',', ':')))
map_content.append(svg_map)
map_content.append(json.dumps(cells_config, ensure_ascii=False, separators=(',', ':')))
map_content.append(json.dumps(cells_data, ensure_ascii=False, separators=(',', ':')))
map_content.append("states=" + json.dumps(states, ensure_ascii=False, separators=(',', ':')))
map_content.append("cultures=" + json.dumps(cultures, ensure_ascii=False, separators=(',', ':')))
map_content.append("burgs=" + json.dumps(burgs, ensure_ascii=False, separators=(',', ':')))
map_content.append(json.dumps(religions, ensure_ascii=False, separators=(',', ':')))

# Write the assembled map file
print(f"\nWriting assembled map to {output_file.name}...")
with open(output_file, 'w', encoding='utf-8', errors='replace') as f:
    f.write('\n'.join(map_content))

print(f"Done! Map file saved as {output_file.name}")
final_content = '\n'.join(map_content)
print(f"File size: {len(final_content)} characters")
