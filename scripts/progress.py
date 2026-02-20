#!/usr/bin/env python3
"""Show progress on detailed game entries vs master list.

Reads master_list.csv (the canonical game catalog) and diffs against
games/ to show what's been researched and what's next. Source lists in
sources/lists/ are used as enrichment for prioritization.

Usage:
    python3 scripts/progress.py        # stats + next 20 games
    python3 scripts/progress.py 50     # stats + next 50 games
    python3 scripts/progress.py 0      # stats only
"""

import csv
import glob
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_CSV = os.path.join(ROOT, "master_list.csv")
LISTS_DIR = os.path.join(ROOT, "sources", "lists")
GAMES_DIR = os.path.join(ROOT, "games")


def load_master_list():
    """Load master_list.csv and return a dict keyed by lowercase name.

    Returns: {lowercase_name: {"name": str, "year": str, "bgg_id": str}}
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
    """Return set of lowercase names and count of game files.

    Includes primary names and alternate_names from each game file.
    Returns: (set of lowercase names, number of game files)
    """
    names = set()
    file_count = 0
    primary_names = set()
    if not os.path.isdir(GAMES_DIR):
        return names, file_count, primary_names

    for fname in os.listdir(GAMES_DIR):
        if not fname.endswith(".yaml"):
            continue
        file_count += 1
        game_path = os.path.join(GAMES_DIR, fname)
        try:
            with open(game_path) as f:
                game_data = yaml.safe_load(f)
            if game_data and "name" in game_data:
                names.add(game_data["name"].lower())
                primary_names.add(game_data["name"].lower())
            if game_data and "alternate_names" in game_data:
                for alt in game_data.get("alternate_names", []):
                    if alt:
                        names.add(alt.lower())
        except Exception:
            pass

    return names, file_count, primary_names


def main():
    show_count = 20
    if len(sys.argv) > 1:
        show_count = int(sys.argv[1])

    master = load_master_list()
    total = len(master)

    if total == 0:
        print("No games found in master_list.csv")
        print("Run: python3 scripts/scrape_wikidata.py")
        return

    existing_names, num_entries, primary_names = load_existing()
    enrichment = load_source_enrichment()

    # Enrich master list with source info
    for key, game in master.items():
        game["sources"] = enrichment.get(key, [])

    # Partition into done vs remaining
    done = {}
    remaining = {}
    for key, game in master.items():
        if key in existing_names:
            done[key] = game
        else:
            remaining[key] = game

    # Orphans: game files whose primary name isn't in the master list
    orphan_count = len(primary_names - set(master.keys()))

    num_sources = len(glob.glob(os.path.join(LISTS_DIR, "*.yaml")))

    pct = len(done) / total * 100 if total else 0
    print(f"Master list: {total} games")
    print(f"Game entries: {num_entries} files")
    if orphan_count:
        print(f"  ({orphan_count} not in master list)")
    print(f"Progress: {len(done)}/{total} ({pct:.1f}%)")
    print(f"Remaining: {len(remaining)}")
    if num_sources:
        print(f"Source lists: {num_sources} files (used for prioritization)")

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
