"""
Helper function to create a complete character with Nature (DNA) and Nurture (DEPC) data

This integrates the DNA system with the DEPC system to create fully-realized characters.
"""

from typing import Optional, Tuple
from .dna_core import DNA, create_child
from .dna_database import CharacterDatabase
from .depc_system import develop_character_depc, calculate_derived_abilities
from .name_generator import generate_full_name
from .update_characters_with_nurture import assign_character_to_burg, load_burgs_by_culture


def create_complete_character(
    parent1_dna: Optional[DNA] = None,
    parent2_dna: Optional[DNA] = None,
    culture_name: str = 'valthir',
    is_noble: bool = False,
    first_name: Optional[str] = None,
    family_name: Optional[str] = None,
    gender: Optional[str] = None,
    birth_year: Optional[int] = None,
    parent1_id: Optional[int] = None,
    parent2_id: Optional[int] = None,
    assign_to_burg: bool = True,
    db: Optional[CharacterDatabase] = None,
    notes: Optional[str] = None
) -> Tuple[int, dict]:
    """
    Create a complete character with both Nature (DNA) and Nurture (DEPC) data
    
    Args:
        parent1_dna: First parent's DNA (None for founder)
        parent2_dna: Second parent's DNA (None for founder)
        culture_name: Culture the character is raised in
        is_noble: Whether character is nobility
        first_name: First name (generated if None)
        family_name: Family name (generated if None)
        gender: 'male' or 'female' (random if None)
        birth_year: Year of birth
        parent1_id: First parent's database ID
        parent2_id: Second parent's database ID
        assign_to_burg: Whether to assign character to a burg
        db: CharacterDatabase instance (creates new if None)
        notes: Optional notes
        
    Returns:
        Tuple of (character_id, character_data_dict)
    """
    
    # Create or inherit DNA
    if parent1_dna and parent2_dna:
        child_dna = create_child(parent1_dna, parent2_dna, mutation_rate=0.01)
    elif parent1_dna:
        # Single parent (cloning or special case)
        child_dna = create_child(parent1_dna, parent1_dna, mutation_rate=0.01)
    else:
        # Founder - create random DNA
        child_dna = DNA()
    
    # Develop DEPC profile
    depc_data = develop_character_depc(child_dna, culture_name, is_noble)
    depc_profile = depc_data['depc_profile']
    developmental_stress = depc_data['developmental_stress']
    
    # Calculate derived abilities
    derived_abilities = calculate_derived_abilities(depc_profile)
    
    # Generate names if not provided
    if not gender:
        gender = 'male' if not first_name else None
    
    if not first_name or not family_name:
        # Get burg for name context if available
        burg_name = None
        if assign_to_burg:
            burgs_by_culture = load_burgs_by_culture()
            burg = assign_character_to_burg(culture_name, burgs_by_culture)
            if burg:
                burg_name = burg.get('name')
        
        gen_first, gen_family, gen_full = generate_full_name(
            culture_name, gender, burg_name
        )
        
        if not first_name:
            first_name = gen_first
        if not family_name:
            family_name = gen_family
    
    full_name = f"{first_name} {family_name}"
    
    # Assign to burg if requested
    burg_id = None
    burg_name = None
    state_name = None
    
    if assign_to_burg:
        burgs_by_culture = load_burgs_by_culture()
        burg = assign_character_to_burg(culture_name, burgs_by_culture)
        if burg:
            burg_id = burg.get('id')
            burg_name = burg.get('name')
            state_name = burg.get('state')
    
    # Save to database
    if db is None:
        db = CharacterDatabase()
    
    char_id = db.save_character(
        name=full_name,
        dna=child_dna,
        parent1_id=parent1_id,
        parent2_id=parent2_id,
        birth_year=birth_year,
        first_name=first_name,
        family_name=family_name,
        culture=culture_name,
        is_noble=is_noble,
        burg_id=burg_id,
        burg_name=burg_name,
        state_name=state_name,
        depc_profile=depc_profile,
        developmental_stress=developmental_stress['total_stress'],
        stress_severity=developmental_stress['severity'],
        notes=notes
    )
    
    # Build complete character data dict
    character_data = {
        'id': char_id,
        'name': full_name,
        'first_name': first_name,
        'family_name': family_name,
        'dna': child_dna,
        'culture': culture_name,
        'is_noble': is_noble,
        'burg_id': burg_id,
        'burg_name': burg_name,
        'state_name': state_name,
        'depc_profile': depc_profile,
        'derived_abilities': derived_abilities,
        'developmental_stress': developmental_stress,
        'development_history': depc_data['development_history'],
        'birth_year': birth_year,
        'notes': notes,
    }
    
    return (char_id, character_data)


if __name__ == "__main__":
    # Example usage
    print("Creating example characters...\n")
    
    # Create a founder
    founder_id, founder_data = create_complete_character(
        culture_name='valthir',
        is_noble=True,
        birth_year=300,
        notes='Founder of a noble house'
    )
    
    print(f"Created founder: {founder_data['name']}")
    print(f"  Culture: {founder_data['culture']}")
    print(f"  Burg: {founder_data['burg_name']} ({founder_data['state_name']})")
    print(f"  DEPC: D={founder_data['depc_profile'].dominance:.1f}, "
          f"E={founder_data['depc_profile'].extroversion:.1f}, "
          f"P={founder_data['depc_profile'].patience:.1f}, "
          f"C={founder_data['depc_profile'].conformity:.1f}")
    print(f"  Stress: {founder_data['developmental_stress']['severity']}")
    print()

