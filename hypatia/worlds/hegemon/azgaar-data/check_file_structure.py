#!/usr/bin/env python3
"""Check the structure of Azgaar map files"""

import json

# Check original file
print("=== ORIGINAL azgaar-data.md ===")
with open('../azgaar-data.md', 'r', encoding='utf-8') as f:
    original_lines = f.readlines()

print(f"Total lines: {len(original_lines)}")
print(f"\nLine structure:")
for i in range(min(173, len(original_lines))):
    line = original_lines[i].strip()
    if len(line) > 100:
        preview = line[:100] + "..."
    else:
        preview = line
    print(f"Line {i+1}: {preview[:150]}")

# Check which lines are JSON arrays
print(f"\n\n=== Checking for JSON arrays ===")
for i in range(len(original_lines)):
    line = original_lines[i].strip()
    if line.startswith('[') and len(line) > 10:
        try:
            data = json.loads(line)
            if isinstance(data, list) and len(data) > 0:
                if isinstance(data[0], dict):
                    if 'i' in data[0] and 'name' in data[0]:
                        print(f"Line {i+1}: States array ({len(data)} states)")
                    elif 'cell' in data[0]:
                        print(f"Line {i+1}: Burgs array ({len(data)} burgs)")
                    elif 'base' in data[0] or 'type' in data[0]:
                        print(f"Line {i+1}: Cultures array ({len(data)} cultures)")
                    elif 'form' in data[0] or 'deity' in data[0]:
                        print(f"Line {i+1}: Religions array ({len(data)} religions)")
                    elif 'type' in data[0] and ('island' in str(data[0]) or 'ocean' in str(data[0])):
                        print(f"Line {i+1}: Cells-data array ({len(data)} items)")
                    else:
                        print(f"Line {i+1}: JSON array ({len(data)} items) - {list(data[0].keys())[:5]}")
        except:
            pass

print(f"\n\n=== CHECKING hegemon.map ===")
with open('hegemon.map', 'r', encoding='utf-8') as f:
    map_lines = f.readlines()

print(f"Total lines: {len(map_lines)}")
print(f"\nLast 5 lines:")
for i in range(min(5, len(map_lines))):
    idx = len(map_lines) - 5 + i
    line = map_lines[idx].strip()
    if len(line) > 100:
        preview = line[:100] + "..."
    else:
        preview = line
    print(f"Line {idx+1}: {preview}")

# Validate last line JSON
print(f"\n\n=== Validating last line JSON ===")
last_line = map_lines[-1].strip()
try:
    data = json.loads(last_line)
    print(f"Last line is valid JSON: {type(data).__name__} with {len(data) if isinstance(data, list) else 'N/A'} items")
except Exception as e:
    print(f"Last line JSON error: {e}")
    print(f"Last 200 chars: {repr(last_line[-200:])}")

