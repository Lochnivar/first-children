# Framework-Primary Structure: Iolinus as Subordinate Story

## Revised Approach: Over-Universe as Primary

Since Iolinus is a **subordinate book within Hypatia**, the framework is the source of truth, not Iolinus.

### Core Principle

**Hypatia framework defines the rules. Iolinus must conform to those rules.**

This is like Brandon Sanderson's Cosmere:
- Cosmere rules are established
- Individual series (Mistborn, Stormlight) conform to those rules
- If a story contradicts Cosmere rules, the story changes (or rules expand)

---

## Recommended Structure: Single Repo, Framework Primary

```
over-universe-repo/
├── README.md                          # "Over-Universe Framework"
│   # This repo contains the universal framework and all stories within it
│
├── FRAMEWORK.md                       # Hypatia framework (PRIMARY)
│   # Source of truth for universal rules
│
├── worlds/                            # All stories/worlds (SUBORDINATE)
│   ├── README.md                      # Index of all worlds
│   ├── iolinus/                       # Iolinus story (one example)
│   │   ├── README.md                  # "Iolinus: A world in Hypatia"
│   │   ├── [all Iolinus content from current repo]
│   │   └── CONSISTENCY_CHECK.md       # How Iolinus conforms to framework
│   └── [future-world]/                # Future stories
│
├── hypatia/                         # Detailed framework docs
│   ├── cosmology.md
│   ├── metaphysics.md
│   ├── rules.md                       # What must be consistent
│   └── guidelines.md                  # How stories must conform
│
└── meta/
    ├── CONSISTENCY_PROCESS.md         # How to handle contradictions
    └── CHANGE_LOG.md                  # Framework changes and story updates
```

---

## Consistency Strategy: Framework Wins

### Change Flow: Framework → Stories

**Direction of Authority:**
1. **Framework is PRIMARY** (source of truth)
2. **Stories (including Iolinus) are SUBORDINATE** (must conform)
3. **When framework changes**, stories update to match
4. **When story contradicts**, story changes OR framework expands (if intentional)

### Handling Contradictions

**Process for contradictions:**

1. **Framework Change:**
   - Update FRAMEWORK.md
   - Check all worlds/ for contradictions
   - Update worlds that contradict
   - Document in CHANGE_LOG.md

2. **Story Change That Contradicts Framework:**
   - Identify the contradiction
   - Decide: Is this an intentional expansion of framework?
     - **If YES:** Update framework first, then story
     - **If NO:** Change story to conform to framework
   - Document decision in world's CONSISTENCY_CHECK.md

3. **New Story Element:**
   - Check against framework
   - If it fits, add to story
   - If it expands framework, update framework first
   - If it contradicts, change the element

---

## Implementation: Migrate Iolinus to Framework-Primary Structure

### Option 1: Create New Repo, Copy Iolinus Into It

**Steps:**
1. Create new repo (e.g., `over-universe` or `multiverse`)
2. Copy OVER_UNIVERSE_FRAMEWORK.md → FRAMEWORK.md (root)
3. Copy entire Iolinus repo → `worlds/iolinus/`
4. Create hypatia/ directory with detailed docs
5. Create meta/CONSISTENCY_PROCESS.md
6. Update worlds/iolinus/README.md to state it's subordinate
7. Create worlds/iolinus/CONSISTENCY_CHECK.md documenting how it conforms

**Result:** Clean structure, framework primary, Iolinus subordinate

### Option 2: Restructure Current Iolinus Repo

**Steps:**
1. Create `hypatia/` directory
2. Move OVER_UNIVERSE_FRAMEWORK.md → `hypatia/FRAMEWORK.md`
3. Create `hypatia/README.md` stating it's primary source of truth
4. Wrap existing content in `worlds/iolinus/` structure:
   - Move characters/ → `worlds/iolinus/characters/`
   - Move world-building/ → `worlds/iolinus/world-building/`
   - Move locations/ → `worlds/iolinus/locations/`
   - Move plots/ → `worlds/iolinus/plots/`
   - Move relationships/ → `worlds/iolinus/relationships/`
   - Move timeline/ → `worlds/iolinus/timeline/`
   - Move meta/ → `worlds/iolinus/meta/`
5. Create `worlds/iolinus/README.md` stating it's subordinate to framework
6. Create `worlds/iolinus/CONSISTENCY_CHECK.md`
7. Create `meta/CONSISTENCY_PROCESS.md` at root
8. Update root README.md to reflect framework-primary structure

**Result:** Current repo restructured, framework primary

---

## Consistency Process Document Template

```markdown
# Consistency Process

## Source of Truth

**The framework in `hypatia/FRAMEWORK.md` is the PRIMARY source of truth.**

All stories in `worlds/` are SUBORDINATE and must conform to framework rules.

## When Framework Changes

1. Update `hypatia/FRAMEWORK.md`
2. Check all worlds in `worlds/` for contradictions
3. Update any world that contradicts
4. Document in `meta/CHANGE_LOG.md`:
   - What changed in framework
   - Which worlds were affected
   - How worlds were updated

## When Story Contradicts Framework

1. Identify the contradiction
2. Decide: Intentional expansion or mistake?
   
   **If Intentional Expansion:**
   - Update framework first to accommodate
   - Then update story
   - Document as framework evolution
   
   **If Mistake:**
   - Change story to conform
   - Document why change was needed
   - Update story's CONSISTENCY_CHECK.md

3. Document decision in story's CONSISTENCY_CHECK.md

## Framework Expansion vs. Contradiction

**Framework Expansion:** Story introduces new element that doesn't contradict, just expands understanding
- Example: New First Child with different personality
- Example: New world with different magic manifestation
- Process: Add to framework as new example/variation

**Contradiction:** Story violates established framework rule
- Example: Story says "First Children can't create worlds" but framework says they can
- Example: Story violates established cosmological constant
- Process: Story must change OR framework rule was wrong and needs correction

## Review Process

- Before major story changes, check framework
- Before framework changes, check all stories
- Regular consistency audits (quarterly?)
- Document all changes
```

---

## Worlds/Iolinus Structure

```
worlds/iolinus/
├── README.md                          # "Iolinus: A World in Hypatia"
│   # States: This world conforms to Hypatia framework
│   # Links to hypatia/FRAMEWORK.md
│
├── CONSISTENCY_CHECK.md               # How Iolinus conforms to framework
│   # - Which framework elements it demonstrates
│   # - How it uses universal rules
│   # - Any intentional variations or expansions
│   # - Last consistency audit date
│
├── characters/                        # Iolinus characters
├── world-building/                    # Iolinus world-building (story-specific)
├── locations/                         # Iolinus locations
├── plots/                            # Iolinus plots
├── relationships/                     # Iolinus relationships
├── timeline/                          # Iolinus timeline
└── meta/                             # Iolinus meta-docs
    ├── PREMISE_TONE_PERSPECTIVE.md
    └── AI_REFRESHER.md
```

### Iolinus README Template

```markdown
# Iolinus

**Status:** Story/World in Hypatia  
**Framework Conformance:** [Status]  
**Last Consistency Check:** [Date]

## Overview

Iolinus is one world/story within the [Over-Universe Framework](../hypatia/FRAMEWORK.md).
This world demonstrates various framework concepts while telling its own story.

## Framework Elements Demonstrated

- First Children: Nala and Zeta/Malachor
- World Creation: Iolinus created against prohibition
- Life Force Binding: Zeta bound to his creation
- Soul Transfer: Earth souls transported via greyrose mechanism
- Liberation Operation: Nala's plan to free Iolinus
- Quantum Abilities: Five fragments manifested in mortals

## How This World Conforms

- [List specific ways Iolinus follows framework rules]
- [Note any intentional variations]
- [Reference framework sections]

## Consistency

See [CONSISTENCY_CHECK.md](CONSISTENCY_CHECK.md) for detailed conformance documentation.

## Framework Reference

Hypatia framework is the source of truth: [Framework Documentation](../hypatia/FRAMEWORK.md)
```

---

## Handling Your Concern: Framework Changes

### The Real Solution: Version Control + Process

**With framework-primary structure, you need:**

1. **Clear Process Document** (meta/CONSISTENCY_PROCESS.md)
   - Defines what to do when contradictions arise
   - Provides decision tree
   - Documents changes

2. **Consistency Check Documents** (one per world)
   - Documents how each world conforms
   - Updated when framework changes
   - Audit trail of conformance

3. **Change Log** (meta/CHANGE_LOG.md)
   - Tracks framework changes
   - Records which worlds were affected
   - Shows evolution over time

4. **Pre-Change Checks**
   - Before framework change: Check all worlds
   - Before story change: Check framework
   - Document impact before making change

### Automation Helps But Process is Key

You could:
- Create a checklist script that checks for contradictions
- Use tags/comments in files linking to framework
- Regular consistency audits

But the main solution is:
- **Clear process** for handling changes
- **Documentation** of decisions
- **Review** before changes
- **Single source** (framework) that stories reference

---

## Recommendation

**Use Option 1: Create New Repo with Framework-Primary Structure**

1. Create new `over-universe` repo
2. Copy framework to root (FRAMEWORK.md)
3. Copy Iolinus to `worlds/iolinus/`
4. Set up consistency process documents
5. Establish clear "framework is primary" principle

This gives you:
- Clean separation: framework vs. stories
- Clear hierarchy: framework wins
- Scalability: easy to add more worlds
- Single repo: no sync issues
- Process: clear way to handle contradictions

**Key:** The consistency solution is **process and documentation**, not structure. The structure just makes it clear which is primary.

---

## Example: Handling a Contradiction

### Scenario: Framework says "All First Children have Quantumancy"
### But: You want a First Child in a new story who doesn't

**Process:**

1. **Identify contradiction**
   - Framework: "First Children have Quantumancy"
   - New story wants First Child without Quantumancy

2. **Decide: Expansion or violation?**
   - Expansion: Can framework accommodate variation?
   - Violation: Does this break fundamental rule?

3. **If expansion:**
   - Update framework: "First Children typically have Quantumancy, but variations exist..."
   - Then add First Child to new story
   - Document as framework evolution

4. **If violation:**
   - Either: Change new story (First Child must have Quantumancy)
   - Or: Revisit framework rule (maybe it was too strict?)

5. **Document:**
   - In CHANGE_LOG.md: What changed and why
   - In new story's CONSISTENCY_CHECK.md: How it conforms
   - In framework: Updated rule or variation

**Result:** Clear process, documented decision, framework remains authoritative but can evolve

