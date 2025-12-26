"""
ASCII art family tree visualization

This module provides functions to generate ASCII art family trees
from database relationships.
"""

from typing import Dict, List, Optional
from .dna_database import CharacterDatabase
from .dna_core import describe_character


class FamilyTree:
    """
    Generates ASCII art family trees from database
    """
    
    def __init__(self, database: CharacterDatabase):
        """
        Initialize with database connection
        
        Args:
            database: CharacterDatabase instance
        """
        self.db = database
    
    def generate_ascii_tree(self, char_id: int, 
                           max_generations_up: int = 3,
                           max_generations_down: int = 3,
                           include_names_only: bool = False) -> str:
        """
        Generate ASCII art family tree
        
        Args:
            char_id: Root character ID (center of tree)
            max_generations_up: Maximum generations above (ancestors)
            max_generations_down: Maximum generations below (descendants)
            include_names_only: If True, show only names (compact mode)
            
        Returns:
            ASCII art tree as string
        """
        # Get ancestors and descendants
        ancestors = self.db.get_ancestors(char_id, max_generations_up)
        descendants = self.db.get_descendants(char_id, max_generations_down)
        
        # Build tree structure
        lines = []
        lines.append("=" * 70)
        root_char = self.db.load_character(char_id)
        if root_char:
            lines.append(f"FAMILY TREE: {root_char['name']} (ID: {char_id})")
        else:
            lines.append(f"FAMILY TREE: Character ID {char_id}")
        lines.append("=" * 70)
        lines.append("")
        
        # Display ancestors (above)
        if ancestors:
            max_ancestor_gen = max(ancestors.keys())
            for gen in sorted([g for g in ancestors.keys() if g > 0], reverse=True):
                gen_chars = ancestors[gen]
                lines.append(f"Generation -{gen} (Ancestors):")
                for char in gen_chars:
                    if include_names_only:
                        lines.append(f"  {char['name']}")
                    else:
                        lines.append(f"  {char['name']} (ID: {char['id']}, Year: {char['birth_year'] or '?'})")
                lines.append("")
        
        # Display root character
        if root_char:
            lines.append("─" * 70)
            if include_names_only:
                lines.append(f"★ {root_char['name']} (ROOT)")
            else:
                lines.append(f"★ {root_char['name']} (ID: {root_char['id']}, Year: {root_char['birth_year'] or '?'})")
            lines.append("─" * 70)
            lines.append("")
        else:
            lines.append("★ [Root character not found]")
            lines.append("")
        
        # Display descendants (below)
        if descendants:
            for gen in sorted([g for g in descendants.keys() if g > 0]):
                gen_chars = descendants[gen]
                lines.append(f"Generation +{gen} (Descendants):")
                for char in gen_chars:
                    if include_names_only:
                        lines.append(f"  {char['name']}")
                    else:
                        lines.append(f"  {char['name']} (ID: {char['id']}, Year: {char['birth_year'] or '?'})")
                lines.append("")
        
        return "\n".join(lines)
    
    def generate_detailed_tree(self, char_id: int,
                              max_generations: int = 2) -> str:
        """
        Generate detailed tree with character descriptions
        
        Args:
            char_id: Root character ID
            max_generations: Maximum generations to show (both up and down)
            
        Returns:
            Detailed tree with character descriptions
        """
        lines = []
        lines.append("=" * 70)
        root_char = self.db.load_character(char_id)
        if root_char:
            lines.append(f"DETAILED FAMILY TREE: {root_char['name']}")
        lines.append("=" * 70)
        lines.append("")
        
        # Get ancestors
        ancestors = self.db.get_ancestors(char_id, max_generations)
        if ancestors:
            lines.append("ANCESTORS:")
            lines.append("")
            for gen in sorted([g for g in ancestors.keys() if g > 0], reverse=True):
                gen_chars = ancestors[gen]
                lines.append(f"  Generation -{gen}:")
                for char in gen_chars:
                    dna = self.db.load_dna(char['id'])
                    if dna:
                        # Get key traits summary
                        from .dna_traits import TRAIT_DEFINITIONS
                        if dna and TRAIT_DEFINITIONS:
                            eyes = dna.get_phenotype(0)
                            hair = dna.get_phenotype(1)
                            magic = dna.get_phenotype(24)
                            eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
                            hair_name = TRAIT_DEFINITIONS[1]['values'][hair]['name']
                            magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
                            lines.append(f"    {char['name']}: {eyes_name} eyes, {hair_name} hair, {magic_name} magic")
                        else:
                            lines.append(f"    {char['name']}")
                    else:
                        lines.append(f"    {char['name']}")
                lines.append("")
        
        # Root character
        if root_char:
            lines.append("─" * 70)
            lines.append(f"ROOT: {root_char['name']}")
            lines.append("─" * 70)
            dna = self.db.load_dna(char_id)
            if dna:
                # Show key traits
                from .dna_traits import TRAIT_DEFINITIONS
                if TRAIT_DEFINITIONS:
                    eyes = dna.get_phenotype(0)
                    hair = dna.get_phenotype(1)
                    magic = dna.get_phenotype(24)
                    stability = dna.get_phenotype(19)
                    eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
                    hair_name = TRAIT_DEFINITIONS[1]['values'][hair]['name']
                    magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
                    stability_name = TRAIT_DEFINITIONS[19]['values'][stability]['name']
                    lines.append(f"  Eyes: {eyes_name}, Hair: {hair_name}")
                    lines.append(f"  Magic: {magic_name}, Stability: {stability_name}")
            lines.append("")
        
        # Get descendants
        descendants = self.db.get_descendants(char_id, max_generations)
        if descendants:
            lines.append("DESCENDANTS:")
            lines.append("")
            for gen in sorted([g for g in descendants.keys() if g > 0]):
                gen_chars = descendants[gen]
                lines.append(f"  Generation +{gen}:")
                for char in gen_chars:
                    dna = self.db.load_dna(char['id'])
                    if dna:
                        from .dna_traits import TRAIT_DEFINITIONS
                        if TRAIT_DEFINITIONS:
                            eyes = dna.get_phenotype(0)
                            hair = dna.get_phenotype(1)
                            magic = dna.get_phenotype(24)
                            eyes_name = TRAIT_DEFINITIONS[0]['values'][eyes]['name']
                            hair_name = TRAIT_DEFINITIONS[1]['values'][hair]['name']
                            magic_name = TRAIT_DEFINITIONS[24]['values'][magic]['name']
                            lines.append(f"    {char['name']}: {eyes_name} eyes, {hair_name} hair, {magic_name} magic")
                        else:
                            lines.append(f"    {char['name']}")
                    else:
                        lines.append(f"    {char['name']}")
                lines.append("")
        
        return "\n".join(lines)
    
    def generate_compact_tree(self, char_id: int, 
                            max_generations: int = 4) -> str:
        """
        Generate compact vertical tree
        
        Args:
            char_id: Root character ID
            max_generations: Maximum generations to show
            
        Returns:
            Compact vertical tree
        """
        # Get all relatives
        ancestors = self.db.get_ancestors(char_id, max_generations)
        descendants = self.db.get_descendants(char_id, max_generations)
        
        lines = []
        root_char = self.db.load_character(char_id)
        root_name = root_char['name'] if root_char else f"ID {char_id}"
        
        # Build vertical tree
        # Ancestors (top)
        for gen in sorted([g for g in ancestors.keys() if g > 0], reverse=True):
            gen_chars = ancestors[gen]
            names = [char['name'] for char in gen_chars]
            lines.append(f"{'  ' * (max_generations - gen)}┌─ {' / '.join(names)}")
        
        # Root (center)
        if root_char:
            try:
                lines.append(f"★ {root_name}")
            except UnicodeEncodeError:
                lines.append(f"* {root_name}")  # Fallback for non-Unicode terminals
        else:
            try:
                lines.append(f"★ [ID {char_id}]")
            except UnicodeEncodeError:
                lines.append(f"* [ID {char_id}]")
        
        # Descendants (bottom)
        for gen in sorted([g for g in descendants.keys() if g > 0]):
            gen_chars = descendants[gen]
            names = [char['name'] for char in gen_chars]
            lines.append(f"{'  ' * gen}└─ {' / '.join(names)}")
        
        return "\n".join(lines)

