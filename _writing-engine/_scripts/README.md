# Long-Form-Writing — Scripts

Optional tooling. The LFW operating volume runs without any of these scripts; they exist for cartridge authors who want structural validation and for maintainers who want to verify the engine + worked example stay internally consistent.

## What's here

### `validate.py`

A stdlib-only Python validator that walks one or more LFW cartridges and reports structural issues.

**Requirements:** Python 3.8 or newer. No third-party packages. No network access. No file writes.

**Usage:**

```bash
# Validate every cartridge in the OV
python3 _writing-engine/_scripts/validate.py

# Validate one specific cartridge
python3 _writing-engine/_scripts/validate.py Example-Project-The-Persistence-Question

# Validate a cartridge anywhere on disk
python3 _writing-engine/_scripts/validate.py /path/to/my-manuscript-cartridge
```

**Exit codes:**

- `0` — all checks passed
- `1` — one or more checks failed (see output for details)
- `2` — usage error or target not found

**Checks performed:**

| Check name | What it catches |
|---|---|
| `wiki-link-resolves` | `[[Foo]]` in any .md file that doesn't resolve to a real file basename |
| `state-Item-exists` | Wiki-links in `_state.md` that point to non-existent files |
| `status-legal` | `lfw_status` values that aren't legal for the Item's `lfw_item_type` |
| `Item-type-known` | `lfw_item_type` values that aren't one of the known ten |
| `template-exists` | Types used in the cartridge that have no corresponding `TEMPLATE-<Type>.md` |
| `filename-conforms` | Filenames that don't match the naming pattern declared in `04-ITEMS-AND-STRUCTURE.md` (chapter-prefixed sections/scenes/beats, `Chapter-NN-<title>` for chapters, etc.) |
| `required-frontmatter` | Items missing `type`, `Item_ID`, or `Title` |
| `unique-item-id` | `Item_ID` collisions across the cartridge |

## When to run

- **Before committing** a substantial change to a cartridge — catches broken links from rename mistakes
- **Before sharing** a cartridge with a collaborator or beta reader — they shouldn't have to discover broken references
- **At engine releases** — verifies the shipped worked example stays clean
- **As part of CI** if you've set that up — the script's exit code is CI-friendly

## When NOT to run

The validator is a sanity tool, not a gate. Don't run it inside the AI session loop — it's not part of the writing protocol. Run it manually or in CI.

## Limitations

- The frontmatter parser is regex-based, not a real YAML library, so unusual frontmatter shapes (nested structures, multi-line strings) may produce false positives. Easier to fix false positives than to add a YAML dependency.
- The `filename-conforms` check is heuristic. It catches the common collision-producing mistakes but won't catch every possible deviation.
- The validator does NOT check prose quality, voice consistency, factual accuracy, or anything topical. It only checks structural integrity. Voice and accuracy live in REVISE and VOICE-CHECK and accuracy-pass activities (see chapters 05, 06, 07 of the writing engine).
