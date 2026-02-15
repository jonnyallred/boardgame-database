#!/usr/bin/env python3
"""Show progress on detailed game entries vs the master list.

Usage:
    python3 scripts/progress.py        # stats + next 20 games
    python3 scripts/progress.py 50     # stats + next 50 games
    python3 scripts/progress.py 0      # stats only
"""

import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_LIST = os.path.join(ROOT, "master_list.yaml")
GAMES_DIR = os.path.join(ROOT, "games")


def main():
    show_count = 20
    if len(sys.argv) > 1:
        show_count = int(sys.argv[1])

    # Load master list
    with open(MASTER_LIST) as f:
        data = yaml.safe_load(f)

    games = data["games"]
    total = len(games)

    # Check which have files
    existing = set()
    for fname in os.listdir(GAMES_DIR):
        if fname.endswith(".yaml"):
            existing.add(fname[:-5])

    done = [g for g in games if g.get("id") in existing]
    remaining = [g for g in games if g.get("id") not in existing]

    pct = len(done) / total * 100
    print(f"Progress: {len(done)}/{total} ({pct:.1f}%)")
    print(f"Remaining: {len(remaining)}")

    if show_count > 0 and remaining:
        print(f"\nNext {min(show_count, len(remaining))} games to add:")
        print("-" * 60)
        for g in remaining[:show_count]:
            source = g.get("source", "?")
            name = g.get("name", "?")
            year = g.get("year", "?")
            print(f"  {name} ({year})  [{source}]")


if __name__ == "__main__":
    main()
