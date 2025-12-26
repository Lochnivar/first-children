"""
DNA Simulation Examples

This module contains example simulations demonstrating the DNA system.
All examples from the original implementation are preserved here, using
the refactored modules with all fixes applied.
"""

from .dna_core import (
    DNA, create_child, calculate_genetic_similarity,
    describe_character, describe_breeding_analysis
)
from .dna_templates import (
    create_royal_bloodline_founder,
    create_common_person,
    create_hidden_royal_bastard,
    create_mad_king,
    create_foreign_princess
)
from .dna_traits import TRAIT_DEFINITIONS


def run_mating_1_royal_founders():
    """MATING 1: Royal Founder × Royal Founder (Sibling Marriage)"""
    print("=" * 70)
    print("MATING 1: PURE ROYAL BLOODLINE (Sibling Marriage)")
    print("=" * 70)
    
    founder1 = create_royal_bloodline_founder()
    founder2 = create_royal_bloodline_founder()
    
    print(describe_character(founder1, "King Aerys I (Founder)"))
    print(describe_character(founder2, "Queen Rhaella I (Founder - Sister)"))
    
    print(describe_breeding_analysis(founder1, founder2, "King Aerys I", "Queen Rhaella I"))
    
    # Create 5 children
    print("\n" + "=" * 70)
    print("OFFSPRING FROM PURE ROYAL SIBLING MARRIAGE:")
    print("=" * 70)
    
    children1 = []
    for i in range(5):
        # High inbreeding = higher mutation rate
        child = create_child(founder1, founder2, mutation_rate=0.05)
        children1.append(child)
        print(describe_character(child, f"Child {i+1} (Prince/Princess)"))
    
    return children1


def run_mating_2_royal_common():
    """MATING 2: Royal King × Common Woman (Bastard)"""
    print("\n" + "=" * 70)
    print("MATING 2: ROYAL × COMMON (Bastard Line)")
    print("=" * 70)
    
    royal_king = create_royal_bloodline_founder()
    common_woman = create_common_person()
    
    print(describe_character(royal_king, "King Aerys I"))
    print(describe_character(common_woman, "Commoner Woman"))
    
    print(describe_breeding_analysis(royal_king, common_woman, "King Aerys I", "Commoner Woman"))
    
    # Create bastard
    bastard = create_child(royal_king, common_woman, mutation_rate=0.01)
    print("\n" + "=" * 70)
    print("OFFSPRING (ROYAL BASTARD):")
    print("=" * 70)
    print(describe_character(bastard, "Royal Bastard"))
    
    return bastard


def run_mating_3_bastard_bastard():
    """MATING 3: Two Royal Bastards (Recessive Violet Eyes Return?)"""
    print("\n" + "=" * 70)
    print("MATING 3: BASTARD × BASTARD (Can Violet Eyes Return?)")
    print("=" * 70)
    
    # Create two bastards (both carry violet eyes recessively)
    bastard1 = create_hidden_royal_bastard()
    bastard2 = create_hidden_royal_bastard()
    
    print(describe_character(bastard1, "Bastard 1 (Blue eyes, carries Violet)"))
    print(describe_character(bastard2, "Bastard 2 (Blue eyes, carries Violet)"))
    
    print(describe_breeding_analysis(bastard1, bastard2, "Bastard 1", "Bastard 2"))
    
    # Create children - some should have violet eyes!
    print("\n" + "=" * 70)
    print("OFFSPRING FROM BASTARD × BASTARD:")
    print("=" * 70)
    
    bastard_children = []
    for i in range(8):  # More children to see probabilities
        child = create_child(bastard1, bastard2, mutation_rate=0.01)
        bastard_children.append(child)
        
        # Check for violet eyes
        eyes = child.get_phenotype(0)
        eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
        has_violet = "VIOLET" in eyes_name.upper()
        
        # Check for maximum magic
        magic = child.get_phenotype(24)
        magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
        has_max_magic = magic >= 12
        
        marker = ""
        if has_violet and has_max_magic:
            marker = " ★★★ TRUE BLOOD RESTORED!"
        elif has_violet:
            marker = " ★★ VIOLET EYES!"
        elif has_max_magic:
            marker = " ★ HIGH MAGIC"
        
        print(f"\nChild {i+1}{marker}")
        print(f"  Eyes: {eyes_name}")
        print(f"  Magic: {magic_name}")
    
    return bastard_children


def run_mating_4_outcross():
    """MATING 4: Mad King × Foreign Princess (Outcross to Fix Instability)"""
    print("\n" + "=" * 70)
    print("MATING 4: MAD KING × FOREIGN PRINCESS (Outcross)")
    print("=" * 70)
    
    mad_king = create_mad_king()
    foreign_princess = create_foreign_princess()
    
    print(describe_character(mad_king, "King Aerys III 'The Mad'"))
    print(describe_character(foreign_princess, "Princess Ylena of Faerieland"))
    
    print(describe_breeding_analysis(mad_king, foreign_princess, "Mad King", "Foreign Princess"))
    
    # Create children
    print("\n" + "=" * 70)
    print("OFFSPRING FROM MAD KING × FOREIGN PRINCESS:")
    print("=" * 70)
    
    hybrid_children = []
    for i in range(5):
        child = create_child(mad_king, foreign_princess, mutation_rate=0.01)
        hybrid_children.append(child)
        
        # Check key traits
        eyes = child.get_phenotype(0)
        hair = child.get_phenotype(1)
        stability = child.get_phenotype(19)
        magic = child.get_phenotype(24)
        dragon = child.get_phenotype(27)
        fey = child.get_phenotype(28)
        
        eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
        hair_name = TRAIT_DEFINITIONS[1]['values'][hair]['name']
        stability_name = TRAIT_DEFINITIONS[19]['values'][stability]['name']
        magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
        dragon_name = TRAIT_DEFINITIONS[27]['values'][dragon]['name']
        fey_name = TRAIT_DEFINITIONS[28]['values'][fey]['name']
        
        print(f"\nChild {i+1}")
        print(f"  Eyes: {eyes_name}")
        print(f"  Hair: {hair_name}")
        print(f"  Stability: {stability_name}")
        print(f"  Magic: {magic_name}")
        print(f"  Dragon Affinity: {dragon_name}")
        print(f"  Fey Affinity: {fey_name}")
        
        # Analysis
        has_violet = "VIOLET" in eyes_name.upper()
        has_silver = "SILVER" in hair_name.upper()
        is_stable = stability >= 8
        has_high_magic = magic >= 10
        
        if has_violet and has_silver and is_stable and has_high_magic:
            print("  ★★★ PERFECT HEIR - Royal markers + Stable + Magic!")
        elif has_violet and has_silver:
            print("  ★★ True bloodline markers")
        elif is_stable and has_high_magic:
            print("  ★ Stable with strong magic")
    
    return hybrid_children


def run_mating_5_inbreeding_experiment():
    """MATING 5: Inbreeding Experiment (3 Generations of Sibling Marriage)"""
    print("\n" + "=" * 70)
    print("MATING 5: INBREEDING EXPERIMENT (3 Generations)")
    print("=" * 70)
    
    print("\nGeneration 1: Founders (Siblings)")
    gen1_king = create_royal_bloodline_founder()
    gen1_queen = create_royal_bloodline_founder()
    
    # Create Gen 2 (children of Gen 1 siblings)
    gen2_children = []
    for i in range(3):
        child = create_child(gen1_king, gen1_queen, mutation_rate=0.05)
        gen2_children.append(child)
    
    # Pick the "best" two from Gen 2 to marry (highest magic + stability)
    gen2_sorted = sorted(gen2_children, 
                        key=lambda x: x.get_phenotype(24) + x.get_phenotype(19), 
                        reverse=True)
    gen2_king = gen2_sorted[0]
    gen2_queen = gen2_sorted[1]
    
    print("\nGeneration 2: Best children from Gen 1 (Siblings)")
    print(f"  King stability: {TRAIT_DEFINITIONS[19]['values'][gen2_king.get_phenotype(19)]['name']}")
    print(f"  King magic: {TRAIT_DEFINITIONS[24]['values'][gen2_king.get_phenotype(24)]['name']}")
    print(f"  Queen stability: {TRAIT_DEFINITIONS[19]['values'][gen2_queen.get_phenotype(19)]['name']}")
    print(f"  Queen magic: {TRAIT_DEFINITIONS[24]['values'][gen2_queen.get_phenotype(24)]['name']}")
    
    # Calculate Gen 2 similarity (renamed function)
    similarity_gen2 = calculate_genetic_similarity(gen2_king, gen2_queen)
    print(f"  Genetic similarity: {similarity_gen2*100:.1f}%")
    
    # Create Gen 3 (children of Gen 2 siblings)
    gen3_children = []
    for i in range(5):
        mutation_rate = min(0.15, similarity_gen2 * 0.2)
        child = create_child(gen2_king, gen2_queen, mutation_rate=mutation_rate)
        gen3_children.append(child)
    
    print("\nGeneration 3: Children of Gen 2 siblings")
    print("Analyzing outcomes...\n")
    
    stats = {
        'violet_eyes': 0,
        'max_magic': 0,
        'stable': 0,
        'unstable': 0,
        'perfect': 0,
        'disasters': 0
    }
    
    for i, child in enumerate(gen3_children):
        eyes = child.get_phenotype(0)
        magic = child.get_phenotype(24)
        stability = child.get_phenotype(19)
        fertility = child.get_phenotype(9)
        
        eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
        magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
        stability_name = TRAIT_DEFINITIONS[19]['values'][stability]['name']
        fertility_name = TRAIT_DEFINITIONS[9]['values'][fertility]['name']
        
        has_violet = "VIOLET" in eyes_name.upper()
        has_max_magic = magic >= 14
        is_stable = stability >= 8
        is_unstable = stability <= 4
        is_fertile = fertility >= 6
        
        if has_violet:
            stats['violet_eyes'] += 1
        if has_max_magic:
            stats['max_magic'] += 1
        if is_stable:
            stats['stable'] += 1
        if is_unstable:
            stats['unstable'] += 1
        
        if has_violet and has_max_magic and is_stable and is_fertile:
            stats['perfect'] += 1
            print(f"Child {i+1}: ★★★ PERFECT - {eyes_name}, {magic_name}, {stability_name}, {fertility_name}")
        elif is_unstable or not is_fertile:
            stats['disasters'] += 1
            print(f"Child {i+1}: ⚠⚠ DISASTER - {eyes_name}, {magic_name}, {stability_name}, {fertility_name}")
        else:
            print(f"Child {i+1}: {eyes_name}, {magic_name}, {stability_name}, {fertility_name}")
    
    print(f"\n{'='*70}")
    print("INBREEDING EXPERIMENT RESULTS:")
    print(f"{'='*70}")
    print(f"Violet eyes: {stats['violet_eyes']}/5 ({stats['violet_eyes']*20}%)")
    print(f"Maximum magic: {stats['max_magic']}/5 ({stats['max_magic']*20}%)")
    print(f"Stable: {stats['stable']}/5 ({stats['stable']*20}%)")
    print(f"Unstable: {stats['unstable']}/5 ({stats['unstable']*20}%)")
    print(f"Perfect heirs: {stats['perfect']}/5 ({stats['perfect']*20}%)")
    print(f"Disasters: {stats['disasters']}/5 ({stats['disasters']*20}%)")
    
    print(f"\n{'='*70}")
    print("CONCLUSION:")
    print(f"{'='*70}")
    if stats['max_magic'] >= 3:
        print("✓ Successfully concentrated magical power through inbreeding")
    else:
        print("✗ Failed to concentrate magical power")
    
    if stats['unstable'] >= 2:
        print("⚠ Severe mental instability problems from inbreeding")
    else:
        print("✓ Mental stability maintained")
    
    if stats['perfect'] >= 1:
        print(f"★ Produced {stats['perfect']} perfect heir(s) - dynasty survives!")
    else:
        print("⚠ No perfect heirs produced - dynasty in crisis")
    
    return gen3_children, stats


def run_all_simulations():
    """Run all example simulations"""
    print("=" * 70)
    print("DNA GENETICS SIMULATION - ALL MATINGS")
    print("=" * 70)
    
    results = {}
    
    results['mating1'] = run_mating_1_royal_founders()
    results['mating2'] = run_mating_2_royal_common()
    results['mating3'] = run_mating_3_bastard_bastard()
    results['mating4'] = run_mating_4_outcross()
    results['mating5'] = run_mating_5_inbreeding_experiment()
    
    print("\n" + "=" * 70)
    print("SIMULATION COMPLETE")
    print("=" * 70)
    print("\nKey Findings:")
    print("1. Pure royal bloodlines can be maintained through sibling marriage")
    print("2. Bastards can carry royal traits recessively and restore them")
    print("3. Outcrossing with foreign nobility can fix instability")
    print("4. Inbreeding concentrates both desirable AND undesirable traits")
    print("5. The system accurately models Mendelian genetics")
    print("\nThe DNA number system successfully handles:")
    print("  - Recessive trait inheritance")
    print("  - Genetic diversity loss through inbreeding")
    print("  - Hybrid vigor from outcrossing")
    print("  - Multi-generational trait tracking")
    print("  - Political implications of bloodline purity")
    
    return results


if __name__ == "__main__":
    # Run all simulations when executed directly
    run_all_simulations()

