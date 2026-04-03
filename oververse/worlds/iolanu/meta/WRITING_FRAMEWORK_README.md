# Writing Framework Guide

This repository contains a structured framework for organizing your writing project, including characters, plots, world-building, and more.

## Directory Structure

```
├── characters/          # Character profiles and information
│   ├── template.md     # Template for creating new characters
│   ├── index.md        # Index of all characters
│   └── [character].md  # Individual character files
│
├── plots/              # Plot-related documentation
│   ├── arcs/           # Major story arcs
│   │   ├── template.md
│   │   └── index.md
│   ├── scenes/         # Individual scene breakdowns
│   │   ├── template.md
│   │   └── index.md
│   ├── threads/        # Subplots and minor threads
│   │   ├── template.md
│   │   └── index.md
│   └── outlines/       # Story and chapter outlines
│       └── template.md
│
├── relationships/       # Character relationship documentation
│   ├── template.md
│   └── index.md
│
├── locations/           # World locations and settings
│   ├── template.md
│   └── index.md
│
├── timeline/           # Chronological event tracking
│   ├── template.md
│   └── index.md
│
└── world-building/     # World-building elements
    ├── template.md
    └── index.md
```

## How to Use

### Creating New Entries

1. **Characters:** Copy `characters/template.md` and rename it to your character's name. Fill in the details and add a link in `characters/index.md`.

2. **Plots:** 
   - For story arcs, use `plots/arcs/template.md`
   - For scenes, use `plots/scenes/template.md`
   - For subplots, use `plots/threads/template.md`
   - For outlines, use `plots/outlines/template.md`

3. **Relationships:** Use `relationships/template.md` to document important character dynamics.

4. **Locations:** Use `locations/template.md` for any significant places in your world.

5. **Timeline:** Use `timeline/template.md` to track chronological events.

6. **World-Building:** Use `world-building/template.md` for magic systems, technology, cultures, etc.

### Maintaining Organization

- Update index files whenever you add new entries
- Link related documents using markdown links
- Keep templates consistent - modify them if needed, but maintain structure
- Use the status fields to track progress (Planning/In Progress/Complete)

### Best Practices

- **Be Consistent:** Follow the template structure to make information easy to find
- **Cross-Reference:** Link related characters, plots, and locations
- **Update Regularly:** Keep your documentation current as your story evolves
- **Use Status Fields:** Track what's complete, in progress, or just planned
- **Keep Notes:** Use the notes sections to capture ideas and connections

## Integration with Existing Content

This framework is designed to work alongside your existing `world-bible/` directory. You can:
- Move existing character files into the `characters/` directory
- Organize plot information from your world bible into the `plots/` structure
- Expand world-building details into the `world-building/` directory

## Tips

- Start with characters and major plot arcs
- Build out relationships as you develop characters
- Add locations as they become relevant to your story
- Use the timeline to track story chronology
- Keep world-building elements organized by category

Happy writing!

