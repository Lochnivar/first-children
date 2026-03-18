# Instructions for AI: Setting Up Over-Universe Repo

## Situation

You are setting up a new repository that will contain:
1. **An over-universe framework** (the primary source of truth)
2. **Iolinus** (a subordinate story/world that demonstrates the framework)

All files from the Iolinus project are being provided to you. Your job is to reorganize them into the framework-primary structure.

## Your Task

1. **Understand the structure** - Read `MIGRATION_PACKAGE.md` for complete file manifest
2. **Create the new structure** - Follow the target structure outlined
3. **Move all files** - Preserve content, reorganize into new locations
4. **Create new documentation** - Framework READMEs, consistency docs, etc.
5. **Update all links** - Fix internal references to match new structure
6. **Document conformance** - Show how Iolinus conforms to framework

## Key Principles

- **Framework is PRIMARY** - `FRAMEWORK.md` is the source of truth
- **Iolinus is SUBORDINATE** - Must conform to framework rules
- **Preserve everything** - Don't delete content, reorganize it
- **Process for contradictions** - Framework wins, but can evolve

## Structure You're Creating

```
over-universe-repo/
├── README.md                          # Over-universe overview
├── FRAMEWORK.md                       # PRIMARY source of truth
├── oververse/                         # Detailed framework docs
├── worlds/
│   ├── README.md                      # Worlds index
│   └── iolinus/                       # Iolinus story (subordinate)
└── meta/                              # Meta-documentation
```

## Critical Files to Read First

1. **MIGRATION_PACKAGE.md** - Complete file manifest and instructions
2. **OVER_UNIVERSE_FRAMEWORK.md** - The framework document (becomes FRAMEWORK.md)
3. **FRAMEWORK_PRIMARY_STRUCTURE.md** - Structure explanation
4. **CONSISTENCY_SOLUTION.md** - Consistency approach

## What to Do

### Step 1: Create Structure
- Create all directories from `MIGRATION_PACKAGE.md`
- Set up oververse/, worlds/iolinus/, meta/

### Step 2: Move Framework
- Copy `OVER_UNIVERSE_FRAMEWORK.md` → `FRAMEWORK.md` (root)
- Extract sections to create `oververse/` detailed docs

### Step 3: Move Iolinus
- Move all Iolinus content to `worlds/iolinus/` per manifest
- Preserve all directory structure and files

### Step 4: Create New Docs
- Root `README.md` - Overview of over-universe
- `worlds/README.md` - Index of worlds
- `worlds/iolinus/README.md` - Rewrite as subordinate world (see template in FRAMEWORK_PRIMARY_STRUCTURE.md)
- `worlds/iolinus/CONSISTENCY_CHECK.md` - Document how Iolinus conforms
- `meta/CONSISTENCY_PROCESS.md` - Process for handling contradictions
- `meta/CHANGE_LOG.md` - Framework change tracking

### Step 5: Update Links
- Find all markdown links in moved files
- Update relative paths to match new structure
- Fix cross-references

### Step 6: Document Conformance
- In `worlds/iolinus/CONSISTENCY_CHECK.md`, document:
  - How Iolinus demonstrates framework elements
  - Which framework rules it follows
  - Any variations or expansions
  - Framework elements it uses (Nala, Zeta, soul transfer, etc.)

## Important Notes

- **Don't delete anything** - Reorganize, don't remove
- **Framework is primary** - Iolinus README should state it's subordinate
- **All content preserved** - Just moved to new locations
- **Links must be updated** - Old relative paths won't work
- **New structure is clear** - Framework primary, stories subordinate

## Questions to Answer

As you reorganize, document:

1. How does Iolinus conform to the framework?
2. Which framework elements does Iolinus demonstrate?
3. Are there any contradictions? (If so, Iolinus needs to change)
4. What new documentation is needed?

## Success Criteria

- [ ] All files moved to correct locations
- [ ] Framework.md is at root
- [ ] Iolinus content is in worlds/iolinus/
- [ ] All new README files created
- [ ] Consistency documentation created
- [ ] All internal links updated
- [ ] Structure is clear (framework primary, stories subordinate)
- [ ] No content lost
- [ ] Everything is documented

Good luck! Use MIGRATION_PACKAGE.md as your primary guide.

