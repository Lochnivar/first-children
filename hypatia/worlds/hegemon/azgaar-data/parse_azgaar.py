#!/usr/bin/env python3
"""
Script to parse Azgaar Fantasy Map Generator export file
into organized sections for the Hegemon world.
"""

import os
import json

# Read the source file
source_file = '../azgaar-data.md'
with open(source_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Find where SVG starts and ends
svg_start = None
svg_end = None
for i, line in enumerate(lines):
    if line.strip().startswith('<svg'):
        svg_start = i
    elif svg_start is not None and line.strip().startswith('</svg>'):
        svg_end = i
        break

# Extract complete SVG (lines 6-140 based on Azgaar structure)
# SVG typically ends before the data arrays start at line 141
if svg_start is not None:
    if svg_end is not None:
        svg_lines = lines[svg_start:svg_end+1]
    else:
        # SVG ends before data arrays (around line 140)
        svg_lines = lines[svg_start:140]
    
    with open('06-map.svg', 'w', encoding='utf-8') as f:
        f.write(''.join(svg_lines))
    print(f"Extracted complete SVG map (lines {svg_start+1} to {svg_start+len(svg_lines)})")

# Extract data sections (lines 141+)
section_files = {
    140: '08-cells-config.json',      # Line 141: {"spacing"...
    146: '09-cells-data.json',         # Line 147: [{"i":0,...
    147: '10-cultures.json',           # Line 148: [{"name":"Wildlands"...
    148: '11-states.json',             # Line 149: [{"i":0,...
    149: '12-burgs.json',              # Line 150: [{"cell":...
    163: '13-religions.json'           # Line 164: [{"name":"No religion"...
}

# Extract identified data sections
extracted_count = 0
for line_idx, filename in section_files.items():
    if line_idx < len(lines):
        line = lines[line_idx].strip()
        if line:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(line)
            print(f"Extracted {filename} from line {line_idx + 1}")
            extracted_count += 1

print(f"\nExtracted {extracted_count} data sections")
print("Parsing complete!")
print("\nNote: The original azgaar-data.md file should be preserved")
print("as it can be loaded directly into Azgaar Fantasy Map Generator.")
