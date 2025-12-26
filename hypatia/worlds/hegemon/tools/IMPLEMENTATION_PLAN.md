# DNA Simulator Refactoring Implementation Plan

## Status

The original code from `HEGEMON-DIALOG.md` (1310 lines, ~54KB) needs to be extracted and refactored into proper Python modules with all fixes applied.

## Required Modules

### 1. `dna_config.py` ✅ CREATED
- Configuration constants (already created)
- TRAIT_DEFINITIONS (needs to be added from original file)

### 2. `dna_core.py` - NEEDS CREATION
- DNA class (with error handling added)
- `create_child()` function (with improved mutation validation)
- `calculate_genetic_similarity()` function (renamed from `calculate_inbreeding_coefficient`)
- `predict_offspring_probabilities()` function
- `describe_character()` function
- `describe_breeding_analysis()` function (uses renamed function)

**Fixes to apply:**
- Remove unused `from enum import Enum` import
- Rename `calculate_inbreeding_coefficient` to `calculate_genetic_similarity`
- Add error handling for `from_hex()`, `get_allele_pair()`, `set_allele_pair()`
- Validate trait_index is 0-31, allele values are 0-15
- Use `NUMERIC_TRAITS` constant from config instead of hardcoded list

### 3. `dna_templates.py` - NEEDS CREATION
- `create_royal_bloodline_founder()`
- `create_common_person()`
- `create_hidden_royal_bastard()`
- `create_mad_king()`
- `create_foreign_princess()`

### 4. `dna_database.py` - NEEDS CREATION
- SQLite database for character persistence
- Character table: id, name, dna_hex, parent1_id, parent2_id, birth_year
- Functions: save_character(), load_character(), get_children(), get_ancestors()

### 5. `dna_tree.py` - NEEDS CREATION
- ASCII art family tree visualization
- Functions to generate tree from database relationships
- Support for multiple generations

### 6. `dna_simulator.py` - NEEDS CREATION
- Main module with example simulations from original file
- All the "MATING" examples preserved
- Uses refactored modules

## Implementation Steps

1. ✅ Created `tools/` directory structure
2. ✅ Created `dna_config.py` with constants
3. ⏳ Create `dna_core.py` with all fixes
4. ⏳ Create `dna_templates.py`
5. ⏳ Create `dna_database.py`
6. ⏳ Create `dna_tree.py`
7. ⏳ Create `dna_simulator.py`
8. ⏳ Update `HEGEMON-DIALOG.md` to reference new location

## Notes

- Original code is in `HEGEMON-DIALOG.md` (lines 1-1310)
- All trait definitions are at the top (lines 13-442)
- DNA class starts at line 448
- Breeding functions start at line 521
- Character templates start at line 760
- Examples start at line 1012

