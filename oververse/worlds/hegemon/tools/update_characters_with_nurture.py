"""
Script to update existing characters with Nurture (DEPC) data, names, and burg assignments

This script:
1. Loads all characters from the database
2. Generates DEPC profiles based on their DNA and culture
3. Assigns culturally appropriate names
4. Assigns them to burgs based on culture
"""

import sqlite3
import random
from pathlib import Path
from typing import List, Dict, Optional

try:
    from .dna_database import CharacterDatabase
    from .dna_core import DNA
    from .depc_system import develop_character_depc
    from .name_generator import generate_full_name, CULTURE_TO_TEMPLATE
except ImportError:
    import sys
    tools_dir = Path(__file__).parent
    sys.path.insert(0, str(tools_dir.parent))
    from tools.dna_database import CharacterDatabase
    from tools.dna_core import DNA
    from tools.depc_system import develop_character_depc
    from tools.name_generator import generate_full_name, CULTURE_TO_TEMPLATE


# Culture index to culture key mapping
CULTURE_INDEX_MAP = {
    0: 'wildlands',
    1: 'qasridan',
    2: 'meridian',
    3: 'valthir',
    4: 'zvezdan',
    5: 'aurelian',
    6: 'sturmgaard',
    7: 'veridian',
    8: 'solemnium',
    9: 'eldermark',
    10: 'yaroslav',
    11: 'khanhthien',
    12: 'sundrakar',
}


def load_burgs_by_culture() -> Dict[str, List[Dict]]:
    """
    Load all burgs from state JSON files, organized by culture
    
    Returns:
        Dict mapping culture_key -> list of burg dicts
    """
    tools_dir = Path(__file__).parent
    states_dir = tools_dir.parent / 'azgaar-data' / 'states'
    
    if not states_dir.exists():
        print(f"Warning: States directory not found: {states_dir}")
        return {}
    
    burgs_by_culture = {}
    
    for state_dir in sorted(states_dir.iterdir()):
        if not state_dir.is_dir() or state_dir.name.startswith('.'):
            continue
        
        burgs_json_path = state_dir / 'burgs.json'
        if not burgs_json_path.exists():
            continue
        
        state_name = state_dir.name.split('-', 1)[-1] if '-' in state_dir.name else state_dir.name
        
        try:
            import json
            with open(burgs_json_path, 'r', encoding='utf-8') as f:
                burgs = json.load(f)
            
            for burg in burgs:
                culture_index = burg.get('culture', 0)
                culture_key = CULTURE_INDEX_MAP.get(culture_index, 'valthir')
                
                if culture_key not in burgs_by_culture:
                    burgs_by_culture[culture_key] = []
                
                burg_data = {
                    'id': burg.get('i', burg.get('id')),
                    'name': burg.get('name', 'Unknown'),
                    'state': state_name,
                    'population': burg.get('population', 0),
                    'type': burg.get('type', 'Generic'),
                }
                burgs_by_culture[culture_key].append(burg_data)
        except Exception as e:
            print(f"Error loading burgs from {state_dir.name}: {e}")
            continue
    
    return burgs_by_culture


def assign_character_to_burg(culture_key: str, burgs_by_culture: Dict[str, List[Dict]]) -> Optional[Dict]:
    """
    Assign a character to a random burg of their culture
    
    Args:
        culture_key: Character's culture
        burgs_by_culture: Dict of burgs organized by culture
        
    Returns:
        Burg dict or None if no burgs available
    """
    if culture_key not in burgs_by_culture or not burgs_by_culture[culture_key]:
        # Fallback to valthir if culture not found
        if 'valthir' in burgs_by_culture and burgs_by_culture['valthir']:
            culture_key = 'valthir'
        else:
            return None
    
    burgs = burgs_by_culture[culture_key]
    # Weight by population (larger burgs more likely)
    weights = [burg.get('population', 1) for burg in burgs]
    return random.choices(burgs, weights=weights)[0]


def update_character_with_nurture(db: CharacterDatabase, char_id: int, char_data: Dict,
                                  burgs_by_culture: Dict[str, List[Dict]]) -> bool:
    """
    Update a single character with DEPC data, names, and burg assignment
    
    Args:
        db: CharacterDatabase instance
        char_id: Character ID
        char_data: Character data dict
        burgs_by_culture: Dict of burgs organized by culture
        
    Returns:
        True if updated successfully
    """
    try:
        # Load DNA
        dna = DNA.from_hex(char_data['dna_hex'])
        
        # Determine culture (from existing data or default)
        culture_key = char_data.get('culture', 'valthir')
        if not culture_key or culture_key not in CULTURE_TO_TEMPLATE:
            # Try to infer from burg if available
            if char_data.get('burg_name'):
                # This is a fallback - ideally culture should be set
                culture_key = 'valthir'
            else:
                culture_key = 'valthir'
        
        # Determine if noble (default: False, but can be inferred from notes or name)
        is_noble = bool(char_data.get('is_noble', 0))
        if not is_noble and char_data.get('notes'):
            # Check notes for nobility indicators
            notes_lower = char_data['notes'].lower()
            if any(word in notes_lower for word in ['king', 'queen', 'duke', 'duchess', 'lord', 'lady', 'noble', 'royal']):
                is_noble = True
        
        # Generate DEPC profile
        depc_data = develop_character_depc(dna, culture_key, is_noble)
        depc_profile = depc_data['depc_profile']
        developmental_stress = depc_data['developmental_stress']
        
        # Generate names if not already set
        first_name = char_data.get('first_name')
        family_name = char_data.get('family_name')
        full_name = char_data.get('name', '')
        
        if not first_name or not family_name:
            # Determine gender from name or random
            gender = None
            if full_name:
                # Try to infer gender from existing name (very basic)
                # This is a heuristic - could be improved
                pass
            
            if not gender:
                gender = random.choice(['male', 'female'])
            
            # Get burg for name generation context
            burg = char_data.get('burg_name')
            new_first, new_family, new_full = generate_full_name(culture_key, gender, burg)
            
            if not first_name:
                first_name = new_first
            if not family_name:
                family_name = new_family
            if not full_name or full_name == 'Character':
                full_name = new_full
        
        # Assign to burg if not already assigned
        burg_id = char_data.get('burg_id')
        burg_name = char_data.get('burg_name')
        state_name = char_data.get('state_name')
        
        if not burg_id or not burg_name:
            burg = assign_character_to_burg(culture_key, burgs_by_culture)
            if burg:
                burg_id = burg.get('id')
                burg_name = burg.get('name')
                state_name = burg.get('state')
        
        # Update character in database
        with sqlite3.connect(db.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE characters SET
                    name = ?,
                    first_name = ?,
                    family_name = ?,
                    culture = ?,
                    is_noble = ?,
                    burg_id = ?,
                    burg_name = ?,
                    state_name = ?,
                    depc_dominance = ?,
                    depc_extroversion = ?,
                    depc_patience = ?,
                    depc_conformity = ?,
                    depc_charisma = ?,
                    developmental_stress = ?,
                    stress_severity = ?
                WHERE id = ?
            """, (
                full_name, first_name, family_name, culture_key, 1 if is_noble else 0,
                burg_id, burg_name, state_name,
                depc_profile.dominance, depc_profile.extroversion,
                depc_profile.patience, depc_profile.conformity, depc_profile.charisma,
                developmental_stress['total_stress'], developmental_stress['severity'],
                char_id
            ))
            conn.commit()
        
        return True
        
    except Exception as e:
        print(f"Error updating character {char_id}: {e}")
        import traceback
        traceback.print_exc()
        return False


def update_all_characters(db_path: str = "characters.db"):
    """
    Update all characters in the database with DEPC data, names, and burg assignments
    
    Args:
        db_path: Path to database file
    """
    db = CharacterDatabase(db_path)
    
    print("Loading burgs by culture...")
    burgs_by_culture = load_burgs_by_culture()
    
    print(f"Loaded burgs for {len(burgs_by_culture)} cultures")
    for culture, burgs in burgs_by_culture.items():
        print(f"  {culture}: {len(burgs)} burgs")
    
    print("\nLoading characters from database...")
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM characters")
        characters = [dict(row) for row in cursor.fetchall()]
    
    print(f"Found {len(characters)} characters to update\n")
    
    if not characters:
        print("No characters found in database. Create some characters first.")
        return
    
    updated = 0
    failed = 0
    
    for i, char_data in enumerate(characters, 1):
        char_id = char_data['id']
        char_name = char_data.get('name', f'Character {char_id}')
        
        print(f"[{i}/{len(characters)}] Updating {char_name} (ID: {char_id})...", end=' ')
        
        if update_character_with_nurture(db, char_id, char_data, burgs_by_culture):
            print("✓")
            updated += 1
        else:
            print("✗")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Update complete: {updated} succeeded, {failed} failed")
    print(f"{'='*60}")


if __name__ == "__main__":
    import sys
    
    db_path = sys.argv[1] if len(sys.argv) > 1 else "characters.db"
    
    print("="*60)
    print("Character Nurture Data Update Script")
    print("="*60)
    print(f"Database: {db_path}\n")
    
    update_all_characters(db_path)

