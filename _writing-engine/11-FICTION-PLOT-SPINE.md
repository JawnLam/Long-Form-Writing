---
type: writing-engine
role: fiction-plot-spine
scope: fiction-screenplay-play
updated: 2026-06-02
lfw_load:
  tier: pack
  genres: [fiction, screenplay, play]
  activities: [SCENE-AUDIT, SETUP-PAYOFF-AUDIT, OUTLINE, READ-THROUGH]
  phase: on-demand
---

# 11 — FICTION PLOT AND SPINE

> **The argument backbone (chapter 10) is non-fiction's logical spine. This chapter is fiction's equivalent: the causal chain. Scenes connected by *and then* are a sequence; scenes connected by *but* and *therefore* are a plot. This chapter adds the artifacts and activities that make the difference visible.**

## Why this chapter exists

Three of the most common failure modes in fiction drafts are not stylistic and not character-level — they're upstream of both:

1. **Scenes don't turn.** A scene has setting and stakes and stated purpose, and at the end of it, nothing has changed. The character ends where they began; no value has shifted. Multiple no-turn scenes in a row are how a draft goes slack.
2. **The causal chain is and-then, not but-therefore.** Scene 4 happens. Then scene 5 happens. Then scene 6. Each scene may be interesting; together they're a sequence, not a plot. The reader's question "why did this happen *because* of what just happened" has no answer.
3. **Setups go unfired. Payoffs come unearned.** A gun introduced in chapter 2 disappears; a reveal in chapter 18 has no foundation in chapter 5. Both happen because no one's tracking promises across hundreds of sessions — which is the whole reason a stateful OV exists.

v1.0–v1.1 had container structure (`_outline.md`) but no causal structure. Scene atoms could capture "purpose" but not "turn." The Source relation vocabulary already contained `prefigures` and `parallels` — the literal bones of setup-and-payoff — but nothing in the engine used them as a discipline.

This chapter introduces the artifacts and activities that close all three gaps.

## Part one — `_spine.md`: the causal backbone

### What it is

`_spine.md` is fiction's analog to non-fiction's `_argument.md`. It tracks the manuscript's **causal structure** distinct from its **container structure**.

The container structure (in `_outline.md`) answers: *what's in the book and in what order.*

The causal structure (in `_spine.md`) answers: *why does each scene happen because of the one before, and what changes inside each scene.*

A novel whose outline and spine align is structurally sound. A novel where the outline contains scenes that the spine doesn't need — scenes that exist but don't cause anything and aren't caused by anything — has structural padding. A novel whose spine contains causal moves the outline doesn't dramatize has unrealized momentum.

### Required sections of `_spine.md`

1. **Premise as causal claim** — what's the *because* that makes this story have to happen? Not "a story about X" but "*because* [protagonist] [wants/fears X], *and because* [obstacle], the story must unfold." The premise as the root of the causal tree.
2. **The dramatic question** — what question does the entire manuscript answer? Stated as a yes/no or which/whether question that won't be settled until the climax. *Will she leave him? Will the city survive? Can the sisters reconcile?* The reader's reason to keep turning pages.
3. **Scene-by-scene value-shifts** — for each Scene atom, the state at the start and the state at the end. The list is the spine's primary content; if a scene's row reads "uncertain → uncertain," that scene doesn't turn and the spine has surfaced it.
4. **Cause→effect linkage between scenes** — for each scene-to-scene transition, the connector word: `but`, `therefore`, or (the warning sign) `and then`. A spine dominated by "and then" is not yet a plot.
5. **Escalation curve** — are the stakes actually rising scene by scene, or repeating at the same altitude? A novel where chapter 12 has the same emotional pressure as chapter 4 is flat, regardless of how interesting each individual chapter is.
6. **The mid-act crisis and the climax** — explicit identification of the manuscript's two highest-pressure moments and what value-shift each delivers.
7. **The honest open** — what's not yet causal in the current draft; where the writer suspects scenes exist for reasons other than causality and is willing to look at it.

### When `_spine.md` is required

- **Fiction** — required (novels, novellas, short-story collections with arc, novellas-in-flash)
- **Screenplay** — required (act structure makes causal chain especially visible)
- **Play** — required (every scene has a turn in good dramatic writing)
- **Non-fiction** — not applicable (use `_argument.md` instead)
- **Dissertation** — not applicable (use `_argument.md` instead)
- **Memoir / narrative non-fiction** — recommended (memoir has both an argument and a causal arc; both backbones are useful)

### How it interacts with `_outline.md`

The outline lists scenes in order; the spine annotates each scene with its causal role and value-shift. Renames in one should propagate to the other; the validator's wiki-link check catches most drift.

A good periodic check (during ARGUMENT-AUDIT or its fiction equivalent — see SCENE-AUDIT below): walk both files in parallel and look for scenes that appear in the outline but have no entry in the spine (structural padding) or moves in the spine the outline doesn't dramatize (unrealized causal beats).

## Part two — SCENE-AUDIT activity

### What it is

A diagnostic activity that examines a drafted Scene atom and tests three questions:

1. **Whose want drives this scene?** — every scene needs a protagonist *for that scene* (often but not always the manuscript's overall protagonist) with a clear want operating in this scene. If no one wants anything, the scene has no fuel.
2. **What's the conflict?** — what stands between the want and its satisfaction within this scene? External obstacle, internal hesitation, opposing character, time pressure, secret. If there's no conflict, the scene is exposition wearing a scene's clothes.
3. **What's different at the end than the beginning?** — the value-shift test. The scene moves from one state (safe, hopeful, ignorant, allied) to its opposite or to a meaningful change. If start-state = end-state, the scene doesn't turn.

The third question is the load-bearing one. It's the most teachable fiction skill the engine ignored in v1.0–v1.1.

### Trigger conditions

- A Scene atom is in `drafted` status
- The Scene's `lfw_value_shift_from` and `lfw_value_shift_to` fields are not yet populated, OR they're populated but identical (no turn declared)
- 3+ consecutive scenes have been drafted without a SCENE-AUDIT on any of them
- The writer flags SCENE-AUDIT explicitly

### Protocol

1. AI reads the target Scene atom in full
2. AI reads the relevant `_spine.md` entry for this scene
3. AI reads the Scene's parent Chapter for surrounding context
4. AI applies the three tests:
   - Whose want drives this scene? Is it visible in the prose?
   - What's the conflict? Is it on the page or only in the writer's intention?
   - What's different at the end? State the start-state and end-state in the AI's own words and compare.
5. AI produces a report:
   - **The driving want** — who, what, evidenced where in the prose
   - **The conflict** — what opposes the want, visible where
   - **The value-shift** — start-state → end-state (or "no detectable shift")
   - **The but/therefore connector to the next scene** — is this scene caused by the previous one, and does it cause the next one?
   - **Verdict** — does the scene turn? If yes, the AI updates the Scene's frontmatter (`lfw_value_shift_from`, `lfw_value_shift_to`). If no, the AI flags the scene as `scene-doesnt-turn` in `_spine.md`'s honest-open section.

### Discipline

The AI does NOT rewrite the scene to make it turn. SCENE-AUDIT is diagnostic. The writer decides whether the scene needs revising, cutting, or merging — or whether the "no turn" diagnosis is actually wrong (some scenes work as interludes; mood pieces; quiet beats between turns). The verdict is "no detectable turn"; the writer's call is "does it need one."

### Failure mode this catches

**F22 — scene-doesn't-turn.** The single most common structural flaw in drafts and the one writers most need trained out of themselves.

## Part three — `_promises.md`: the setup/payoff ledger

### What it is

Most plots run on **promises**: a setup planted in chapter 2 that pays off in chapter 18, a character behavior in scene 5 that recontextualizes a scene 31 reveal, a piece of information dropped early that becomes load-bearing late. The reader's pleasure in fiction is significantly about promises being kept.

The OV's stateful nature makes promise-tracking possible across hundreds of sessions. v1.0–v1.1 had the `prefigures` relation in the vocabulary but no discipline that used it. `_promises.md` is that discipline.

### Required sections of `_promises.md`

1. **Promises planted** — every setup planted in the draft, with the scene where it appears, the character or situation it concerns, and the **shape of the payoff it implies**. The implied payoff is what makes the promise a promise rather than a detail.
2. **Promises fired** — every payoff delivered, with the scene where it lands, the original setup it discharges, and the **earned or unearned** verdict.
3. **Promises currently outstanding** — setups planted but not yet paid off; flagged if they've been outstanding for many chapters with no foreshadowing of imminent payoff.
4. **Payoffs without setups** — reveals or moves that the reader will experience as arbitrary because they weren't planted. The unearned payoff is the inverse of the unfired Chekhov's gun and just as deadly.
5. **Promises retired** — setups the writer has decided not to pay off (deliberately, with a reason). Often these were experimental and didn't survive revision; documenting that they're retired prevents them from being treated as outstanding.

### When `_promises.md` is required

- **Fiction with plot** — required (mystery, thriller, literary novel with subplot, anything where reader satisfaction depends on payoff)
- **Screenplay** — required
- **Play** — required
- **Non-fiction** — not applicable
- **Pure stream-of-consciousness literary fiction without plot** — optional; the form's contract is different

### How the `prefigures` relation feeds the ledger

In an atom's frontmatter or body, the `prefigures` relation between two atoms (Scene A prefigures Scene B) is the canonical way to declare a promise. The ledger consolidates these declarations into the central view. The validator can check (in a future v1.x): every `prefigures` link has an entry in `_promises.md`; every entry in `_promises.md` has a `prefigures` link in the relevant atoms.

## Part four — SETUP-PAYOFF-AUDIT activity

### What it is

A periodic audit of `_promises.md` against the drafted manuscript. Surfaces unfired Chekhov's guns and unearned payoffs.

### Trigger conditions

- 10+ scenes have been drafted since last SETUP-PAYOFF-AUDIT
- A new chapter has been outlined that touches outstanding promises
- Before READ-THROUGH at chapter or book scale
- Before BETA-PREP (the audit should happen before the writer sends a draft out)

### Protocol

1. AI reads `_promises.md` in full
2. AI reads the relevant Scene/Chapter atoms covered by current promises
3. AI tests:
   - **Outstanding promises**: for each, is there a planted-foreshadow trail in the recent draft that the reader can connect when the payoff lands? Or has the promise faded?
   - **Recently fired promises**: for each, is the payoff earned by the setup, or does it feel unearned in execution?
   - **Payoffs without setups**: are there recent reveals or moves whose setup is missing from the planted list?
4. AI produces a report categorized by:
   - **Unfired (long-outstanding)** — setup planted N chapters ago, no payoff visible, no foreshadowing of imminent payoff
   - **Unearned (recently fired)** — payoff delivered but the setup is too thin to land
   - **Unsetup (recently delivered)** — payoff with no foundational planting
   - **Healthy** — setups planted, foreshadowed, and either paid off well or on a visible track to payoff
5. Writer decides what to address. Often the answer is "I forgot about that promise; cut the setup or write the payoff." Sometimes it's "that wasn't actually a promise, just a detail." Both are valid; the audit surfaces, the writer judges.

### Failure modes this catches

**F23 — promise-unfired-or-unearned.** Both halves of the failure: the gun on the mantel that never goes off, and the bullet from nowhere.

## Part five — the but/therefore test

A simple, ruthless discipline for testing causal structure. Pixar's South Park-derived rule:

> *Take your story beats and connect them with "but" or "therefore." If "and then" is the natural connector between any two beats, the story has gone flat at that point.*

The test applies at three scales:

- **Scene-to-scene** — annotated in `_spine.md`'s scene-by-scene table
- **Chapter-to-chapter** — in `_spine.md`'s escalation curve
- **Act-to-act** — for screenplays/plays in particular; also for novels with formal act structure

The AI's discipline during SCENE-AUDIT and ARGUMENT-AUDIT-equivalent passes for fiction: walk the spine and flag every transition where "and then" is the only honest connector.

### How to use this test in revision

- A "but" connection means: scene B happens despite scene A's outcome (escalation through obstacle)
- A "therefore" connection means: scene B happens because of scene A's outcome (escalation through consequence)
- An "and then" connection means: scenes A and B are in chronological sequence but not causally linked (slack)

A novel may have a few "and then" transitions (a time skip; a pure mood scene; a deliberate quiet beat). A novel that's mostly "and then" is a sequence, not a plot.

## Part six — how this chapter interacts with the rest of the engine

- **Chapter 03 (Cadence and Sessions)** — adds SCENE-AUDIT and SETUP-PAYOFF-AUDIT to the activity table (now 23 activities total as of v1.3.1)
- **Chapter 04 (Atoms and Structure)** — Scene template updated with `lfw_value_shift_from` and `lfw_value_shift_to` frontmatter fields; the three new backbone files (`_spine.md`, `_continuity.md`, `_promises.md`) documented in the Cartridge backbone files section. *(v1.3.1: Scene also gains `lfw_scene_type` field for scene-vs-sequel distinction — see chapter 14 §1.)*
- **Chapter 07 (Revision Discipline)** — SCENE-AUDIT findings feed into structural and prose-line revision passes
- **Chapter 09 (Writer Development)** — fiction-specific error vocabulary added to the craft-log discipline (scene-doesn't-turn, telling-not-showing, flat-antagonist, head-hopping, filter words, arc-asserted-not-earned)
- **Chapter 10 (Reader and Argument)** — non-fiction's analogs; fiction's chapter 11 is structured to parallel chapter 10's organization
- **Chapter 12 (Fiction Character and Continuity)** — sister chapter; together with this chapter forms the fiction-craft-foundation layer (v1.2)
- **Chapter 13 (Fiction Dialogue and POV-Voice)** *(v1.3.1)* — line-level craft inside the Scene
- **Chapter 14 (Fiction Structure Overlays and Extensions)** *(v1.3.1)* — scene-and-sequel rhythm extends this chapter's value-shift discipline; Theme atom, beat-sheet overlays, Character-Bible
- **`_meta/FAILURE-MODES.md`** — adds F22 (scene-doesn't-turn), F23 (promise-unfired-or-unearned); v1.3.1 adds F38–F40 (missing-sequels, over-sequel'd, sequel-without-decision)

## When the discipline applies and when it relaxes

The discipline above assumes plot-driven fiction. Some fiction forms relax these constraints by design:

- **Pure literary fiction without plot** (mood pieces, character studies, formally experimental work) — the value-shift discipline still applies (even mood pieces have a tonal shift) but the causal-chain discipline relaxes
- **Vignettes and flash fiction** — too short for `_spine.md`'s machinery to earn its keep; the form contains its own discipline
- **Linked short stories** — apply scene-level discipline within each story; the inter-story connections may be thematic rather than causal
- **Genre fiction with established conventions** (cozy mystery, romance, thriller) — the discipline applies *more* rigorously; readers in these genres punish unfulfilled promises and untracked stakes more than literary-fiction readers do

The writer declares in the cartridge manifest if the discipline should relax (e.g., `lfw_form: vignette-collection` triggers a relaxed protocol). Default is full discipline.
