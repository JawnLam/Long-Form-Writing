---
Item_ID: "<UUID>"
type: fped
title: "<working title>"
pov: "<POV character, or 'ensemble'>"
status: working          # working | parked | promoted | abandoned
intended_position: "<rough placement in the manuscript>"
written: <YYYY-MM-DD>
references: []           # relevant atom / spine / promises / continuity file paths this draft draws on
craft_notes: |
  What this FPED is trying to do; what's being planted; what worked and what didn't.
# promoted_to: Items/Scenes/<file>.md   # add ONLY when status: promoted — the canonical atom this graduated into; the FPED stays for provenance
---

# <working title>

> **FPED — Full Prose Exploratory Draft.** Write the scene/passage OUT in prose to feel out tone, voice, shape, or a character moment — WITHOUT committing to the canonical Scene/Section atom system. Always written-out prose (crude to nearly-final); never a shorthand fragment (that belongs in `_notes/` or an `Items/Notes/` atom). An FPED *references* canonical atoms but is not referenced *by* them until promoted.

<Write the full-prose draft here.>

---

## Craft notes

*What this draft is testing — voice, a turn, a character beat, structure. What's planted for later. What worked; what didn't. (Mirror the one-line summary in the `craft_notes` frontmatter; expand here.)*

## Lifecycle

- `working` — active candidate, still iterating
- `parked` — set aside, might revisit
- `promoted` — graduated into a canonical Scene/Section atom (`promoted_to` links it); this FPED stays for provenance
- `abandoned` — dead, but **kept indefinitely** (never delete an FPED; a discarded draft may matter later)
