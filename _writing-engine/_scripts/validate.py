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
                            _manuscript-manifest, _argument, _craft-log, _spine,
                            _continuity, _promises).
  2. state-atom-exists    : every wiki-link in <cartridge>/_state.md targets an
                            atom file that exists.
  3. status-legal         : every atom's lfw_status value is in the legal enum
                            for its lfw_atom_type.
  4. atom-type-known      : every atom's lfw_atom_type is a known type (beat,
                            scene, section, chapter, act, character,
                            character-bible, reader, motif, theme, thread,
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
  9. scene-value-shift    : every Scene with status `drafted | revising |
                            revised | final` must declare lfw_value_shift_from
                            and lfw_value_shift_to, and the two must differ
                            (v1.2 fiction-craft enforcement of the SCENE-AUDIT
                            discipline in chapter 11 §1). Exempt: sequel-typed
                            Scenes (v1.3.1 — they carry decisions, not turns).
 10. scene-type-legal     : lfw_scene_type, when set, must be one of
                            scene | sequel | scene-sequel (v1.3.1 — chapter 14
                            §1 scene-and-sequel discipline).
 11. pov-voice-register   : advisory warning when an established protagonist /
                            antagonist Character omits lfw_pov_voice_register
                            (v1.3.1 — chapter 13 POV-voice differentiation).
 12. timeline-layer       : Timeline atom must declare lfw_timeline_layer in
                            the legal set; character-specific layer must also
                            declare lfw_character (v1.3.2 — chapter 15 §2).
 13. load-declared        : every engine chapter file declares a valid
                            lfw_load block (tier, genres, activities, phase)
                            with codes from chapter 03's activity set
                            (v1.5 — feat/core-pack-progressive-disclosure).
 14. router-fresh         : regenerate _ROUTER.md in memory from chapter
                            lfw_load frontmatter and compare to the committed
                            file; fail if they differ. Correct-by-construction
                            guarantee (v1.5).
 15. session-read-coverage: each session log's lfw_chapters_loaded must
                            include the chapters the router marks required
                            for (cartridge-genre, session-activity). Missing
                            required chapters fails; extra chapters warn.
                            Unknown activities (META, BOOTSTRAP) skip (v1.5).
 16. genre-isolation      : positive assertion that the router never
                            dispatches fiction-pack chapters under non-fiction
                            or dissertation genres, and never dispatches
                            chapter 06 / 10-ARGUMENT under fiction / screenplay
                            / play. The packaging is correct by construction
                            and this check is the executable proof (v1.5).

The script is intentionally simple and forgiving: it parses YAML frontmatter
without a YAML library (regex + line-walk), so unusual frontmatter shapes
may emit false positives. False positives are easier to fix than false
negatives.
"""

import importlib.util
import os
import re
import sys
import pathlib
from collections import defaultdict


# ---- Router-driven checks (v1.5; loaded lazily so old cartridges still validate) ----

def _load_build_router():
    """Import build-router.py as a module (hyphen in filename → use spec_from_file_location).
    Returns the module or None if unavailable. Stdlib-only."""
    here = pathlib.Path(__file__).resolve().parent
    br_path = here / "build-router.py"
    if not br_path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("build_router", br_path)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

# ---- Schema knowledge --------------------------------------------------------

# Legal status values per atom type.
# Prose-bearing atoms share the universal enum; non-fiction Section adds
# fact-checked. Non-prose atoms have type-specific lifecycles.
STATUS_ENUM = {
    "beat":            {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "scene":           {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "section":         {"planned", "drafting", "drafted", "revising", "revised", "fact-checked", "final"},
    "chapter":         {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "act":             {"planned", "drafting", "drafted", "revising", "revised", "final"},
    "character":       {"developing", "established", "revised", "final"},
    "character-bible": {"drafting", "established", "revised", "final"},   # v1.3.1 addition
    "reader":          {"developing", "active", "retired"},
    "motif":           {"latent", "emerging", "woven", "resolved"},        # v1.2 addition
    "theme":           {"candidate", "developing", "threaded", "resolved"},  # v1.3.1 addition
    "timeline":        {"drafting", "established", "revised", "final"},    # v1.3.2 addition
    "inspiration":     {"noted", "absorbed", "folded-in", "retired"},      # v1.3.2 addition
    "thread":          {"emerging", "active", "concluded"},
    "source":          {"identified", "ingested", "folded-in", "superseded"},
    "setting":         {"sketched", "defined", "final"},
    "note":            {"unplaced", "placed", "discarded"},
}

# v1.3.2: legal lfw_timeline_layer values
TIMELINE_LAYER_ENUM = {"story-time", "world-history", "real-world", "character-specific"}

# v1.3.1: legal lfw_scene_type values
SCENE_TYPE_ENUM = {"scene", "sequel", "scene-sequel"}

# v1.3.1: legal lfw_fiction_subgenre values (advisory; enforced on manuscript-manifest only)
FICTION_SUBGENRE_ENUM = {
    "literary", "thriller", "mystery", "romance",
    "sff", "speculative", "historical", "horror", "ya",
    "",  # unset is legal
}

KNOWN_ATOM_TYPES = set(STATUS_ENUM.keys())

# Cartridge backbone files (not atoms; valid wiki-link targets)
BACKBONE_FILES = {
    "_state", "_outline", "_voice-samples", "_manuscript-manifest",
    "_argument", "_craft-log",                       # v1.1 additions
    "_spine", "_continuity", "_promises",            # v1.2 fiction backbones
    "_worldbuilding", "_storyboard",                 # v1.3.2 structural backbones
    "_style-sheet", "_relationships",                # v1.3.2 structural backbones
}

# ---- Helpers -----------------------------------------------------------------

def is_cartridge(path: pathlib.Path) -> bool:
    """A folder is a cartridge if it contains _manuscript-manifest.md."""
    return (path / "_manuscript-manifest.md").is_file()

def find_cartridges(ov_root: pathlib.Path):
    """Find all cartridge folders directly under the OV root."""
    return [p for p in ov_root.iterdir() if p.is_dir() and is_cartridge(p)]

def parse_frontmatter(text: str) -> dict:
    """Tiny YAML-ish frontmatter parser. Stdlib-only — no PyYAML.
    Handles flat keys, scalar values, [list] inline, multi-line block lists
    (`key:\\n  - item`), and one-level nested key/value blocks (`key:\\n  child: val`).
    Returns a dict; list values are returned as Python lists."""
    out = {}
    if not text.startswith("---\n"):
        return out
    end_idx = text.find("\n---\n", 4)
    if end_idx == -1:
        return out
    fm_text = text[4:end_idx]
    lines = fm_text.splitlines()

    def _strip_scalar(v):
        if isinstance(v, str):
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            elif v.startswith("'") and v.endswith("'"):
                v = v[1:-1]
            v = re.sub(r'\s+#.*$', '', v).strip()
        return v

    def _parse_inline_value(val):
        """Parse a scalar OR inline list `[a, b, c]`."""
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            if not inner:
                return []
            return [_strip_scalar(x.strip()) for x in inner.split(",")]
        return _strip_scalar(val)

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith(" ") or line.startswith("\t"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val:
            out[key] = _parse_inline_value(val)
            i += 1
            continue
        # Empty value → nested block (list or dict) follows
        i += 1
        nested_items = []
        nested_dict = {}
        is_list = None  # determined by first non-blank child
        while i < len(lines):
            child = lines[i]
            if not child.strip():
                i += 1
                continue
            if not (child.startswith(" ") or child.startswith("\t")):
                break
            stripped = child.strip()
            if stripped.startswith("- "):
                if is_list is False:
                    break  # mixed block; stop
                is_list = True
                item_val = stripped[2:].strip()
                nested_items.append(_strip_scalar(item_val))
                i += 1
                continue
            if stripped == "-":
                if is_list is False:
                    break
                is_list = True
                nested_items.append("")
                i += 1
                continue
            if ":" in stripped:
                if is_list is True:
                    break
                is_list = False
                ckey, _, cval = stripped.partition(":")
                nested_dict[ckey.strip()] = _parse_inline_value(cval)
                i += 1
                continue
            i += 1
        if is_list:
            out[key] = nested_items
        else:
            out[key] = nested_dict
    return out

def extract_wiki_links(text: str) -> set:
    """Return the set of wiki-link names (without [[ ]]) in the text.

    Handles Obsidian-style pipe aliases: [[Target|alias]] yields "Target".
    Handles section anchors: [[Target#Section]] yields "Target".
    Strips outer whitespace.
    """
    raw = re.findall(r'\[\[([^\]]+)\]\]', text)
    out = set()
    for link in raw:
        # Strip alias after |
        target = link.split("|", 1)[0]
        # Strip section anchor after #
        target = target.split("#", 1)[0]
        out.add(target.strip())
    return out

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
            if not re.match(r'^\d{2}-\d{2}-Beat-', stem) and not re.match(r'^Beat-\d{2}-\d{2}-\d{2}-', stem):
                issues.append(("filename-conforms", f"{rel}: beat filename should match `Beat-NN-NN-NN-<slug>` or chapter-prefixed `<ch>-<sec>-Beat-<order>-<slug>` pattern"))
        elif atom_type == "act":
            if not re.match(r'^Act-\d+-', stem):
                issues.append(("filename-conforms", f"{rel}: act filename should match `Act-N-<title>` pattern"))
        # motif, character, reader, thread, source, setting, note: free TitleCase-Hyphenated naming; no filename check

        # Check 9 (v1.2 + v1.3.1): value-shift declared on drafted Scenes
        # If a Scene's status is `drafted | revising | revised | final`, both
        # lfw_value_shift_from and lfw_value_shift_to must be set and must differ.
        # SCENE-AUDIT (chapter 11 §1) treats a non-shifting scene as a flag.
        # v1.3.1: scenes with lfw_scene_type = "sequel" are exempt — they carry
        # decisions, not value-shifts (chapter 14 §1).
        if atom_type == "scene" and status in {"drafted", "revising", "revised", "final"}:
            scene_type = fm.get("lfw_scene_type", "scene").strip() or "scene"
            if scene_type != "sequel":
                v_from = fm.get("lfw_value_shift_from", "").strip()
                v_to = fm.get("lfw_value_shift_to", "").strip()
                if not v_from or not v_to:
                    issues.append(("scene-value-shift", f"{rel}: scene status='{status}' but lfw_value_shift_from/to not both set"))
                elif v_from == v_to:
                    issues.append(("scene-value-shift", f"{rel}: lfw_value_shift_from == lfw_value_shift_to ('{v_from}') — scene does not turn"))

        # Check 10 (v1.3.1): scene-type legal value
        if atom_type == "scene":
            scene_type = fm.get("lfw_scene_type", "").strip()
            if scene_type and scene_type not in SCENE_TYPE_ENUM:
                issues.append(("scene-type-legal", f"{rel}: lfw_scene_type='{scene_type}' not in legal set (expected: {', '.join(sorted(SCENE_TYPE_ENUM))})"))

        # Check 11 (v1.3.1): POV-bearing Characters should declare lfw_pov_voice_register
        # Soft check — only fires if the Character's `lfw_role` includes "pov" or
        # the Character's filename appears as `lfw_pov:` in any Scene atom.
        # For v1.3.1 the simple form: if lfw_role contains "protagonist" or "antagonist"
        # and the Character is `established` or above, expect lfw_pov_voice_register populated.
        # This is advisory — emits warnings only when status >= established AND the field is missing entirely.
        if atom_type == "character" and status in {"established", "revised", "final"}:
            role = fm.get("lfw_role", "").strip().lower()
            if any(r in role for r in ("protagonist", "antagonist")):
                if "lfw_pov_voice_register" not in fm and not any(
                    k.startswith("lfw_pov_voice_register") for k in fm
                ):
                    # field absent entirely — flag soft warning
                    issues.append(("pov-voice-register-advisory", f"{rel}: established {role} Character should declare lfw_pov_voice_register (chapter 13)"))

        # Check 12 (v1.3.2): Timeline layer must be legal
        if atom_type == "timeline":
            layer = fm.get("lfw_timeline_layer", "").strip()
            if not layer:
                issues.append(("timeline-layer", f"{rel}: timeline atom requires lfw_timeline_layer (story-time | world-history | real-world | character-specific)"))
            elif layer not in TIMELINE_LAYER_ENUM:
                issues.append(("timeline-layer", f"{rel}: lfw_timeline_layer='{layer}' not in legal set (expected: {', '.join(sorted(TIMELINE_LAYER_ENUM))})"))
            # character-specific timelines should declare a Character
            if layer == "character-specific":
                if not fm.get("lfw_character", "").strip():
                    issues.append(("timeline-layer", f"{rel}: character-specific Timeline should declare lfw_character (wikilink to Character atom)"))

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


def check_load_declared(ov_root: pathlib.Path, build_router) -> list:
    """Check 13 (v1.5): every engine chapter file declares a valid lfw_load block.
    Returns issues from build_router.validate_lfw_load for each source."""
    if build_router is None:
        return [("load-declared", "build-router.py is unavailable; cannot verify lfw_load declarations")]
    issues = []
    sources = build_router.collect_sources()
    if not sources:
        issues.append(("load-declared", "no engine sources with lfw_load found"))
        return issues
    # Cross-check: every engine .md file must have lfw_load (no silent omissions)
    engine = ov_root / "_writing-engine"
    expected = set()
    for p in sorted(engine.glob("*.md")):
        if p.name == "_ROUTER.md":
            continue
        expected.add(p.relative_to(ov_root).as_posix())
    for p in sorted((engine / "_meta").glob("*.md")):
        expected.add(p.relative_to(ov_root).as_posix())
    declared = {rel for rel, _, _ in sources}
    missing = expected - declared
    for m in sorted(missing):
        issues.append(("load-declared", f"{m}: missing lfw_load frontmatter block"))
    # Per-source validation
    for rel, ll, _ in sources:
        for r, err in build_router.validate_lfw_load(rel, ll):
            issues.append(("load-declared", f"{r}: {err}"))
    return issues


def check_router_fresh(ov_root: pathlib.Path, build_router) -> list:
    """Check 14 (v1.5): regenerate the router in memory; fail if the committed
    _ROUTER.md differs. Stale router becomes a build failure."""
    if build_router is None:
        return [("router-fresh", "build-router.py is unavailable; cannot verify _ROUTER.md freshness")]
    router_path = ov_root / "_writing-engine" / "_ROUTER.md"
    if not router_path.is_file():
        return [("router-fresh", "_writing-engine/_ROUTER.md is missing; run build-router.py")]
    sources = build_router.collect_sources()
    try:
        expected = build_router.render_router(sources)
    except SystemExit as e:
        return [("router-fresh", f"build-router rejected sources during render: {e}")]
    actual = router_path.read_text()
    if expected != actual:
        return [("router-fresh", "_ROUTER.md is stale; regenerate with `python3 _writing-engine/_scripts/build-router.py`")]
    return []


def check_genre_isolation(build_router) -> list:
    """Check 16 (v1.5): positive assertion that the router never dispatches
    fiction-pack chapters for non-fiction/dissertation cartridges, and never
    dispatches chapter 06 / 10-ARGUMENT for fiction cartridges. The router
    construction makes this impossible by design; this check is the executable
    proof."""
    if build_router is None:
        return [("genre-isolation", "build-router.py is unavailable; cannot assert genre isolation")]
    sources = build_router.collect_sources()
    _, _, by_genre_activity = build_router.build_dispatch_tables(sources)

    # Identify the chapters that should NEVER appear under the wrong genre.
    fiction_pack_paths = set()
    nonfic_pack_paths = set()
    for rel, ll, _ in sources:
        if ll.get("tier") != "pack":
            continue
        genres = ll.get("genres", [])
        if "fiction" in genres or "screenplay" in genres or "play" in genres:
            if "non-fiction" not in genres and "dissertation" not in genres:
                fiction_pack_paths.add(rel)
        if "non-fiction" in genres or "dissertation" in genres:
            if "fiction" not in genres and "screenplay" not in genres and "play" not in genres:
                nonfic_pack_paths.add(rel)

    issues = []
    # Fiction-pack must never appear under non-fiction or dissertation
    for (g, a), paths in by_genre_activity.items():
        if g in ("non-fiction", "dissertation"):
            for p in paths:
                if p in fiction_pack_paths:
                    issues.append(("genre-isolation",
                                   f"router dispatches fiction-pack chapter '{p}' under "
                                   f"genre='{g}' activity='{a}' — this should never happen"))
        if g in ("fiction", "screenplay", "play"):
            for p in paths:
                if p in nonfic_pack_paths:
                    issues.append(("genre-isolation",
                                   f"router dispatches non-fiction-pack chapter '{p}' under "
                                   f"genre='{g}' activity='{a}' — this should never happen"))
    return issues


# Activity codes legal in chapter 03's set (kept here as a fallback if build-router
# is unavailable; build_router.VALID_ACTIVITIES is the canonical source).
_SESSION_KNOWN_ACTIVITIES = {
    "SESSION-START", "OUTLINE", "DRAFT", "REVISE", "RESEARCH-INTEGRATION",
    "READ-THROUGH", "STUCK-DIAGNOSTIC", "VOICE-CHECK", "WORLDBUILDING", "BETA-PREP",
    "READER-SIMULATION", "ARGUMENT-AUDIT", "CLAIM-EVIDENCE-CHECK", "STEELMAN",
    "SYNTHESIS-CHECK", "CRAFT-REVIEW",
    "SCENE-AUDIT", "CHARACTER-CONSISTENCY", "CONTINUITY-CHECK", "SETUP-PAYOFF-AUDIT",
    "DIALOGUE-AUDIT", "POV-VOICE-DRIFT", "THEME-CHECK",
    "WEATHER-CHECK", "MIDDLE-AUDIT",
}


def check_session_read_coverage(cartridge: pathlib.Path, build_router, manifest_genre: str) -> list:
    """Check 15 (v1.5): for every session log in the cartridge, verify lfw_chapters_loaded
    contains at least the chapters the router marks required for that (genre, activity).
    Warn on over-reading. Skip when activity is unknown (META, BOOTSTRAP, etc.)."""
    issues = []
    sessions_dir = cartridge / "Sessions"
    if not sessions_dir.is_dir():
        return issues
    if build_router is None:
        # Cannot compute coverage without router knowledge; skip rather than fail
        return issues
    sources = build_router.collect_sources()
    bootstrap, _, by_genre_activity = build_router.build_dispatch_tables(sources)
    bootstrap_set = set(bootstrap)
    # Add the router itself — it's always loaded (the AI consults it)
    bootstrap_set.add("_writing-engine/_ROUTER.md")

    valid_activities = getattr(build_router, "VALID_ACTIVITIES", _SESSION_KNOWN_ACTIVITIES)

    for session_file in sorted(sessions_dir.glob("*.md")):
        if session_file.name.startswith("."):
            continue
        try:
            text = session_file.read_text()
        except Exception as e:
            issues.append(("session-read-coverage", f"{session_file.relative_to(cartridge)}: cannot read ({e})"))
            continue
        fm = parse_frontmatter(text)
        # Activity field: prefer lfw_activity, fall back to lfw_session_activity
        activity = fm.get("lfw_activity", "") or fm.get("lfw_session_activity", "")
        if isinstance(activity, str):
            activity = activity.strip()
        rel = session_file.relative_to(cartridge).as_posix()
        if not activity:
            issues.append(("session-read-coverage", f"{rel}: missing lfw_activity / lfw_session_activity"))
            continue
        # Skip non-standard activities (BOOTSTRAP, META, etc.) — they don't have router dispatch
        if activity not in valid_activities or activity == "all":
            # Warn-only: chapters_loaded recommended but not enforceable
            chapters_loaded = fm.get("lfw_chapters_loaded", None)
            if chapters_loaded is None:
                issues.append(("session-read-coverage-warn",
                               f"{rel}: activity '{activity}' is not a known cadence activity; "
                               f"lfw_chapters_loaded coverage check skipped (informational)"))
            continue
        # Required set: bootstrap + on-demand dispatched for (genre, activity)
        required = set(bootstrap_set)
        dispatched = by_genre_activity.get((manifest_genre, activity), [])
        required |= set(dispatched)
        # Check lfw_chapters_loaded
        chapters_loaded = fm.get("lfw_chapters_loaded", None)
        if chapters_loaded is None:
            issues.append(("session-read-coverage",
                           f"{rel}: missing lfw_chapters_loaded (required for activity '{activity}')"))
            continue
        if not isinstance(chapters_loaded, list):
            issues.append(("session-read-coverage",
                           f"{rel}: lfw_chapters_loaded must be a list, got {type(chapters_loaded).__name__}"))
            continue
        loaded_set = set(str(c).strip() for c in chapters_loaded if str(c).strip())
        missing = required - loaded_set
        extra = loaded_set - required
        if missing:
            issues.append(("session-read-coverage",
                           f"{rel}: activity '{activity}' under genre '{manifest_genre}' "
                           f"required chapters not in lfw_chapters_loaded: {sorted(missing)}"))
        if extra:
            issues.append(("session-read-coverage-warn",
                           f"{rel}: activity '{activity}' loaded extra chapters not required by router: {sorted(extra)}"))
    return issues


def manifest_genre(cartridge: pathlib.Path) -> str:
    """Return the cartridge's lfw_genre from the manifest, or empty string."""
    mp = cartridge / "_manuscript-manifest.md"
    if not mp.is_file():
        return ""
    fm = parse_frontmatter(mp.read_text())
    return str(fm.get("lfw_genre", "")).strip()

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

    # Load build-router lazily (v1.5 router-driven checks)
    build_router = _load_build_router()
    total_issues = 0
    total_warnings = 0
    all_types = set()

    # OV-level router checks: load-declared (13), router-fresh (14), genre-isolation (16)
    print("=== Engine router checks ===")
    engine_issues = check_load_declared(ov_root, build_router)
    engine_issues += check_router_fresh(ov_root, build_router)
    engine_issues += check_genre_isolation(build_router)
    if not engine_issues:
        print("  (no issues)")
    else:
        by_check = defaultdict(list)
        for severity, msg in engine_issues:
            by_check[severity].append(msg)
        for check, msgs in sorted(by_check.items()):
            label = "warn" if check.endswith("-warn") else "FAIL"
            print(f"  [{check}] {len(msgs)} issue(s) ({label}):")
            for m in msgs:
                print(f"    - {m}")
            if check.endswith("-warn"):
                total_warnings += len(msgs)
            else:
                total_issues += len(msgs)
    print()

    for cartridge in cartridges:
        print(f"=== {cartridge.name} ===")
        issues, types = check_cartridge(cartridge)
        issues += check_state_references(cartridge)
        # v1.5: session read-coverage (check 15)
        c_genre = manifest_genre(cartridge)
        issues += check_session_read_coverage(cartridge, build_router, c_genre)
        all_types |= types
        if not issues:
            print("  (no issues)")
        else:
            # Group by check name
            by_check = defaultdict(list)
            for severity, msg in issues:
                by_check[severity].append(msg)
            for check, msgs in sorted(by_check.items()):
                label = "warn" if check.endswith("-warn") else "FAIL"
                print(f"  [{check}] {len(msgs)} issue(s) ({label}):")
                for m in msgs:
                    print(f"    - {m}")
                if check.endswith("-warn"):
                    total_warnings += len(msgs)
                else:
                    total_issues += len(msgs)
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
        if total_warnings:
            print(f"ALL CHECKS PASSED ({total_warnings} warning(s))")
        else:
            print("ALL CHECKS PASSED")
        sys.exit(0)
    else:
        print(f"TOTAL ISSUES: {total_issues}" + (f" (+{total_warnings} warning(s))" if total_warnings else ""))
        sys.exit(1)

if __name__ == "__main__":
    main()
