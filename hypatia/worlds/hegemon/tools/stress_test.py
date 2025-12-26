"""
Stress Test: Generate 5 families with 10 generations each

This script tests the DNA simulation system with a large dataset:
- 5 founding families
- 10 generations per family
- Database persistence
- Family tree generation

Run from the tools directory:
    python stress_test.py

Or import as module:
    from tools.stress_test import run_stress_test
"""

import random
import sys
from pathlib import Path

# Handle both direct execution and module import
try:
    from .dna_database import CharacterDatabase
    from .dna_core import create_child, calculate_genetic_similarity
    from .dna_templates import (
        create_royal_bloodline_founder,
        create_common_person,
        create_foreign_princess
    )
    from .dna_tree import FamilyTree
except ImportError:
    # Direct execution - add parent directory to path
    tools_dir = Path(__file__).parent
    sys.path.insert(0, str(tools_dir.parent))
    from tools.dna_database import CharacterDatabase
    from tools.dna_core import create_child, calculate_genetic_similarity
    from tools.dna_templates import (
        create_royal_bloodline_founder,
        create_common_person,
        create_foreign_princess
    )
    from tools.dna_tree import FamilyTree


def generate_family(db: CharacterDatabase, family_name: str, founder_template, 
                   start_year: int = 0, generations: int = 10):
    """
    Generate a family tree with specified generations
    
    Args:
        db: Database instance
        family_name: Name of the family (e.g., "House Stark")
        founder_template: Function to create founder DNA
        start_year: Starting year for the family
        generations: Number of generations to generate
        
    Returns:
        Dictionary with family stats
    """
    print(f"\n{'='*70}")
    print(f"Generating {family_name} - {generations} generations")
    print(f"{'='*70}")
    
    # Create founders (couple)
    founder1_dna = founder_template()
    founder2_dna = founder_template() if random.random() < 0.5 else create_common_person()
    
    founder1_id = db.save_character(
        f"{family_name} Founder 1", 
        founder1_dna, 
        birth_year=start_year,
        notes="Founding member of the family"
    )
    founder2_id = db.save_character(
        f"{family_name} Founder 2", 
        founder2_dna, 
        birth_year=start_year,
        notes="Founding member of the family"
    )
    
    print(f"Founders created: IDs {founder1_id}, {founder2_id}")
    
    # Track current generation (as pairs of IDs)
    current_generation_pairs = [(founder1_id, founder2_id)]
    all_ids = [founder1_id, founder2_id]
    
    stats = {
        'total_people': 2,
        'generations': 1,
        'max_children': 0,
        'min_children': 1000,
        'total_children': 0,
        'generation_sizes': [2],
        'avg_children_per_pair': []
    }
    
    # Generate generations
    for gen_num in range(2, generations + 1):
        next_generation_ids = []
        gen_year = start_year + (gen_num - 1) * 25  # 25 years per generation
        
        print(f"\nGeneration {gen_num} (Year {gen_year})...")
        
        # Generate children from all parent pairs
        gen_children = 0
        gen_pairs = 0
        
        for p1_id, p2_id in current_generation_pairs:
            # Each pair has 1-3 children (ensure at least 1 for survival)
            # Only allow 0 children if we have multiple pairs (not all pairs need children)
            if len(current_generation_pairs) > 1:
                num_children = random.randint(0, 3) if random.random() < 0.85 else 1
            else:
                # Last pair must have children to continue
                num_children = random.randint(1, 3)
            
            if num_children == 0:
                continue
            
            gen_pairs += 1
            
            # Load parent DNA
            parent1_dna = db.load_dna(p1_id)
            parent2_dna = db.load_dna(p2_id)
            
            if not parent1_dna or not parent2_dna:
                continue
            
            # Calculate similarity for mutation rate
            similarity = calculate_genetic_similarity(parent1_dna, parent2_dna)
            mutation_rate = min(0.10, similarity * 0.15)
            
            # Create children
            for child_num in range(num_children):
                child_dna = create_child(parent1_dna, parent2_dna, mutation_rate=mutation_rate)
                
                child_id = db.save_character(
                    f"{family_name} Gen{gen_num}-{len(next_generation_ids)+1}",
                    child_dna,
                    parent1_id=p1_id,
                    parent2_id=p2_id,
                    birth_year=gen_year + child_num,  # Slight stagger
                    notes=f"Generation {gen_num}, Child {child_num+1}"
                )
                
                next_generation_ids.append(child_id)
                all_ids.append(child_id)
                gen_children += 1
        
        # Pair up next generation for the following generation
        # Shuffle to randomize pairings
        random.shuffle(next_generation_ids)
        next_generation_pairs = []
        
        # Pair them up
        for i in range(0, len(next_generation_ids) - 1, 2):
            next_generation_pairs.append((next_generation_ids[i], next_generation_ids[i+1]))
        
        # If odd number, pair last one with someone (or itself for now)
        if len(next_generation_ids) % 2 == 1:
            # Pair with someone from existing pairs or self
            if len(next_generation_pairs) > 0:
                # Replace one pair with a triple (simplified - just pair with first)
                last_id = next_generation_ids[-1]
                first_pair = next_generation_pairs[0]
                next_generation_pairs[0] = (first_pair[0], last_id)
            else:
                # Only one person - pair with themselves (will be skipped in next gen)
                next_generation_pairs.append((next_generation_ids[-1], next_generation_ids[-1]))
        
        current_generation_pairs = next_generation_pairs if next_generation_pairs else [(founder1_id, founder2_id)]
        
        # Update statistics
        stats['total_people'] += gen_children
        stats['generations'] = gen_num
        stats['max_children'] = max(stats['max_children'], gen_children)
        stats['min_children'] = min(stats['min_children'], gen_children) if gen_children > 0 else stats['min_children']
        stats['total_children'] += gen_children
        stats['generation_sizes'].append(gen_children)
        if gen_pairs > 0:
            stats['avg_children_per_pair'].append(gen_children / gen_pairs)
        
        print(f"  Generated {gen_children} children from {gen_pairs} pairs")
    
    avg_children = sum(stats['avg_children_per_pair']) / len(stats['avg_children_per_pair']) if stats['avg_children_per_pair'] else 0
    
    print(f"\n{family_name} Complete:")
    print(f"  Total people: {stats['total_people']}")
    print(f"  Generations: {stats['generations']}")
    print(f"  Avg children per pair: {avg_children:.1f}")
    
    return {
        'founder1_id': founder1_id,
        'founder2_id': founder2_id,
        'stats': stats,
        'all_ids': all_ids
    }


def run_stress_test(num_families: int = 5, generations: int = 10, db_path: str = "stress_test_characters.db"):
    """
    Run the stress test
    
    Args:
        num_families: Number of families to generate
        generations: Number of generations per family
        db_path: Path to database file
    """
    print("=" * 70)
    print(f"DNA SIMULATION STRESS TEST")
    print(f"{num_families} families × {generations} generations")
    print("=" * 70)
    
    # Create database (delete existing for fresh test)
    import os
    if os.path.exists(db_path):
        print(f"\nRemoving existing database: {db_path}")
        os.remove(db_path)
    
    print(f"\nCreating database: {db_path}")
    db = CharacterDatabase(db_path)
    
    # Family templates
    templates = [
        (create_royal_bloodline_founder, "House Royal"),
        (create_royal_bloodline_founder, "House Dragon"),
        (create_foreign_princess, "House Fey"),
        (create_common_person, "House Common"),
        (create_royal_bloodline_founder, "House Noble"),
    ]
    
    families = []
    start_year = 0
    
    # Generate families
    for i, (template, name) in enumerate(templates[:num_families]):
        try:
            family_data = generate_family(db, name, template, start_year, generations)
            families.append({
                'name': name,
                'data': family_data
            })
            start_year += 100  # Stagger family start years
        except Exception as e:
            print(f"\nERROR generating {name}: {e}")
            import traceback
            traceback.print_exc()
    
    # Print statistics
    print("\n" + "=" * 70)
    print("STRESS TEST RESULTS")
    print("=" * 70)
    
    total_people = 0
    for family in families:
        stats = family['data']['stats']
        total_people += stats['total_people']
        avg_children = sum(stats['avg_children_per_pair']) / len(stats['avg_children_per_pair']) if stats['avg_children_per_pair'] else 0
        print(f"\n{family['name']}:")
        print(f"  Total people: {stats['total_people']}")
        print(f"  Generations: {stats['generations']}")
        print(f"  Avg children per pair: {avg_children:.1f}")
        print(f"  Max children in one gen: {stats['max_children']}")
        print(f"  Min children in one gen: {stats['min_children']}")
    
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
    
    # Generate sample family tree
    if families:
        print(f"\n{'='*70}")
        print("SAMPLE FAMILY TREE (First Family, 5 generations)")
        print(f"{'='*70}")
        sample_family = families[0]
        founder_id = sample_family['data']['founder1_id']
        
        tree = FamilyTree(db)
        try:
            print(tree.generate_compact_tree(founder_id, max_generations=5))
        except UnicodeEncodeError:
            # Fallback for non-Unicode terminals
            print("\n(Family tree visualization skipped - Unicode not supported in this terminal)")
            print(f"Use tree.generate_ascii_tree({founder_id}) for ASCII-only output")
    
    print(f"\n{'='*70}")
    print("STRESS TEST COMPLETE")
    print(f"{'='*70}")
    print(f"Database file: {db_path}")
    print(f"Total people generated: {total_people}")
    print(f"Database size: {os.path.getsize(db_path) / 1024:.1f} KB")
    
    return db, families


if __name__ == "__main__":
    db, families = run_stress_test(num_families=5, generations=10)
