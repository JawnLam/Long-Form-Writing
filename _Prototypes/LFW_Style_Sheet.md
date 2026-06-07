---
Item_Prototype: Fleeting
Item_ID: prototype-lfw-style-sheet
Title: "LFW_Style_Sheet Prototype"
Date_Added: 2026-06-06
Date_Modified: 2026-06-06
Needs_Processing: false
---

# `LFW_Style_Sheet` — Prototype Definition

> **What this file is.** The canonical definition of the `LFW_Style_Sheet` Prototype for the Long-Form-Writing Operating Volume. Items in any cartridge that declare `Item_Prototype: LFW_Style_Sheet` conform to the contract described below.

## Purpose

The Style Sheet captures the cartridge's **style-and-language conventions** — spelling, capitalization, italics, punctuation, numbers, dialogue formatting, lexicon, anachronism risks. State choices once; honor them. Consulted at BETA-PREP and at line-edit REVISE passes. Drift in style sheet conventions (F36 from v1.3.1, F48 from v1.3.2) reads as inattention to editors and agents — the kind of drift that signals an inadequately-edited manuscript. Optional backbone but strongly recommended; non-trivial for any manuscript with substantial invented vocabulary (fantasy/SFF) or period-specific conventions. Introduced in v1.3.2 (chapter 15 §4).

## Required frontmatter

| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `Item_Prototype` | string | yes | Must equal `LFW_Style_Sheet` |
| `Item_ID` | string | yes | Format: `<manuscript-slug>-style-sheet` |
| `Title` | string | yes | Format: `"<Manuscript Title> — Style Sheet"` |
| `Date_Added` | date | yes | When the Style Sheet was created |
| `Date_Modified` | date | yes | When last changed |
| `lfw_manuscript` | string | yes | Manuscript slug |
| `lfw_style_sheet_version` | integer | yes | Bumped on substantial restructuring |

## Body structure

```markdown
# <Manuscript Title> — Style Sheet

## Voice and register reminders
*Brief summary; pointer to `_voice-samples.md` if used.*

## Spelling
- **US vs UK:**
- **Specific words you've chosen one form for:**
- **Brand-name capitalization:**
- **Proper-noun spellings:**

## Capitalization
- **Deity / pronouns for deity:**
- **Titles:**
- **Period-specific conventions:**
- **Quoted dialogue:**

## Italics
- **Foreign words:**
- **Inner dialogue:**
- **Emphasis:**
- **Titles:**
- **Sound effects (if any):**

## Punctuation
- **Oxford comma:**
- **Em-dash style:**
- **Ellipsis:**
- **Quotation marks:**
- **Serial commas in dialogue tags:**

## Numbers
- **Spelled-out vs numerals:**
- **Time formats:**
- **Date formats:**
- **Ages:**

## Dialogue formatting *(cross-reference chapter 13 §1)*
- **Tags:**
- **Adverbs in tags:**
- **Em-dash for interruption / Ellipsis for trail-off:**
- **Foreign-language quoted material:**
- **Inner dialogue:**
- **Dialect:**

## Lexicon
*Per-cartridge invented terms, proper nouns, technical terminology.*
| Term | Definition / context | First appears | Pronunciation |

## Anachronism risk catalog *(historical / period work)*
| Term | Anachronism risk | Period it would feel wrong in |

## Inconsistencies to fix
*Running log of style drift caught in revision; not yet resolved.*
- [ ]

## Notes
```

## Naming

- **Filename:** `_style-sheet.md` (fixed; one per cartridge)
- **Location:** cartridge root
- **Wikilink target:** `_style-sheet`

## Example Item

```markdown
---
Item_Prototype: LFW_Style_Sheet
Item_ID: the-late-frost-style-sheet
Title: "The Late Frost — Style Sheet"
Date_Added: 2026-05-12
Date_Modified: 2026-06-04
lfw_manuscript: the-late-frost
lfw_style_sheet_version: 2
---

# The Late Frost — Style Sheet

## Voice and register reminders
Maya's first-person, present-tense. Cadenced sentences; specific botanical/oenological nouns as anchors before abstract feeling. Voice mode is `writer-maintains`; no `_voice-samples.md`.

## Spelling
- **US vs UK:** US
- **Specific words:**
  - `grey` (the manuscript's chosen form; do not normalize to `gray`)
  - `okay` (not `OK`)
  - `toward` (not `towards`)
  - `vineyard` (lowercase except in proper names)
- **Brand-name capitalization:**
  - `Mason` (jars; capitalized as proper noun)
  - `Hofstra` (the family name and vineyard label)
- **Proper-noun spellings:**
  - `Hollis` (the family)
  - `Reyes` (Hector's surname)

## Capitalization
- **Deity:** lower-case (the manuscript's posture toward religion is observational, not declarative)
- **Titles:** uppercase before name (`Sister Margaret`); lowercase after (`Margaret, the sister`)

## Italics
- **Foreign words:** first instance only; not on re-use
- **Inner dialogue:** none (no italics, no markers — interiority is in first-person register)
- **Emphasis:** sparingly; only for true beat-stress
- **Titles of books:** italic (`Gilead`, `Persuasion`)

## Punctuation
- **Oxford comma:** yes
- **Em-dash style:** unspaced — like this
- **Ellipsis:** three dots `...` (not the unicode character)
- **Quotation marks:** double; American
- **Serial commas in dialogue tags:** standard

## Numbers
- **Spelled-out vs numerals:** spell out 1–100; numerals beyond. Exception: ages always numerals (`38`, not `thirty-eight`)
- **Time formats:** 12-hour, lowercase, no period (`3pm`, not `3 PM` or `3:00 p.m.`)
- **Date formats:** in prose, spell month (`March 22`)
- **Ages:** numerals always

## Dialogue formatting
- **Tags:** said-only as default; mixed-tag (`said`, `asked`, `whispered`) sparingly. Action-beats over tags whenever possible.
- **Adverbs in tags:** disallowed (no `said quietly`)
- **Em-dash for interruption:** yes (`"You—"`)
- **Ellipsis for trail-off:** yes (`"I just..."`)
- **Inner dialogue:** none

## Lexicon
| Term | Definition / context | First appears | Pronunciation |
|------|----------------------|---------------|---------------|
| Cabernet Franc | grape variety; one of two grown at the vineyard | [[01-02-Frost-Damage-Neighbor]] | KAB-er-nay FRONK |
| North Fork | Long Island region | [[01-01-The-Approach]] | |
| trellised | wire-supported vine cultivation | [[01-04-Empty-House-Walkthrough]] | |
| kettle-pond | glacial pond type | [[01-01-The-Approach]] | |
| rootstock | vine grafting term | (planned, Ch 3) | |

## Anachronism risk catalog
*(Manuscript is contemporary 2026; minimal anachronism risk. Backstory references to 1968–2018 may surface anachronisms.)*

| Term | Anachronism risk | Period it would feel wrong in |
|------|------------------|-------------------------------|
| `vinifera` | technical viticulture term; check first-use in backstory scenes | 1968 (would have been known but rarely spoken; verify register) |

## Inconsistencies to fix
- [ ] In Chapter 1, used both `vineyard` and `Vineyard` (capitalized) — normalize to lowercase except proper-name use
- [ ] Hector's surname appears as both `Reyes` (correct) and `Reyez` (typo, twice) — fix all
- [ ] Em-dashes in Chapter 2 are sometimes spaced; should all be unspaced

## Notes
- The manuscript's voice depends on specific noun-precision. The Style Sheet's role here is less about rules and more about consistency — when Maya uses a precise term, she uses it correctly every time.
```

## Relationships

- `LFW_Voice_Samples` — When `_voice-samples.md` is present, the Style Sheet references it as the voice source-of-truth; the Style Sheet captures the *conventions* the voice has chosen, not the voice itself.
- `LFW_Worldbuilding` — When `_worldbuilding.md` is present (v1.3.2), invented vocabulary may be defined there and referenced in the Style Sheet's lexicon section.
- `LFW_Setting` — Settings may supply lexicon entries (period-specific or technical terms); the Style Sheet centralizes them.
- `LFW_Revision_Pass` — Style Sheet drift is caught during prose-line and voice revision passes; inconsistencies surface to the `Inconsistencies to fix` section.
- `LFW_Manuscript_Manifest` — Optional backbone; not required by any genre.

## Notes

- **State once; honor.** The Style Sheet is operative because the writer chose. If the choice is in the file, the choice is the law for the cartridge.
- **F36 / F48 — Style sheet drift.** Drift reads as inattention. The writer who can hold these conventions across 85,000 words signals to readers and editors that the manuscript was made with care.
- **Lexicon vs Style.** Style is *how* things are spelled, capitalized, punctuated. Lexicon is *what* specific terms mean and how they're pronounced. Both belong here; for fantasy/SFF with substantial invented vocabulary, the Lexicon may grow into a separate `_lexicon.md` file.
- **Anachronism risk is period-work-specific.** For contemporary fiction, this section is usually empty or near-empty. For historical fiction, alt-history, period drama, it's load-bearing.
- **Inconsistencies-to-fix is the working log.** Revision passes catch drift; entries here are commitments to resolve in the next prose-line pass.
