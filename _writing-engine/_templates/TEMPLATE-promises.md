---
Item_Prototype: LFW_Promises
Item_ID: "<manuscript-slug>-promises"
Title: "<Manuscript Title> — Setup/Payoff Ledger"
Date_Added:
Date_Modified:
lfw_manuscript: "<manuscript-slug>"
lfw_promises_version: 1
---

# <Manuscript Title> — Setup/Payoff Ledger

> **Tracks promises planted in the manuscript and whether they've been fired. Required for plot-driven fiction. SETUP-PAYOFF-AUDIT sessions (chapter 11 §4) work against this file.**

## Promises planted

*Every setup planted in the draft. Each entry: planted-in scene, character or situation it concerns, and the shape of the payoff it implies. The implied payoff is what makes the promise a promise rather than just a detail.*

### Promise 1 — <short name>

- **Planted in:** [[Scene-filename]]
- **Concerns:** *(character, object, situation)*
- **Implied payoff:** *(what shape will fire this promise)*
- **Status:** outstanding | fired | retired
- **Foreshadow trail:** *(scenes where the promise is reinforced before payoff)*

### Promise 2 — <short name>

*(repeat per promise)*

## Promises fired

*Every payoff delivered in the draft. Each entry: fired-in scene, original setup it discharges, and the earned-or-unearned verdict.*

### Payoff 1 — <short name>

- **Fired in:** [[Scene-filename]]
- **Discharges promise:** Promise N above
- **Earned?** earned | unearned | mixed
- **Notes:** *(if unearned, what setup is thin; if earned, what made it land)*

## Promises currently outstanding

*Setups planted but not yet paid off. Flag those outstanding for many chapters with no foreshadowing of imminent payoff.*

- **Promise N** ([[Scene-filename]]) — outstanding for N chapters; foreshadow trail: [[Scene-filename]], [[Scene-filename]]
- **Promise M** ([[Scene-filename]]) — outstanding for N chapters; **no foreshadow trail since the planting** — fading risk

## Payoffs without setups

*Reveals or moves that the reader will experience as arbitrary because they weren't planted. The unearned payoff is as deadly as the unfired Chekhov's gun.*

- **Payoff X** ([[Scene-filename]]) — needs setup added in: *(suggested earlier scene)*

## Promises retired

*Setups the writer has decided not to pay off. Often experimental setups that didn't survive revision. Documenting that they're retired prevents treating them as outstanding.*

### Retired promise 1 — <short name>

- **Originally planted in:** [[Scene-filename]]
- **Retired on:** <YYYY-MM-DD>
- **Reason:** *(brief)*
- **Action taken:** *(setup removed in revision pass / setup left as a "red herring" / setup repurposed)*

---

## How to use this file

For the AI:

- Read at session start when activity is SETUP-PAYOFF-AUDIT, READ-THROUGH, or BETA-PREP
- Cross-reference with `prefigures` relations in Scene Items — every `prefigures` should appear here as a promise; every promise should have a corresponding `prefigures`
- Update when a new scene plants a setup or fires a payoff
- Surface unfired or unearned promises during audits; don't silently rewrite

For the writer:

- Add a promise entry every time you plant something significant — don't trust your memory across hundreds of sessions
- Review the "currently outstanding" list periodically; retire what's not going to fire, write the payoffs for what is
- Use during revision: a draft's structural soundness is largely measured by this file
