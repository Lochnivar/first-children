#!/usr/bin/env python3
"""
Script to update culture README files with narrative details from HEGEMON-DIALOG.md
"""

import os
import re
from pathlib import Path

# Get the script's directory and work from there
script_dir = Path(__file__).parent.absolute()
azgaar_data_dir = script_dir.parent
hegemon_dir = azgaar_data_dir.parent
dialog_file = hegemon_dir / 'HEGEMON-DIALOG.md'

# Read the dialog file
with open(dialog_file, 'r', encoding='utf-8') as f:
    dialog_content = f.read()

# Map culture names to their dialog sections
culture_sections = {
    'Valthir': ('### Valthir (Culture Index 3)', '### Sturmgaard (Culture Index 6)'),
    'Sturmgaard': ('### Sturmgaard (Culture Index 6)', '### Eldermark (Culture Index 9)'),
    'Eldermark': ('### Eldermark (Culture Index 9)', '## LATIN TEMPLATE CULTURES'),
    'Veridian': ('### Veridian (Culture Index 7)', '### Solemnium (Culture Index 8)'),
    'Solemnium': ('### Solemnium (Culture Index 8)', '### Aurelian (Culture Index 5)'),
    'Aurelian': ('### Aurelian (Culture Index 5)', '### Meridian (Culture Index 2)'),
    'Meridian': ('### Meridian (Culture Index 2)', '## BERBER TEMPLATE CULTURE'),
    'Qasridan': ('### Qasridan (Culture Index 1)', '## SLAVIC TEMPLATE CULTURES'),
    'Zvezdan': ('### Zvezdan (Culture Index 4)', '### Yaroslav (Culture Index 10)'),
    'Yaroslav': ('### Yaroslav (Culture Index 10)', '## FUSION CULTURE'),
    'Sundrakar': ('### Sundrakar (Culture Index 12)', '## SPECIAL CULTURES'),
    'Khanhthien': ('### Khanhthien (Culture Index 11)', '### Wildlands (Culture Index 0)'),
    'Wildlands': ('### Wildlands (Culture Index 0)', '---'),
}

def extract_section(content, start_marker, end_marker):
    """Extract a section from the content between two markers."""
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return None
    
    # Find the end of the section
    if end_marker:
        end_idx = content.find(end_marker, start_idx + len(start_marker))
        if end_idx == -1:
            section = content[start_idx:]
        else:
            section = content[start_idx:end_idx]
    else:
        section = content[start_idx:]
    
    # Clean up the section - remove the header line
    lines = section.split('\n')
    content_lines = []
    skip_header = True
    for line in lines:
        if skip_header:
            if line.strip() and not line.startswith('#'):
                skip_header = False
            else:
                continue
        content_lines.append(line)
    
    return '\n'.join(content_lines).strip()

def update_culture_readme(culture_dir, culture_name, section_content):
    """Update a culture's README file with narrative content."""
    readme_path = culture_dir / 'README.md'
    
    if not readme_path.exists():
        print(f"Warning: README not found for {culture_name} at {readme_path}")
        return False
    
    # Read current README
    with open(readme_path, 'r', encoding='utf-8') as f:
        current_content = f.read()
    
    # Get the narrative content
    narrative_content = section_content.strip()
    
    # Find where to insert the narrative content
    # Look for "## Additional Data Files" or end of file
    if '## Additional Data Files' in current_content:
        # Insert before "Additional Data Files"
        parts = current_content.split('## Additional Data Files')
        new_content = parts[0].rstrip() + '\n\n## Narrative Description\n\n' + narrative_content + '\n\n## Additional Data Files' + parts[1]
    elif '---' in current_content:
        # Insert before the footer
        parts = current_content.split('---')
        # Find the last occurrence (footer)
        footer_part = '---' + parts[-1] if len(parts) > 1 else ''
        main_part = '---'.join(parts[:-1]) if len(parts) > 1 else parts[0]
        new_content = main_part.rstrip() + '\n\n## Narrative Description\n\n' + narrative_content + '\n\n' + footer_part
    else:
        new_content = current_content.rstrip() + '\n\n## Narrative Description\n\n' + narrative_content
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

# Update each culture
updated_count = 0
for culture_name, (start_marker, end_marker) in culture_sections.items():
    section_content = extract_section(dialog_content, start_marker, end_marker)
    
    if not section_content:
        print(f"Warning: Could not find section for {culture_name}")
        continue
    
    # Determine the path based on culture name
    culture_dir = None
    
    if culture_name in ['Valthir', 'Sturmgaard', 'Eldermark']:
        culture_dir = script_dir / 'germanic' / 'subcultures' / culture_name.lower()
    elif culture_name in ['Veridian', 'Solemnium', 'Aurelian', 'Meridian']:
        culture_dir = script_dir / 'latin' / 'subcultures' / culture_name.lower()
    elif culture_name == 'Qasridan':
        culture_dir = script_dir / 'berber' / 'subcultures' / culture_name.lower()
    elif culture_name in ['Zvezdan', 'Yaroslav']:
        culture_dir = script_dir / 'slavic' / 'subcultures' / culture_name.lower()
    elif culture_name == 'Sundrakar':
        culture_dir = script_dir / 'fusions' / culture_name.lower()
    elif culture_name in ['Khanhthien', 'Wildlands']:
        culture_dir = script_dir / 'special' / culture_name.lower()
    
    if culture_dir and culture_dir.exists():
        if update_culture_readme(culture_dir, culture_name, section_content):
            print(f"Updated {culture_name}")
            updated_count += 1
        else:
            print(f"Failed to update {culture_name}")
    else:
        print(f"Warning: Directory not found for {culture_name}: {culture_dir}")

print(f"\nCulture detail updates complete! Updated {updated_count} cultures.")
