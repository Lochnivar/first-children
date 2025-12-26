#!/usr/bin/env python3
"""
Copy the original azgaar-data.md file and update state and burg names directly
This is safer than reassembling from components
"""

import re
from pathlib import Path

script_dir = Path(__file__).parent
original_file = script_dir.parent / 'azgaar-data.md'
output_file = script_dir / 'hegemon.map'

# State name mappings
state_renames = {
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
state_full_renames = {
    "Tridia": "Grand Duchy of Trevalia",
    "Torklia": "Republic of Tormaline",
    "Kutiotania": "Kutiograd Theocracy",
    "Cailinhia": "Protectorate of Kailhen",
    "Ngatria": "Duchy of Ngathar",
    "Shibaha": "Emirate of Shibara",
    "Brinachia": "Principality of Brinach",
    "Sigdakland": "Protectorate of Sigdak",
    "Sealia": "Principality of Sealaris",
    "Ponden": "Dominion of Pondara",
}

# Burg renames
burg_renames = {
    "Postignino": "Taghrast",
    "Duy Hoa Thuy": "Duyhaven",
    "Monte": "Mzurit",  # First instance in Agrima - we'll handle both
    "Capra": "Qabrash",
    "Lanovilliter": "Tazaghrut",
    "Binh": "Binhar",
    "Thai": "Thaidar",  # Not found in Agrima, but keeping for reference
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

print("Reading original file...")
with open(original_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} characters")

# Update state names in JSON arrays
print("\nUpdating state names...")
for old_name, new_name in state_renames.items():
    # Count occurrences before
    pattern = rf'"name"\s*:\s*"{re.escape(old_name)}"'
    count_before = len(re.findall(pattern, content))
    
    # Update in states array (JSON) - name field
    replacement = f'"name":"{new_name}"'
    content = re.sub(pattern, replacement, content)
    
    # Update fullName field if it contains the old name
    if old_name in state_full_renames:
        new_full_name = state_full_renames[old_name]
        # Pattern for fullName that contains the old name
        pattern_full = rf'"fullName"\s*:\s*"([^"]*){re.escape(old_name)}([^"]*)"'
        def replace_fullname(match):
            prefix = match.group(1)
            suffix = match.group(2)
            # Replace old_name with new_name in the fullName
            return f'"fullName":"{prefix}{new_name}{suffix}"'
        content = re.sub(pattern_full, replace_fullname, content)
    
    count_after = len(re.findall(pattern, content))
    if count_before > 0:
        print(f"  Updated {old_name} -> {new_name} ({count_before - count_after} name field(s))")

# Update burg names in JSON arrays
print("\nUpdating burg names...")
monte_count = 0
for old_name, new_name in burg_renames.items():
    if old_name == "Monte":
        # Special handling for "Monte" - there are two instances in Agrima
        # First: Monte -> Mzurit (already handled if Mzurit exists)
        # Second: Monte -> Mazraq
        # We need to check if this is in the Agrima state (state 4)
        # For now, just replace the first occurrence with Mzurit, second with Mazraq
        pattern = rf'"name"\s*:\s*"{re.escape(old_name)}"'
        matches = list(re.finditer(pattern, content))
        if len(matches) >= 2:
            # Replace first with Mzurit, second with Mazraq
            pos = matches[0].end()
            content = content[:matches[0].start()] + f'"name":"Mzurit"' + content[matches[0].end():]
            # Find next occurrence after the first replacement
            remaining = content[pos:]
            next_match = re.search(pattern, remaining)
            if next_match:
                actual_pos = pos + next_match.start()
                content = content[:actual_pos] + f'"name":"Mazraq"' + content[actual_pos + next_match.end():]
                print(f"  Updated Monte -> Mzurit (first) and Monte -> Mazraq (second)")
        else:
            # Just replace with Mzurit if only one
            content = re.sub(pattern, f'"name":"{new_name}"', content, count=1)
            print(f"  Updated Monte -> {new_name} (single occurrence)")
    else:
        pattern = rf'"name"\s*:\s*"{re.escape(old_name)}"'
        count_before = len(re.findall(pattern, content))
        content = re.sub(pattern, f'"name":"{new_name}"', content)
        count_after = len(re.findall(pattern, content))
        if count_before > 0:
            print(f"  Updated {old_name} -> {new_name} ({count_before - count_after} occurrences)")

print(f"\nWriting updated file...")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! Updated file saved as {output_file.name}")
print(f"File size: {len(content)} characters")

