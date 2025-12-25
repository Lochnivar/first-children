#!/usr/bin/env python3
"""
Script to update state README files to include burgs references.
"""

import os
import re

states_dir = 'states'

# Find all state directories
state_dirs = [d for d in os.listdir(states_dir) 
              if os.path.isdir(os.path.join(states_dir, d)) and d != '.' and d != '..']

for state_dir_name in sorted(state_dirs):
    state_dir_path = os.path.join(states_dir, state_dir_name)
    readme_path = os.path.join(state_dir_path, 'README.md')
    
    if not os.path.exists(readme_path):
        continue
    
    # Check if burgs files exist
    burgs_json = os.path.join(state_dir_path, 'burgs.json')
    burgs_md = os.path.join(state_dir_path, 'burgs.md')
    
    if not os.path.exists(burgs_json):
        continue
    
    # Read the README
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if burgs is already mentioned
    if 'burgs.md' in content or 'Burgs' in content:
        # Update existing reference if needed
        if '## Additional Data Files' in content and '[Burgs]' not in content:
            # Add burgs to the Additional Data Files section
            content = re.sub(
                r'(- \[Provinces\]\(provinces\.json\) - Province list and structure)',
                r'\1\n- [Burgs](burgs.md) - Cities and settlements (see also [burgs.json](burgs.json))',
                content
            )
    else:
        # Add burgs reference
        if '## Additional Data Files' in content:
            content = re.sub(
                r'(- \[Provinces\]\(provinces\.json\) - Province list and structure)',
                r'\1\n- [Burgs](burgs.md) - Cities and settlements (see also [burgs.json](burgs.json))',
                content
            )
        elif '## Additional Data Files' not in content:
            # Add the section if it doesn't exist (shouldn't happen, but safety check)
            content += "\n## Additional Data Files\n\n- [Burgs](burgs.md) - Cities and settlements (see also [burgs.json](burgs.json))\n"
    
    # Write back
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {state_dir_name}/README.md")

print(f"\nUpdated {len(state_dirs)} state README files")

