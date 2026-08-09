# QSON — The First Children's Descriptive Notation

**Status:** Framework Element - Universal (Background / Speculative — a depth layer, not required story knowledge)
**Category:** Metaphysics / Universal Forces
**Related:** [Quantum Foundation](quantum-foundation.md), [Coherent Patterns](coherent-patterns.md), [Souls and Identity](souls-and-identity.md), [First Children](../cosmology/first-children.md), [Genetic Frameworks](../races/genetic-frameworks.md), [../../FRAMEWORK.md](../../FRAMEWORK.md)

## Overview

QSON is not the quantum substrate itself — it's the First Children's own notation for describing it. The substrate (see [Quantum Foundation](quantum-foundation.md)) is the actual "vast, indifferent quantum sea." QSON is the FC's working model of that sea: a comprehension tool, the same way the Library metaphor is a comprehension tool for Hypatia as a whole. It is a map, not the territory, and it is entirely possible for it to be incomplete or approximate even in FC hands.

Structurally, QSON is a small, fixed, recursive schema — the same shape whether it's describing a quark or a kitsune queen. Complexity lives in the data (how deep the nesting goes, how many components a thing has), never in the format itself. This is deliberate: a notation that had to grow new kinds of complexity to describe bigger things would not have survived as a "communal, open-source" FC tool (see [Genetic Frameworks](../races/genetic-frameworks.md)).

```
{ id, type, properties: {...}, dimensions: [...], components: [...] }
```

- **id** — identifier for this pattern
- **type** — what kind of thing this is (excitation, particle, atom, organism, etc.)
- **properties** — static/qualitative attributes of the pattern
- **dimensions** — the reinforcement/relationship edges that hold the pattern together (see below)
- **components** — nested sub-patterns this thing is composed of (empty at the excitation floor)

## Why It's Not Reality Itself

Keeping QSON as a notation rather than the substrate matters for consistency: `library/index.md` and `FRAMEWORK.md` both already establish that "no mortal—and few of the First Children—will ever grasp the true nature of Hypatia," and that the Library metaphor is "purely conceptual... not a literal description." QSON has to sit on the FC side of that line, not replace it. FC writing and reading QSON are working with their own formalization of the substrate, not with the substrate directly — which leaves room for the formalization to be wrong, lossy, or contested between FC lineages, same as any modeling language.

**Note on the name:** "QSON" is framework/author-facing shorthand for this concept, not necessarily a term any First Child would say out loud. Treat it the way "theway" or "wetware" are treated elsewhere in the framework — internal vocabulary for describing a mechanic, not guaranteed in-world terminology.

## The Existence Floor: Excitation Points

The base primitive of QSON is the field excitation:

```
{ id: <long unique identifier>, frequency: <value>, xyz: <coordinates> }
```

- **id** and **frequency** identify what the excitation is.
- **xyz** is literally its physical location on the three-dimensional frame — a real coordinate, not a metaphor.

This is deliberately just bookkeeping. Having a location and a frequency doesn't make a point "real" in the sense that matters to the rest of the cosmology — a lone, unlinked excitation is functionally indistinguishable from quantum noise. That's what **dimensions** are for.

## Dimensions: The Reinforcement Layer

Where "properties" describe what a point *is*, "dimensions" describe how it's *linked* to other points — and linkage, not location, is what `foundational-cosmology.md` already defines as the source of physicality: "something becomes physical through its entanglement and interaction with surrounding waveforms. The more interactions constrain a waveform, the more solid and real it becomes."

Two dimension-types are already implied by existing framework docs, independently, before QSON gave them a shared name:

- **Physical/entanglement dimension** — edges are mutual interaction with surrounding waveforms. Dense, strong edges = solid matter. Loosen them and the result is the "looser" coherent patterns described in [Coherent Patterns](coherent-patterns.md) (ghosts, spirits).
- **Narrative/identity dimension** — edges are the causal memory links described in [Souls and Identity](souls-and-identity.md) ("I am angry BECAUSE he betrayed me"). A thick, redundant chain is a stable soul; a thin chain dissolves easily. This dimension needs no physical anchoring at all — it's self-sustaining by definition.

A living mortal runs both dimensions at once (physically anchored *and* self-anchored). Death is the physical dimension collapsing; whether a ghost results depends entirely on whether the narrative dimension is still holding on its own.

**Open question, left deliberately unresolved:** are these two dimension-types a closed set, or is "dimension" an open-ended category any FC could add a new kind to? Open-ended fits the repo's established lack of governance better; closed is tidier. Not decided.

## Particle Level and Upward Stacking

A particle-level document references excitation IDs as its components:

```
{ id: <particle id>, type: "proton", components: [<quark excitation ids>], properties: {...} }
```

Everything above that — atoms, molecules, organs, organisms — is more of the same operation: stacking components, adding dimensions, compressing logarithmically as you go up. A human body's QSON does not enumerate its ~10²⁸ particles any more than a species entry in the genetic repo enumerates every cell; it references known, already-resolved patterns instead of re-deriving them, for the same reason the genetic repo is fork-and-reuse rather than build-from-scratch (see below).

**The middle of that stack is intentionally not fully defined.** This isn't a gap to fill in later — it's consistent with what the cosmology already says about itself. `foundational-cosmology.md` states even the most empathetic FC can't fully bridge to mortal experience; `library/index.md` states few FC grasp Hypatia's true nature. A stack that even its regular users don't trace end-to-end is the correct epistemic state for this cosmology, not an oversight. FC use compressed layers the way a programmer uses a library function — trusting the compression without personally verifying every instruction underneath.

## Recipes, Not Templates: The Genetic Repository in QSON

[Genetic Frameworks](../races/genetic-frameworks.md) already describes the FC's shared species repository in explicitly fork/modify/contribute-back terms. QSON gives that repository its actual file format — but the entries are better understood as **recipes** than as templates with inheritance. A recipe is a stacking procedure (combine these components, at these dimensions, in this order), not a class definition to extend. Individual named instances aren't "child records" of a parent template — they're built by running the recipe and then stacking further, world- and instance-specific layers on top.

This also explains why the repo is "sprawling, no governance, and occasionally contradictory" (per `genetic-frameworks.md`): without a shared schema authority, different FC lineages' recipes drift — inconsistent conventions, undocumented shortcuts, dialects that don't quite match. That's texture, not a bug — and it's a standing joke MJFL's already primed for, given his bio already calls the manuscripts "uneven."

## Design-Time vs. Runtime: QSON and Quantumancy

Writing or editing a QSON document is descriptive, not causal. It says what a pattern *should* look like. Making the substrate actually conform to that description is [Quantumancy](../magic-systems/quantumancy.md) — collapsing probability into the described state. Holding that state without constant attention requires an **Anchor** (see [Quantum Foundation](quantum-foundation.md), the Persistence Problem). QSON is the blueprint; Quantumancy is what executes it; an Anchor is what keeps it running unattended.

This gives "forking" real teeth as a concept, not just a metaphor: an illegal world-fork (see Iolanu's Malachor/Zeta) can be read as copying a QSON subtree — a world, a soul-set — without peer authorization, then personally anchoring the divergent branch. It's a specific, describable act with a specific victim (the unauthorized copy), not just a narrative label for "did something bad."

## Who Can Perceive It

FC work with QSON directly as their notation, though per the section above, even they don't trace it to the excitation floor in ordinary use. At the mortal level, **Weavers** are the existing answer to "who else can see this": they're already defined (see [Quantumancy](../magic-systems/quantumancy.md)) as perceiving "quantum connections between people/things" and assessing the "health" of those threads. That's a raw, sensorial read of the dimensional layer — not literacy in FC notation, just picking up the same graph QSON formally describes.

## Identity Is Pattern, Not Substrate

Because excitation-level tokens are fungible (a frequency and a position, nothing more — any electron is interchangeable with any other) and identity lives entirely in the narrative dimension (per [Souls and Identity](souls-and-identity.md)), an entity's specific quanta are never "essentially" it. Swap every excitation in a body and the identity survives intact as long as the dimensional chain transfers with it. That's a free, already-consistent answer to resurrection-in-a-different-body, possession, and teleportation-continuity questions — no new rule required, just this framing made explicit.

Individual worlds remain free to violate this on purpose — a relic that's sacred specifically because it's the *literal same matter*, not just the same pattern — as a world-specific exception, not a framework contradiction.

## Naming as the Top of the Stack

At the far end of the compression, an ordinary name — "Name: Michael" — is just a meta-tag: a human-legible alias pointing at one fully-resolved (if never fully traced) QSON stack. Nobody, including the FC who could in principle read the whole thing, actually walks it top to bottom in practice; the name is the interface everyone actually uses.

**Unresolved thread, not asserted here:** whether First Speech "true names" (the Thohalla `A'` convention, etc.) sit conceptually closer to the root of the stack than a mortal nickname does. Worth revisiting if First Speech gets developed further, not decided now.

## Open Questions

- Closed vs. open-ended set of dimension-types.
- Whether QSON has any spoken in-world name FC actually use, or stays purely a reader/author-facing model.
- Whether excitation IDs carry traceable provenance (relevant to Echo-type forensic reconstruction) or are opaque tokens.

## Framework Note

This is an optional depth layer. Nothing currently in the framework requires QSON to be named on the page, and most stories never need to surface it. Its job is internal consistency for world-building, not a system any character needs to reference directly.

---

*For quantum foundation, see [quantum-foundation.md](quantum-foundation.md)*
*For coherent patterns (ghosts/spirits), see [coherent-patterns.md](coherent-patterns.md)*
*For souls and identity, see [souls-and-identity.md](souls-and-identity.md)*
*For the genetic repository, see [../races/genetic-frameworks.md](../races/genetic-frameworks.md)*
*For framework overview, see [../../FRAMEWORK.md](../../FRAMEWORK.md)*
