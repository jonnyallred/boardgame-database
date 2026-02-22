#!/usr/bin/env python3
"""Show progress on detailed game entries vs master list.

Reads master_list.csv (the canonical game catalog) and diffs against
games/ to show what's been researched and what's next. Source lists in
sources/lists/ are used as enrichment for prioritization.

Usage:
    python3 scripts/progress.py           # stats + next 20 games
    python3 scripts/progress.py 50        # stats + next 50 games
    python3 scripts/progress.py 0         # stats only
    python3 scripts/progress.py --failed  # list entries with status=failed
    python3 scripts/progress.py --skipped # list entries with status=skip
"""

import csv
import glob
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_CSV = os.path.join(ROOT, "master_list.csv")
LISTS_DIR = os.path.join(ROOT, "sources", "lists")
GAMES_DIR = os.path.join(ROOT, "games")


def slugify(name):
    """Convert a game name to a slug for fuzzy matching.

    E.g. "7 Wonders: Duel" -> "7-wonders-duel"
    """
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


EXCLUDED_STATUSES = {"skip", "failed", "ambiguous", "duplicate"}


def load_master_list():
    """Load master_list.csv and return a dict keyed by lowercase name.

    Returns: {lowercase_name: {"name": str, "year": str, "bgg_id": str,
              "status": str, "notes": str, "yaml_id": str}}
    """
    games = {}
    if not os.path.isfile(MASTER_CSV):
        return games
    with open(MASTER_CSV) as f:
        for row in csv.DictReader(f):
            name = row["name"].strip()
            key = name.lower()
            if key not in games:
                games[key] = {
                    "name": name,
                    "year": row.get("year", "") or "?",
                    "bgg_id": row.get("bgg_id", ""),
                    "status": (row.get("status", "") or "").strip(),
                    "notes": (row.get("notes", "") or "").strip(),
                    "yaml_id": (row.get("yaml_id", "") or "").strip(),
                    "sources": [],
                }
    return games


def load_source_enrichment():
    """Load source lists and return a dict of {lowercase_name: [source_names]}.

    Used to enrich master list entries with provenance info for prioritization.
    """
    enrichment = {}
    list_files = sorted(glob.glob(os.path.join(LISTS_DIR, "*.yaml")))
    for path in list_files:
        with open(path) as f:
            data = yaml.safe_load(f)
        if not data or "games" not in data:
            continue
        source_name = data.get("source", os.path.basename(path))
        for g in data["games"]:
            name = g.get("name", "").strip()
            if not name:
                continue
            key = name.lower()
            enrichment.setdefault(key, []).append(source_name)
    return enrichment


def load_existing():
    """Return matching data for all existing game entries.

    Returns: (set of lowercase names, set of file slugs, number of game files)
    """
    names = set()
    slugs = set()
    file_count = 0
    if not os.path.isdir(GAMES_DIR):
        return names, slugs, file_count

    for fname in os.listdir(GAMES_DIR):
        if not fname.endswith(".yaml"):
            continue
        file_count += 1
        slugs.add(fname[:-5])
        game_path = os.path.join(GAMES_DIR, fname)
        try:
            with open(game_path) as f:
                game_data = yaml.safe_load(f)
            if game_data and "name" in game_data:
                names.add(game_data["name"].lower())
            if game_data and "alternate_names" in game_data:
                for alt in game_data.get("alternate_names", []):
                    if alt:
                        names.add(alt.lower())
        except Exception:
            pass

    return names, slugs, file_count


def main():
    show_count = 20
    filter_status = None

    # Parse args
    args = sys.argv[1:]
    for arg in args:
        if arg.startswith("--"):
            filter_status = arg.lstrip("-")  # e.g. "failed", "skipped", "ambiguous"
            if filter_status == "skipped":
                filter_status = "skip"
        else:
            show_count = int(arg)

    master = load_master_list()
    total = len(master)

    if total == 0:
        print("No games found in master_list.csv")
        print("Run: python3 scripts/scrape_wikidata.py")
        return

    existing_names, existing_slugs, num_entries = load_existing()
    enrichment = load_source_enrichment()

    # Enrich master list with source info
    for key, game in master.items():
        game["sources"] = enrichment.get(key, [])

    # Partition into done / excluded / remaining
    done = {}
    excluded = {}  # entries with a non-empty status (skip, failed, etc.)
    remaining = {}
    for key, game in master.items():
        status = game["status"]
        yaml_id = game["yaml_id"]

        # Check yaml_id first (explicit mapping), then name/slug matching
        if yaml_id and os.path.isfile(os.path.join(GAMES_DIR, f"{yaml_id}.yaml")):
            done[key] = game
        elif key in existing_names or slugify(game["name"]) in existing_slugs:
            done[key] = game
        elif status in EXCLUDED_STATUSES:
            excluded[key] = game
        else:
            remaining[key] = game

    # Status breakdown among excluded entries
    status_counts = {}
    for game in excluded.values():
        s = game["status"]
        status_counts[s] = status_counts.get(s, 0) + 1

    # Orphans: game file slugs not matching any master list entry
    master_slugs = {slugify(g["name"]) for g in master.values()}
    master_yaml_ids = {g["yaml_id"] for g in master.values() if g["yaml_id"]}
    orphan_count = len(existing_slugs - master_slugs - master_yaml_ids)

    num_sources = len(glob.glob(os.path.join(LISTS_DIR, "*.yaml")))

    pct = len(done) / total * 100 if total else 0
    print(f"Master list: {total} games")
    print(f"Game entries: {num_entries} files")
    if orphan_count:
        print(f"  ({orphan_count} not in master list)")
    print(f"Progress: {len(done)}/{total} ({pct:.1f}%)")
    print(f"Remaining: {len(remaining)}")
    if excluded:
        parts = [f"{v} {k}" for k, v in sorted(status_counts.items())]
        print(f"Excluded: {len(excluded)} ({', '.join(parts)})")
    if num_sources:
        print(f"Source lists: {num_sources} files (used for prioritization)")

    # If --<status> flag given, list those entries instead of the queue
    if filter_status:
        matches = {k: g for k, g in master.items() if g["status"] == filter_status}
        if not matches:
            print(f"\nNo entries with status '{filter_status}'")
            return
        print(f"\nEntries with status '{filter_status}' ({len(matches)}):")
        print("-" * 70)
        for key, g in sorted(matches.items(), key=lambda x: x[1]["name"].lower()):
            notes = f"  -- {g['notes']}" if g["notes"] else ""
            print(f"  {g['name']} ({g['year']}){notes}")
        return

    if show_count > 0 and remaining:
        # Sort: most source-list nominations first, then alphabetically
        sorted_remaining = sorted(
            remaining.items(),
            key=lambda x: (-len(x[1]["sources"]), x[1]["name"].lower()),
        )
        n = min(show_count, len(sorted_remaining))
        print(f"\nNext {n} games to add:")
        print("-" * 70)
        for key, g in sorted_remaining[:n]:
            sources = ", ".join(g["sources"])
            suffix = f"  [{sources}]" if sources else ""
            print(f"  {g['name']} ({g['year']}){suffix}")


if __name__ == "__main__":
    main()
