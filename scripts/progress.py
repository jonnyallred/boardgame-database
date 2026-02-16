#!/usr/bin/env python3
"""Show progress on detailed game entries vs source lists.

Reads all YAML files in sources/lists/, unions game IDs across them,
and diffs against games/ to show what's been researched and what's next.

Usage:
    python3 scripts/progress.py        # stats + next 20 games
    python3 scripts/progress.py 50     # stats + next 50 games
    python3 scripts/progress.py 0      # stats only
"""

import glob
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTS_DIR = os.path.join(ROOT, "sources", "lists")
GAMES_DIR = os.path.join(ROOT, "games")


def load_all_lists():
    """Load all source list files and return a unified game dict.

    Returns dict keyed by game id:
        {id: {"name": str, "year": int, "sources": [str, ...]}}
    """
    games = {}
    list_files = sorted(glob.glob(os.path.join(LISTS_DIR, "*.yaml")))
    for path in list_files:
        with open(path) as f:
            data = yaml.safe_load(f)
        if not data or "games" not in data:
            continue
        source_name = data.get("source", os.path.basename(path))
        for g in data["games"]:
            gid = g.get("id")
            if not gid:
                continue
            if gid not in games:
                games[gid] = {
                    "name": g.get("name", gid),
                    "year": g.get("year", "?"),
                    "sources": [],
                }
            games[gid]["sources"].append(source_name)
    return games


def load_existing():
    """Return set of game IDs and dict of all names (including alternates) to IDs.

    Returns: (set of IDs, dict of {name: id})
    """
    existing_ids = set()
    name_to_id = {}  # Maps all names (primary + alternates) to game ID

    if not os.path.isdir(GAMES_DIR):
        return existing_ids, name_to_id

    for fname in os.listdir(GAMES_DIR):
        if not fname.endswith(".yaml"):
            continue

        game_id = fname[:-5]
        existing_ids.add(game_id)

        # Load the game file to get name and alternate_names
        game_path = os.path.join(GAMES_DIR, fname)
        try:
            with open(game_path) as f:
                game_data = yaml.safe_load(f)

            # Map primary name to ID
            if game_data and "name" in game_data:
                name_to_id[game_data["name"].lower()] = game_id

            # Map alternate names to ID
            if game_data and "alternate_names" in game_data:
                for alt_name in game_data.get("alternate_names", []):
                    if alt_name:
                        name_to_id[alt_name.lower()] = game_id
        except Exception:
            # If we can't read the file, just skip the name mapping
            pass

    return existing_ids, name_to_id


def main():
    show_count = 20
    if len(sys.argv) > 1:
        show_count = int(sys.argv[1])

    all_games = load_all_lists()
    existing_ids, name_to_id = load_existing()
    total = len(all_games)

    if total == 0:
        print("No source lists found in sources/lists/")
        print("Add YAML files there to start tracking games.")
        return

    # Check if game exists by ID or by name match
    done_ids = set()
    remaining = {}
    for gid, g in all_games.items():
        # Check if ID exists
        if gid in existing_ids:
            done_ids.add(gid)
            continue

        # Check if name matches any existing game (by primary or alternate name)
        game_name_lower = g["name"].lower()
        if game_name_lower in name_to_id:
            done_ids.add(gid)
            continue

        # Not found, add to remaining
        remaining[gid] = g

    orphans = existing_ids - set(all_games.keys())

    pct = len(done_ids) / total * 100 if total else 0
    print(f"Progress: {len(done_ids)}/{total} ({pct:.1f}%)")
    print(f"Remaining: {len(remaining)}")
    print(f"Sources: {len(glob.glob(os.path.join(LISTS_DIR, '*.yaml')))} list files")
    if orphans:
        print(f"Orphans: {len(orphans)} game files not in any source list")

    if show_count > 0 and remaining:
        # Sort by number of sources (most-nominated first), then alphabetically
        sorted_remaining = sorted(
            remaining.items(),
            key=lambda x: (-len(x[1]["sources"]), x[0]),
        )
        n = min(show_count, len(sorted_remaining))
        print(f"\nNext {n} games to add:")
        print("-" * 70)
        for gid, g in sorted_remaining[:n]:
            sources = ", ".join(g["sources"])
            print(f"  {g['name']} ({g['year']})  [{sources}]")


if __name__ == "__main__":
    main()
