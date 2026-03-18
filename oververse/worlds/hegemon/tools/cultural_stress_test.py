"""
Cultural Preferences Stress Test

Generates 10 families per culture (12 active cultures = 120 families total)
Uses cultural preferences for mate selection.
Uses existing stress test families as random genetic influences.
"""

import random
import sys
from pathlib import Path
from typing import List, Tuple

try:
    from .dna_database import CharacterDatabase
    from .dna_core import create_child, calculate_genetic_similarity
    from .dna_templates import (
        create_royal_bloodline_founder,
        create_common_person,
        create_foreign_princess
    )
    from .hegemon_cultures import ACTIVE_CULTURES, HEGEMON_CULTURES
except ImportError:
    tools_dir = Path(__file__).parent
    sys.path.insert(0, str(tools_dir.parent))
    from tools.dna_database import CharacterDatabase
    from tools.dna_core import create_child, calculate_genetic_similarity
    from tools.dna_templates import (
        create_royal_bloodline_founder,
        create_common_person,
        create_foreign_princess
    )
    from tools.hegemon_cultures import ACTIVE_CULTURES, HEGEMON_CULTURES


def load_existing_families(db_path: str = "stress_test_characters.db") -> List:
    """
    Load existing stress test families to use as random genetic influences
    
    Args:
        db_path: Path to existing stress test database
        
    Returns:
        List of DNA samples from existing families
    """
    influence_dnas = []
    
    try:
        import os
        if os.path.exists(db_path):
            old_db = CharacterDatabase(db_path)
            # Get some random characters from the old database
            chars = old_db.search_characters(limit=50)
            for char in chars:
                dna = old_db.load_dna(char['id'])
                if dna:
                    influence_dnas.append(dna)
            
            print(f"Loaded {len(influence_dnas)} DNA samples from existing families")
        else:
            print(f"No existing database found at {db_path}, using template DNA only")
    except Exception as e:
        print(f"Error loading existing families: {e}, using template DNA only")
    
    # Add some template DNA as fallback
    if len(influence_dnas) < 10:
        influence_dnas.extend([
            create_royal_bloodline_founder(),
            create_common_person(),
            create_foreign_princess(),
        ])
    
    return influence_dnas


def create_founder_pair(culture, influence_dnas: List):
    """
    Create a founding pair for a culture
    
    The founders should have traits that align with the culture's preferences,
    but with some genetic diversity from random influences.
    
    Args:
        culture: Culture object
        influence_dnas: List of DNA samples to use as influences
        
    Returns:
        Tuple of (founder1_dna, founder2_dna)
    """
    # Base DNA - start with template that might align with culture preferences
    # Then mix with random influences
    
    # Choose base template based on culture preferences
    # For simplicity, use random template and mix with influences
    base_templates = [
        create_royal_bloodline_founder,
        create_common_person,
        create_foreign_princess,
    ]
    
    base_template = random.choice(base_templates)
    base_dna = base_template()
    
    # Mix with random influence DNA to add diversity
    if influence_dnas:
        influence_dna = random.choice(influence_dnas)
        # Create child of base + influence (simulates mixing)
        founder1_dna = create_child(base_dna, influence_dna, mutation_rate=0.02)
    else:
        founder1_dna = base_dna
    
    # Second founder - either similar to first or from different influence
    if random.random() < 0.5:
        # Similar founder (same base template)
        if influence_dnas:
            influence_dna = random.choice(influence_dnas)
            founder2_dna = create_child(base_dna, influence_dna, mutation_rate=0.02)
        else:
            founder2_dna = base_template()
    else:
        # Different founder (different template or strong influence)
        other_template = random.choice([t for t in base_templates if t != base_template])
        other_base = other_template()
        if influence_dnas:
            influence_dna = random.choice(influence_dnas)
            founder2_dna = create_child(other_base, influence_dna, mutation_rate=0.02)
        else:
            founder2_dna = other_base
    
    return (founder1_dna, founder2_dna)


def generate_cultural_family(db: CharacterDatabase, culture_name: str, culture, 
                             family_num: int, start_year: int, generations: int,
                             influence_dnas: List):
    """
    Generate a family tree using cultural preferences for mate selection
    
    Args:
        db: Database instance
        culture_name: Name of the culture
        culture: Culture object with preferences
        family_num: Family number within this culture (1-10)
        start_year: Starting year for the family
        generations: Number of generations to generate
        influence_dnas: List of DNA samples for random influences
        
    Returns:
        Dictionary with family stats
    """
    family_label = f"{culture_name} Family {family_num}"
    
    # Create founders
    founder1_dna, founder2_dna = create_founder_pair(culture, influence_dnas)
    
    founder1_id = db.save_character(
        f"{family_label} Founder 1",
        founder1_dna,
        birth_year=start_year,
        notes=f"Founding member of {family_label} ({culture_name} culture)"
    )
    founder2_id = db.save_character(
        f"{family_label} Founder 2",
        founder2_dna,
        birth_year=start_year,
        notes=f"Founding member of {family_label} ({culture_name} culture)"
    )
    
    # Track current generation (as pairs of IDs)
    current_generation_pairs = [(founder1_id, founder2_id)]
    
    stats = {
        'total_people': 2,
        'generations': 1,
        'total_children': 0,
    }
    
    # Generate generations
    for gen_num in range(2, generations + 1):
        next_generation_ids = []
        gen_year = start_year + (gen_num - 1) * 25
        
        # Generate children from all parent pairs
        for p1_id, p2_id in current_generation_pairs:
            # Each pair has 1-3 children
            num_children = random.randint(1, 3)
            
            parent1_dna = db.load_dna(p1_id)
            parent2_dna = db.load_dna(p2_id)
            
            if not parent1_dna or not parent2_dna:
                continue
            
            # Calculate mutation rate based on similarity
            similarity = calculate_genetic_similarity(parent1_dna, parent2_dna)
            mutation_rate = min(0.10, similarity * 0.15)
            
            # Create children
            for child_num in range(num_children):
                child_dna = create_child(parent1_dna, parent2_dna, mutation_rate=mutation_rate)
                
                child_id = db.save_character(
                    f"{family_label} Gen{gen_num}-{len(next_generation_ids)+1}",
                    child_dna,
                    parent1_id=p1_id,
                    parent2_id=p2_id,
                    birth_year=gen_year + child_num,
                    notes=f"{culture_name} culture, Generation {gen_num}"
                )
                
                next_generation_ids.append(child_id)
                stats['total_people'] += 1
                stats['total_children'] += 1
        
        # Pair up next generation using CULTURAL PREFERENCES
        if len(next_generation_ids) > 1:
            # Score all possible pairings by cultural preferences
            # For each person, find best cultural match
            paired_ids = set()
            next_generation_pairs = []
            
            # Shuffle to randomize selection order
            random.shuffle(next_generation_ids)
            
            for person_id in next_generation_ids:
                if person_id in paired_ids:
                    continue
                
                person_dna = db.load_dna(person_id)
                if not person_dna:
                    continue
                
                # Get available mates (unpaired members of same generation)
                available_mates = []
                available_mate_ids = []
                for mate_id in next_generation_ids:
                    if mate_id != person_id and mate_id not in paired_ids:
                        mate_dna = db.load_dna(mate_id)
                        if mate_dna:
                            available_mates.append(mate_dna)
                            available_mate_ids.append(mate_id)
                
                if available_mates:
                    # Use culture to select mate
                    selected_mate_dna = culture.select_mate(person_dna, available_mates)
                    
                    # Find the ID of the selected mate
                    for i, mate_dna in enumerate(available_mates):
                        if mate_dna == selected_mate_dna:
                            selected_mate_id = available_mate_ids[i]
                            next_generation_pairs.append((person_id, selected_mate_id))
                            paired_ids.add(person_id)
                            paired_ids.add(selected_mate_id)
                            break
                    else:
                        # Fallback - pair with first available
                        if available_mate_ids:
                            selected_mate_id = available_mate_ids[0]
                            next_generation_pairs.append((person_id, selected_mate_id))
                            paired_ids.add(person_id)
                            paired_ids.add(selected_mate_id)
                else:
                    # No available mates - pair with self (will be skipped in next gen)
                    next_generation_pairs.append((person_id, person_id))
                    paired_ids.add(person_id)
            
            current_generation_pairs = next_generation_pairs
        else:
            # Only one person - pair with self
            current_generation_pairs = [(next_generation_ids[0], next_generation_ids[0])] if next_generation_ids else [(founder1_id, founder2_id)]
        
        stats['generations'] = gen_num
    
    return {
        'founder1_id': founder1_id,
        'founder2_id': founder2_id,
        'stats': stats,
    }


def run_cultural_stress_test(families_per_culture: int = 10, generations: int = 10,
                            db_path: str = "cultural_stress_test.db"):
    """
    Run stress test with cultural preferences
    
    Args:
        families_per_culture: Number of families per culture
        generations: Number of generations per family
        db_path: Path to database file
    """
    print("=" * 70)
    print(f"CULTURAL PREFERENCES STRESS TEST")
    print(f"{len(ACTIVE_CULTURES)} cultures × {families_per_culture} families × {generations} generations")
    print("=" * 70)
    
    # Load existing families as influences
    influence_dnas = load_existing_families("stress_test_characters.db")
    
    # Create database
    import os
    if os.path.exists(db_path):
        print(f"\nRemoving existing database: {db_path}")
        os.remove(db_path)
    
    print(f"\nCreating database: {db_path}")
    db = CharacterDatabase(db_path)
    
    all_families = []
    start_year = 0
    
    # Generate families for each culture
    for culture_key, culture in ACTIVE_CULTURES.items():
        print(f"\n{'-'*70}")
        print(f"Generating {culture.name} families ({families_per_culture} families)")
        print(f"{'-'*70}")
        
        culture_families = []
        
        for family_num in range(1, families_per_culture + 1):
            try:
                family_data = generate_cultural_family(
                    db, culture_key, culture, family_num, 
                    start_year, generations, influence_dnas
                )
                culture_families.append(family_data)
                start_year += 5  # Small stagger between families
                
                if family_num % 5 == 0:
                    print(f"  Completed {family_num}/{families_per_culture} families...")
            except Exception as e:
                print(f"  ERROR generating {culture.name} Family {family_num}: {e}")
                import traceback
                traceback.print_exc()
        
        all_families.append({
            'culture': culture_key,
            'culture_name': culture.name,
            'families': culture_families
        })
        
        print(f"\n{culture.name}: {len(culture_families)} families generated")
    
    # Print statistics
    print("\n" + "=" * 70)
    print("CULTURAL STRESS TEST RESULTS")
    print("=" * 70)
    
    total_people = 0
    for culture_group in all_families:
        culture_stats = {
            'families': len(culture_group['families']),
            'total_people': 0,
            'avg_per_family': 0
        }
        
        for family in culture_group['families']:
            culture_stats['total_people'] += family['stats']['total_people']
        
        culture_stats['avg_per_family'] = culture_stats['total_people'] / culture_stats['families'] if culture_stats['families'] > 0 else 0
        total_people += culture_stats['total_people']
        
        print(f"\n{culture_group['culture_name']}:")
        print(f"  Families: {culture_stats['families']}")
        print(f"  Total people: {culture_stats['total_people']}")
        print(f"  Avg per family: {culture_stats['avg_per_family']:.1f}")
    
    # Database statistics
    db_stats = db.get_statistics()
    print(f"\n{'='*70}")
    print("DATABASE STATISTICS")
    print(f"{'='*70}")
    print(f"Total characters: {db_stats['total_characters']}")
    print(f"Characters with parents: {db_stats['characters_with_parents']}")
    print(f"Root characters: {db_stats['root_characters']}")
    print(f"Max generations: {db_stats['max_generations']}")
    if db_stats['birth_year_range']:
        print(f"Birth year range: {db_stats['birth_year_range'][0]} - {db_stats['birth_year_range'][1]}")
    
    print(f"\n{'='*70}")
    print("STRESS TEST COMPLETE")
    print(f"{'='*70}")
    print(f"Database file: {db_path}")
    print(f"Total people generated: {total_people}")
    print(f"Database size: {os.path.getsize(db_path) / 1024:.1f} KB")
    
    return db, all_families


if __name__ == "__main__":
    db, families = run_cultural_stress_test(families_per_culture=10, generations=10)
