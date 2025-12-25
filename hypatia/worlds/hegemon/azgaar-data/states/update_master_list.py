#!/usr/bin/env python3
"""
Script to update all state name references in STATES_MASTER_LIST.md
"""

from pathlib import Path
import re

# State name mappings: old_name -> new_name
state_name_replacements = {
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

# Full name mappings
full_name_replacements = {
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

script_dir = Path(__file__).parent.absolute()
master_list_path = script_dir / "STATES_MASTER_LIST.md"

with open(master_list_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace full names first (to avoid partial replacements)
for old_full, new_full in full_name_replacements.items():
    content = content.replace(old_full, new_full)

# Replace short names
for old_name, new_name in state_name_replacements.items():
    # Use word boundaries to avoid partial replacements
    pattern = r'\b' + re.escape(old_name) + r'\b'
    content = re.sub(pattern, new_name, content)

with open(master_list_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated STATES_MASTER_LIST.md with new state names")

