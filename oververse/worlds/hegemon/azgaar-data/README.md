# Azgaar Fantasy Map Generator Export Data

**Status:** Reference Data - Hegemon World  
**Source:** Azgaar Fantasy Map Generator v1.108.13  
**Export Date:** 2025-12-24  
**Map Seed:** 385169078  
**Map Dimensions:** 1707×791  

## Overview

This directory contains the parsed export data from an Azgaar Fantasy Map Generator map created for the Hegemon world. The original export file (`../azgaar-data.md`) has been organized into separate files for easier reference and maintenance.

## Master Lists

- **[BURGS_MASTER_LIST.md](BURGS_MASTER_LIST.md)** - Comprehensive master list of all burgs (cities/settlements)
- **[States Master List](states/STATES_MASTER_LIST.md)** - Master list of all states
- **[Cultures Master List](cultures/CULTURES_MASTER_LIST.md)** - Master list of all cultures

## File Structure

### Core Metadata

- **`01-metadata-header.txt`** - Version, generator URL, export date, map seed, dimensions
- **`02-map-settings.txt`** - Map configuration (units, temperature, military types, era settings)
- **`03-coordinates.json`** - Geographic bounds (latitude/longitude ranges)

### Terrain & Biomes

- **`04-biomes.txt`** - Biome color codes, names, and elevation ranges
  - Includes: Marine, Hot desert, Cold desert, Savanna, Grassland, Tropical seasonal forest, Temperate deciduous forest, Tropical rainforest, Temperate rainforest, Taiga, Tundra, Glacier, Wetland

### Military Data

- **`05-regiments.json`** - Complete military regiment data
  - Contains all regiments with their formations, compositions, and historical context
  - Includes infantry, archers, cavalry, artillery, and fleet units
  - Organized by state/territory

### Map Visualization

- **`06-map.svg`** - Complete SVG map file
  - Full vector map with all geographic features
  - Can be viewed in any SVG-compatible viewer
  - Preserves all visual details from the generator

### Geographic Data

- **`08-cells-config.json`** - Cell system configuration
  - Grid spacing, cell dimensions, boundary definitions
  
- **`09-cells-data.json`** - Geographic cell data
  - Individual cell properties, terrain types, land/water classification

### Cultural & Political Data

- **`10-cultures.json`** - Cultural groups and their properties (original export format)
  - Cultures include: Wildlands, Berberan, Luari, Norse, Slovan, Portuzian, Shwazen, Romian, and others
  - Expansionism values, base cultures, shield types, centers
  - **See also:** [`cultures/`](cultures/README.md) directory for individual culture folders with organized data files

- **`11-states.json`** - Political states and territories (original export format)
  - State definitions with colors, capitals, expansionism, types
  - Territory boundaries and relationships
  - Campaign and diplomatic histories
  - **See also:** [`states/`](states/README.md) directory for individual state folders with organized data files

- **`12-burgs.json`** - Cities, towns, and settlements (burgs) (original export format)
  - Population data, coordinates, cultural affiliations
  - Settlement types (Naval, Generic, etc.)
  - Feature classifications
  - **See also:** Burgs have been organized into individual state folders in [`states/`](states/README.md) (see `burgs.json` and `burgs.md` in each state folder)

- **`13-religions.json`** - Religious systems
  - Religious groups and their properties
  - Deities, forms (Polytheism, Shamanism, Ancestor Worship, etc.)
  - Cultural associations and expansion patterns

## Usage

### Loading Back into Azgaar

The original export file (`../azgaar-data.md`) can be loaded directly into [Azgaar Fantasy Map Generator](https://azgaar.github.io/Fantasy-Map-Generator) to continue editing the map.

**Note:** The parsed files in this directory are for reference only. To reload the map into Azgaar, use the original `azgaar-data.md` file.

### Reference Purposes

These parsed files can be used for:
- Extracting specific data (cultures, states, regiments) for world-building documentation
- Understanding the map structure and relationships
- Integrating map data into Hegemon world documentation
- Creating custom visualizations or data analysis

### State Organization

The states data has been further organized into individual folders:
- **`states/`** - Directory containing one folder per state
  - Each state folder includes: README overview, complete state data, military units, diplomacy relations, campaigns, provinces, and burgs
  - See [states/README.md](states/README.md) for the complete index

### Culture Organization

The cultures data has been further organized into individual folders:
- **`cultures/`** - Directory containing one folder per culture
  - Each culture folder includes: README overview and complete culture data
  - See [cultures/README.md](cultures/README.md) for the complete index

## Era Information

- **Current Era:** Hacutonce Era (HE)
- **Year:** 374 HE
- **Era Abbreviation:** HE

## Map Context for Hegemon

This map represents the geographic foundation of the Hegemon world, where:

- **Territories** correspond to coherent quantum energy patterns
- **States** represent political entities controlled by First Children (The Strategists)
- **Cultures** reflect mortal civilizations shaped by quantum manipulation
- **Military Regiments** demonstrate the strategic game mechanics in action
- **Religions** show how mortals interpret the First Children's influence

For more information about how this map integrates with the Hegemon world concept, see:
- [World Structure](../world-structure.md)
- [Game Mechanics](../game-mechanics.md)
- [Mortal Experience](../mortal-experience.md)

## Maintenance

### Re-parsing

If the original `azgaar-data.md` file is updated, run the parsing script:

```bash
cd azgaar-data
python parse_azgaar.py
```

This will regenerate all parsed files from the source export.

### Notes

- The parsing script (`parse_azgaar.py`) identifies sections by line numbers based on Azgaar's export format
- Some data arrays may span multiple lines in the original format but are stored as single-line JSON in parsed files
- The SVG file preserves the complete map visualization including all filters and definitions

---

*For Hegemon world documentation, see [../README.md](../README.md)*  
*For framework reference, see [../../../FRAMEWORK.md](../../../FRAMEWORK.md)*

