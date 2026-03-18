"""
SQLite database support for character and family persistence

This module provides database functionality for storing characters, their DNA,
family relationships, and retrieving them for analysis and visualization.
"""

import sqlite3
from typing import Optional, List, Dict, Tuple
from datetime import datetime
from pathlib import Path

from .dna_core import DNA


class CharacterDatabase:
    """
    SQLite database for storing characters and family relationships
    """
    
    def __init__(self, db_path: str = "characters.db"):
        """
        Initialize or connect to database
        
        Args:
            db_path: Path to SQLite database file
        """
        self.db_path = db_path
        self._init_database()
    
    def _init_database(self):
        """Create database tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Characters table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS characters (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    first_name TEXT,
                    family_name TEXT,
                    dna_hex TEXT NOT NULL,
                    parent1_id INTEGER,
                    parent2_id INTEGER,
                    birth_year INTEGER,
                    culture TEXT,
                    is_noble INTEGER DEFAULT 0,
                    burg_id INTEGER,
                    burg_name TEXT,
                    state_name TEXT,
                    depc_dominance REAL,
                    depc_extroversion REAL,
                    depc_patience REAL,
                    depc_conformity REAL,
                    depc_charisma REAL,
                    developmental_stress REAL,
                    stress_severity TEXT,
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (parent1_id) REFERENCES characters(id),
                    FOREIGN KEY (parent2_id) REFERENCES characters(id)
                )
            """)
            
            # Create index for faster parent lookups
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_parent1 ON characters(parent1_id)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_parent2 ON characters(parent2_id)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_burg_id ON characters(burg_id)
            """)
            cursor.execute("""
                CREATE INDEX IF NOT EXISTS idx_culture ON characters(culture)
            """)
            
            # Migrate existing tables to add new columns if they don't exist
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN first_name TEXT")
            except sqlite3.OperationalError:
                pass  # Column already exists
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN family_name TEXT")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN culture TEXT")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN is_noble INTEGER DEFAULT 0")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN burg_id INTEGER")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN burg_name TEXT")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN state_name TEXT")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN depc_dominance REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN depc_extroversion REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN depc_patience REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN depc_conformity REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN depc_charisma REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN developmental_stress REAL")
            except sqlite3.OperationalError:
                pass
            
            try:
                cursor.execute("ALTER TABLE characters ADD COLUMN stress_severity TEXT")
            except sqlite3.OperationalError:
                pass
            
            conn.commit()
    
    def save_character(self, name: str, dna: DNA, 
                       parent1_id: Optional[int] = None,
                       parent2_id: Optional[int] = None,
                       birth_year: Optional[int] = None,
                       first_name: Optional[str] = None,
                       family_name: Optional[str] = None,
                       culture: Optional[str] = None,
                       is_noble: bool = False,
                       burg_id: Optional[int] = None,
                       burg_name: Optional[str] = None,
                       state_name: Optional[str] = None,
                       depc_profile: Optional[object] = None,
                       developmental_stress: Optional[float] = None,
                       stress_severity: Optional[str] = None,
                       notes: Optional[str] = None) -> int:
        """
        Save a character to the database
        
        Args:
            name: Character full name
            dna: DNA instance
            parent1_id: ID of first parent (optional)
            parent2_id: ID of second parent (optional)
            birth_year: Year of birth (optional)
            first_name: First name (optional)
            family_name: Family name (optional)
            culture: Culture name (optional)
            is_noble: Whether character is nobility (default: False)
            burg_id: Burg ID (optional)
            burg_name: Burg name (optional)
            state_name: State name (optional)
            depc_profile: DEPCProfile object (optional)
            developmental_stress: Total developmental stress (optional)
            stress_severity: Stress severity category (optional)
            notes: Optional notes about the character
            
        Returns:
            ID of the saved character
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Extract DEPC values if profile provided
            depc_dominance = depc_profile.dominance if depc_profile else None
            depc_extroversion = depc_profile.extroversion if depc_profile else None
            depc_patience = depc_profile.patience if depc_profile else None
            depc_conformity = depc_profile.conformity if depc_profile else None
            depc_charisma = depc_profile.charisma if depc_profile else None
            
            cursor.execute("""
                INSERT INTO characters (
                    name, first_name, family_name, dna_hex, parent1_id, parent2_id, 
                    birth_year, culture, is_noble, burg_id, burg_name, state_name,
                    depc_dominance, depc_extroversion, depc_patience, depc_conformity,
                    depc_charisma, developmental_stress, stress_severity, notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name, first_name, family_name, dna.to_hex(), parent1_id, parent2_id,
                birth_year, culture, 1 if is_noble else 0, burg_id, burg_name, state_name,
                depc_dominance, depc_extroversion, depc_patience, depc_conformity,
                depc_charisma, developmental_stress, stress_severity, notes
            ))
            conn.commit()
            return cursor.lastrowid
    
    def load_character(self, char_id: int) -> Optional[Dict]:
        """
        Load a character from the database
        
        Args:
            char_id: Character ID
            
        Returns:
            Dictionary with character data, or None if not found
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM characters WHERE id = ?
            """, (char_id,))
            row = cursor.fetchone()
            
            if row:
                return dict(row)
            return None
    
    def load_dna(self, char_id: int) -> Optional[DNA]:
        """
        Load DNA for a character
        
        Args:
            char_id: Character ID
            
        Returns:
            DNA instance, or None if character not found
        """
        char_data = self.load_character(char_id)
        if char_data:
            return DNA.from_hex(char_data['dna_hex'])
        return None
    
    def get_children(self, parent_id: int) -> List[Dict]:
        """
        Get all children of a character
        
        Args:
            parent_id: Parent character ID
            
        Returns:
            List of child character dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM characters 
                WHERE parent1_id = ? OR parent2_id = ?
                ORDER BY birth_year, id
            """, (parent_id, parent_id))
            return [dict(row) for row in cursor.fetchall()]
    
    def get_ancestors(self, char_id: int, max_generations: int = 10) -> Dict[int, List[Dict]]:
        """
        Get ancestors of a character by generation
        
        Args:
            char_id: Character ID
            max_generations: Maximum generations to trace back
            
        Returns:
            Dictionary mapping generation (0 = self, 1 = parents, etc.) to list of ancestors
        """
        ancestors = {0: [self.load_character(char_id)] if self.load_character(char_id) else []}
        
        current_gen_ids = [char_id] if self.load_character(char_id) else []
        
        for generation in range(1, max_generations + 1):
            if not current_gen_ids:
                break
            
            next_gen_ids = set()
            gen_ancestors = []
            
            for parent_id in current_gen_ids:
                char_data = self.load_character(parent_id)
                if char_data:
                    if char_data['parent1_id']:
                        next_gen_ids.add(char_data['parent1_id'])
                    if char_data['parent2_id']:
                        next_gen_ids.add(char_data['parent2_id'])
            
            for pid in next_gen_ids:
                ancestor = self.load_character(pid)
                if ancestor:
                    gen_ancestors.append(ancestor)
            
            if gen_ancestors:
                ancestors[generation] = gen_ancestors
                current_gen_ids = list(next_gen_ids)
            else:
                break
        
        return ancestors
    
    def get_descendants(self, char_id: int, max_generations: int = 10) -> Dict[int, List[Dict]]:
        """
        Get descendants of a character by generation
        
        Args:
            char_id: Character ID
            max_generations: Maximum generations to trace forward
            
        Returns:
            Dictionary mapping generation (0 = self, 1 = children, etc.) to list of descendants
        """
        descendants = {0: [self.load_character(char_id)] if self.load_character(char_id) else []}
        
        current_gen_ids = [char_id] if self.load_character(char_id) else []
        
        for generation in range(1, max_generations + 1):
            if not current_gen_ids:
                break
            
            next_gen_ids = []
            gen_descendants = []
            
            for parent_id in current_gen_ids:
                children = self.get_children(parent_id)
                for child in children:
                    next_gen_ids.append(child['id'])
                    gen_descendants.append(child)
            
            if gen_descendants:
                descendants[generation] = gen_descendants
                current_gen_ids = next_gen_ids
            else:
                break
        
        return descendants
    
    def search_characters(self, name_pattern: Optional[str] = None,
                         birth_year_min: Optional[int] = None,
                         birth_year_max: Optional[int] = None,
                         limit: int = 100) -> List[Dict]:
        """
        Search for characters by various criteria
        
        Args:
            name_pattern: SQL LIKE pattern for name search (e.g., "%king%")
            birth_year_min: Minimum birth year
            birth_year_max: Maximum birth year
            limit: Maximum number of results
            
        Returns:
            List of matching character dictionaries
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            query = "SELECT * FROM characters WHERE 1=1"
            params = []
            
            if name_pattern:
                query += " AND name LIKE ?"
                params.append(name_pattern)
            
            if birth_year_min is not None:
                query += " AND birth_year >= ?"
                params.append(birth_year_min)
            
            if birth_year_max is not None:
                query += " AND birth_year <= ?"
                params.append(birth_year_max)
            
            query += " ORDER BY birth_year, id LIMIT ?"
            params.append(limit)
            
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]
    
    def delete_character(self, char_id: int) -> bool:
        """
        Delete a character from the database
        
        Note: This will fail if the character has children (foreign key constraint).
        Delete children first, or set their parent IDs to NULL.
        
        Args:
            char_id: Character ID to delete
            
        Returns:
            True if deleted, False if not found or has children
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM characters WHERE id = ?", (char_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError:
            # Has children, cannot delete
            return False
    
    def update_character(self, char_id: int, name: Optional[str] = None,
                        dna: Optional[DNA] = None,
                        notes: Optional[str] = None) -> bool:
        """
        Update character information
        
        Args:
            char_id: Character ID
            name: New name (optional)
            dna: New DNA (optional)
            notes: New notes (optional)
            
        Returns:
            True if updated, False if not found
        """
        updates = []
        params = []
        
        if name is not None:
            updates.append("name = ?")
            params.append(name)
        
        if dna is not None:
            updates.append("dna_hex = ?")
            params.append(dna.to_hex())
        
        if notes is not None:
            updates.append("notes = ?")
            params.append(notes)
        
        if not updates:
            return False
        
        params.append(char_id)
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            query = f"UPDATE characters SET {', '.join(updates)} WHERE id = ?"
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
    
    def get_statistics(self) -> Dict:
        """
        Get database statistics
        
        Returns:
            Dictionary with statistics (total characters, generations, etc.)
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            stats = {}
            
            # Total characters
            cursor.execute("SELECT COUNT(*) FROM characters")
            stats['total_characters'] = cursor.fetchone()[0]
            
            # Characters with parents
            cursor.execute("SELECT COUNT(*) FROM characters WHERE parent1_id IS NOT NULL")
            stats['characters_with_parents'] = cursor.fetchone()[0]
            
            # Root characters (no parents)
            cursor.execute("SELECT COUNT(*) FROM characters WHERE parent1_id IS NULL")
            stats['root_characters'] = cursor.fetchone()[0]
            
            # Max generations (approximate)
            cursor.execute("""
                WITH RECURSIVE generations AS (
                    SELECT id, 0 as depth FROM characters WHERE parent1_id IS NULL
                    UNION ALL
                    SELECT c.id, g.depth + 1
                    FROM characters c
                    JOIN generations g ON c.parent1_id = g.id
                )
                SELECT MAX(depth) FROM generations
            """)
            result = cursor.fetchone()[0]
            stats['max_generations'] = result if result else 0
            
            # Birth year range
            cursor.execute("SELECT MIN(birth_year), MAX(birth_year) FROM characters WHERE birth_year IS NOT NULL")
            year_range = cursor.fetchone()
            if year_range[0] is not None:
                stats['birth_year_range'] = (year_range[0], year_range[1])
            else:
                stats['birth_year_range'] = None
            
            return stats

