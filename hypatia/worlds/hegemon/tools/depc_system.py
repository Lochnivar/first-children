"""
DEPC Personality System - Cultural Development of Personality
Dominance, Extroversion, Patience, Conformity

This system models personality as NURTURE (cultural development)
rather than genetic inheritance.

Based on comprehensive implementation guide in HEGEMON-DIALOG.md
"""

import random
from typing import Dict, List, Tuple
from dataclasses import dataclass

try:
    from .dna_core import DNA
except ImportError:
    import sys
    from pathlib import Path
    tools_dir = Path(__file__).parent
    sys.path.insert(0, str(tools_dir.parent))
    from tools.dna_core import DNA


# ============================================================================
# DEPC PROFILE CLASS
# ============================================================================

@dataclass
class DEPCProfile:
    """
    Represents a character's personality (DEPC = Dominance, Extroversion, 
    Patience, Conformity).
    
    IMPORTANT: DEPC is NOT genetically inherited. It develops from:
    - Genetic tendencies (30%)
    - Cultural shaping (50%)
    - Life events (20%)
    """
    
    dominance: float      # 1-100: Assertiveness, leadership, control
    extroversion: float   # 1-100: Sociability, outgoingness, energy
    patience: float       # 1-100: Tolerance, deliberation, calmness
    conformity: float     # 1-100: Traditionalism, obedience, conventionality
    
    def __post_init__(self):
        """Calculate derived values after initialization"""
        # Clamp all values to 1-100
        self.dominance = max(1, min(100, self.dominance))
        self.extroversion = max(1, min(100, self.extroversion))
        self.patience = max(1, min(100, self.patience))
        self.conformity = max(1, min(100, self.conformity))
        
        # Calculate base personality (charisma) = mean of DEPC
        self.charisma = (self.dominance + self.extroversion + 
                        self.patience + self.conformity) / 4
        
        # Calculate expressions (strengths/weaknesses relative to mean)
        self.d_expression = self.dominance - self.charisma
        self.e_expression = self.extroversion - self.charisma
        self.p_expression = self.patience - self.charisma
        self.c_expression = self.conformity - self.charisma
    
    def get_trait_expression(self, trait_name: str) -> float:
        """Get expression value for a trait"""
        expressions = {
            'dominance': self.d_expression,
            'extroversion': self.e_expression,
            'patience': self.p_expression,
            'conformity': self.c_expression,
        }
        return expressions.get(trait_name, 0)
    
    def get_strengths(self) -> Dict[str, float]:
        """Return traits with positive expression (strengths)"""
        return {
            trait: expr for trait, expr in [
                ('dominance', self.d_expression),
                ('extroversion', self.e_expression),
                ('patience', self.p_expression),
                ('conformity', self.c_expression),
            ] if expr >= 5
        }
    
    def get_weaknesses(self) -> Dict[str, float]:
        """Return traits with negative expression (weaknesses)"""
        return {
            trait: expr for trait, expr in [
                ('dominance', self.d_expression),
                ('extroversion', self.e_expression),
                ('patience', self.p_expression),
                ('conformity', self.c_expression),
            ] if expr <= -5
        }


# ============================================================================
# GENETIC FOUNDATION (STAGE 1: 30% INFLUENCE)
# ============================================================================

def calculate_genetic_depc_tendencies(dna: DNA) -> Dict[str, float]:
    """
    Extract DEPC tendencies from genetic traits.
    
    Genetics provide TENDENCIES, not determinism.
    These account for 30% of final personality.
    
    Args:
        dna: DNA object with genetic traits
        
    Returns:
        Dict with 'dominance', 'extroversion', 'patience', 'conformity' (0-100)
    """
    
    # Extract relevant genetic traits (0-15 scale) and convert to 0-100
    charisma = dna.get_phenotype(18) * 6.67
    willpower = dna.get_phenotype(20) * 6.67
    stability = dna.get_phenotype(19) * 6.67
    intelligence = dna.get_phenotype(16) * 6.67
    empathy = dna.get_phenotype(21) * 6.67
    
    # DOMINANCE: Charisma + Willpower + (inverse Empathy)
    # Logic: High charisma/willpower = commanding, low empathy = ruthless
    dominance_genetic = (
        charisma * 0.4 +
        willpower * 0.4 +
        (100 - empathy) * 0.2
    )
    
    # EXTROVERSION: Charisma + Empathy + (inverse Stability)
    # Logic: Charisma = enjoys social, empathy = attuned to others,
    #        low stability = seeks external stimulation
    extroversion_genetic = (
        charisma * 0.5 +
        empathy * 0.3 +
        (100 - stability) * 0.2
    )
    
    # PATIENCE: Stability + (inverse Intelligence)
    # Logic: Stable people wait calmly, smart people are impatient
    patience_genetic = (
        stability * 0.6 +
        (100 - intelligence) * 0.4
    )
    
    # CONFORMITY: Stability + Empathy + (inverse Willpower)
    # Logic: Stable = likes structure, empathy = group harmony,
    #        low willpower = less resistance to social pressure
    conformity_genetic = (
        stability * 0.4 +
        empathy * 0.3 +
        (100 - willpower) * 0.3
    )
    
    return {
        'dominance': max(1, min(100, dominance_genetic)),
        'extroversion': max(1, min(100, extroversion_genetic)),
        'patience': max(1, min(100, patience_genetic)),
        'conformity': max(1, min(100, conformity_genetic)),
    }


# ============================================================================
# CULTURAL INFLUENCE (STAGE 2: 50% INFLUENCE)
# ============================================================================

@dataclass
class CultureDEPCInfluence:
    """
    Defines how a culture shapes personality during development.
    
    Each culture has:
    - Target DEPC values (what the culture promotes)
    - Cultural pressure (how strongly it enforces conformity)
    """
    
    name: str
    depc_targets: Dict[str, float]  # Target values for D, E, P, C (1-100)
    depc_pressure: float             # 0.0-1.0 (strength of cultural influence)
    
    def shape_depc(self, genetic_tendencies: Dict[str, float]) -> Dict[str, float]:
        """
        Apply cultural shaping to genetic tendencies.
        
        Formula: shaped = genetic × (1 - pressure) + target × pressure
        
        High pressure = culture overrides genetics more
        Low pressure = genetics express more freely
        
        Args:
            genetic_tendencies: Dict with genetic DEPC values
            
        Returns:
            Dict with culturally shaped DEPC values
        """
        
        shaped_depc = {}
        
        for trait in ['dominance', 'extroversion', 'patience', 'conformity']:
            genetic_value = genetic_tendencies[trait]
            cultural_target = self.depc_targets[trait]
            
            # Blend genetic tendency with cultural target
            shaped_value = (
                genetic_value * (1 - self.depc_pressure) +
                cultural_target * self.depc_pressure
            )
            
            shaped_depc[trait] = max(1, min(100, shaped_value))
        
        return shaped_depc


# ============================================================================
# HEGEMON CULTURAL DEPC DEFINITIONS
# ============================================================================

HEGEMON_CULTURE_DEPC = {
    
    # GERMANIC TEMPLATE
    
    'valthir': CultureDEPCInfluence(
        name="Valthir",
        depc_targets={
            'dominance': 45,
            'extroversion': 40,
            'patience': 75,
            'conformity': 85,
        },
        depc_pressure=0.70
    ),
    
    'sturmgaard': CultureDEPCInfluence(
        name="Sturmgaard",
        depc_targets={
            'dominance': 55,
            'extroversion': 50,
            'patience': 70,
            'conformity': 70,
        },
        depc_pressure=0.60
    ),
    
    'eldermark': CultureDEPCInfluence(
        name="Eldermark",
        depc_targets={
            'dominance': 80,
            'extroversion': 70,
            'patience': 35,
            'conformity': 40,
        },
        depc_pressure=0.65
    ),
    
    # LATIN TEMPLATE
    
    'veridian': CultureDEPCInfluence(
        name="Veridian",
        depc_targets={
            'dominance': 70,
            'extroversion': 65,
            'patience': 60,
            'conformity': 75,
        },
        depc_pressure=0.65
    ),
    
    'solemnium': CultureDEPCInfluence(
        name="Solemnium",
        depc_targets={
            'dominance': 50,
            'extroversion': 75,
            'patience': 55,
            'conformity': 60,
        },
        depc_pressure=0.55
    ),
    
    'aurelian': CultureDEPCInfluence(
        name="Aurelian",
        depc_targets={
            'dominance': 60,
            'extroversion': 55,
            'patience': 65,
            'conformity': 50,
        },
        depc_pressure=0.60
    ),
    
    'meridian': CultureDEPCInfluence(
        name="Meridian",
        depc_targets={
            'dominance': 55,
            'extroversion': 70,
            'patience': 60,
            'conformity': 75,
        },
        depc_pressure=0.65
    ),
    
    # BERBER TEMPLATE
    
    'qasridan': CultureDEPCInfluence(
        name="Qasridan",
        depc_targets={
            'dominance': 65,
            'extroversion': 45,
            'patience': 75,
            'conformity': 70,
        },
        depc_pressure=0.70
    ),
    
    # SLAVIC TEMPLATE
    
    'zvezdan': CultureDEPCInfluence(
        name="Zvezdan",
        depc_targets={
            'dominance': 70,
            'extroversion': 60,
            'patience': 50,
            'conformity': 55,
        },
        depc_pressure=0.55
    ),
    
    'yaroslav': CultureDEPCInfluence(
        name="Yaroslav",
        depc_targets={
            'dominance': 75,
            'extroversion': 65,
            'patience': 45,
            'conformity': 50,
        },
        depc_pressure=0.60
    ),
    
    # FUSION
    
    'sundrakar': CultureDEPCInfluence(
        name="Sundrakar",
        depc_targets={
            'dominance': 85,
            'extroversion': 75,
            'patience': 25,
            'conformity': 20,
        },
        depc_pressure=0.75
    ),
    
    # SPECIAL
    
    'khanhthien': CultureDEPCInfluence(
        name="Khanhthien",
        depc_targets={
            'dominance': 50,
            'extroversion': 45,
            'patience': 80,
            'conformity': 65,
        },
        depc_pressure=0.55
    ),
}


# ============================================================================
# LIFE EVENTS (STAGE 3: 20% INFLUENCE)
# ============================================================================

UPBRINGING_EVENTS = [
    {
        'name': 'Harsh Military Training',
        'description': 'Subjected to brutal warrior training from young age',
        'depc_modifiers': {'dominance': +15, 'patience': -10, 'conformity': +20},
        'probability': 0.15,
        'cultures': ['eldermark', 'yaroslav', 'sundrakar', 'veridian'],
    },
    {
        'name': 'Isolated Childhood',
        'description': 'Raised in isolation, limited social contact',
        'depc_modifiers': {'extroversion': -20, 'patience': +10},
        'probability': 0.10,
    },
    {
        'name': 'Traumatic Loss',
        'description': 'Lost parent/sibling/mentor at young age',
        'depc_modifiers': {'dominance': -15, 'extroversion': -10, 'patience': +5},
        'probability': 0.12,
    },
    {
        'name': 'Mentored by Rebel',
        'description': 'Taught by unconventional mentor who questioned authority',
        'depc_modifiers': {'dominance': +10, 'conformity': -25},
        'probability': 0.08,
    },
    {
        'name': 'Court Education',
        'description': 'Educated at royal court, learned social graces',
        'depc_modifiers': {'extroversion': +15, 'conformity': +15, 'patience': +10},
        'probability': 0.20,
        'nobility_only': True,
    },
    {
        'name': 'Survived Plague',
        'description': 'Survived deadly plague that killed many around them',
        'depc_modifiers': {'dominance': +5, 'patience': +15},
        'probability': 0.05,
    },
    {
        'name': 'Religious Upbringing',
        'description': 'Raised in temple/monastery, steeped in religious teaching',
        'depc_modifiers': {'patience': +15, 'conformity': +20, 'dominance': -10},
        'probability': 0.15,
    },
    {
        'name': 'Raised by Servants',
        'description': 'Noble child raised primarily by servants, not parents',
        'depc_modifiers': {'dominance': -10, 'extroversion': +10, 'conformity': +10},
        'probability': 0.10,
        'nobility_only': True,
    },
    {
        'name': 'Witnessed Brutality',
        'description': 'Witnessed extreme violence/cruelty at formative age',
        'depc_modifiers': {'dominance': +10, 'patience': -15, 'conformity': -10},
        'probability': 0.08,
        'cultures': ['sundrakar', 'yaroslav', 'eldermark'],
    },
    {
        'name': 'Natural Leader',
        'description': 'Naturally took charge among peers, recognized early',
        'depc_modifiers': {'dominance': +20, 'extroversion': +10},
        'probability': 0.12,
    },
    {
        'name': 'Bookish Youth',
        'description': 'Spent youth absorbed in study and contemplation',
        'depc_modifiers': {'extroversion': -15, 'patience': +20},
        'probability': 0.15,
    },
    {
        'name': 'Bullied Mercilessly',
        'description': 'Suffered constant bullying from peers',
        'depc_modifiers': {'dominance': -20, 'extroversion': -15, 'conformity': +10},
        'probability': 0.08,
    },
]


def generate_upbringing_events(culture_name: str, is_noble: bool) -> List[Dict]:
    """
    Generate 0-3 random events during childhood.
    
    Args:
        culture_name: Culture the child is raised in
        is_noble: Whether child is nobility (affects event availability)
        
    Returns:
        List of event dicts that occurred during upbringing
    """
    
    num_events = random.randint(0, 3)
    events = []
    
    for _ in range(num_events):
        # Filter applicable events
        applicable_events = [
            event for event in UPBRINGING_EVENTS
            if (not event.get('nobility_only') or is_noble) and
               (not event.get('cultures') or culture_name in event.get('cultures', []))
        ]
        
        if not applicable_events:
            continue
        
        # Weight by probability
        weights = [e['probability'] for e in applicable_events]
        chosen_event = random.choices(applicable_events, weights=weights)[0]
        events.append(chosen_event)
    
    return events


def apply_upbringing_events(base_depc: Dict[str, float], 
                            events: List[Dict]) -> Dict[str, float]:
    """
    Apply event modifiers to DEPC values.
    
    Args:
        base_depc: DEPC values after cultural shaping
        events: List of events that occurred
        
    Returns:
        Final DEPC values with event modifiers applied
    """
    
    modified_depc = base_depc.copy()
    
    for event in events:
        for trait, modifier in event['depc_modifiers'].items():
            modified_depc[trait] = max(1, min(100, 
                modified_depc[trait] + modifier
            ))
    
    return modified_depc


# ============================================================================
# CHILDHOOD DEVELOPMENTAL STRESS
# ============================================================================

def calculate_developmental_stress(genetic_tendencies: Dict[str, float],
                                   culture: CultureDEPCInfluence) -> Dict:
    """
    Calculate stress experienced during childhood development.
    
    High stress occurs when genetics clash with cultural expectations.
    This creates permanent psychological damage.
    
    Args:
        genetic_tendencies: Child's natural DEPC tendencies from genetics
        culture: Culture raising the child
        
    Returns:
        Dict with:
            - total_stress: Total developmental stress
            - trait_breakdown: Stress per trait
            - severity: Overall severity category
            - long_term_effects: Permanent damage
    """
    
    RESISTANCE_FACTORS = {
        'dominance': 2.0,     # Very hard to force (core personality)
        'extroversion': 1.5,  # Hard to force (temperament)
        'patience': 1.0,      # Moderate (can be trained)
        'conformity': 1.3,    # Moderate-hard (values)
    }
    
    total_stress = 0
    trait_breakdown = {}
    
    for trait in ['dominance', 'extroversion', 'patience', 'conformity']:
        genetic_value = genetic_tendencies[trait]
        cultural_target = culture.depc_targets[trait]
        
        # Calculate gap between nature and cultural expectation
        gap = abs(cultural_target - genetic_value)
        
        # Stress = gap × cultural_pressure × resistance_factor
        trait_stress = gap * culture.depc_pressure * RESISTANCE_FACTORS[trait]
        
        trait_breakdown[trait] = {
            'gap': gap,
            'stress': trait_stress,
            'severity': _categorize_trait_stress(trait_stress)
        }
        
        total_stress += trait_stress
    
    # Calculate long-term damage
    long_term_effects = {
        'genetic_stability_damage': min(5, int(total_stress / 80)),
        'flexibility_penalty': min(0.5, total_stress / 800),
        'breakdown_susceptibility': min(0.3, total_stress / 1200),
        'baseline_stress': _calculate_baseline_stress(total_stress),
        'description': _describe_developmental_outcome(total_stress)
    }
    
    return {
        'total_stress': total_stress,
        'trait_breakdown': trait_breakdown,
        'severity': _categorize_total_stress(total_stress),
        'long_term_effects': long_term_effects
    }


def _categorize_trait_stress(stress: float) -> str:
    """Categorize individual trait stress level"""
    if stress < 20: return "Minimal conflict"
    elif stress < 40: return "Moderate pressure"
    elif stress < 60: return "High stress"
    elif stress < 80: return "Severe trauma"
    else: return "CRITICAL damage"


def _categorize_total_stress(total: float) -> str:
    """Categorize total developmental stress"""
    if total < 80: return "HEALTHY (aligned upbringing)"
    elif total < 150: return "MILD stress (normal pressures)"
    elif total < 250: return "MODERATE stress (difficult childhood)"
    elif total < 350: return "SEVERE stress (traumatic childhood)"
    else: return "CRITICAL stress (psychologically damaging)"


def _calculate_baseline_stress(total_stress: float) -> float:
    """Calculate permanent baseline stress from childhood trauma"""
    if total_stress < 80: return 0
    elif total_stress < 150: return 10
    elif total_stress < 250: return 30
    elif total_stress < 350: return 60
    else: return 100


def _describe_developmental_outcome(total_stress: float) -> str:
    """Narrative description of developmental outcome"""
    if total_stress < 80:
        return "Healthy development, well-adjusted adult"
    elif total_stress < 150:
        return "Minor childhood struggles, normal adult functioning"
    elif total_stress < 250:
        return "Difficult childhood left emotional scars, functional but wounded"
    elif total_stress < 350:
        return "Traumatic childhood caused lasting psychological damage"
    else:
        return "Severely damaged by childhood, prone to breakdowns throughout life"


# ============================================================================
# COMPLETE CHARACTER DEVELOPMENT
# ============================================================================

def develop_character_depc(genetic_dna: DNA,
                           culture_name: str,
                           is_noble: bool = False) -> Dict:
    """
    Complete DEPC development process: Genetics + Culture + Events
    
    This is the MAIN FUNCTION to call when creating a character.
    
    Args:
        genetic_dna: DNA object with genetic traits
        culture_name: Name of culture raising the child
        is_noble: Whether child is nobility
        
    Returns:
        Dict with:
            - depc_profile: DEPCProfile object
            - developmental_stress: Childhood stress analysis
            - development_history: Complete development data for narrative
    """
    
    # STAGE 1: Extract genetic tendencies (30% weight)
    genetic_tendencies = calculate_genetic_depc_tendencies(genetic_dna)
    
    # Get culture object
    if culture_name not in HEGEMON_CULTURE_DEPC:
        raise ValueError(f"Unknown culture: {culture_name}")
    culture = HEGEMON_CULTURE_DEPC[culture_name]
    
    # Calculate developmental stress (happens during childhood)
    developmental_stress = calculate_developmental_stress(
        genetic_tendencies,
        culture
    )
    
    # STAGE 2: Apply cultural shaping (50% weight)
    culturally_shaped = culture.shape_depc(genetic_tendencies)
    
    # STAGE 3: Generate and apply life events (20% weight)
    upbringing_events = generate_upbringing_events(culture_name, is_noble)
    final_depc_values = apply_upbringing_events(culturally_shaped, upbringing_events)
    
    # Create DEPC Profile
    depc_profile = DEPCProfile(
        dominance=final_depc_values['dominance'],
        extroversion=final_depc_values['extroversion'],
        patience=final_depc_values['patience'],
        conformity=final_depc_values['conformity']
    )
    
    # Store complete development history
    development_history = {
        'genetic_tendencies': genetic_tendencies,
        'culture': culture_name,
        'cultural_pressure': culture.depc_pressure,
        'culturally_shaped': culturally_shaped,
        'upbringing_events': upbringing_events,
        'final_depc': final_depc_values,
    }
    
    return {
        'depc_profile': depc_profile,
        'developmental_stress': developmental_stress,
        'development_history': development_history,
    }


# ============================================================================
# DERIVED ABILITIES FROM DEPC
# ============================================================================

def calculate_derived_abilities(depc: DEPCProfile) -> Dict[str, float]:
    """
    Calculate derived abilities from DEPC.
    
    Uses randomized means of DEPC pairs to simulate talent/aptitude variation.
    Two people with same DEPC can have different derived abilities.
    
    Args:
        depc: DEPCProfile object
        
    Returns:
        Dict with ability scores (1-100):
            - war: D + C (command + discipline)
            - diplomacy: E + C (charm + protocol)
            - intrigue: D + P (ambition + patience)
            - stewardship: P + C (detail + system)
            - learning: E + P (curiosity + focus)
            - prowess: D + E (aggression + energy)
            - piety: C + P (devotion + patience)
            - leadership: D + E + P (three-way)
            - innovation: E + (100-C) (curiosity + nonconformity)
    """
    
    def randomized_mean(val1: float, val2: float) -> float:
        """Calculate mean with ±20% random talent variation"""
        base = (val1 + val2) / 2
        talent_factor = random.gauss(1.0, 0.15)
        talent_factor = max(0.8, min(1.2, talent_factor))
        result = base * talent_factor
        return max(1, min(100, result))
    
    def randomized_mean_triple(val1: float, val2: float, val3: float) -> float:
        """Calculate three-way mean with talent variation"""
        base = (val1 + val2 + val3) / 3
        talent_factor = random.gauss(1.0, 0.15)
        talent_factor = max(0.8, min(1.2, talent_factor))
        result = base * talent_factor
        return max(1, min(100, result))
    
    return {
        'war': randomized_mean(depc.dominance, depc.conformity),
        'diplomacy': randomized_mean(depc.extroversion, depc.conformity),
        'intrigue': randomized_mean(depc.dominance, depc.patience),
        'stewardship': randomized_mean(depc.patience, depc.conformity),
        'learning': randomized_mean(depc.extroversion, depc.patience),
        'prowess': randomized_mean(depc.dominance, depc.extroversion),
        'piety': randomized_mean(depc.conformity, depc.patience),
        'leadership': randomized_mean_triple(depc.dominance, depc.extroversion, depc.patience),
        'innovation': randomized_mean(depc.extroversion, 100 - depc.conformity),
    }


def get_ability_expression(ability_raw: float, charisma: float) -> Tuple[float, str]:
    """
    Get ability expression (relative to base personality).
    
    Expression = how much the ability differs from baseline charisma.
    This determines if it's a strength, weakness, or average.
    
    Args:
        ability_raw: Raw ability score (1-100)
        charisma: Character's base charisma (DEPC mean)
        
    Returns:
        Tuple of (expression_value, rating_string)
    """
    
    expression = ability_raw - charisma
    
    if expression >= 30:
        rating = "LEGENDARY"
    elif expression >= 20:
        rating = "EXCEPTIONAL"
    elif expression >= 10:
        rating = "STRENGTH"
    elif expression >= 5:
        rating = "Above Average"
    elif expression >= -4:
        rating = "Average"
    elif expression >= -9:
        rating = "Below Average"
    elif expression >= -19:
        rating = "WEAKNESS"
    elif expression >= -29:
        rating = "MAJOR WEAKNESS"
    else:
        rating = "CATASTROPHIC"
    
    return (expression, rating)


# ============================================================================
# STRESS SYSTEM (STANDARD DEVIATION MODEL)
# ============================================================================

class StressSystem:
    """
    Calculate stress as standard deviations from DEPC baseline.
    
    Stress occurs when character must act outside their natural DEPC range.
    Uses statistical z-scores to determine psychological strain.
    """
    
    def __init__(self, character_depc: DEPCProfile, genetic_dna: DNA):
        """
        Initialize stress system for a character.
        
        Args:
            character_depc: Character's DEPC profile
            genetic_dna: Character's DNA (for flexibility calculation)
        """
        self.character = character_depc
        self.flexibility = self._calculate_flexibility(genetic_dna)
    
    def _calculate_flexibility(self, dna: DNA) -> Dict[str, float]:
        """
        Calculate standard deviation (flexibility) for each DEPC trait.
        
        Higher SD = More flexible personality (can adapt more easily)
        Lower SD = More rigid personality (harder to act differently)
        
        Factors:
        - Mental Stability (genetic): Higher = more flexible
        - Patience (DEPC): Higher = more flexible
        - Charisma (DEPC): Higher = wider comfort zone
        - Intelligence (genetic): Higher = can "fake it" better
        
        Args:
            dna: DNA object with genetic traits
            
        Returns:
            Dict with SD values for each DEPC trait
        """
        
        # Base standard deviations for each trait
        base_sd = {
            'dominance': 15.0,     # Most rigid (hard to fake)
            'extroversion': 12.0,  # Moderately flexible
            'patience': 10.0,      # More flexible
            'conformity': 18.0,    # Very rigid (moral/cultural core)
        }
        
        # Get modifying factors from genetics and DEPC
        stability = dna.get_phenotype(19) / 7.5  # 0.0 to 2.0
        intelligence = dna.get_phenotype(16) / 15  # 0.0 to 1.0
        patience_factor = self.character.patience / 50  # 0.0 to 2.0
        charisma_factor = self.character.charisma / 50  # 0.0 to 2.0
        
        # Combined flexibility multiplier
        flexibility_mult = (
            stability * 0.4 +
            patience_factor * 0.3 +
            charisma_factor * 0.2 +
            intelligence * 0.1
        )
        
        # Clamp to reasonable range
        flexibility_mult = max(0.5, min(2.5, flexibility_mult))
        
        # Apply to base SDs
        return {
            trait: base * flexibility_mult
            for trait, base in base_sd.items()
        }
    
    def calculate_situational_stress(self,
                                     required_depc: Dict[str, float],
                                     duration_months: float = 1.0) -> Dict:
        """
        Calculate stress from having to act outside natural DEPC range.
        
        Stress = Σ(z-scores²) × duration × 100
        Where z-score = (required - natural) / standard_deviation
        
        Args:
            required_depc: Required DEPC values for situation
            duration_months: How long situation lasts
            
        Returns:
            Dict with:
                - total_stress: Total stress points
                - z_scores: Individual z-scores per trait
                - severity: Stress severity level
                - effects: Mechanical effects
        """
        
        total_z_squared = 0
        z_scores = {}
        
        for trait, required_value in required_depc.items():
            natural_value = getattr(self.character, trait)
            sd = self.flexibility[trait]
            
            # Calculate z-score (standard deviations from natural)
            z_score = (required_value - natural_value) / sd
            z_squared = z_score ** 2
            
            z_scores[trait] = {
                'z_score': z_score,
                'z_squared': z_squared,
                'interpretation': self._interpret_z_score(z_score)
            }
            
            total_z_squared += z_squared
        
        # Total stress = sum of squared z-scores × duration × scale
        base_stress = total_z_squared * 100
        total_stress = base_stress * duration_months
        
        return {
            'total_stress': total_stress,
            'z_scores': z_scores,
            'severity': self._get_severity(total_stress),
            'effects': self._get_effects(total_stress)
        }
    
    def _interpret_z_score(self, z: float) -> str:
        """Interpret z-score magnitude"""
        abs_z = abs(z)
        if abs_z < 0.5:
            return "Within comfort zone"
        elif abs_z < 1.0:
            return "Mild adjustment (manageable)"
        elif abs_z < 2.0:
            return "Significant adjustment (stressful)"
        elif abs_z < 3.0:
            return "Extreme adjustment (very stressful)"
        else:
            return "Beyond normal range (psychological crisis)"
    
    def _get_severity(self, stress: float) -> str:
        """Categorize stress level"""
        if stress < 100: return "MINIMAL"
        elif stress < 300: return "MODERATE"
        elif stress < 600: return "HIGH"
        elif stress < 1000: return "SEVERE"
        else: return "CRITICAL"
    
    def _get_effects(self, stress: float) -> Dict:
        """Get mechanical effects of stress"""
        if stress < 50:
            return {
                'ability_penalty': 0,
                'description': 'No significant effects'
            }
        elif stress < 100:
            return {
                'ability_penalty': -10,
                'description': 'Minor discomfort, slight performance loss'
            }
        elif stress < 200:
            return {
                'ability_penalty': -25,
                'health_damage': 5,
                'description': 'Noticeable strain, moderate performance loss'
            }
        elif stress < 300:
            return {
                'ability_penalty': -50,
                'health_damage': 15,
                'stability_damage': 10,
                'breakdown_risk': 0.25,
                'description': 'Severe stress, high breakdown risk'
            }
        else:
            return {
                'ability_penalty': -75,
                'health_damage': 30,
                'stability_damage': 25,
                'breakdown_risk': 0.75,
                'description': 'CRITICAL - psychological break imminent'
            }


