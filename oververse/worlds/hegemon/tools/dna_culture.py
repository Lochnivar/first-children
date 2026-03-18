"""
Cultural Preferences System for DNA Simulation

Implements the three-layer mate selection system:
1. Cultural Preferences (baseline)
2. First Children Interference (future implementation)
3. Political Override (future implementation)

Based on the design document in HEGEMON-DIALOG.md
"""

from typing import Dict, List, Optional, Callable
from .dna_core import DNA


class Culture:
    """
    Represents a culture with specific trait preferences for mate selection
    """
    
    def __init__(self, name: str, preferences: Dict[int, Callable], mate_selection_pressure: float = 0.7):
        """
        Initialize a culture
        
        Args:
            name: Culture name
            preferences: Dictionary mapping trait_index -> scoring_function
                        Scoring functions take a phenotype value (0-15) and return a score
            mate_selection_pressure: 0.0-1.0, how much culture matters in mate selection (default: 0.7)
        """
        self.name = name
        self.preferences = preferences  # trait_index -> scoring function
        self.mate_selection_pressure = mate_selection_pressure  # 0.0-1.0, how much culture matters
    
    def score_mate(self, candidate_dna: DNA) -> float:
        """
        Score a potential mate based on cultural preferences
        
        Args:
            candidate_dna: DNA of the candidate
            
        Returns:
            Total score (higher = better match for this culture)
        """
        total_score = 0.0
        
        for trait_index, scoring_func in self.preferences.items():
            try:
                phenotype = candidate_dna.get_phenotype(trait_index)
                trait_score = scoring_func(phenotype)
                total_score += trait_score
            except (KeyError, IndexError, ValueError):
                # Skip traits that don't exist or invalid values
                continue
        
        return total_score
    
    def select_mate(self, person_dna: DNA, available_mates: List[DNA], 
                   political_override: Optional[DNA] = None) -> DNA:
        """
        Select mate with cultural preferences or political override
        
        Args:
            person_dna: DNA of the person selecting a mate
            available_mates: List of potential mate DNA
            political_override: Optional forced match (for arranged marriages)
            
        Returns:
            Selected mate DNA
        """
        if political_override:
            return political_override
        
        if not available_mates:
            raise ValueError("No available mates to select from")
        
        # Score all candidates
        scored_candidates = []
        for mate_dna in available_mates:
            cultural_score = self.score_mate(mate_dna)
            scored_candidates.append((mate_dna, cultural_score))
        
        # Apply cultural selection pressure
        # High pressure = strongly prefer high-scoring candidates
        # Low pressure = more random selection
        if self.mate_selection_pressure > 0.5:
            # Strong preference - pick from top candidates
            scored_candidates.sort(key=lambda x: x[1], reverse=True)
            # Take top 30% weighted by score
            top_count = max(1, int(len(scored_candidates) * 0.3))
            top_candidates = scored_candidates[:top_count]
            
            # Weight selection by score
            import random
            total_score = sum(score for _, score in top_candidates)
            if total_score > 0:
                r = random.random() * total_score
                cumulative = 0
                for mate_dna, score in top_candidates:
                    cumulative += score
                    if r <= cumulative:
                        return mate_dna
                return top_candidates[0][0]  # Fallback
            else:
                return random.choice(top_candidates)[0]
        else:
            # Moderate/weak preference - weighted random
            import random
            # Normalize scores to positive range
            min_score = min(score for _, score in scored_candidates)
            normalized = [(dna, score - min_score + 1) for dna, score in scored_candidates]
            total_score = sum(score for _, score in normalized)
            
            if total_score > 0:
                r = random.random() * total_score
                cumulative = 0
                for mate_dna, score in normalized:
                    cumulative += score
                    if r <= cumulative:
                        return mate_dna
                return normalized[0][0]  # Fallback
            else:
                return random.choice(available_mates)


def create_culture_from_dict(culture_dict: Dict) -> Culture:
    """
    Create a Culture instance from a dictionary definition
    
    Args:
        culture_dict: Dictionary with 'name', 'preferences', 'mate_selection_pressure'
        
    Returns:
        Culture instance
    """
    culture = Culture(
        name=culture_dict['name'],
        preferences=culture_dict.get('preferences', {})
    )
    culture.mate_selection_pressure = culture_dict.get('mate_selection_pressure', 0.7)
    return culture
