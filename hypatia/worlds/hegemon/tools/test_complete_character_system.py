"""
Test script to demonstrate the complete character creation system
with Nature (DNA) and Nurture (DEPC) data, names, and burg assignments
"""

from .dna_core import DNA
from .create_complete_character import create_complete_character
from .dna_database import CharacterDatabase
import random
import sqlite3

def test_character_creation():
    """Test creating characters with full data"""
    
    print("="*70)
    print("Testing Complete Character Creation System")
    print("="*70)
    print()
    
    # Use a test database
    db = CharacterDatabase("test_characters.db")
    
    # Create a few founder characters from different cultures
    cultures = ['valthir', 'veridian', 'eldermark', 'qasridan', 'khanhthien']
    
    founders = []
    
    print("Creating founder characters...\n")
    for i, culture in enumerate(cultures):
        founder_id, founder_data = create_complete_character(
            culture_name=culture,
            is_noble=random.choice([True, False]),
            birth_year=300 + i * 5,
            db=db,
            notes=f'Founder from {culture} culture'
        )
        founders.append((founder_id, founder_data))
        
        print(f"[OK] {founder_data['name']} ({culture})")
        print(f"    Burg: {founder_data['burg_name']} in {founder_data['state_name']}")
        print(f"    DEPC: D={founder_data['depc_profile'].dominance:.1f}, "
              f"E={founder_data['depc_profile'].extroversion:.1f}, "
              f"P={founder_data['depc_profile'].patience:.1f}, "
              f"C={founder_data['depc_profile'].conformity:.1f}")
        print(f"    Stress: {founder_data['developmental_stress']['severity']}")
        print()
    
    # Create some children
    print("Creating child characters...\n")
    if len(founders) >= 2:
        parent1_id, parent1_data = founders[0]
        parent2_id, parent2_data = founders[1]
        
        # Create child from two founders
        child_id, child_data = create_complete_character(
            parent1_dna=parent1_data['dna'],
            parent2_dna=parent2_data['dna'],
            culture_name=parent1_data['culture'],  # Raised in first parent's culture
            is_noble=True,
            parent1_id=parent1_id,
            parent2_id=parent2_id,
            birth_year=320,
            db=db,
            notes='Child of two founders'
        )
        
        print(f"[OK] {child_data['name']} (Child)")
        print(f"    Parents: {parent1_data['name']} & {parent2_data['name']}")
        print(f"    Culture: {child_data['culture']}")
        print(f"    Burg: {child_data['burg_name']} in {child_data['state_name']}")
        print(f"    DEPC: D={child_data['depc_profile'].dominance:.1f}, "
              f"E={child_data['depc_profile'].extroversion:.1f}, "
              f"P={child_data['depc_profile'].patience:.1f}, "
              f"C={child_data['depc_profile'].conformity:.1f}")
        print(f"    Stress: {child_data['developmental_stress']['severity']}")
        print()
    
    # Show database statistics
    print("="*70)
    print("Database Statistics")
    print("="*70)
    stats = db.get_statistics()
    print(f"Total characters: {stats['total_characters']}")
    print(f"Characters with parents: {stats['characters_with_parents']}")
    print(f"Root characters: {stats['root_characters']}")
    print(f"Max generations: {stats['max_generations']}")
    if stats['birth_year_range']:
        print(f"Birth year range: {stats['birth_year_range'][0]} - {stats['birth_year_range'][1]}")
    print()
    
    # Show characters by culture
    print("Characters by Culture:")
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT culture, COUNT(*) as count
        FROM characters
        WHERE culture IS NOT NULL
        GROUP BY culture
        ORDER BY count DESC
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")
    conn.close()
    print()
    
    # Show characters by burg
    print("Characters by Burg (top 10):")
    conn = sqlite3.connect(db.db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT burg_name, state_name, COUNT(*) as count
        FROM characters
        WHERE burg_name IS NOT NULL
        GROUP BY burg_name, state_name
        ORDER BY count DESC
        LIMIT 10
    """)
    for row in cursor.fetchall():
        print(f"  {row[0]} ({row[1]}): {row[2]}")
    conn.close()
    print()
    
    print("="*70)
    print("Test complete! Database: test_characters.db")
    print("="*70)


if __name__ == "__main__":
    test_character_creation()

