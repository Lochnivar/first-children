"""
Core DNA class and breeding functions

This module contains the DNA class and core genetic simulation functions,
with all fixes from the analysis applied.
"""

import random
from typing import Tuple, Dict, Optional
from dataclasses import dataclass

# Import configuration constants
from .dna_config import (
    NUM_TRAITS, NUMERIC_TRAITS, KEY_TRAITS,
    SEVERE_INBREEDING_THRESHOLD, SIGNIFICANT_INBREEDING_THRESHOLD, MODERATE_INBREEDING_THRESHOLD
)

# Import trait definitions
from .dna_traits import TRAIT_DEFINITIONS


class DNAError(Exception):
    """Base exception for DNA-related errors"""
    pass


class InvalidTraitIndexError(DNAError):
    """Raised when trait index is out of valid range"""
    pass


class InvalidAlleleValueError(DNAError):
    """Raised when allele value is out of valid range"""
    pass


class InvalidHexStringError(DNAError):
    """Raised when hex string is malformed"""
    pass


@dataclass
class DNA:
    """
    256-bit DNA encoding (32 traits × 8 bits each)
    Each trait has two 4-bit alleles (maternal and paternal)
    
    This is a simplified genetic model for fantasy world-building.
    Real genetics is more complex (polygenic traits, epistasis, etc.)
    """
    # Store as two 128-bit integers (maternal and paternal alleles)
    maternal: int  # 128 bits
    paternal: int  # 128 bits
    
    def __init__(self, maternal: Optional[int] = None, paternal: Optional[int] = None):
        """
        Initialize DNA
        
        Args:
            maternal: Maternal allele bits (128-bit int), None for random
            paternal: Paternal allele bits (128-bit int), None for random
        """
        if maternal is None:
            # Generate random DNA
            self.maternal = random.getrandbits(128)
            self.paternal = random.getrandbits(128)
        else:
            self.maternal = maternal
            self.paternal = paternal
    
    def _validate_trait_index(self, trait_index: int):
        """Validate that trait index is in valid range"""
        if not (0 <= trait_index < NUM_TRAITS):
            raise InvalidTraitIndexError(
                f"Trait index must be 0-{NUM_TRAITS-1}, got {trait_index}"
            )
    
    def _validate_allele_value(self, allele: int):
        """Validate that allele value is in valid range (0-15)"""
        if not (0 <= allele <= 0xF):
            raise InvalidAlleleValueError(
                f"Allele value must be 0-15 (0x0-0xF), got {allele}"
            )
    
    def get_allele_pair(self, trait_index: int) -> Tuple[int, int]:
        """
        Get both alleles for a specific trait (0-31)
        
        Args:
            trait_index: Trait index (0-31)
            
        Returns:
            Tuple of (maternal_allele, paternal_allele), each 0-15
            
        Raises:
            InvalidTraitIndexError: If trait_index is out of range
        """
        self._validate_trait_index(trait_index)
        
        shift = trait_index * 4
        mask = 0xF  # 4 bits
        
        maternal_allele = (self.maternal >> shift) & mask
        paternal_allele = (self.paternal >> shift) & mask
        
        return (maternal_allele, paternal_allele)
    
    def set_allele_pair(self, trait_index: int, maternal_allele: int, paternal_allele: int):
        """
        Set both alleles for a specific trait
        
        Args:
            trait_index: Trait index (0-31)
            maternal_allele: Maternal allele value (0-15)
            paternal_allele: Paternal allele value (0-15)
            
        Raises:
            InvalidTraitIndexError: If trait_index is out of range
            InvalidAlleleValueError: If allele values are out of range
        """
        self._validate_trait_index(trait_index)
        self._validate_allele_value(maternal_allele)
        self._validate_allele_value(paternal_allele)
        
        shift = trait_index * 4
        mask = 0xF
        
        # Clear existing bits
        clear_mask = ~(mask << shift)
        self.maternal = (self.maternal & clear_mask) | (maternal_allele << shift)
        self.paternal = (self.paternal & clear_mask) | (paternal_allele << shift)
    
    def get_phenotype(self, trait_index: int) -> int:
        """
        Get expressed phenotype for a trait based on dominance
        
        Args:
            trait_index: Trait index (0-31)
            
        Returns:
            Phenotype value (0-15) - the expressed trait
            
        Raises:
            InvalidTraitIndexError: If trait_index is out of range
            KeyError: If trait definitions are missing
        """
        self._validate_trait_index(trait_index)
        
        maternal, paternal = self.get_allele_pair(trait_index)
        
        # Get dominance values from trait definitions
        if not TRAIT_DEFINITIONS:
            raise DNAError("TRAIT_DEFINITIONS not loaded")
        
        trait_def = TRAIT_DEFINITIONS[trait_index]
        mat_dom = trait_def['values'][maternal]['dominance']
        pat_dom = trait_def['values'][paternal]['dominance']
        
        # Higher dominance wins
        if mat_dom > pat_dom:
            return maternal
        elif pat_dom > mat_dom:
            return paternal
        else:
            # Equal dominance - average for numeric traits, random for others
            if trait_index in NUMERIC_TRAITS:
                return (maternal + paternal) // 2
            else:
                return random.choice([maternal, paternal])
    
    def to_hex(self) -> str:
        """
        Convert to hex string for display and storage
        
        Returns:
            Hex string in format "MATERNAL_PATERNAL" (64 hex chars each)
        """
        return f"{self.maternal:032X}_{self.paternal:032X}"
    
    @classmethod
    def from_hex(cls, hex_string: str) -> 'DNA':
        """
        Create DNA from hex string
        
        Args:
            hex_string: Hex string in format "MATERNAL_PATERNAL"
            
        Returns:
            DNA instance
            
        Raises:
            InvalidHexStringError: If hex string is malformed
        """
        try:
            parts = hex_string.split('_')
            if len(parts) != 2:
                raise InvalidHexStringError(
                    f"Hex string must contain exactly one underscore, got {len(parts)-1}"
                )
            
            maternal = int(parts[0], 16)
            paternal = int(parts[1], 16)
            
            # Validate that values fit in 128 bits
            max_value = (1 << 128) - 1
            if maternal > max_value or paternal > max_value:
                raise InvalidHexStringError(
                    f"Hex values too large (must be ≤ 128 bits)"
                )
            
            return cls(maternal, paternal)
        except ValueError as e:
            raise InvalidHexStringError(f"Invalid hex string: {e}") from e


def create_child(parent1: DNA, parent2: DNA, mutation_rate: float = 0.01) -> DNA:
    """
    Create child DNA from two parents using Mendelian inheritance
    
    This implements a simplified Mendelian model where:
    - Child randomly inherits one allele from each parent
    - Mutations can flip random bits (simplified model)
    - Values are clamped to valid range (0-15)
    
    Args:
        parent1: First parent's DNA
        parent2: Second parent's DNA
        mutation_rate: Chance of mutation per allele (default 1%)
        
    Returns:
        Child DNA
    """
    if mutation_rate < 0 or mutation_rate > 1:
        raise ValueError(f"Mutation rate must be 0.0-1.0, got {mutation_rate}")
    
    child = DNA(maternal=0, paternal=0)
    
    for trait_index in range(NUM_TRAITS):
        # Get parent alleles
        p1_mat, p1_pat = parent1.get_allele_pair(trait_index)
        p2_mat, p2_pat = parent2.get_allele_pair(trait_index)
        
        # Child randomly inherits one allele from each parent
        from_parent1 = random.choice([p1_mat, p1_pat])
        from_parent2 = random.choice([p2_mat, p2_pat])
        
        # Apply mutations (simplified model - flip random bit)
        if random.random() < mutation_rate:
            # Flip random bit in parent1's contribution
            bit_to_flip = random.randint(0, 3)
            from_parent1 ^= (1 << bit_to_flip)
        
        if random.random() < mutation_rate:
            # Flip random bit in parent2's contribution
            bit_to_flip = random.randint(0, 3)
            from_parent2 ^= (1 << bit_to_flip)
        
        # Ensure values stay in 0-15 range (clamp after mutation)
        from_parent1 &= 0xF
        from_parent2 &= 0xF
        
        # Set child's alleles
        child.set_allele_pair(trait_index, from_parent1, from_parent2)
    
    return child


def calculate_genetic_similarity(parent1: DNA, parent2: DNA) -> float:
    """
    Calculate genetic similarity between parents (0.0 to 1.0)
    
    This measures allele similarity (identity by state), not true inbreeding
    coefficient which would require tracking actual family relationships.
    High values indicate similar genetics (potential inbreeding risk).
    
    Args:
        parent1: First parent's DNA
        parent2: Second parent's DNA
        
    Returns:
        Similarity score (0.0 = completely different, 1.0 = identical)
    """
    matches = 0
    total = 0
    
    for trait_index in range(NUM_TRAITS):
        p1_mat, p1_pat = parent1.get_allele_pair(trait_index)
        p2_mat, p2_pat = parent2.get_allele_pair(trait_index)
        
        # Check all combinations (2×2 = 4 comparisons)
        if p1_mat == p2_mat: matches += 1
        if p1_mat == p2_pat: matches += 1
        if p1_pat == p2_mat: matches += 1
        if p1_pat == p2_pat: matches += 1
        
        total += 4
    
    return matches / total


def predict_offspring_probabilities(parent1: DNA, parent2: DNA, trait_index: int) -> Dict[int, float]:
    """
    Calculate Punnett square probabilities for a specific trait
    
    This predicts the probability of each phenotype in offspring,
    considering all possible allele combinations and dominance.
    
    Args:
        parent1: First parent's DNA
        parent2: Second parent's DNA
        trait_index: Trait index to analyze (0-31)
        
    Returns:
        Dictionary of {phenotype: probability} where probability is 0.0-1.0
    """
    if not TRAIT_DEFINITIONS:
        raise DNAError("TRAIT_DEFINITIONS not loaded")
    
    p1_mat, p1_pat = parent1.get_allele_pair(trait_index)
    p2_mat, p2_pat = parent2.get_allele_pair(trait_index)
    
    # All possible combinations (2×2 = 4 outcomes)
    outcomes = [
        (p1_mat, p2_mat),
        (p1_mat, p2_pat),
        (p1_pat, p2_mat),
        (p1_pat, p2_pat),
    ]
    
    # Count genotypes (normalize order for comparison)
    genotype_counts = {}
    for genotype in outcomes:
        normalized = tuple(sorted(genotype))
        genotype_counts[normalized] = genotype_counts.get(normalized, 0) + 1
    
    # Convert to phenotypes using dominance rules
    phenotype_probs = {}
    trait_def = TRAIT_DEFINITIONS[trait_index]
    
    for genotype, count in genotype_counts.items():
        # Determine expressed phenotype based on dominance
        mat_dom = trait_def['values'][genotype[0]]['dominance']
        pat_dom = trait_def['values'][genotype[1]]['dominance']
        
        if mat_dom > pat_dom:
            phenotype = genotype[0]
        elif pat_dom > mat_dom:
            phenotype = genotype[1]
        else:
            # Equal dominance - average if numeric, split probability otherwise
            if trait_index in NUMERIC_TRAITS:
                phenotype = (genotype[0] + genotype[1]) // 2
            else:
                # For non-numeric with equal dominance, split probability between both
                for allele in genotype:
                    phenotype_probs[allele] = phenotype_probs.get(allele, 0) + count / 8.0
                continue
        
        phenotype_probs[phenotype] = phenotype_probs.get(phenotype, 0) + count / 4.0
    
    return phenotype_probs


def describe_character(dna: DNA, name: str = "Character") -> str:
    """
    Generate detailed character description from DNA
    
    Args:
        dna: DNA instance to describe
        name: Character name
        
    Returns:
        Formatted string description
    """
    if not TRAIT_DEFINITIONS:
        raise DNAError("TRAIT_DEFINITIONS not loaded")
    
    lines = [f"\n{'='*70}"]
    lines.append(f"{name}")
    lines.append(f"DNA: {dna.to_hex()}")
    lines.append(f"{'='*70}\n")
    
    # Physical traits (0-7)
    lines.append("PHYSICAL TRAITS:")
    for i in range(8):
        trait_def = TRAIT_DEFINITIONS[i]
        mat, pat = dna.get_allele_pair(i)
        phenotype = dna.get_phenotype(i)
        
        mat_name = trait_def['values'][mat]['name']
        pat_name = trait_def['values'][pat]['name']
        phen_name = trait_def['values'][phenotype]['name']
        is_marker = trait_def['values'][phenotype]['marker']
        
        marker = " ★" if is_marker else ""
        
        if mat == pat:
            lines.append(f"  {trait_def['name']}: {phen_name} (pure){marker}")
            lines.append(f"    Genotype: {mat_name}/{pat_name}")
        else:
            lines.append(f"  {trait_def['name']}: {phen_name}{marker}")
            lines.append(f"    Genotype: {mat_name}/{pat_name}")
            if phenotype == mat:
                lines.append(f"    Carries: {pat_name} (recessive)")
            else:
                lines.append(f"    Carries: {mat_name} (recessive)")
    
    # Health traits (8-15)
    lines.append("\nHEALTH TRAITS:")
    for i in range(8, 16):
        trait_def = TRAIT_DEFINITIONS[i]
        mat, pat = dna.get_allele_pair(i)
        phenotype = dna.get_phenotype(i)
        
        phen_name = trait_def['values'][phenotype]['name']
        is_marker = trait_def['values'][phenotype]['marker']
        marker = " ★" if is_marker else ""
        
        lines.append(f"  {trait_def['name']}: {phen_name}{marker}")
    
    # Mental traits (16-23)
    lines.append("\nMENTAL TRAITS:")
    for i in range(16, 24):
        trait_def = TRAIT_DEFINITIONS[i]
        mat, pat = dna.get_allele_pair(i)
        phenotype = dna.get_phenotype(i)
        
        phen_name = trait_def['values'][phenotype]['name']
        is_marker = trait_def['values'][phenotype]['marker']
        marker = " ★" if is_marker else ""
        
        lines.append(f"  {trait_def['name']}: {phen_name}{marker}")
    
    # Magical traits (24-31)
    lines.append("\nMAGICAL/SPECIAL TRAITS:")
    for i in range(24, 32):
        trait_def = TRAIT_DEFINITIONS[i]
        mat, pat = dna.get_allele_pair(i)
        phenotype = dna.get_phenotype(i)
        
        phen_name = trait_def['values'][phenotype]['name']
        is_marker = trait_def['values'][phenotype]['marker']
        marker = " ★" if is_marker else ""
        
        if phenotype > 0:  # Only show if not "None"
            lines.append(f"  {trait_def['name']}: {phen_name}{marker}")
    
    return '\n'.join(lines)


def describe_breeding_analysis(parent1: DNA, parent2: DNA, 
                               parent1_name: str = "Parent 1", 
                               parent2_name: str = "Parent 2") -> str:
    """
    Analyze potential offspring from two parents
    
    Args:
        parent1: First parent's DNA
        parent2: Second parent's DNA
        parent1_name: Name of first parent (for display)
        parent2_name: Name of second parent (for display)
        
    Returns:
        Formatted string analysis
    """
    if not TRAIT_DEFINITIONS:
        raise DNAError("TRAIT_DEFINITIONS not loaded")
    
    from .dna_config import KEY_TRAITS, SEVERE_INBREEDING_THRESHOLD, SIGNIFICANT_INBREEDING_THRESHOLD, MODERATE_INBREEDING_THRESHOLD
    
    lines = [f"\n{'='*70}"]
    lines.append(f"BREEDING ANALYSIS: {parent1_name} × {parent2_name}")
    lines.append(f"{'='*70}\n")
    
    # Calculate genetic similarity (renamed from inbreeding coefficient)
    similarity = calculate_genetic_similarity(parent1, parent2)
    lines.append(f"Genetic Similarity: {similarity*100:.1f}%")
    
    if similarity > SEVERE_INBREEDING_THRESHOLD:
        lines.append("  ⚠⚠ SEVERE INBREEDING - High mutation risk")
    elif similarity > SIGNIFICANT_INBREEDING_THRESHOLD:
        lines.append("  ⚠ SIGNIFICANT INBREEDING - Elevated mutation risk")
    elif similarity > MODERATE_INBREEDING_THRESHOLD:
        lines.append("  ⚠ MODERATE INBREEDING - Some risk")
    else:
        lines.append("  ✓ Low inbreeding risk")
    
    lines.append(f"\nRecommended mutation rate: {min(0.10, similarity * 0.15):.2%}\n")
    
    # Analyze key traits
    lines.append("KEY TRAIT PREDICTIONS:")
    for trait_index in KEY_TRAITS:
        trait_def = TRAIT_DEFINITIONS[trait_index]
        probs = predict_offspring_probabilities(parent1, parent2, trait_index)
        
        lines.append(f"\n  {trait_def['name']}:")
        for phenotype, probability in sorted(probs.items(), key=lambda x: -x[1]):
            phen_name = trait_def['values'][phenotype]['name']
            is_marker = trait_def['values'][phenotype]['marker']
            marker = " ★" if is_marker else ""
            lines.append(f"    {probability*100:5.1f}% - {phen_name}{marker}")
    
    return '\n'.join(lines)

