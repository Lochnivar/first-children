#!/usr/bin/env python3
"""
Script to fix the Index column in Agrima's burgs.md - replace "Zvezdan" with "4"
"""

from pathlib import Path

script_dir = Path(__file__).parent.absolute()
agrima_burgs_md = script_dir / "states" / "04-agrima" / "burgs.md"

with open(agrima_burgs_md, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Zvezdan" in the Index column (before "Agrima")
content = content.replace("| Zvezdan | Agrima |", "| 4 | Agrima |")

with open(agrima_burgs_md, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed Index column in Agrima's burgs.md")

