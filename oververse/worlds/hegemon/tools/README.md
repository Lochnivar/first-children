# DNA Simulation Tools

**Status:** ✅ Complete - All modules refactored and tested  
**Purpose:** Genetic simulation for tracking character traits, bloodlines, and inheritance patterns in the Hegemon world

## Module Structure

- **`dna_config.py`** ✅ - Configuration constants
- **`dna_traits.py`** ✅ - TRAIT_DEFINITIONS dictionary (32 traits)
- **`dna_core.py`** ✅ - Core DNA class and breeding functions (with all fixes applied)
- **`dna_templates.py`** ✅ - Character template creation functions
- **`dna_database.py`** ✅ - SQLite database persistence for characters and family trees
- **`dna_tree.py`** ✅ - ASCII art family tree visualization
- **`dna_simulator.py`** ✅ - Example simulations demonstrating the system

## Changes from Original

### Fixes Applied
1. ✅ Removed unused `from enum import Enum` import
2. ✅ Renamed `calculate_inbreeding_coefficient()` to `calculate_genetic_similarity()` (more accurate naming)
3. ✅ Added error handling and input validation
4. ✅ Added configuration constants for hardcoded values
5. ✅ Improved mutation system validation

### New Features
- ✅ SQLite database support for persistence
- ✅ ASCII art family tree visualization
- ✅ Proper module structure for maintainability
- ✅ Comprehensive error handling

## Usage

### Basic Usage

```python
from tools.dna_core import DNA, create_child, calculate_genetic_similarity
from tools.dna_templates import create_royal_bloodline_founder, create_common_person

# Create characters
royal = create_royal_bloodline_founder()
common = create_common_person()

# Create child
child = create_child(royal, common)

# Calculate genetic similarity
similarity = calculate_genetic_similarity(royal, common)
print(f"Similarity: {similarity:.2%}")
```

### Database Usage

```python
from tools.dna_database import CharacterDatabase
from tools.dna_tree import FamilyTree
from tools.dna_core import create_child
from tools.dna_templates import create_royal_bloodline_founder

# Create database
db = CharacterDatabase('characters.db')

# Create and save characters
king_id = db.save_character('King Aerys I', create_royal_bloodline_founder(), birth_year=100)
queen_id = db.save_character('Queen Rhaella I', create_royal_bloodline_founder(), birth_year=100)

# Create child and save with parents
king_dna = db.load_dna(king_id)
queen_dna = db.load_dna(queen_id)
child_dna = create_child(king_dna, queen_dna)
child_id = db.save_character('Prince Aerys II', child_dna, 
                              parent1_id=king_id, parent2_id=queen_id, 
                              birth_year=120)

# Generate family tree
tree = FamilyTree(db)
print(tree.generate_ascii_tree(child_id))
```

### Running Example Simulations

```python
from tools.dna_simulator import run_all_simulations

# Run all example simulations
results = run_all_simulations()
```

## Database Schema

The SQLite database stores:
- Characters (id, name, dna_hex, parent1_id, parent2_id, birth_year)
- Relationships (for building family trees)

## Notes

- Original code extracted from `HEGEMON-DIALOG.md`
- All examples from the original file are preserved in `dna_simulator.py`
- The system models simplified Mendelian inheritance (documented as such)

---

*For detailed analysis of the code, see [../DNA_SIMULATION_ANALYSIS.md](../DNA_SIMULATION_ANALYSIS.md)*

