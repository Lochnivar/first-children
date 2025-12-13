# Framework Change Log

**Tracking all changes to the framework and their impact on worlds.**

## Change Log Format

Each entry should include:
- Date
- What changed (in framework or world)
- Why it changed
- Which worlds were affected
- How worlds were updated (if applicable)

---

## December 2024

### Core Cosmology Updated with First Speech Terminology
- **Date:** December 2024
- **Change:** Updated framework with concise cosmology using First Speech terminology
- **Key Updates:**
  - "Big 'G' God" → "Prime Author" (withdrew forever after creation)
  - Added First Speech: *hypatia* — simultaneously "library" and "creator"
  - Clarified that First Children are "many siblings"
  - Worlds can be shaped by one sibling, several in collaboration, or contested when visions clash
  - Iolinus details: Two contending siblings, Godstone/Shattering unique to Iolinus
  - Noted that future worlds may have no Godstone equivalent and different structures
- **Files Updated:** FRAMEWORK.md, hypatia/cosmology/big-g-god.md, hypatia/cosmology/first-children.md, hypatia/worlds/iolinus.md, hypatia/worlds/README.md, README.md

### Library Metaphor Added to Framework
- **Date:** December 2024
- **Change:** Added conceptual metaphor to framework documentation
- **Metaphor:** Big 'G' God = Author, Hypatia = Library, Worlds = Books, First Children = Librarians who live in the library and access books
- **Reason:** Provide a clear conceptual framework for understanding the structure of Hypatia
- **Files Updated:** FRAMEWORK.md, hypatia/README.md, hypatia/cosmology/big-g-god.md, hypatia/cosmology/first-children.md, hypatia/mechanics/world-creation.md, hypatia/worlds/README.md, README.md
- **Impact:** The metaphor helps clarify the relationship between the Big 'G' God, Hypatia, worlds, and First Children

### Framework Renamed to Hypatia
- **Date:** December 2024
- **Change:** Renamed framework directory to `hypatia/` and established "Hypatia" as the name of the over-universe
- **Reason:** Give the over-universe a distinct identity and name
- **Impact:** All references to "framework/" updated to "hypatia/", all references to "over-universe" updated to "Hypatia" where appropriate
- **Files Updated:** All files in repository updated to reflect new naming

### Framework Reorganization: Structured Like Iolinus World-Building
- **Date:** December 2024
- **Change:** Reorganized framework directory into subdirectories mirroring Iolinus world-building structure
- **Reason:** Create organized structure like Iolinus with categories (cosmology, magic-systems, mechanics, etc.)
- **New Structure:**
  - `hypatia/cosmology/` - Big 'G' God, First Children, Marcionite theology
  - `hypatia/metaphysics/` - Quantum foundation (universal forces)
  - `hypatia/magic-systems/` - Quantumancy
  - `hypatia/mechanics/` - Soul transfer, world creation, liberation operations
  - `hypatia/rules/` - Cosmological constants
  - `hypatia/guidelines/` - Expansion guidelines
  - `hypatia/narrative/` - Story types, character types, themes
  - `hypatia/philosophy/` - Balance and imbalance (already existed)
  - `hypatia/races/` - Races (already existed)
  - `hypatia/worlds/` - Framework-level world documentation (NEW)
- **Files Created:**
  - Extracted narrative framework content (story-types.md, character-types.md, themes.md)
  - Created rules and guidelines documentation
  - Created metaphysics/quantum-foundation.md
  - Created hypatia/worlds/iolinus.md (framework summary)
  - Created README.md files for each subdirectory
- **Files Moved:**
  - Moved cosmology files to `cosmology/`
  - Moved quantumancy.md to `magic-systems/`
  - Moved mechanics files to `mechanics/`
- **Files Updated:**
  - Updated all cross-references in framework files
  - Updated all links in Iolinus files to point to new structure
  - Updated hypatia/README.md to reflect new structure
  - Updated FRAMEWORK.md to reference new structure
- **Notes:** Framework now mirrors Iolinus structure with organized subdirectories

### Framework Gaps Analysis: Identified Missing Documentation
- **Date:** December 2024
- **Change:** Analyzed gaps between framework expectations and existing documentation
- **Findings:**
  - Fixed broken link: `quantum.md` → `quantumancy.md` in first-children.md
  - Identified expected files that don't exist: metaphysics.md, rules.md, guidelines.md
  - Identified content in FRAMEWORK.md not extracted to detailed docs (narrative framework, world-building guidelines)
  - Created `hypatia/GAPS_ANALYSIS.md` documenting gaps
- **Status:** Analysis complete, recommendations documented

### Races Framework: Added Kitsune and Giff
- **Date:** December 2024
- **Change:** Added kitsune and giff race documentation to framework
- **Files Created:**
  - `hypatia/races/kitsune.md` - Kitsune race documentation (shapeshifting fox-people)
  - `hypatia/races/giff.md` - Giff race documentation (hippo-like military humanoids)
- **Files Updated:**
  - Updated `hypatia/races/README.md` to include kitsune and giff
- **Notes:** Additional fantasy races added to framework options

### Races Framework: Created Races Documentation
- **Date:** December 2024
- **Change:** Created hypatia/races/ directory with documentation for universal intelligent races
- **Reason:** Provide common races available across Hypatia for world-building consistency
- **Worlds Affected:** All worlds (races available as options), Iolinus (currently human-only)
- **Files Created:**
  - `hypatia/races/README.md` - Overview of races framework
  - `hypatia/races/humans.md` - Human race documentation
  - `hypatia/races/elves.md` - Elven race documentation
  - `hypatia/races/dwarves.md` - Dwarven race documentation
  - `hypatia/races/orcs.md` - Orc race documentation
  - `hypatia/races/halflings.md` - Halfling race documentation
  - `hypatia/races/template.md` - Template for additional races
- **Files Updated:**
  - Updated `hypatia/README.md` to include races section
  - Updated `FRAMEWORK.md` to include races in detailed documentation
- **Notes:** Races are universal options available for all worlds; individual worlds can include, exclude, or modify races as needed

### Philosophy Migration: Balance Philosophy Moved to Framework
- **Date:** December 2024
- **Change:** Moved philosophy folder from Iolinus to framework
- **Reason:** Balance and imbalance is a universal philosophical principle applicable across all worlds
- **Worlds Affected:** Iolinus (philosophy now in framework), future worlds (can reference framework)
- **Files Moved:**
  - `worlds/iolinus/world-building/philosophy/` → `hypatia/philosophy/`
  - Updated `balance_philosophy.md` to reflect framework status
- **Files Updated:**
  - Updated `hypatia/README.md` to include philosophy section
  - Updated `FRAMEWORK.md` to include philosophy in detailed documentation
- **Notes:** Philosophy is now universal framework element, applicable to all worlds and stories

### Cosmology Migration: Big 'G' God and Marcionite Theology Moved to Framework
- **Date:** December 2024
- **Change:** Moved universal cosmology files from Iolinus to framework
- **Reason:** Big 'G' God and Marcionite theological structure are universal framework elements, not Iolinus-specific
- **Worlds Affected:** Iolinus (updated links), future worlds (can reference framework)
- **Files Moved:**
  - `worlds/iolinus/world-building/cosmology/big_g_god.md` → `hypatia/big-g-god.md`
  - `worlds/iolinus/world-building/cosmology/marcionite_theology.md` → `hypatia/marcionite-theology.md`
- **Files Updated:**
  - Updated links in `nala_goddess.md` and `zeta_god.md` to reference framework
  - Updated `hypatia/README.md` to include cosmology section
- **Notes:** Universal cosmology now in framework, Iolinus-specific religious details (Malachor faith, naming) remain in Iolinus

### Framework Migration: Universal Elements Moved from Iolinus
- **Date:** December 2024
- **Change:** Moved universal framework elements from Iolinus files to framework, updated Iolinus files to link to framework
- **Reason:** Establish framework as primary source of truth, Iolinus as subordinate with links
- **Worlds Affected:** Iolinus (updated to link to framework)
- **Impact:** Framework now contains universal elements, Iolinus contains only Iolinus-specific details with framework links
- **Files Updated:**
  - `worlds/iolinus/world-building/cosmology/nala_goddess.md` - Now links to hypatia/first-children.md and hypatia/liberation-operations.md
  - `worlds/iolinus/world-building/cosmology/zeta_god.md` - Now links to hypatia/first-children.md and hypatia/world-creation.md
  - `worlds/iolinus/world-building/magic-systems/quantum_abilities.md` - Now links to hypatia/quantumancy.md
  - `worlds/iolinus/world-building/organizations/greyroses.md` - Now links to hypatia/soul-transfer.md
  - `worlds/iolinus/characters/groups/earth_souls.md` - Now links to hypatia/soul-transfer.md and hypatia/liberation-operations.md
- **Notes:** Iolinus files now contain only Iolinus-specific details, with clear links to universal framework documentation

### Framework Extraction and Population
- **Date:** December 2024
- **Change:** Extracted over-universe elements from Iolinus and created detailed framework documentation
- **Reason:** Populate framework with universal elements extracted from Iolinus examples
- **Worlds Affected:** Iolinus (as source), future worlds (will conform to framework)
- **Impact:** Framework now has detailed documentation extracted from Iolinus
- **Documentation Created:**
  - `hypatia/first-children.md` - First Children details extracted from Nala/Zeta examples
  - `hypatia/quantumancy.md` - Quantumancy and fragmented abilities details
  - `hypatia/soul-transfer.md` - Soul transfer mechanisms (greyroses, Earth souls as examples)
  - `hypatia/world-creation.md` - World creation and life force binding details
  - `hypatia/liberation-operations.md` - Liberation operation patterns from Nala's plan
- **Notes:** All documentation extracts universal patterns while noting Iolinus-specific examples

### Initial Framework Establishment
- **Date:** December 2024
- **Change:** Framework extracted from Iolinus and established as primary source of truth
- **Reason:** Reorganization to framework-primary structure
- **Worlds Affected:** Iolinus
- **Impact:** Iolinus now documented as subordinate world
- **Documentation:** Created FRAMEWORK.md, CONSISTENCY_CHECK.md, CONSISTENCY_PROCESS.md

### Repository Reorganization
- **Date:** December 2024
- **Change:** Moved from flat structure to framework-primary structure
- **Reason:** Clear separation between framework and individual worlds
- **Worlds Affected:** Iolinus (now located at hypatia/worlds/iolinus/)
- **Impact:** New directory structure, updated paths and references
- **Documentation:** Migration completed, all files reorganized

---

## Future Changes

As the framework evolves and new worlds are added, changes will be documented here with:
- Clear description of what changed
- Reason for the change
- Impact assessment on existing worlds
- Steps taken to maintain consistency

---

*All framework changes should go through the consistency process outlined in [CONSISTENCY_PROCESS.md](CONSISTENCY_PROCESS.md)*

