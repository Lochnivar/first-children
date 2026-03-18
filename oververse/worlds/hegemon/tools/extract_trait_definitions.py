#!/usr/bin/env python3
"""
Extract TRAIT_DEFINITIONS from HEGEMON-DIALOG.md

This script extracts the TRAIT_DEFINITIONS dictionary from the original file.
"""

import re
from pathlib import Path

script_dir = Path(__file__).parent
hegemon_dir = script_dir.parent
dialog_file = hegemon_dir / 'HEGEMON-DIALOG.md'

print(f"Reading {dialog_file}...")
with open(dialog_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find TRAIT_DEFINITIONS block
# It starts with "TRAIT_DEFINITIONS = {" and ends with "}"

# Find the start
start_pattern = r'TRAIT_DEFINITIONS\s*=\s*\{'
start_match = re.search(start_pattern, content)
if not start_match:
    print("ERROR: Could not find TRAIT_DEFINITIONS in file")
    exit(1)

start_pos = start_match.end() - 1  # Include the {

# Find matching closing brace (need to track nesting)
brace_count = 0
pos = start_pos
in_string = False
string_char = None

while pos < len(content):
    char = content[pos]
    
    # Track string state (simple quote tracking)
    if char in ('"', "'") and (pos == 0 or content[pos-1] != '\\'):
        if not in_string:
            in_string = True
            string_char = char
        elif char == string_char:
            in_string = False
            string_char = None
    
    if not in_string:
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = pos + 1
                break
    
    pos += 1
else:
    print("ERROR: Could not find closing brace for TRAIT_DEFINITIONS")
    exit(1)

# Extract the dictionary
trait_defs_code = content[start_pos:end_pos]
print(f"Extracted {len(trait_defs_code)} characters of trait definitions")

# Write to dna_traits.py
output_file = script_dir / 'dna_traits.py'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('"""\n')
    f.write('Trait Definitions\n\n')
    f.write('This module contains the TRAIT_DEFINITIONS dictionary defining all 32 traits,\n')
    f.write('their possible values, dominance hierarchies, and markers.\n')
    f.write('"""\n\n')
    f.write('# Each trait has 16 possible values (4 bits = 0-15)\n')
    f.write('# We define what each value means and dominance hierarchy\n\n')
    f.write('TRAIT_DEFINITIONS = ')
    f.write(trait_defs_code)
    f.write('\n')

print(f"Written to {output_file}")
print("Success!")

