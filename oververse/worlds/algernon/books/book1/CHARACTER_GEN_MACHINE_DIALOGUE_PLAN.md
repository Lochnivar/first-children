---
title: Character Generation — machine dialogue (plan)
status: Deferred — implement in prose when ready
note: TheWay rules live in the sibling `theway` repo; paths below use `theway/` as shorthand.
---

# Character Generation Machine Dialogue — Plan

## Context Summary

**Boot-up style** (from [Chapter 1](./Chapter%201)):

- Code blocks with nested bullet lists
- Status markers: `COMPLETE`, `IN PROGRESS [%]`, `INCOMPLETE`
- Technical jargon (QWAN, Cayminus, Pineal Gland, Amygdala, QRVI)
- Encoded terms: `'LGRNN` = Algernon

**Story beats** (from [book1-orcus-sapiens.md](../../plots/arcs/book1-orcus-sapiens.md) and [charlie.md](../../characters/main/charlie.md)):

- Character Gen = Orcus Sapiens revelation + choice to stay human
- Charlie: lumberjack (physical labor), level 5 start, no prior literacy in Path rules or participant UI (first exposure to TheWay as enforced system)

**Mechanical authority:** **TheWay** (`theway/CORE/08-Character-Creation.md`, Path Matrix, DOCS). Algernon in-fiction presents this as `'LGRNN` / QWAN questing OS terminology.

**Fiction vs TheWay:** **Countdown timeouts** and “default on expiry” in the HUD are **literary tools** (pressure, overwhelm, Charlie failing to parse the UI)—**not** TheWay rules at the table unless you deliberately add them later. At the table, Training Montage and assessment prompts are **player/GM choice** with no clock. **Defer → +2 to Primary Path** in this plan is an **Algernon trial-OS story beat** for Charlie; do not treat it as core TheWay until/unless `theway/CORE/08-Character-Creation.md` says so.

**TheWay mechanics** (from `theway/CORE/08-Character-Creation.md`):

- Primary Path determines ability array (STR=15/14/12/10/8/8, etc.)
- Training Montage: +2 one stat OR +1 two stats
- Primary Path names: Tough (STR), Quick (DEX), Hardy (CON), Smart (INT), Wise (WIS), Bold (CHA)
- Charlie's background (lumberjack) maps cleanly to **STR Path (Tough)** — "You grew up strong through physical labor"

---

## Suggested Machine Dialogue Blocks

### Block 1: Race Selection (Emotional Pivot)

This is the core beat. The system reveals birth race and offers the choice.

```
    * RACE/SKIN SELECTION -- AWAITING PARTICIPANT INPUT
        - BIRTH SUBSTRATE DETECTED: ORCUS SAPIENS
            - Designation: Adversarial Template / Trial Mob
            - Skin Options Available:
                [A] ORCUS SAPIENS (Native) -- Default Adversarial Stats / Might-Makes-Right Protocols
                    -- OPTION INELIGIBLE FOR SELECTION (Adversarial/NPC designation)
                [B] HOMO SAPIENS (Converted Baseline) -- Human Skin / Participant Stats
                [C] OTHER -- Expand to see options
                    - [C1] PACHI -- Restitution-based / Genetic framework
                    - [C2] CHELONARI -- Chain coherence
                    - [C3] CAYMINUS -- Contractual
                    - [C4] KITSUNE -- Word-bound
                    - [C5] CAPRA -- Territorial
                    - [C6] [Additional species per genetic repo...]
        - RECOMMENDATION: [A] for trial efficiency. [B] for... legacy substrate retention.
        - SELECTION REQUIRED TO PROCEED
```

**Rationale:** Dry, procedural tone. [A] is greyed out—Orcus are NPC/adversary designation, not participant-eligible (per FC meta). The system still lists it (birth substrate) but marks it ineligible. [C] expands to the genetic repo "salad bar" (Pachi, Chelonari, Cayminus, Kitsune, Capra per FC meta)—world-building depth for readers who recognize the species, but Charlie has no context and would likely ignore it. "Legacy substrate retention" is the system's oblique way of acknowledging Charlie's lived human experience. The recommendation may still nudge toward [A] (trial efficiency) despite ineligibility—system logic vs. rules—or it could recommend [B] as fallback.

---

### Block 1b: Staff/Homo Options (Triggered by Charlie's Mutter)

Charlie reads the options and mutters *"What, no Elf"* to himself—verbalizing the thought in his head. The system responds via thought detection (Pineal/Amygdala interface) and generates an expanded block with Staff/Homo options as [D].

```
    * RACE/SKIN SELECTION -- SUPPLEMENTARY OPTIONS LOADED
        - PARTICIPANT THOUGHT DETECTED: [phonetic match: "elf"]
        - MATCH FOUND: HOMO SYLVANIUS (Elf)
        - STAFF/HOMO DESIGNATION -- Expand to see options
            - [D] STAFF/HOMO -- Designated Staff Species (Genus Homo)
                - [D1] HOMO SAPIENS -- Generalist staff / Baseline
                - [D2] HOMO GOBLINUS -- Admin / Record-keepers / Protocol
                - [D3] HOMO SYLVANIUS -- [Elf]
                - [D4] [Additional Homo variants per genetic repo...]
        - RECOMMENDATION: [A] for trial efficiency. [B] or [D1] for legacy substrate retention.
        - SELECTION REQUIRED TO PROCEED
```

**Rationale:** Charlie's folk label (*elf*) maps to TheWay/FC taxonomy—Homo Sylvanius. The system surfaces it under Staff/Homo [D3]. His mutter is half-snark, verbalizing the thought in his head; the Pineal/Amygdala interface picks it up directly (thought detection, not voice). [D1] Homo sapiens is the same as [B] but framed as Staff designation; Charlie might not notice the distinction.

---

### Block 2: Primary Path Assignment (TheWay Mapping)

After race choice, the system assigns Path based on substrate scan (his life = physical labor).

```
    * PRIMARY PATH ASSIGNMENT -- IN PROGRESS
        - SUBSTRATE LIFECOURSE ANALYSIS... COMPLETE
            - Occupational Signature: Physical Labor / Forestry Extraction
            - Suggested Path: STR (Tough) -- "You grew up strong through physical labor"
        - ABILITY ARRAY LOCKED:
            - STR 15 | CON 14 | DEX 12 | WIS 10 | INT 8 | CHA 8
        - PRIMARY PATH ABILITY: TOUGH -- Installed
        - Do you accept this assessment or wish to generate your own?
            - CAUTION: Customization may result in unfavorable stats or skill choices.
            - [Accept] [Customize] -- DEFAULT: Accept (timeout 60s)  ← fiction only; see Fiction vs TheWay above
```

**Rationale:** TheWay's STR Path array and flavor text fit Charlie exactly. "Forestry Extraction" is the system's clinical term for lumberjacking. The array is the standard STR Path from `theway/CORE/08-Character-Creation.md`. The accept/customize prompt gives Charlie agency; in prose he may accept without engaging Customize (timeout as narrative pressure, not a TTRPG rule)—no literacy yet in Path-assignment tradeoffs or TheWay character creation flow.

---

### Block 3: Training Montage (Optional Customization)

TheWay's Training Montage: +2 one stat OR +1 two stats. Charlie has no Path-rules literacy yet, so he might not engage—the defer default applies.

```
    * TRAINING MONTAGE -- AWAITING PARTICIPANT INPUT (Optional)
        - Allocate preparation bonus:
            [1] +2 to one ability score
            [2] +1 to two different ability scores
        - DEFAULT: Defer assignment (timeout 60s)  ← fiction only
        - DEFERRED: +2 applied to Primary Path (P-tier) ability  ← Algernon trial resolution; not core TheWay unless written in
```

**Rationale:** In fiction, timeout/defer reads as the OS moving on without losing the bonus—+2 lands on Primary Path ability (STR for Charlie). Serves disorientation and avoids a “wasted” beat. At the TheWay table, players choose montage allocation explicitly; no timer unless the table wants a house rule.

---

### Block 4: Advanced Path (Level 5 Start)

Charlie starts at level 5 per [charlie.md](../../characters/main/charlie.md). He needs an Advanced Path choice. Charlie selects [C] DEX — Ranger/Scout (STR/DEX hybrid). Build: Tough/Quick.

```
    * ADVANCED PATH SELECTION -- AWAITING PARTICIPANT INPUT
        - LEVEL 5 START DETECTED (Adult/Background Start Protocol)
        - Primary Path: STR (Tough) -- Locked
        - Advanced Path Options:
            [A] STR -- Fighter (Pure) -- Melee specialization
            [B] CON -- Barbarian (Hybrid) -- Power of body / Endurance
            [C] DEX -- Ranger / Scout (Hybrid) -- Adaptability
            [D] WIS -- Paladin (Hybrid) -- Judgment / Divine
            [E] INT -- Battlemage (Hybrid) -- Knowledge / Arcane
            [F] CHA -- [Descriptive] (Hybrid) -- Force of will
        - RECOMMENDATION: [A] or [B] based on substrate resilience profile
        - SELECTION REQUIRED TO PROCEED
```

**Rationale:** Presents the **Advanced Path** step per TheWay `theway/CORE/03-Path-Matrix.md` and `theway/DOCS/Path-Naming-Convention.md`. Labels (Fighter, Barbarian, Ranger, Paladin, Battlemage, etc.) are **TheWay** canonical pure/hybrid names. Charlie's pick is STR Primary + DEX Advanced — presented here as Ranger/Scout (adaptability); lock final TheWay hybrid label when you reconcile STR/DEX with the naming doc. [A] STR/STR and [B] STR/CON remain valid recommendations; he chooses [C] for agency. Fits forestry work: terrain, woods, hazards.

---

### Block 5: Derived Stats / Completion

```
    * DERIVED STATS CALCULATION... COMPLETE
        - Hit Points: [CON-based]
        - Strain Max: [Sum of skill-die averages]
        - Armor Class: 10 + DEX (unarmored baseline)
    * CHARACTER GENERATION -- COMPLETE
    * 'LGRNN ORIENTATION -- IN PROGRESS
```

**Rationale:** Mirrors the completion pattern from the biological scan block. Keeps TheWay terms (Strain, skill-die) in-system. Specific numbers can be filled when you lock Charlie's build.

---

## Integration Notes

1. **Order of blocks:** Race first (emotional pivot), then Path/abilities (mechanical), then completion. Race choice should land before or right after the decontamination/clothing destruction—so Charlie is naked, disoriented, and then confronted with "you're Orcus Sapiens, pick a skin."
2. **Charlie's reaction:** He doesn't understand the options. "Legacy substrate retention" and "trial efficiency" mean nothing to him. He picks human because it's the only thing that matches what he knows he is. The system's dry recommendation for Orcus makes his refusal more pointed.
3. **Advanced Path:** Charlie chooses [C] DEX — Ranger/Scout (STR/DEX hybrid). Build: Tough/Quick. [A] and [B] remain valid recommendations; his choice represents agency over the system's suggestions. Fits forestry work: reading terrain, moving through woods, reacting to hazards.
4. **Terminology:** The mechanical truth is **TheWay** (Path, Strain, skill die, MADRT, Path Matrix). Algernon's HUD may alias terms (e.g. PATHS Protocol, Energetic Load) but the rules are TheWay. `theway/DOCS/AI-Refresher-Sheet.md` is the quick rules anchor. Strain remains central to Charlie's arc (skin vs. Orcus template under load).

---

## Optional: Condensed Single Block

If you prefer one scroll instead of several:

```
    * CHARACTER GENERATION -- IN PROGRESS
        - RACE/SKIN: ORCUS SAPIENS (Birth) | HOMO SAPIENS (Selected) -- COMPLETE
        - PRIMARY PATH: STR (Tough) -- Substrate Analysis Match -- COMPLETE
        - ABILITY ARRAY: STR 17 | CON 14 | DEX 12 | WIS 10 | INT 8 | CHA 8 -- Post-Training Montage (base STR 15 +2 P-tier)
        - TRAINING MONTAGE: Deferred -- +2 to Primary Path (STR) -- COMPLETE
        - ADVANCED PATH: DEX (Ranger/Scout) -- Charlie selected -- COMPLETE
        - DERIVED STATS: HP/Strain/AC -- Calculated
    * CHARACTER GENERATION -- COMPLETE
```

Use when you want one HUD scroll: still reflects Charlie's agency on Advanced Path [C]; Training Montage deferred, not skipped.
