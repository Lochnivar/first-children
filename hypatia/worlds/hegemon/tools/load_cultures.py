"""
Load Hegemon cultures from HEGEMON-DIALOG.md

This module extracts and loads culture definitions from the dialog file.
"""

import re
from pathlib import Path
from .dna_culture import Culture


def load_hegemon_cultures(dialog_file: str = None) -> Dict[str, Culture]:
    """
    Load culture definitions from HEGEMON-DIALOG.md
    
    Args:
        dialog_file: Path to HEGEMON-DIALOG.md (default: looks in parent directory)
        
    Returns:
        Dictionary mapping culture name -> Culture instance
    """
    if dialog_file is None:
        # Default path
        tools_dir = Path(__file__).parent
        dialog_file = tools_dir.parent / 'HEGEMON-DIALOG.md'
    
    with open(dialog_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cultures = {}
    
    # Find all culture definitions
    # Pattern: CULTURE_NAME = Culture(name="...", preferences={...})
    
    # Extract culture blocks
    culture_pattern = r'([A-Z_]+)\s*=\s*Culture\(\s*name="([^"]+)"[^}]*preferences=\{[^}]*\}\s*\)'
    
    # More flexible pattern - find Culture(...) blocks
    culture_blocks = re.finditer(
        r'([A-Z_]+)\s*=\s*Culture\(\s*name="([^"]+)"(.*?)\)\s*(?:STURMGAARD|ELDERMARK|VERIDIAN|SOLEMNIUM|AURELIAN|MERIDIAN|QASRIDAN|ZVEZDAN|YAROSLAV|SUNDRAKAR|KHANHTHIEN|WILDLANDS|\Z)',
        content,
        re.DOTALL
    )
    
    # Try a different approach - parse the actual Python-like syntax
    # Since the file contains valid-looking Python code, we'll execute it safely
    
    # Extract just the culture definitions section
    start_marker = '# Culture 1: VALTHIR'
    end_marker = '# ============================================================================'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        raise ValueError("Could not find culture definitions in file")
    
    # Find the end of culture definitions (before CULTURE REGISTRY)
    end_idx = content.find('CULTURE REGISTRY FOR HEGEMON WORLD', start_idx)
    if end_idx == -1:
        end_idx = len(content)
    
    culture_section = content[start_idx:end_idx]
    
    # Since we can't safely eval() arbitrary code, we'll parse it manually
    # or better - import the file as a module if it's valid Python
    
    # For now, let's create cultures manually based on what we can extract
    # Actually, let's try to import it directly since it looks like valid Python
    
    return _parse_culture_definitions(culture_section)


def _parse_culture_definitions(content: str) -> Dict[str, Culture]:
    """
    Parse culture definitions from the content string
    """
    cultures = {}
    
    # We'll use regex to extract the key information
    # For each culture, we need:
    # - Name
    # - Preferences dict
    # - mate_selection_pressure
    
    # Pattern to find culture name and pressure
    name_pattern = r'name="([^"]+)"'
    pressure_pattern = r'mate_selection_pressure\s*=\s*([0-9.]+)'
    
    # Split by culture definitions
    culture_sections = re.split(r'# Culture \d+:', content)
    
    for section in culture_sections[1:]:  # Skip first empty split
        # Extract name
        name_match = re.search(name_pattern, section)
        if not name_match:
            continue
        
        culture_name = name_match.group(1)
        
        # Extract pressure
        pressure_match = re.search(pressure_pattern, section)
        pressure = float(pressure_match.group(1)) if pressure_match else 0.7
        
        # For preferences, we'll need to extract the lambda functions
        # This is complex, so let's use a safer approach: execute in a sandbox
        # Actually, let's just create a helper that loads from the actual file structure
        
        # For now, return empty - we'll load from the actual file structure
        cultures[culture_name.lower()] = None  # Placeholder
    
    return cultures


# Better approach: import the actual definitions
def load_cultures_from_module():
    """
    Load cultures by importing them from a generated Python module
    """
    # We'll create a proper Python module from the definitions
    pass


