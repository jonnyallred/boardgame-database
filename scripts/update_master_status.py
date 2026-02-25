#!/usr/bin/env python3
"""Update master_list.csv rows with status, notes, and yaml_id.

Single update:
    python3 scripts/update_master_status.py "1776" --yaml-id 1776-the-game-of-the-american-revolutionary-war
    python3 scripts/update_master_status.py "Andada" --status failed --notes "No sources found"

Batch from JSON:
    python3 scripts/update_master_status.py --from-results results.json

Backfill yaml_id by matching YAML names against master list:
    python3 scripts/update_master_status.py --backfill
    python3 scripts/update_master_status.py --backfill --dry-run
"""

import argparse
import csv
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_CSV = os.path.join(ROOT, "master_list.csv")
GAMES_DIR = os.path.join(ROOT, "games")
FIELDNAMES = ["bgg_id", "name", "year", "type", "status", "notes", "yaml_id"]


def slugify(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def read_csv():
    """Read master_list.csv and return list of dicts."""
    rows = []
    with open(MASTER_CSV) as f:
        for row in csv.DictReader(f):
            # Ensure new columns exist
            for col in ("status", "notes", "yaml_id"):
                row.setdefault(col, "")
                if row[col] is None:
                    row[col] = ""
            rows.append(row)
    return rows


def write_csv(rows):
    """Write rows back to master_list.csv."""
    with open(MASTER_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def update_row(rows, name, status=None, notes=None, yaml_id=None):
    """Find row by name (case-insensitive) and update fields. Returns True if found."""
    target = name.lower().strip()
    for row in rows:
        if row["name"].lower().strip() == target:
            if status is not None:
                row["status"] = status
            if notes is not None:
                row["notes"] = notes
            if yaml_id is not None:
                row["yaml_id"] = yaml_id
            return True
    return False


def build_yaml_name_map():
    """Build {lowercase_name: slug, alt_name: slug} from all YAML files."""
    name_to_slug = {}
    if not os.path.isdir(GAMES_DIR):
        return name_to_slug
    for fname in os.listdir(GAMES_DIR):
        if not fname.endswith(".yaml"):
            continue
        slug = fname[:-5]
        try:
            with open(os.path.join(GAMES_DIR, fname)) as f:
                data = yaml.safe_load(f)
            if not data:
                continue
            if "name" in data:
                name_to_slug[data["name"].lower()] = slug
            for alt in data.get("alternate_names") or []:
                if alt:
                    name_to_slug[alt.lower()] = slug
        except Exception:
            pass
    return name_to_slug


def _is_subtitle_match(short, long):
    """Check if short is the base name and long adds a subtitle.

    Matches patterns like:
      "heat" → "heat: pedal to the metal"
      "1776" → "1776: the game of the american revolutionary war"
      "the crew" → "the crew: the quest for planet nine"
    Does NOT match:
      "ants" → "ants in the pants" (no subtitle delimiter)
      "steam" → "age of steam" (not a prefix)
    """
    if not long.startswith(short):
        return False
    rest = long[len(short):]
    if not rest:
        return False
    # Must be followed by a subtitle delimiter
    return rest[0] in (":", ",") or rest.startswith(" -") or rest.startswith(" (")


def backfill(dry_run=False):
    """Auto-populate yaml_id for master list entries that match YAML files by name."""
    rows = read_csv()
    name_to_slug = build_yaml_name_map()
    existing_slugs = {f[:-5] for f in os.listdir(GAMES_DIR) if f.endswith(".yaml")}

    updated = 0
    for row in rows:
        # Skip if already has yaml_id or has an excluded status
        if row.get("yaml_id", "").strip():
            continue
        if row.get("status", "").strip() in ("skip", "failed", "ambiguous", "duplicate"):
            continue

        name = row["name"].strip()
        name_lower = name.lower()
        slug = slugify(name)

        # Already matches by slug — no yaml_id needed
        if slug in existing_slugs:
            continue

        # Already matches by exact name — no yaml_id needed
        if name_lower in name_to_slug and name_to_slug[name_lower] == slug:
            continue

        # Strip parenthetical suffixes like "(game)", "(board game)" for matching
        stripped = re.sub(r"\s*\((?:game|board game|card game|dup)\)\s*$", "", name_lower, flags=re.IGNORECASE)
        stripped_slug = slugify(stripped) if stripped != name_lower else None

        # Already matches by stripped slug — just needs yaml_id
        if stripped_slug and stripped_slug in existing_slugs and stripped_slug != slug:
            matched_slug = stripped_slug
        else:
            # Check if YAML name/alt exactly matches this master name
            matched_slug = name_to_slug.get(name_lower)
            if not matched_slug and stripped != name_lower:
                matched_slug = name_to_slug.get(stripped)

        if not matched_slug:
            # Try subtitle matching: "Heat" matches "Heat: Pedal to the Metal"
            # Only match if name appears before a subtitle delimiter (: or -)
            candidates = []
            for yaml_name, yaml_slug in name_to_slug.items():
                if _is_subtitle_match(name_lower, yaml_name):
                    candidates.append((yaml_name, yaml_slug))
            if len(candidates) == 1:
                matched_slug = candidates[0][1]

        if matched_slug and os.path.isfile(os.path.join(GAMES_DIR, f"{matched_slug}.yaml")):
            if dry_run:
                print(f"  Would set: {name} → {matched_slug}")
            else:
                row["yaml_id"] = matched_slug
            updated += 1

    if not dry_run and updated:
        write_csv(rows)

    return updated


def main():
    parser = argparse.ArgumentParser(description="Update master_list.csv status fields")
    parser.add_argument("name", nargs="?", help="Game name to update")
    parser.add_argument("--status", help="Set status (skip, failed, ambiguous, duplicate)")
    parser.add_argument("--notes", help="Set notes")
    parser.add_argument("--yaml-id", help="Set yaml_id (slug of the YAML file)")
    parser.add_argument("--from-results", help="Batch update from JSON results file")
    parser.add_argument("--backfill", action="store_true", help="Auto-populate yaml_id from YAML names")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change without writing")
    args = parser.parse_args()

    if args.backfill:
        count = backfill(dry_run=args.dry_run)
        label = "Would update" if args.dry_run else "Updated"
        print(f"{label} {count} entries")
        return

    if args.from_results:
        with open(args.from_results) as f:
            results = json.load(f)
        rows = read_csv()
        updated = 0
        not_found = []
        for entry in results:
            name = entry.get("name", "")
            status = entry.get("status")
            # "done" status means clear the status field (it's a normal completed entry)
            if status == "done":
                status = ""
            notes = entry.get("notes")
            yaml_id = entry.get("yaml_id")
            if update_row(rows, name, status=status, notes=notes, yaml_id=yaml_id):
                updated += 1
            else:
                not_found.append(name)
        if not args.dry_run:
            write_csv(rows)
        print(f"Updated {updated}/{len(results)} entries")
        if not_found:
            print(f"Not found in master list: {', '.join(not_found)}")
        return

    if not args.name:
        parser.print_help()
        sys.exit(1)

    rows = read_csv()
    if update_row(rows, args.name, status=args.status, notes=args.notes, yaml_id=args.yaml_id):
        if not args.dry_run:
            write_csv(rows)
            print(f"Updated '{args.name}'")
        else:
            print(f"Would update '{args.name}'")
    else:
        print(f"'{args.name}' not found in master_list.csv", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
