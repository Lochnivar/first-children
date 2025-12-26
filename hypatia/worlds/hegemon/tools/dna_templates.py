"""
Character template creation functions

This module provides functions to create DNA for specific character archetypes.
These are used for testing, examples, and initial population seeding.
"""

from .dna_core import DNA


def create_royal_bloodline_founder() -> DNA:
    """
    Create a 'perfect' royal bloodline founder
    
    This creates a DNA profile with pure homozygous traits for royal markers:
    - Violet eyes (pure)
    - Silver hair (pure)
    - Porcelain skin (pure)
    - Maximum magical aptitude
    - High mental traits
    - Royal markers
    
    Returns:
        DNA instance with royal founder traits
    """
    dna = DNA(maternal=0, paternal=0)
    
    # Set specific desirable traits (pure homozygous for royal markers)
    traits_to_set = {
        0: (0b1010, 0b1010),  # Violet eyes (pure)
        1: (0b1100, 0b1100),  # Silver hair (pure)
        2: (0b1001, 0b1001),  # Porcelain skin (pure)
        3: (0b1010, 0b1010),  # Tall (70 inches / 5'10")
        4: (0b1000, 0b1000),  # Stocky build
        5: (0b1011, 0b1011),  # Noble features
        6: (0b1010, 0b1010),  # Commanding voice
        7: (0b1011, 0b1011),  # Exotic scent
        
        # Health
        8: (0b1100, 0b1100),   # Heroic constitution
        9: (0b1000, 0b1000),   # Very High fertility
        10: (0b1100, 0b1100),  # 100 year lifespan
        11: (0b1010, 0b1010),  # Exceptional disease resistance
        12: (0b1000, 0b1000),  # High pain tolerance
        13: (0b1001, 0b1001),  # Very fast healing
        14: (0b0110, 0b0110),  # Fast metabolism
        15: (0b1001, 0b1001),  # Very strong toxin resistance
        
        # Mental
        16: (0b1011, 0b1011),  # Genius intelligence
        17: (0b1001, 0b1001),  # Sage wisdom
        18: (0b1100, 0b1100),  # Legendary charisma
        19: (0b1010, 0b1010),  # Rock solid stability
        20: (0b1011, 0b1011),  # Heroic willpower
        21: (0b0111, 0b0111),  # Empathetic
        22: (0b1010, 0b1010),  # Exceptional creativity
        23: (0b1011, 0b1011),  # Eidetic memory
        
        # Magical
        24: (0b1111, 0b1111),  # Godlike magical aptitude
        25: (0b1110, 0b1110),  # Elder blood
        26: (0b1100, 0b1100),  # Exalted divine favor
        27: (0b1111, 0b1111),  # True Dragon affinity
        28: (0b0000, 0b0000),  # No fey (avoid mixing)
        29: (0b0000, 0b0000),  # No elemental
        30: (0b1101, 0b1101),  # Destined
        31: (0b0000, 0b0000),  # No shadow
    }
    
    for trait_index, (mat, pat) in traits_to_set.items():
        dna.set_allele_pair(trait_index, mat, pat)
    
    return dna


def create_common_person() -> DNA:
    """
    Create a typical common person with average traits
    
    This creates a DNA profile with typical human traits:
    - Common eye/hair colors (brown, hazel)
    - Average physical traits
    - Average health and mental traits
    - Low/none magical traits
    
    Returns:
        DNA instance with common person traits
    """
    dna = DNA(maternal=0, paternal=0)
    
    traits_to_set = {
        0: (0b0001, 0b0010),  # Brown/Hazel eyes
        1: (0b0011, 0b0010),  # Light brown/brown hair
        2: (0b0110, 0b0101),  # Medium/Tan skin
        3: (0b0110, 0b0111),  # Average height (66-69 inches / 5'6"-5'9")
        4: (0b0101, 0b0110),  # Average/Athletic build
        5: (0b0100, 0b0101),  # Unremarkable/Average features
        6: (0b0101, 0b0110),  # Average/Pleasant voice
        7: (0b0101, 0b0110),  # Neutral/Clean scent
        
        # Health - average to slightly below
        8: (0b0110, 0b0111),   # Average/Healthy constitution
        9: (0b0110, 0b0111),   # Above average fertility
        10: (0b0110, 0b0111),  # 70-75 year lifespan
        11: (0b0110, 0b0111),  # Average/Good disease resistance
        12: (0b0101, 0b0110),  # Average pain tolerance
        13: (0b0110, 0b0111),  # Average/Good healing
        14: (0b0101, 0b0110),  # Average metabolism
        15: (0b0110, 0b0111),  # Average/Good toxin resistance
        
        # Mental - average
        16: (0b0110, 0b0111),  # Above average/Bright intelligence
        17: (0b0101, 0b0110),  # Average/Above average wisdom
        18: (0b0101, 0b0110),  # Average/Above average charisma
        19: (0b0111, 0b1000),  # Average/Stable
        20: (0b0110, 0b0111),  # Above average/Strong willpower
        21: (0b0110, 0b0111),  # Average/Empathetic
        22: (0b0101, 0b0110),  # Average/Creative
        23: (0b0101, 0b0110),  # Average/Good memory
        
        # Magical - low/none
        24: (0b0000, 0b0010),  # None/Minimal magic
        25: (0b0000, 0b0001),  # None/Trace bloodline
        26: (0b0101, 0b0110),  # Average divine favor
        27: (0b0000, 0b0000),  # No dragon
        28: (0b0000, 0b0000),  # No fey
        29: (0b0000, 0b0000),  # No elemental
        30: (0b0000, 0b0001),  # No/trace prophecy
        31: (0b0000, 0b0000),  # No shadow
    }
    
    for trait_index, (mat, pat) in traits_to_set.items():
        dna.set_allele_pair(trait_index, mat, pat)
    
    return dna


def create_hidden_royal_bastard() -> DNA:
    """
    Create a bastard with one royal parent, one common parent
    
    This creates a DNA profile where royal traits are carried recessively:
    - Shows common traits (hazel eyes, brown hair)
    - Carries royal markers (violet eyes, silver hair) as recessive alleles
    - Mixed health/mental traits
    - Carries high magical aptitude recessively
    
    Returns:
        DNA instance with hidden royal bastard traits
    """
    dna = DNA(maternal=0, paternal=0)
    
    traits_to_set = {
        0: (0b1010, 0b0010),  # Violet/Hazel (carries violet!)
        1: (0b1100, 0b0011),  # Silver/Light brown (carries silver!)
        2: (0b1001, 0b0101),  # Porcelain/Tan
        3: (0b1010, 0b0111),  # Tall/Average
        4: (0b1000, 0b0110),  # Stocky/Athletic
        5: (0b1011, 0b0101),  # Noble/Average features
        6: (0b1010, 0b0110),  # Commanding/Pleasant voice
        7: (0b1011, 0b0110),  # Exotic/Clean scent
        
        # Health - mixed
        8: (0b1100, 0b0111),   # Heroic/Healthy constitution
        9: (0b1000, 0b0111),   # Very High/Above average fertility
        10: (0b1100, 0b0111),  # Long/Average lifespan
        11: (0b1010, 0b0111),  # Exceptional/Good disease resistance
        12: (0b1000, 0b0110),  # High/Above average pain tolerance
        13: (0b1001, 0b0111),  # Very fast/Good healing
        14: (0b0110, 0b0110),  # Fast/Average metabolism
        15: (0b1001, 0b0111),  # Very strong/Good toxin resistance
        
        # Mental - above average (royal influence)
        16: (0b1011, 0b0111),  # Genius/Bright intelligence
        17: (0b1001, 0b0110),  # Sage/Above average wisdom
        18: (0b1100, 0b0110),  # Legendary/Above average charisma
        19: (0b1010, 0b1000),  # Rock solid/Stable
        20: (0b1011, 0b0111),  # Heroic/Strong willpower
        21: (0b0111, 0b0111),  # Empathetic
        22: (0b1010, 0b0110),  # Exceptional/Creative
        23: (0b1011, 0b0110),  # Eidetic/Good memory
        
        # Magical - diluted but present (carries maximum!)
        24: (0b1111, 0b0010),  # Godlike/Minimal (CARRIES MAXIMUM!)
        25: (0b1110, 0b0001),  # Elder/Trace (CARRIES ELDER!)
        26: (0b1100, 0b0110),  # Exalted/Average
        27: (0b1111, 0b0000),  # True Dragon/None (CARRIES!)
        28: (0b0000, 0b0000),  # No fey
        29: (0b0000, 0b0000),  # No elemental
        30: (0b1101, 0b0001),  # Destined/Trace (CARRIES!)
        31: (0b0000, 0b0000),  # No shadow
    }
    
    for trait_index, (mat, pat) in traits_to_set.items():
        dna.set_allele_pair(trait_index, mat, pat)
    
    return dna


def create_mad_king() -> DNA:
    """
    Create a king with concentrated bloodline but severe instability
    
    This demonstrates the cost of extreme inbreeding:
    - Pure royal markers maintained (violet eyes, silver hair)
    - Maximum magical power
    - BUT: Severe mental instability (madness, sociopathy)
    - Reduced fertility from inbreeding
    
    Returns:
        DNA instance with mad king traits (inbreeding consequences)
    """
    dna = DNA(maternal=0, paternal=0)
    
    traits_to_set = {
        0: (0b1010, 0b1010),  # Violet eyes (pure)
        1: (0b1100, 0b1100),  # Silver hair (pure)
        2: (0b1001, 0b1001),  # Porcelain skin (pure)
        3: (0b1010, 0b1010),  # Tall
        4: (0b0110, 0b0110),  # Athletic (not as strong as founder)
        5: (0b1011, 0b1011),  # Noble features
        6: (0b1010, 0b1010),  # Commanding voice
        7: (0b1011, 0b1011),  # Exotic scent
        
        # Health - weakened by inbreeding
        8: (0b1000, 0b1000),   # Stocky constitution (down from Heroic)
        9: (0b0011, 0b0011),   # Below average fertility (INBREEDING COST)
        10: (0b1010, 0b1010),  # 90 year lifespan (still good)
        11: (0b1000, 0b1000),  # Strong disease resistance (down from Exceptional)
        12: (0b1000, 0b1000),  # High pain tolerance
        13: (0b1001, 0b1001),  # Very fast healing
        14: (0b0110, 0b0110),  # Fast metabolism
        15: (0b1001, 0b1001),  # Very strong toxin resistance
        
        # Mental - SEVERE INSTABILITY
        16: (0b1011, 0b1011),  # Genius intelligence (maintained)
        17: (0b0011, 0b0011),  # Inexperienced wisdom (DAMAGED)
        18: (0b1100, 0b1100),  # Legendary charisma (maintained)
        19: (0b0010, 0b0010),  # MADNESS (INBREEDING COST) ⚠⚠
        20: (0b1011, 0b1011),  # Heroic willpower (can't overcome madness)
        21: (0b0001, 0b0001),  # Sociopath (INBREEDING COST) ⚠⚠
        22: (0b1010, 0b1010),  # Exceptional creativity
        23: (0b1011, 0b1011),  # Eidetic memory
        
        # Magical - MAXIMUM
        24: (0b1111, 0b1111),  # Godlike magical aptitude (concentrated!)
        25: (0b1110, 0b1110),  # Elder blood (pure)
        26: (0b1100, 0b1100),  # Exalted divine favor
        27: (0b1111, 0b1111),  # True Dragon affinity (concentrated!)
        28: (0b0000, 0b0000),  # No fey
        29: (0b0000, 0b0000),  # No elemental
        30: (0b1101, 0b1101),  # Destined
        31: (0b0000, 0b0000),  # No shadow
    }
    
    for trait_index, (mat, pat) in traits_to_set.items():
        dna.set_allele_pair(trait_index, mat, pat)
    
    return dna


def create_foreign_princess() -> DNA:
    """
    Create a foreign princess with different bloodline
    
    This creates a DNA profile with different traits from the royal line:
    - Different eye/hair colors (blue, blonde)
    - Excellent health traits
    - Strong mental stability (opposite of mad king)
    - Low magical traits but high fey affinity (different bloodline)
    
    Returns:
        DNA instance with foreign princess traits (good for outcrossing)
    """
    dna = DNA(maternal=0, paternal=0)
    
    traits_to_set = {
        0: (0b0110, 0b0111),  # Blue/Ice blue eyes (different from violet!)
        1: (0b0110, 0b0111),  # Blonde/Ash blonde hair (different from silver!)
        2: (0b0111, 0b1000),  # Fair/Pale skin
        3: (0b1000, 0b1001),  # Tall (68-71 inches)
        4: (0b0110, 0b0111),  # Athletic/Muscular build
        5: (0b1001, 0b1010),  # Beautiful/Striking features
        6: (0b1001, 0b1001),  # Resonant voice
        7: (0b1000, 0b1001),  # Floral/Sweet scent
        
        # Health - excellent
        8: (0b1010, 0b1011),   # Very Strong/Exceptional constitution
        9: (0b1100, 0b1101),   # Massive/Legendary fertility
        10: (0b1010, 0b1011),  # 90-95 year lifespan
        11: (0b1001, 0b1010),  # Very Strong/Exceptional disease resistance
        12: (0b1000, 0b1001),  # High/Very High pain tolerance
        13: (0b1000, 0b1001),  # Fast/Very fast healing
        14: (0b0110, 0b0111),  # Fast/Very fast metabolism
        15: (0b1000, 0b1001),  # Strong/Very strong toxin resistance
        
        # Mental - strong, especially stability
        16: (0b1000, 0b1001),  # Very Bright/Gifted intelligence
        17: (0b1000, 0b1001),  # Very Wise/Sage wisdom
        18: (0b1001, 0b1010),  # Magnetic/Very magnetic charisma
        19: (0b1100, 0b1101),  # Iron Will/Adamantine stability ★
        20: (0b1001, 0b1010),  # Exceptional/Remarkable willpower
        21: (0b1001, 0b1010),  # Compassionate/Very compassionate
        22: (0b1000, 0b1001),  # Highly Creative/Exceptional
        23: (0b1000, 0b1001),  # Very Good/Excellent memory
        
        # Magical - LOW (different bloodline) but high FEY
        24: (0b0100, 0b0101),  # Low/Below average magic
        25: (0b0010, 0b0011),  # Weak/Minor bloodline
        26: (0b1001, 0b1010),  # Blessed/Very blessed (different god)
        27: (0b0000, 0b0000),  # No dragon
        28: (0b1100, 0b1101),  # FEY BLOODLINE instead! ★
        29: (0b0000, 0b0000),  # No elemental
        30: (0b0010, 0b0011),  # Minimal/Weak prophecy
        31: (0b0000, 0b0000),  # No shadow
    }
    
    for trait_index, (mat, pat) in traits_to_set.items():
        dna.set_allele_pair(trait_index, mat, pat)
    
    return dna

