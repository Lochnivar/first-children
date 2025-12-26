#!/usr/bin/env python3
"""
Script to edit state borders (conquered territories) in Azgaar map format.

NOTE: State ownership in Azgaar is stored in a "pack" array which is a compressed
representation. This script provides guidance, but the RECOMMENDED approach is:

1. Load hegemon.map into Azgaar Fantasy Map Generator
2. Use Azgaar's built-in tools to edit state borders manually
3. Re-export the map

However, if you need programmatic control, this script can help identify where
border changes would need to be made.

For programmatic editing, you would need to:
1. Decompress the pack array (if it exists in the format)
2. Identify which cells belong to which states
3. Change cell ownership
4. Recalculate state statistics (area, cells count, neighbors)
5. Update burg state assignments if they change territories
6. Recompress and update the map file
"""

import json
import re
from pathlib import Path

def find_pack_array_in_map(map_file):
    """Look for pack array in the map file (if it exists)."""
    with open(map_file, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Look for "pack=" or similar patterns
    pack_pattern = r'pack\s*=\s*\[.*?\]'
    matches = re.findall(pack_pattern, content, re.DOTALL)
    
    if matches:
        print(f"Found {len(matches)} potential pack array(s)")
        return matches
    else:
        print("No pack array found in standard format")
        print("\nNOTE: State ownership may be stored in:")
        print("  1. SVG paths with fill colors matching state colors")
        print("  2. A compressed pack array in a different format")
        print("  3. Computed from burg locations and cell proximity")
        return None

def analyze_state_territories(map_file):
    """Analyze current state territories from burg locations."""
    script_dir = Path(__file__).parent.absolute()
    
    # Load states
    states_file = script_dir / "11-states.json"
    with open(states_file, 'r', encoding='utf-8-sig') as f:
        states = json.load(f)
    
    # Load burgs
    burgs_file = script_dir / "12-burgs.json"
    with open(burgs_file, 'r', encoding='utf-8-sig') as f:
        burgs = json.load(f)
    
    print("\n=== Current State Territories (from state data) ===\n")
    for state in states:
        if state and 'i' in state and 'name' in state:
            print(f"State {state['i']}: {state['name']}")
            print(f"  - Cells: {state.get('cells', 'N/A')}")
            print(f"  - Area: {state.get('area', 'N/A')}")
            print(f"  - Burgs: {state.get('burgs', 'N/A')}")
            print(f"  - Neighbors: {state.get('neighbors', [])}")
            print()
    
    print("\n=== Recommended Approach ===\n")
    print("To edit state borders (conquered territories):")
    print()
    print("OPTION 1 - Manual Editing (RECOMMENDED):")
    print("  1. Load hegemon.map into Azgaar Fantasy Map Generator")
    print("     https://azgaar.github.io/Fantasy-Map-Generator")
    print("  2. Use Tools > States > Edit States to change borders")
    print("  3. Use Tools > States > Transfer Cells to move territory")
    print("  4. Re-export the map")
    print()
    print("OPTION 2 - Programmatic Editing (Complex):")
    print("  Requires understanding Azgaar's pack array compression")
    print("  Would need to:")
    print("    - Decompress cell ownership data")
    print("    - Change cell-to-state mappings")
    print("    - Update state statistics (area, cells, neighbors)")
    print("    - Update burg state assignments")
    print("    - Recompress and reassemble map")
    print()
    print("=== Alternative: Update Burg States ===\n")
    print("If cities change hands, you can update burg state assignments:")
    print("  - This affects which state owns specific cities")
    print("  - May affect territory visualization")
    print("  - Use update_burg_states() function below")

def update_burg_states(burgs_file, state_changes):
    """
    Update burg state assignments.
    
    Args:
        burgs_file: Path to burgs JSON file
        state_changes: Dict mapping burg_index -> new_state_index
            Example: {42: 5, 43: 5}  # Burgs 42 and 43 -> State 5
    """
    with open(burgs_file, 'r', encoding='utf-8-sig') as f:
        burgs = json.load(f)
    
    updated = 0
    for burg in burgs:
        if burg and 'i' in burg:
            burg_id = burg['i']
            if burg_id in state_changes:
                old_state = burg.get('state')
                new_state = state_changes[burg_id]
                burg['state'] = new_state
                print(f"Updated burg {burg_id}: state {old_state} -> {new_state}")
                updated += 1
    
    if updated > 0:
        with open(burgs_file, 'w', encoding='utf-8') as f:
            json.dump(burgs, f, indent=2, ensure_ascii=False)
        print(f"\nUpdated {updated} burg state assignments")
        print("NOTE: You will need to reassemble the map file after this change")
    else:
        print("No burgs updated")

if __name__ == "__main__":
    script_dir = Path(__file__).parent.absolute()
    map_file = script_dir / "hegemon.map"
    
    print("=" * 60)
    print("Azgaar Map State Border Editing Guide")
    print("=" * 60)
    
    if map_file.exists():
        print(f"\nAnalyzing {map_file.name}...")
        find_pack_array_in_map(map_file)
        analyze_state_territories(map_file)
    else:
        print(f"\nMap file not found: {map_file}")
        print("Please ensure hegemon.map exists in the same directory")
    
    print("\n" + "=" * 60)
    print("\nExample usage for updating burg states:")
    print("""
    # If you need to transfer cities to different states:
    from edit_state_borders import update_burg_states
    
    state_changes = {
        42: 5,   # Burg 42 -> State 5 (Niljalia)
        43: 5,   # Burg 43 -> State 5 (Niljalia)
    }
    
    update_burg_states('12-burgs.json', state_changes)
    """)

