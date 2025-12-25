#!/usr/bin/env python3
"""
Script to create a master list of all burgs from the Azgaar data
"""

import json
import os

# Read the burgs JSON file
with open('12-burgs.json', 'r', encoding='utf-8') as f:
    burgs_data = json.load(f)

# Read the states JSON file to get state names
with open('11-states.json', 'r', encoding='utf-8') as f:
    states_data = json.load(f)

# Create state ID to name mapping
state_id_to_name = {}
for state in states_data:
    state_id = state.get('i')
    state_name = state.get('name', f'State_{state_id}')
    state_id_to_name[state_id] = state_name

# Organize burgs by state
burgs_by_state = {}
burgs_by_type = {}
burgs_by_culture = {}
total_population = 0

for burg in burgs_data:
    state_id = burg.get('state')
    burg_type = burg.get('type', 'Unknown')
    culture_id = burg.get('culture', 'N/A')
    population = burg.get('population', 0)
    
    total_population += population
    
    # Group by state (handle None values)
    state_key = state_id if state_id is not None else -1
    if state_key not in burgs_by_state:
        burgs_by_state[state_key] = []
    burgs_by_state[state_key].append(burg)
    
    # Group by type
    if burg_type not in burgs_by_type:
        burgs_by_type[burg_type] = []
    burgs_by_type[burg_type].append(burg)
    
    # Group by culture
    if culture_id not in burgs_by_culture:
        burgs_by_culture[culture_id] = []
    burgs_by_culture[culture_id].append(burg)

# Sort burgs by population (descending) for top lists
all_burgs_sorted = sorted(burgs_data, key=lambda x: x.get('population', 0), reverse=True)

# Generate the master list markdown
output = []
output.append("# Hegemon Burgs Master List\n")
output.append("**Status:** Reference Document  \n")
output.append("**Era:** Hacutonce Era (374 HE)  \n")
output.append("**Last Updated:** December 2024  \n")
output.append(f"**Total Burgs:** {len(burgs_data)}  \n")
output.append(f"**Total Population:** {total_population:.2f}\n")
output.append("\n---\n\n")
output.append("## Overview\n\n")
output.append("This master list provides a comprehensive reference for all burgs (cities and settlements) in the Hegemon world, organized by various categories for quick reference.\n\n")
output.append("---\n\n")

# Statistics by state
output.append("## Burgs by State\n\n")
output.append("| State | Burg Count | Total Population | Average Population |\n")
output.append("|-------|------------|------------------|-------------------|\n")

state_stats = []
for state_id, burg_list in sorted(burgs_by_state.items()):
    if state_id == -1:
        state_name = "Unassigned"
    else:
        state_name = state_id_to_name.get(state_id, f'State_{state_id}')
    burg_count = len(burg_list)
    state_pop = sum(b.get('population', 0) for b in burg_list)
    avg_pop = state_pop / burg_count if burg_count > 0 else 0
    state_stats.append((state_name, burg_count, state_pop, avg_pop))

# Sort by burg count descending
state_stats.sort(key=lambda x: x[1], reverse=True)
for state_name, burg_count, state_pop, avg_pop in state_stats:
    output.append(f"| {state_name} | {burg_count} | {state_pop:.2f} | {avg_pop:.2f} |\n")

output.append("\n---\n\n")

# Statistics by type
output.append("## Burgs by Type\n\n")
output.append("| Type | Count | Total Population | Average Population |\n")
output.append("|------|-------|------------------|-------------------|\n")

type_stats = []
for burg_type, burg_list in sorted(burgs_by_type.items()):
    burg_count = len(burg_list)
    type_pop = sum(b.get('population', 0) for b in burg_list)
    avg_pop = type_pop / burg_count if burg_count > 0 else 0
    type_stats.append((burg_type, burg_count, type_pop, avg_pop))

# Sort by count descending
type_stats.sort(key=lambda x: x[1], reverse=True)
for burg_type, burg_count, type_pop, avg_pop in type_stats:
    output.append(f"| {burg_type} | {burg_count} | {type_pop:.2f} | {avg_pop:.2f} |\n")

output.append("\n---\n\n")

# Top 20 largest burgs
output.append("## Top 20 Largest Burgs (by Population)\n\n")
output.append("| Rank | Name | State | Type | Population | Culture |\n")
output.append("|------|------|-------|------|------------|---------|\n")

for rank, burg in enumerate(all_burgs_sorted[:20], 1):
    burg_name = burg.get('name', 'Unknown')
    state_id = burg.get('state')
    if state_id is None:
        state_name = "Unassigned"
    else:
        state_name = state_id_to_name.get(state_id, f'State_{state_id}')
    burg_type = burg.get('type', 'Unknown')
    population = burg.get('population', 0)
    culture_id = burg.get('culture', 'N/A')
    output.append(f"| {rank} | {burg_name} | {state_name} | {burg_type} | {population:.2f} | {culture_id} |\n")

output.append("\n---\n\n")

# Complete burgs list (abbreviated - showing key information)
output.append("## Complete Burgs List\n\n")
output.append("*Note: This is a summary table. For detailed information, see individual state burg files.*\n\n")
output.append("| Index | Name | State | Type | Population | Culture |\n")
output.append("|-------|------|-------|------|------------|---------|\n")

# Sort all burgs by index
burgs_sorted_by_index = sorted(burgs_data, key=lambda x: x.get('i', 0))

for burg in burgs_sorted_by_index:
    burg_index = burg.get('i', 'N/A')
    burg_name = burg.get('name', 'Unknown')
    state_id = burg.get('state')
    if state_id is None:
        state_name = "Unassigned"
    else:
        state_name = state_id_to_name.get(state_id, f'State_{state_id}')
    burg_type = burg.get('type', 'Unknown')
    population = burg.get('population', 0)
    culture_id = burg.get('culture', 'N/A')
    output.append(f"| {burg_index} | {burg_name} | {state_name} | {burg_type} | {population:.2f} | {culture_id} |\n")

output.append("\n---\n\n")

# Framework context
output.append("## Framework Context\n\n")
output.append("Burgs represent cities, towns, and settlements within the Hegemon world. These are the centers of population, commerce, and strategic importance where the First Children's game is played out through mortal agents.\n\n")
output.append("**Key Framework Points:**\n")
output.append("- Burgs are mortal settlements within the quantum foundation\n")
output.append("- Population indicates economic and strategic importance\n")
output.append("- Type (Naval, Generic, River, Lake, etc.) reflects strategic characteristics\n")
output.append("- Cultural affiliation shapes how burgs respond to manipulation\n")
output.append("- State ownership determines political control and strategic value\n\n")
output.append("---\n\n")

# Related documentation
output.append("## Related Documentation\n\n")
output.append("- [States Master List](states/STATES_MASTER_LIST.md) - State-level overview\n")
output.append("- [States Index](states/README.md) - State directory structure\n")
output.append("- [Individual State Burgs](states/) - Detailed burg information by state\n")
output.append("- [Cultures Master List](cultures/CULTURES_MASTER_LIST.md) - Cultural foundations\n\n")
output.append("---\n\n")
output.append("*For Azgaar map data reference, see [README.md](README.md)*  \n")
output.append("*For Hegemon world documentation, see [../README.md](../README.md)*  \n")
output.append("*For framework documentation, see [../../FRAMEWORK.md](../../FRAMEWORK.md)*\n")

# Write the file
with open('BURGS_MASTER_LIST.md', 'w', encoding='utf-8') as f:
    f.writelines(output)

print(f"Created BURGS_MASTER_LIST.md with {len(burgs_data)} burgs")
print(f"Total population: {total_population:.2f}")

