#!/usr/bin/env python3
"""
Clean up old numbered culture directories after reorganization.
"""

import os
import shutil
import re

cultures_dir = 'cultures'

# List of old numbered directories to remove (they've been moved to new structure)
old_dirs = []
for item in os.listdir(cultures_dir):
    item_path = os.path.join(cultures_dir, item)
    if os.path.isdir(item_path) and re.match(r'^\d{2}-', item):
        old_dirs.append(item_path)

# Remove old directories
for old_dir in old_dirs:
    print(f"Removing old directory: {old_dir}")
    shutil.rmtree(old_dir)

print(f"\nRemoved {len(old_dirs)} old culture directories")
print("New hierarchical structure is now clean!")

