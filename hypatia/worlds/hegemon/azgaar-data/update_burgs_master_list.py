#!/usr/bin/env python3
"""
Script to update burg names in BURGS_MASTER_LIST.md
"""

import re
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent.absolute()
burgs_list_path = script_dir / "BURGS_MASTER_LIST.md"

# Burg renames to apply
burg_renames = {
    "Postignino": "Taghrast",
    "Duy Hoa Thuy": "Duyhaven",
    "Monte": None,  # Special case - replaced with Mzurit and Mazraq
    "Capra": "Qabrash",
    "Lanovilliter": "Tazaghrut",
    "Binh": "Binhar",
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

with open(burgs_list_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace burg names
for old_name, new_name in burg_renames.items():
    if new_name is None:
        # Special case for Monte - replace with Mzurit for first instance, Mazraq for second
        # But we'll handle it differently - replace both instances appropriately
        content = re.sub(r'\bMonte\b', 'Mzurit', content, count=1)
        content = re.sub(r'\bMonte\b', 'Mazraq', content, count=1)
    else:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(old_name) + r'\b'
        content = re.sub(pattern, new_name, content)

with open(burgs_list_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated BURGS_MASTER_LIST.md with new burg names")
