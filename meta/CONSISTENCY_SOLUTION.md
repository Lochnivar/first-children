# Consistency Solution: Single Source of Truth Approach

## The Problem

**Two repos = consistency nightmare:**
- Changes to framework might contradict Iolanu details
- Changes to Iolanu might invalidate framework
- Hard to know which is authoritative
- Risk of contradictions growing over time
- Difficult to maintain sync

## The Solution: This repository as single source of truth

### Approach: Framework lives in this repo (first-children)

**Structure:**
```
iolanu/
├── README.md                          # Iolanu project overview
├── [existing structure]               # All current Iolanu content
│
├── oververse/                         # Over-universe framework
│   ├── README.md                      # Framework overview
│   ├── OVER_UNIVERSE_FRAMEWORK.md    # The framework document
│   ├── cosmology.md                   # Extracted universal rules
│   ├── metaphysics.md                 # Universal forces
│   ├── rules.md                       # What must be consistent
│   └── guidelines.md                  # Expansion guidelines
│
└── meta/
    ├── PREMISE_TONE_PERSPECTIVE.md   # Existing
    └── [other meta docs]
```

**Benefits:**
- ✅ Single source of truth (this repository)
- ✅ Framework extracted FROM Iolanu (not imposed on it)
- ✅ Changes in Iolanu automatically inform framework
- ✅ No sync issues
- ✅ Framework documents what Iolanu demonstrates
- ✅ Can evolve framework as Iolanu develops

### Change Flow: Iolanu → Framework

**Direction of Authority:**
1. **Iolanu story/details are PRIMARY** (source of truth)
2. **Framework documents/extracts** universal principles FROM Iolanu
3. **When Iolanu changes**, framework is updated to reflect it
4. **Framework doesn't impose** rules on Iolanu - it documents what exists

**Process:**
- Change Iolanu → Extract/update framework to match
- Framework change → Check against Iolanu → If contradiction, Iolanu wins, framework adjusts

---

## Alternative: Reverse Extract Approach

### Framework as "Living Document" Derived from Iolanu

**The framework document should:**
- Be written as "extracted from Iolanu" not "applied to Iolanu"
- Explicitly reference Iolanu as the source
- State: "This framework is derived from Iolanu. Iolanu details take precedence."
- Be updated when Iolanu changes, not the other way around

**In framework document, add:**

```markdown
## Source of Truth

**Iolanu is the primary source of truth for this framework.**

This framework document extracts universal principles demonstrated in Iolanu. 
If contradictions arise between this framework and Iolanu details:

1. Iolanu details are authoritative
2. This framework should be updated to match Iolanu
3. Framework changes that would contradict Iolanu are invalid

The framework documents what exists in Iolanu, not what should exist.
```

---

## Best Solution: Keep Everything in One Repo

### Recommended Structure

```
iolanu/
├── README.md                          # "Iolanu: A story in Hypatia"
│
├── story/                             # Iolanu story-specific content
│   ├── characters/
│   ├── world-building/
│   ├── locations/
│   ├── plots/
│   └── relationships/
│
├── oververse/                         # Over-universe framework
│   ├── README.md                      # "Universal framework extracted from Iolanu"
│   ├── cosmology.md                   # Big G God, First Children
│   ├── metaphysics.md                 # Quantumancy, soul transfer
│   ├── rules.md                       # Consistency rules
│   ├── guidelines.md                  # Expansion guidelines
│   └── OVER_UNIVERSE_FRAMEWORK.md    # Complete framework doc
│
├── meta/                              # Project meta-docs
│   ├── PREMISE_TONE_PERSPECTIVE.md
│   ├── AI_REFRESHER.md
│   └── CONSISTENCY_NOTES.md          # How framework relates to story
│
└── archive/                           # Raw files, etc.
```

### How It Works

**Story Content (story/):**
- All Iolanu-specific details
- Characters, world-building, plots
- This is the PRIMARY source of truth
- Can change freely

**Framework Content (oververse/):**
- Extracted universal principles
- Documents what Iolanu demonstrates
- Updated when story changes
- Provides structure for future stories

**Meta Content (meta/):**
- Documents about the project
- How framework relates to story
- Consistency notes

### Change Process

**When Iolanu story changes:**
1. Update story content in `story/`
2. Review if change affects universal principles
3. If yes, update `oververse/` to reflect new reality
4. Update `meta/CONSISTENCY_NOTES.md` if needed

**When considering framework change:**
1. Check if it contradicts Iolanu story
2. If contradiction, either:
   - Reject framework change (Iolanu is source of truth)
   - Or update Iolanu story to match (if intentional expansion)
3. Document decision in CONSISTENCY_NOTES.md

---

## Implementation: Adding Framework to Current Repo

### Step-by-Step

1. **Create `oververse/` directory** in this repository
2. **Move OVER_UNIVERSE_FRAMEWORK.md** to `oververse/`
3. **Add oververse/README.md** that explains:
   - This framework is extracted from Iolanu
   - Iolanu is the source of truth
   - Framework documents universal principles
4. **Create meta/CONSISTENCY_NOTES.md** documenting:
   - How framework relates to story
   - Change process
   - Source of truth principle
5. **Update root README.md** to mention framework

### No New Repo Needed

**Benefits:**
- Everything in one place
- No sync issues
- Clear hierarchy (story → framework)
- Easy to maintain consistency
- Can still reference framework separately if needed

**For future stories:**
- Create new repos that reference framework
- Or add to this repo under `stories/` directory
- Framework remains extracted from Iolanu (first example)

---

## Example: How Framework Updates Work

### Scenario: You add a new First Child to Iolanu

**Current Situation:**
- Framework says "First Children can create worlds"
- You introduce a First Child in Iolanu who has never created a world

**Process:**
1. Add First Child to Iolanu story content
2. Check framework: Does it still accurately describe First Children?
3. Update framework if needed: "First Children CAN create worlds, but not all do"
4. Framework now reflects what exists in Iolanu

**Result:** No contradiction, framework updated to match story

### Scenario: Framework suggests a rule that contradicts Iolanu

**Current Situation:**
- Framework says "Soul transfer always requires greyrose"
- But in Iolanu, you want a different mechanism

**Process:**
1. Check contradiction: Does Iolanu need this mechanism?
2. Iolanu is source of truth
3. Update framework: "Soul transfer mechanisms vary. In Iolanu, greyrose is used. Other worlds may use different mechanisms."
4. Framework now allows variation based on Iolanu reality

**Result:** Framework adapts to story, not vice versa

---

## Consistency Notes Document Template

```markdown
# Consistency Notes

## Source of Truth Principle

**Iolanu story details are the primary source of truth.**

The framework in `oververse/` extracts universal principles from Iolanu.
It documents what exists, not what should exist.

## Change Process

1. Story changes → Update framework to match
2. Framework change → Check against story → If contradiction, story wins
3. Document exceptions or intentional expansions

## Known Relationships

- Framework cosmology matches Iolanu cosmology
- Framework First Children examples are Nala and Zeta from Iolanu
- Framework soul transfer mechanism based on Iolanu greyroses
- Framework liberation structure based on Nala's plan in Iolanu

## Future Stories

When creating new stories:
- Use framework as guide
- Framework allows variation (doesn't impose rigid rules)
- New stories inform framework evolution
- Framework documents patterns, not restrictions
```

---

## Recommendation

**Keep everything in this repository.**

1. Add `oververse/` directory with framework documents
2. Add `meta/CONSISTENCY_NOTES.md` explaining the relationship
3. Update root README to mention framework
4. Treat framework as "extracted from Iolanu" not "applied to Iolanu"
5. When changes happen, Iolanu wins, framework adapts

This gives you:
- Single source of truth
- No sync issues
- Clear hierarchy
- Framework as documentation, not imposition
- Can still reference framework separately for future stories

**No need for a separate repo** unless you specifically want to publish just the framework separately (which you can still do by copying oververse/ directory).

