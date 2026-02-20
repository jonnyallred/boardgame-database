#!/usr/bin/env python3
"""
Wikidata board game scraper

Queries Wikidata's public SPARQL endpoint for board games. No authentication
required. Each run fetches one page of 10,000 results and appends to
master_list.csv. Run again to get the next page.

State tracked in wikidata_state.json:
    offset  — number of rows already fetched
    done    — true once a page comes back with fewer than PAGE_SIZE results

Usage:
    python scripts/scrape_wikidata.py           # fetch next 10,000 games
    python scripts/scrape_wikidata.py --status  # show progress without fetching

Requirements:
    pip install requests
"""

import csv
import json
import sys
from pathlib import Path

import requests

# ── Config ────────────────────────────────────────────────────────────────────

ENDPOINT  = "https://query.wikidata.org/sparql"
OUTPUT    = Path("master_list.csv")
STATE     = Path("wikidata_state.json")
PAGE_SIZE = 10_000
FIELDS    = ["bgg_id", "name", "year", "type"]

# Wikidata Q131436 = board game
# P577  = publication date
# P2339 = BoardGameGeek ID
QUERY = """\
SELECT DISTINCT ?game ?gameLabel ?date ?bggId WHERE {{
  ?game wdt:P31 wd:Q131436 .
  OPTIONAL {{ ?game wdt:P577 ?date }}
  OPTIONAL {{ ?game wdt:P2339 ?bggId }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" . }}
}}
ORDER BY ?game
LIMIT {limit}
OFFSET {offset}
"""

HEADERS = {
    # Wikidata asks that automated tools identify themselves
    "User-Agent": "BoardGameDatabase/1.0 (personal collection project)",
    "Accept": "application/sparql-results+json",
}

# ── State ─────────────────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"offset": 0, "done": False}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2))

# ── Fetch & parse ─────────────────────────────────────────────────────────────

def fetch_page(offset: int) -> list[dict]:
    query = QUERY.format(limit=PAGE_SIZE, offset=offset)
    r = requests.get(
        ENDPOINT,
        params={"query": query, "format": "json"},
        headers=HEADERS,
        timeout=90,
    )
    r.raise_for_status()

    rows = []
    seen = set()  # deduplicate by (name, bgg_id)

    for b in r.json()["results"]["bindings"]:
        name   = b.get("gameLabel", {}).get("value", "")
        bgg_id = b.get("bggId",     {}).get("value", "")
        date   = b.get("date",      {}).get("value", "")

        # Skip entries where Wikidata has no English label (shows as Q-number)
        if not name or (name.startswith("Q") and name[1:].isdigit()):
            continue

        # Extract year from ISO date string ("2019-01-01T00:00:00Z" → "2019")
        year = date[:4] if date else ""

        key = (name, bgg_id)
        if key in seen:
            continue
        seen.add(key)

        rows.append({
            "bgg_id": bgg_id,
            "name":   name,
            "year":   year,
            "type":   "boardgame",
        })

    return rows

# ── Status ────────────────────────────────────────────────────────────────────

def print_status(s: dict) -> None:
    if s["done"]:
        print(f"Complete. {s['offset']:,} total rows fetched — all pages done.")
    else:
        print(f"Progress: {s['offset']:,} rows fetched so far.")
        print(f"Next run will fetch rows {s['offset']:,}–{s['offset'] + PAGE_SIZE:,}.")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    s = load_state()

    if "--status" in sys.argv:
        print_status(s)
        return

    if s["done"]:
        print("All pages already fetched. Use --status to review, or delete")
        print(f"{STATE} to start over.")
        return

    offset = s["offset"]
    print(f"Fetching rows {offset:,}–{offset + PAGE_SIZE:,} from Wikidata...")

    rows = fetch_page(offset)
    n    = len(rows)

    first_write = not OUTPUT.exists()
    with OUTPUT.open("w" if first_write else "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if first_write:
            writer.writeheader()
        writer.writerows(rows)

    s["offset"] = offset + PAGE_SIZE
    if n < PAGE_SIZE:
        s["done"] = True

    save_state(s)

    print(f"Done. {n:,} games written to {OUTPUT}.")
    if s["done"]:
        print("Last page reached — scrape complete.")
    else:
        print(f"Run again to fetch the next {PAGE_SIZE:,}.")


if __name__ == "__main__":
    main()
