# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Board Game Database** - a curated collection of board games with detailed metadata, ratings, and categorization. The project stores data as YAML files rather than using a traditional database, making it easy to version control and maintain.

**Key Stats:**
- `sources/lists/`: One YAML file per source (article, award list, etc.) — the "want list"
- `games/`: Individual YAML files with detailed research — the "done list"
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

**Player Information:**
- `possible_counts[]`: Player counts supported by box rules
- `true_counts[]`: Optimal/best player counts per community consensus

**Other:**
- `description`: Game summary and key mechanics
- `upgrades[]`: Optional custom components or accessories
- `plays_tracked`: Play history tracking (total_plays and configs)

### Source Lists

Game nominations live in `sources/lists/`, one YAML file per source. Each file has:

```yaml
source: "Human-readable source name"
url: "https://..."
fetched: 2026-02-16
games:
  - id: azul
    name: Azul
    year: 2017
```

The progress script unions all list files by `id`, deduplicates, and diffs against `games/` to show what's next. Games appearing in multiple sources are prioritized. See `sources/lists/README.md` for details.

### Schema

`schema.yaml` documents all valid values for ratings, categories, and templates. Refer to it when:
- Adding new category tags
- Understanding rating scales
- Creating new game entries

## Common Commands

### File Operations

**Add a new game:**
Use the `/add-game` skill to create new game entries. This skill handles web research, schema validation, and YAML creation automatically.

When adding multiple games at once, use the Task tool to launch parallel `general-purpose` subagents — one per game — all in a single message. Each subagent receives the full add-game instructions (from `SKILL.md`) and works independently. Do **not** use the Skill tool directly for batch additions; explicit Task subagents are faster and truly parallel. This is the preferred workflow for batch additions.

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

## Architecture Notes

**No External Tools:** This project has no build process, testing framework, or linting—it's a pure data collection. Validation is manual against the schema.

**Git-Friendly:** YAML format with one game per file makes diffs, merges, and reviews straightforward.

**Expansion & Variant Tracking:** The `game_family` field allows grouping related games (different editions, expansions) without creating confusion. Use this when games share a name but are different editions.

## Blocked Sources

**Do NOT use boardgamegeek.com** for any research or data gathering. All game data should come from publisher sites, Wikipedia, retailers, review sites, and other public sources. The `/add-game` skill enforces this with `blocked_domains`.

## Source Provenance

All URLs consulted during game research are logged in `sources/research-log.yaml`. The `/add-game` skill appends entries automatically. This provides an audit trail of where game data originated.
