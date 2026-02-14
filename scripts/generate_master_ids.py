#!/usr/bin/env python3
"""One-time migration: add `id` slugs to every entry in master_list.yaml.

For games that already have detailed files in games/, uses the actual file id.
For the rest, auto-generates a slug from the game name.

Uses string manipulation (not yaml.dump) to preserve section comments.
"""

import os
import re
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_LIST = os.path.join(ROOT, "master_list.yaml")
GAMES_DIR = os.path.join(ROOT, "games")


def slugify(name: str) -> str:
    """Generate a URL-friendly slug from a game name."""
    s = name.lower()
    # Normalize unicode (strip accents)
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    # Replace & with 'and'
    s = s.replace("&", "and")
    # Drop apostrophes
    s = s.replace("'", "")
    s = s.replace("\u2019", "")  # right single quotation mark
    # Replace en-dash / em-dash with hyphen
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    # Non-alphanumeric → hyphen
    s = re.sub(r"[^a-z0-9]+", "-", s)
    # Collapse multiple hyphens
    s = re.sub(r"-+", "-", s)
    # Strip leading/trailing hyphens
    s = s.strip("-")
    return s


def load_existing_game_ids() -> set:
    """Get all game ids from files in games/."""
    ids = set()
    for fname in os.listdir(GAMES_DIR):
        if fname.endswith(".yaml"):
            ids.add(fname[:-5])  # strip .yaml
    return ids


def build_name_to_id_map(existing_ids: set) -> dict:
    """Build mappings from game name/year to actual file id for existing games.

    Returns (name_year_map, name_only_map) where name_year_map is keyed by
    (name, year) and name_only_map is keyed by name alone (for fallback).
    """
    name_year_to_id = {}
    name_to_id = {}
    for game_id in existing_ids:
        filepath = os.path.join(GAMES_DIR, f"{game_id}.yaml")
        name = None
        year = None
        with open(filepath) as f:
            for line in f:
                if line.startswith("name:"):
                    m = re.match(r'name:\s*"(.+?)"', line)
                    if m:
                        name = m.group(1)
                    else:
                        name = line.split(":", 1)[1].strip()
                elif line.startswith("year:"):
                    year = line.split(":", 1)[1].strip()
                if name and year:
                    break
        if name and year:
            name_year_to_id[(name, year)] = game_id
        if name:
            name_to_id[name] = game_id
    return name_year_to_id, name_to_id


def extract_name_year(entry_lines: list) -> tuple:
    """Extract name and year from a list of YAML lines for one entry."""
    name = None
    year = None
    for line in entry_lines:
        # Match name: in the line (may be preceded by "- ")
        m = re.search(r'name:\s*"(.+?)"', line)
        if m:
            name = m.group(1)
            continue
        m = re.search(r'name:\s*(.+)', line)
        if m and not name:
            name = m.group(1).strip().strip('"')
            continue
        m = re.search(r'year:\s*(-?\d+)', line)
        if m:
            year = m.group(1)
    return name, year


def process_master_list():
    with open(MASTER_LIST) as f:
        content = f.read()

    existing_ids = load_existing_game_ids()
    name_year_to_id, name_to_id = build_name_to_id_map(existing_ids)

    lines = content.split("\n")
    output_lines = []
    slug_counts = {}  # track all slugs for collision detection
    all_assignments = []  # (line_index, slug, name) for reporting

    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if this line starts a list entry (  - name: or  - id:)
        if re.match(r"^  - name:", line):
            # Collect all lines of this entry
            entry_start = i
            entry_lines = [line]
            i += 1
            while i < len(lines) and re.match(r"^    \w", lines[i]):
                entry_lines.append(lines[i])
                i += 1

            name, year = extract_name_year(entry_lines)
            if not name:
                # Can't process, keep as-is
                output_lines.extend(entry_lines)
                continue

            # Determine slug: prefer existing file id, else auto-generate
            key = (name, str(year) if year else "")
            if key in name_year_to_id:
                slug = name_year_to_id[key]
            elif name in name_to_id:
                slug = name_to_id[name]
            else:
                slug = slugify(name)

            # Track for collision detection
            slug_counts.setdefault(slug, []).append(name)
            all_assignments.append((entry_start, slug, name))

            # Insert id as first field: replace "  - name:" with "  - id: slug\n    name:"
            first_line = entry_lines[0]
            # Extract the name part after "  - name:"
            name_part = first_line.split("- name:", 1)[1]
            new_first = f"  - id: {slug}"
            new_name_line = f"    name:{name_part}"
            output_lines.append(new_first)
            output_lines.append(new_name_line)
            output_lines.extend(entry_lines[1:])
        elif re.match(r"^  - id:", line):
            # Already has an id field — skip (idempotent)
            output_lines.append(line)
            i += 1
        else:
            output_lines.append(line)
            i += 1

    # Check for collisions
    collisions = {slug: names for slug, names in slug_counts.items() if len(names) > 1}
    if collisions:
        print("COLLISION DETECTED — aborting!")
        for slug, names in collisions.items():
            print(f"  {slug}: {names}")
        return False

    # Verify all existing game files have a match
    matched_ids = set()
    for _, slug, _ in all_assignments:
        if slug in existing_ids:
            matched_ids.add(slug)
    unmatched = existing_ids - matched_ids
    if unmatched:
        print(f"WARNING: {len(unmatched)} game files not matched to master list entries:")
        for uid in sorted(unmatched):
            print(f"  {uid}")

    # Write output
    result = "\n".join(output_lines)
    with open(MASTER_LIST, "w") as f:
        f.write(result)

    print(f"Done! Added id slugs to {len(all_assignments)} entries.")
    print(f"Existing game files matched: {len(matched_ids)}/{len(existing_ids)}")
    if unmatched:
        print(f"Unmatched game files (not in master list): {len(unmatched)}")
    return True


if __name__ == "__main__":
    process_master_list()
