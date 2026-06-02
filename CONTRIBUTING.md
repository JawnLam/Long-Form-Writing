# Contributing to Long-Form-Writing

LFW ships at v1.0.0 with a stable atom schema and engine file structure. This document describes when a contribution is in-scope at v1.x, when it requires a major version bump, and how to propose either.

For day-to-day operation, see `OPERATOR-GUIDE.md`. For release history, see `CHANGELOG.md`.

---

## 1. What is in-scope at v1.x

The following contributions do **not** require a major version bump:

| Contribution                                                                | Where it lives                                                                |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| New worked-example cartridge for a different genre / project type           | `Example-Project-<Name>/` at the root, paralleling the shipped example        |
| New entry in the failure-modes catalog                                       | `_writing-engine/_meta/FAILURE-MODES.md`                                       |
| New atom subtype for an under-covered genre                                  | `_writing-engine/_templates/TEMPLATE-<Subtype>.md` + section in `02-GENRE-AND-SCHEMA.md` |
| Clarification, correction, or expansion in any engine file (00–08, BOOTSTRAP) | Edit in place; minor version bump                                            |
| Documentation fix (README, INSTALL, OPERATOR-GUIDE, this file)              | Edit in place                                                                  |
| New optional field on an atom prototype (additive only)                     | Update `_meta/SCHEMA-OF-SCHEMAS.md` + the template + minor version bump        |
| New session activity beyond the universal ten                                | Document in `03-CADENCE-AND-SESSIONS.md` with trigger conditions; minor bump  |

## 2. What requires a major version bump (v2.0)

Any change that breaks existing cartridges:

- Adding a **required** field to a cartridge backbone file or atom prototype
- Renaming or removing an atom type
- Changing the cartridge folder convention (e.g., renaming `Atoms/`, `Sessions/`, `Revision-Passes/`)
- Restructuring the engine such that v1 cartridges can't be read
- Changing the universal activity set in a way that breaks existing session logs

Major bumps require: documented migration path, scripted or manual migration steps, clear `CHANGELOG.md` flag.

## 3. What is explicitly out of scope

- **Hardcoded references to a specific manuscript in `_writing-engine/`.** The engine is subject-agnostic. Manuscript-specific guidance lives in cartridges, not the engine.
- **Personal data in shipped files.** No real names, emails, paths, or project references. Use placeholders.
- **Genre-collapsing.** The schema explicitly accommodates fiction / non-fiction / screenplay / play / dissertation. Don't propose collapsing two genres into one — they have genuinely different atom needs.
- **AI-platform-specific code.** Markdown only.

## 4. How to propose a change

### In-scope contribution (no version bump)

1. Locate the right path per §1.
2. Conform to existing conventions.
3. Test your change against the shipped worked example — does the engine still work?
4. Submit (PR if hosted on GitHub, or share by other means).

### Major version bump (v2.0)

1. Draft the schema/structure change as a markdown spec — what changes, why, what breaks, what migration looks like.
2. Author the migration path.
3. Test against multiple cartridges of different genres.
4. Update `CHANGELOG.md` flagging the break.
5. Update `VERSION.md`.

## 5. Voice and tone conventions

When authoring engine content (`_writing-engine/` and subfolders):

- **Subject-agnostic.** Never name a specific manuscript except in illustrative tables.
- **Peer register.** Adult writer-to-adult-writer.
- **No flattery, no filler.** "Great question," "interesting," etc. are forbidden.
- **No emojis.** Plain prose.

When authoring docs at the root (README, INSTALL, OPERATOR-GUIDE, this file): explanatory prose is fine. Still no emojis, still no flattery.

## 6. Genre coverage

LFW v1.0 covers five long-form genres. If you want to propose explicit support for an additional genre (e.g., poetry collections, graphic novels, comic-book scripts, RPG adventure modules, long-form journalism), that's an in-scope minor-version contribution. The pattern:

1. Add a `## Genre — <name>` section to `02-GENRE-AND-SCHEMA.md` covering what atoms emphasize, what conventions apply
2. If the genre needs new atom subtypes, propose them per §1
3. Update `BOOTSTRAP-NEW-MANUSCRIPT.md` to include the genre in its CQ asking the writer
4. Add a worked-example cartridge if you can (very useful for adopters)

## 7. Sharing cartridges

A worked-example cartridge is a complete `<Cartridge>/` folder. To share as a contribution:

- Strip personal references (real names, identifying details)
- Ensure the manuscript premise is clearly hypothetical (so readers don't mistake it for a real published work)
- Submit as a PR adding `Example-Project-<Name>/` at the LFW root

## Version

This contribution guide ships with Long-Form-Writing v1.0.0.
