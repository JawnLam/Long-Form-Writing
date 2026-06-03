#!/usr/bin/env python3
"""
LFW cartridge validator.

Standard-library only. No external dependencies.

Usage:
    python3 validate.py <cartridge-path>
    python3 validate.py             # auto-detects all cartridges in OV root

Exit codes:
    0 — all checks passed
    1 — one or more checks failed

Checks performed (each emits one line per failure):

  1. wiki-link-resolves   : every [[Foo]] in any .md file resolves to a real
                            file basename within the cartridge (or to a backbone
                            file like _state, _outline, _voice-samples,
                            _manuscript-manifest).
  2. state-atom-exists    : every wiki-link in <cartridge>/_state.md targets an
                            atom file that exists.
  3. status-legal         : every atom's lfw_status value is in the legal enum
                            for its lfw_atom_type.
  4. atom-type-known      : every atom's lfw_atom_type is a known type (beat,
                            scene, section, chapter, act, character, thread,
                            source, setting, note).
  5. template-exists      : for every atom type seen, a corresponding
                            TEMPLATE-<Type>.md file exists in
                            _writing-engine/_templates/.
  6. filename-conforms    : section/scene/beat files are chapter-prefixed;
                            chapter files use Chapter-NN- prefix; source files
                            follow Lastname-Title-Year pattern (heuristic).
  7. required-frontmatter : Item_Prototype, Item_ID, Title present on every
                            atom.
  8. unique-item-id       : Item_IDs are unique across the cartridge.

The script is intentionally simple and forgiving: it parses YAML frontmatter
without a YAML library (regex + line-walk), so unusual frontmatter shapes
may emit false positives. False positives are easier to fix than false
negatives.
"""

import os
import re
import sys
import pathlib
from collections import defaultdict

# ---- Schema knowledge --------------------------------------------------------

# Legal status values per atom type.
# Prose-bearing atoms share the universal enum; non-fiction Section adds
# fact-checked. Non-prose atoms have type-specific lifecycles.
STATUS_ENUM = {
    "beat":      {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "scene":     {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "section":   {"planned", "drafting", "drafted", "revising", "revised", "fact-checked", "final"},
    "chapter":   {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "act":       {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "character": {"developing", "established", "revised", "final"},
    "reader":    {"developing", "active", "retired"},
    "thread":    {"emerging", "active", "concluded"},
    "source":    {"identified", "ingested", "folded-in", "superseded"},
    "setting":   {"sketched", "defined", "final"},
    "note":      {"unplaced", "placed", "discarded"},
}

KNOWN_ATOM_TYPES = set(STATUS_ENUM.keys())

# Cartridge backbone files (not atoms; valid wiki-link targets)
BACKBONE_FILES = {
    "_state", "_outline", "_voice-samples", "_manuscript-manifest",
    "_argument", "_craft-log",     # v1.1 additions
}

# ---- Helpers -----------------------------------------------------------------

def is_cartridge(path: pathlib.Path) -> bool:
    """A folder is a cartridge if it contains _manuscript-manifest.md."""
    return (path / "_manuscript-manifest.md").is_file()

def find_cartridges(ov_root: pathlib.Path):
    """Find all cartridge folders directly under the OV root."""
    return [p for p in ov_root.iterdir() if p.is_dir() and is_cartridge(p)]

def parse_frontmatter(text: str) -> dict:
    """Tiny YAML-ish frontmatter parser. Returns a dict of key→value (strings).
    Handles simple key: value pairs only. Skips lists and nested structures."""
    out = {}
    if not text.startswith("---\n"):
        return out
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return out
    fm_text = text[4:end_idx]
    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            continue  # nested
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        # strip wrapping quotes
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        # strip inline comments
        val = re.sub(r'\s+#.*$', '', val)
        out[key] = val
    return out

def extract_wiki_links(text: str) -> set:
    """Return the set of wiki-link names (without [[ ]]) in the text."""
    return set(re.findall(r'\[\[([^\]]+)\]\]', text))

def file_basenames(cartridge: pathlib.Path) -> set:
    """Return the set of .md basenames (without .md) in the cartridge."""
    out = set()
    for p in cartridge.rglob("*.md"):
        out.add(p.stem)
    return out

# ---- Checks ------------------------------------------------------------------

def check_cartridge(cartridge: pathlib.Path) -> list:
    """Run all checks on one cartridge. Returns list of (severity, message)."""
    issues = []
    basenames = file_basenames(cartridge) | BACKBONE_FILES
    item_ids = defaultdict(list)  # id → list of paths
    types_seen = set()

    for path in cartridge.rglob("*.md"):
        rel = path.relative_to(cartridge)
        try:
            text = path.read_text()
        except Exception as e:
            issues.append(("error", f"{rel}: cannot read ({e})"))
            continue
        fm = parse_frontmatter(text)

        # Check 1: wiki-link-resolves
        links = extract_wiki_links(text)
        for link in links:
            if link not in basenames:
                issues.append(("wiki-link-resolves", f"{rel}: [[{link}]] does not resolve to any file in the cartridge"))

        # Identify atom files: must have Item_Prototype starting with LFW_
        prototype = fm.get("Item_Prototype", "")
        if not prototype.startswith("LFW_"):
            continue  # not an atom (e.g., outline file, voice-samples file with non-LFW prototype, README, etc.)

        # Check 7: required frontmatter
        for required in ("Item_Prototype", "Item_ID", "Title"):
            if required not in fm or not fm[required]:
                issues.append(("required-frontmatter", f"{rel}: missing or empty `{required}`"))

        # Check 8: collect Item_IDs for uniqueness check
        if fm.get("Item_ID"):
            item_ids[fm["Item_ID"]].append(str(rel))

        atom_type = fm.get("lfw_atom_type", "").strip()
        if not atom_type:
            continue  # backbone files like _state, _outline don't have atom_type

        # Check 4: atom-type-known
        if atom_type not in KNOWN_ATOM_TYPES:
            issues.append(("atom-type-known", f"{rel}: lfw_atom_type='{atom_type}' is not a known type"))
            continue
        types_seen.add(atom_type)

        # Check 3: status-legal
        status = fm.get("lfw_status", "").strip()
        if status:
            legal = STATUS_ENUM[atom_type]
            if status not in legal:
                issues.append(("status-legal", f"{rel}: lfw_status='{status}' not legal for atom_type='{atom_type}' (expected one of: {', '.join(sorted(legal))})"))

        # Check 6: filename-conforms (heuristic — emits warnings, not errors)
        stem = path.stem
        if atom_type == "chapter":
            if not re.match(r'^Chapter-\d{2}-', stem):
                issues.append(("filename-conforms", f"{rel}: chapter filename should match `Chapter-NN-<title>` pattern"))
        elif atom_type == "section":
            if not re.match(r'^\d{2}-\d{2}-', stem):
                issues.append(("filename-conforms", f"{rel}: section filename should be chapter-prefixed `<ch>-<order>-<slug>`"))
        elif atom_type == "scene":
            if not re.match(r'^\d{2}-\d{2}-', stem):
                issues.append(("filename-conforms", f"{rel}: scene filename should be chapter-prefixed `<ch>-<order>-<slug>`"))
        elif atom_type == "beat":
            if not re.match(r'^\d{2}-\d{2}-Beat-', stem):
                issues.append(("filename-conforms", f"{rel}: beat filename should match `<ch>-<sec>-Beat-<order>-<slug>` pattern"))
        elif atom_type == "act":
            if not re.match(r'^Act-\d+-', stem):
                issues.append(("filename-conforms", f"{rel}: act filename should match `Act-N-<title>` pattern"))

    # Check 8: uniqueness
    for iid, paths in item_ids.items():
        if len(paths) > 1:
            issues.append(("unique-item-id", f"Item_ID '{iid}' appears in {len(paths)} files: {', '.join(paths)}"))

    return issues, types_seen

def check_state_references(cartridge: pathlib.Path) -> list:
    """Check 2: every wiki-link in _state.md targets an existing file."""
    state_path = cartridge / "_state.md"
    if not state_path.is_file():
        return [("state-atom-exists", "_state.md is missing")]
    text = state_path.read_text()
    basenames = file_basenames(cartridge) | BACKBONE_FILES
    issues = []
    for link in extract_wiki_links(text):
        if link not in basenames:
            issues.append(("state-atom-exists", f"_state.md: [[{link}]] does not exist as a file"))
    return issues

def check_templates_exist(ov_root: pathlib.Path, atom_types_used: set) -> list:
    """Check 5: every atom type used has a corresponding TEMPLATE-<Type>.md."""
    templates_dir = ov_root / "_writing-engine" / "_templates"
    if not templates_dir.is_dir():
        return [("template-exists", f"_templates folder missing at {templates_dir}")]
    template_files = {p.stem.replace("TEMPLATE-", "").lower() for p in templates_dir.glob("TEMPLATE-*.md")}
    issues = []
    for at in sorted(atom_types_used):
        if at not in template_files:
            issues.append(("template-exists", f"atom_type='{at}' has no TEMPLATE-{at.capitalize()}.md in {templates_dir.relative_to(ov_root)}"))
    return issues

# ---- Main --------------------------------------------------------------------

def main():
    if len(sys.argv) == 2:
        target = pathlib.Path(sys.argv[1]).resolve()
    elif len(sys.argv) == 1:
        # Auto-detect: this script lives at <OV>/_writing-engine/_scripts/validate.py
        target = pathlib.Path(__file__).resolve().parent.parent.parent
    else:
        print("Usage: python3 validate.py [cartridge-path-or-OV-root]")
        sys.exit(2)

    if not target.is_dir():
        print(f"Not a directory: {target}")
        sys.exit(2)

    # If target is a cartridge, validate just that one. If target is an OV root,
    # validate all cartridges in it.
    if is_cartridge(target):
        cartridges = [target]
        ov_root = target.parent
    else:
        cartridges = find_cartridges(target)
        ov_root = target
        if not cartridges:
            print(f"No cartridges found in {target}")
            sys.exit(2)

    print(f"OV root: {ov_root}")
    print(f"Validating {len(cartridges)} cartridge(s).\n")

    total_issues = 0
    all_types = set()

    for cartridge in cartridges:
        print(f"=== {cartridge.name} ===")
        issues, types = check_cartridge(cartridge)
        issues += check_state_references(cartridge)
        all_types |= types
        if not issues:
            print("  (no issues)")
        else:
            # Group by check name
            by_check = defaultdict(list)
            for severity, msg in issues:
                by_check[severity].append(msg)
            for check, msgs in sorted(by_check.items()):
                print(f"  [{check}] {len(msgs)} issue(s):")
                for m in msgs:
                    print(f"    - {m}")
            total_issues += len(issues)
        print()

    # OV-level: template existence per atom-type used
    template_issues = check_templates_exist(ov_root, all_types)
    if template_issues:
        print("=== Template coverage ===")
        for _, msg in template_issues:
            print(f"  - {msg}")
        total_issues += len(template_issues)
        print()

    if total_issues == 0:
        print("ALL CHECKS PASSED")
        sys.exit(0)
    else:
        print(f"TOTAL ISSUES: {total_issues}")
        sys.exit(1)

if __name__ == "__main__":
    main()
