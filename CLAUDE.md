# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Board Game Database** - a curated collection of board games with detailed metadata, ratings, and categorization. The project stores data as YAML files rather than using a traditional database, making it easy to version control and maintain.

**Key Stats:**
- `master_list.csv`: Canonical catalog of all known board games — the "want list" (source of truth)
- `games/`: Individual YAML files with detailed research — the "done list"
- `sources/lists/`: Award/article YAML files — enrichment for prioritization (not the source of truth)
- `schema.yaml`: Complete data structure and validation rules
- `publishers.yaml`: Publisher directory with press kit URLs and contacts
- `images/sources.yaml`: Image provenance tracking (source, license, date)
- `sources/research-log.yaml`: Provenance log of all URLs consulted during research

## Data Structure

### Game Entry Format

Each game file (`games/{slug}.yaml`) contains:

**Identifiers & Metadata:**
- `id`: lowercase slug (e.g., `azul`)
- `name`: Full display name
- `alternate_names[]`: Other titles for the same game (translations, regional names like "Adel Verpflichtet" / "Hoity Toity")
- `year`: Publication year
- `designer[]`: List of designer names
- `publisher[]`: List of publisher names
- `playtime_minutes`, `min_playtime`, `max_playtime`: Playtime information
- `min_age`: Minimum player age

**Relationships:**
- `game_family`: For tracking editions (e.g., "brass" for both "Brass: Lancashire" and "Brass: Birmingham")
- `edition`: Edition identifier for variants
- `base_game`: ID of base game (for expansions)
- `expansions[]`: List of expansion IDs
- `compatible_with[]`: Other games that can be combined

**Rating Scales (0-4):** All ratings use a 4-point scale
- `length`: Snack (0) → Marathon (4)
- `rules_complexity`: Preschool (0) → PhD (4)
- `strategic_depth`: Reflex (0) → Master Plan (4)
- `feel`: Solitary (0) → Fierce (4)
- `value`: Impulse (0) → Heirloom (4)
- `affinity`: Personal overall rating (null until rated)
- `hotness`: Personal "want to play now" rating (null until rated)

**Categorization:**
- `categories[]`: Tags from schema (mechanics, styles, themes, designers, publishers)
  - **Mechanics**: 40+ options (Worker Placement, Deck Building, etc.)
  - **Styles**: Euro, Ameritrash, Abstract, Party, etc.
  - **Themes**: Fantasy, Sci-Fi, Horror, Historical, etc.
  - **Designers**: Reiner Knizia, Uwe Rosenberg, etc. (tags only, not names)
  - **Publishers**: Stonemaier Games, Fantasy Flight, etc. (tags only, not names)

**Evokes (top 5):**
- `evokes[]`: The top 5 feelings a game is designed to evoke, from 18 possible values:
  - **Agency** — High player control, meaningful choices
  - **Clever** — Combos, optimization, "aha" moments
  - **Complete** — Set collection, filling objectives, finishing
  - **Connection** — Shared experiences, bonding, cooperation
  - **Creative** — Open-ended expression, sandbox design
  - **Discovery** — Exploration, hidden content, reveals
  - **Dread** — Horror, survival, looming threats
  - **Humor** — Absurdity, designed-to-laugh moments
  - **Lucky** — Press-your-luck, dice, draw-dependent thrills
  - **Masterful** — High skill ceiling, improving over many plays
  - **Mystery** — Piecing together clues, intrigue
  - **Persuasion** — Dealmaking, convincing others, social influence
  - **Powerful** — Escalation, dominance, asymmetric strength
  - **Progress** — Engine building, tech trees, visible accumulation
  - **Rivalry** — Direct competition, head-to-head contest
  - **Tension** — Close scoring, hidden roles, nail-biting decisions
  - **Unique** — Asymmetry, variable powers, every-session-different
  - **Wonder** — Spectacle, beautiful emergence, awe

**Player Information:**
- `possible_counts[]`: Player counts supported by box rules
- `true_counts[]`: Optimal/best player counts per community consensus

**Other:**
- `description`: Game summary and key mechanics
- `upgrades[]`: Optional custom components or accessories
- `plays_tracked`: Play history tracking (total_plays and configs)

### Master List (Source of Truth)

`master_list.csv` is the canonical catalog of all known board games. It is the source of truth for "what games exist" and drives progress tracking. CSV columns: `bgg_id`, `name`, `year`, `type`.

Games are added to the master list from two sources:
- **Wikidata scraper** (`scripts/scrape_wikidata.py`) — bulk discovery from Wikidata's public SPARQL endpoint
- **Manual additions** — games from source lists, game entries, or other research that aren't already in Wikidata

### Source Lists (Enrichment)

Source lists in `sources/lists/` provide provenance and prioritization data. Each file represents an award list, article, or curated recommendation:

```yaml
source: "Human-readable source name"
url: "https://..."
fetched: 2026-02-16
games:
  - id: azul
    name: Azul
    year: 2017
```

Source lists do **not** define the total game universe — `master_list.csv` does. Instead, they enrich the progress script's output: games appearing in more source lists are prioritized higher in the "next to add" queue. See `sources/lists/README.md` for details.

### Schema

`schema.yaml` documents all valid values for ratings, categories, and templates. Refer to it when:
- Adding new category tags
- Understanding rating scales
- Creating new game entries

## Common Commands

### File Operations

**Add a new game:**
Use the `/add-game` skill (single game) or the `game-researcher` agent (one or many games). Both handle web research, schema validation, and YAML creation automatically.

When adding multiple games at once, split the list into **chunks of 20** and launch one `game-researcher` agent per chunk — all in parallel via the Task tool. Each agent receives a numbered list and processes them sequentially within the batch.

Example: 50 games → 3 agents (20 + 20 + 10), launched in a single message. Do **not** use the Skill tool directly for batch additions.

**Manual alternative** (if needed):
1. Create `games/{slug}.yaml` based on the template in schema.yaml
2. Use an existing game file as reference if any exist
3. Ensure the `id` field matches the filename slug

**Update game data:**
- Edit the YAML file directly
- Validate against schema.yaml if adding new categories

**Add images:**
- Place box art in `images/` folder
- Naming: `Game Name (Year).jpg`
- Record provenance in `images/sources.yaml`
- See `images/README.md` for guidelines and `publishers.yaml` for press contacts

### Validation

The project uses YAML structure only—no linting tools are configured. When editing:
- Maintain YAML syntax (proper indentation with spaces, not tabs)
- Keep field order consistent with the schema
- Ensure `categories[]` values exist in `schema.yaml`

### Progress Tracking

**Check progress:**
- Run `python3 scripts/progress.py` to see completion stats and next games to work on
- Or use the `/progress` skill in Claude Code
- `python3 scripts/progress.py 50` — show next 50 games
- `python3 scripts/progress.py 0` — stats only
- Progress is measured against `master_list.csv` (the source of truth)
- Games appearing in more source lists are shown first (most-nominated = highest priority)

**Image progress:**
- Run `python3 scripts/image_manager.py` to see image coverage stats
- `python3 scripts/image_manager.py publishers` — games grouped by publisher with image status
- `python3 scripts/image_manager.py publisher "Name"` — detail view for one publisher
- `python3 scripts/image_manager.py missing` — list all games missing images
- `python3 scripts/image_manager.py check` — validate image files

**Session history:** Check `SESSION_NOTES.md` for past sessions and TODO items

## Key Information for Editing

### YAML Formatting
- Use **spaces** for indentation (2 spaces per level)
- Arrays use hyphens: `- item1` on separate lines
- Null values use `null` (not empty)
- Multi-line strings use `|` for block literals

### ID/Slug Naming Convention
- Lowercase, hyphen-separated
- Examples: `azul`, `ark-nova`, `pandemic-legacy-season-1`, `twilight-imperium-4`
- Use exact match between filename and `id` field

### Category Tags
Always use **exact** text from `schema.yaml`. Do not invent new tags. Common mechanics include:
- Worker Placement, Deck Building, Engine Building, Area Control, Tile Placement
- Cooperative, 1 vs Many, Teams, Drafting, Auctions/Bidding

### Personal Ratings
- `affinity` and `hotness` are intentionally left `null` until the owner rates them
- These should remain null during initial data entry

### Date Fields
Game year is the publication year of that specific edition, not the original design year. For example:
- `Brass: Lancashire (2007)` has `year: 2007`
- `Brass: Birmingham (2018)` has `year: 2018`

### Master List & Wikidata Scraping

`master_list.csv` is the **source of truth** for the game catalog. It contains all known board games and drives progress tracking. New games can be added to it from any source.

**Populating from Wikidata:**
```bash
pip install -r scripts/requirements.txt
python3 scripts/scrape_wikidata.py           # fetch next 10,000 games
python3 scripts/scrape_wikidata.py --status  # check progress without fetching
```

Queries Wikidata's free public SPARQL endpoint — no API key or registration needed.
Each run fetches 10,000 games. State is persisted in `wikidata_state.json`.
CSV columns: `bgg_id`, `name`, `year`, `type`.

**Adding games manually:** Append rows to `master_list.csv` with at minimum a `name`. Leave `bgg_id` empty if unknown.

## Architecture Notes

**Tooling:**
- `scripts/progress.py` — tracks game entries vs `master_list.csv`; uses `sources/lists/` for prioritization
- `scripts/image_manager.py` — image coverage tracking
- `scripts/scrape_wikidata.py` — populates `master_list.csv` from Wikidata SPARQL
- `scripts/game_pipeline.py` — research pipeline used by the `game-researcher` agent: fetches URLs, strips HTML to clean text, caches in `pipeline_cache.db`. Returns clean text per source; the calling agent handles all structured data extraction. Use `--log SLUG` to auto-append provenance entries to `sources/research-log.yaml`.
- `scripts/html_preprocessor.py` — HTML → clean text (Trafilatura + BS4 fallback), truncated to 3000 chars per source

No build process or linting.

**Git-Friendly:** YAML format with one game per file makes diffs, merges, and reviews straightforward.

**Expansion & Variant Tracking:** The `game_family` field allows grouping related games (different editions, expansions) without creating confusion. Use this when games share a name but are different editions.

## Blocked Sources

**Do NOT use boardgamegeek.com** for any research or data gathering. All game data should come from publisher sites, Wikipedia, retailers, review sites, and other public sources. The `/add-game` skill enforces this with `blocked_domains`.

## Source Provenance

All URLs consulted during game research are logged in `sources/research-log.yaml`. The `/add-game` skill appends entries automatically. This provides an audit trail of where game data originated.
