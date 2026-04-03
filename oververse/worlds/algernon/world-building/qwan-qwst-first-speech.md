# QWAN, QWST (First Speech), iQuest

**Purpose:** Canonical terminology for the questing stack (network → product → voice/UI). Use this to avoid conflating layers in prose, marketing, and cross-repo notes.

**Broader frame:** Universal **First Speech** naming patterns (world tokens, trial branding, phonetic estrangement) are summarized for the whole oververse in [First Speech conventions (trials & quest interfaces)](../../../mechanics/first-speech-conventions.md). **Cosmological** First Speech (glyphs, triconsonantal roots, Prime Author vocabulary, Malachor’s tag): [First Speech (cosmology)](../../../cosmology/first-speech.md). This file is the **Algernon / stack** detail.

**Not sacred subtext:** Naming choices below are **phonetic and structural**, not biblical or theological allegory. See [First Speech (design intent)](#first-speech-design-intent).

---

## QWAN — Quantum Wide Area Network

- **What it is:** Infrastructure / transport layer for wetware-linked questing systems (e.g. Pineal–Amygdala bridge, handshake, tokens).
- **What it is not:** The visible UI or the snarky voice. Characters rarely “see” QWAN except as technical readouts (`QWAN networking`, `QWAN Handshake`).

---

## QWST — First Speech (iQuest)

- **Branded name:** The official product string is **a leading grave accent / backtick (U+0060) immediately followed by `QWST`** — i.e. `` `QWST `` as characters, not “QWST” alone. In copy you may write **backtick-QWST** if a literal `` ` `` would break layout.
- **Role:** **First Speech** for **iQuest** — the participant-facing voice and console layer that sits *above* raw QWAN plumbing (compare: TCP/IP vs a given app’s UI).
- **In fiction:** The layer Charlie treats as the “snarky tin can”; official lines use `*` bullets; unofficial bleed uses `~` (see [TheWay Interface](theway-interface.md)).

**Publishing / Markdown:** A literal backtick can interact with Markdown or ebook renderers. In source files, escape or use inline code spans so the branded name renders as text, not broken formatting.

---

## iQuest

- **What it is:** The questing / orientation product stack that presents TheWay-aligned rules to participants (character generation, quests, level-up prompts, etc.).
- **Relationship:** QWAN carries the bits; **iQuest** is the stack; **QWST (First Speech)** is the voice/UI skin Charlie experiences as the primary dialogue channel.

---

## First Speech names (world / deployment) — universal trope

Across worlds and deployments, **First Speech** is not only the iQuest voice layer — it is also a **setting-wide convention** for how trials and quest OSes **label** a given reality: a **cryptic string** (compressed consonants, odd apostrophes, “unpronounceable” spellings) that reads **alien but patterned**, the same *kind* of orthographic quirk wherever participants are dropped. **Not** an Algernon-only joke; **universal in-universe trope**.

**Examples (canonical):**

| World / place | First Speech token | Notes |
|---------------|-------------------|--------|
| **Algernon** | `'LGRNN` | e.g. *'LGRNN Orientation Quest* — leading apostrophe as part of the string |
| **Atahom** | `'THM` | First Speech for Atahom; common Tahom; roots & lexicon: [First Speech — Atahom](../../atahom/world-building/first-speech-lexicon.md) |
| **Legara** | `LGRH` | First Speech for Legara |
| **Mercara** | `MRCRH` | First Speech for Mercara |

**Relationship to `` `QWST`` / iQuest:** **World tokens** (`'LGRNN`, `'THM`, `LGRH`, `MRCRH`, …) identify **which** deployment / reality the UI is bound to; **`` `QWST``** is **First Speech for the iQuest product** (the shared voice/shell) and can appear across those instances. Participants may see both: e.g. orientation under the world token while the snark layer remains the same class of system.

---

## First Speech — design intent

- **Scope:** The same principles apply to **world deployment tokens** (`'LGRNN`, `'THM`, `LGRH`, `MRCRH`, …) and to **product/voice** names (e.g. `` `QWST`` for iQuest).
- **Linguistic texture:** First Speech **echoes Semitic language concepts** in a **structural / phonetic** sense (e.g. pattern-like naming, register), so names feel **odd but still pronounceable** to many English readers.
- **Intent:** **Alien enough to be strange, close enough to be recognizable** — **phonetic estrangement**, not symbolism from scripture.
- **Explicitly not:** Biblical narrative, sacred-text allegory, or religious framing. Do not treat Semitic **sound-shape** as costume for holy themes.

---

## Quick reference

| Term | Layer |
|------|--------|
| **QWAN** | Network / technology (Quantum Wide Area Network) |
| **iQuest** | Questing product stack |
| **QWST** (branded: `` ` `` + QWST) | First Speech **for iQuest** — shared UI/voice layer |
| **`'LGRNN`**, **`'THM`**, **`LGRH`**, **`MRCRH`**, … | First Speech **for a world** — deployment token (universal naming trope) |
| **`~` (in HUD)** | Unofficial / side-channel mutter (not QWAN vs QWST confusion) |
