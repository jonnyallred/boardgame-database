# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Board Game Database** - a curated collection of board games with detailed metadata, ratings, and categorization. The project stores data as YAML files rather than using a traditional database, making it easy to version control and maintain.

**Key Stats:**
- `master_list.yaml`: 1,000 games from BoardGameGeek top rankings
- `games/`: Individual YAML files (currently 227 detailed entries)
- `schema.yaml`: Complete data structure and validation rules

## Data Structure

### Game Entry Format

Each game file (`games/{slug}.yaml`) contains:

**Identifiers & Metadata:**
- `id`: lowercase slug (e.g., `azul`)
- `name`: Full display name
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

### Master List

`master_list.yaml` contains 1,000 games with minimal data: `id`, `name`, `year`, and `bgg_rank`. This is used as a reference for which games exist in the collection.

### Schema

`schema.yaml` documents all valid values for ratings, categories, and templates. Refer to it when:
- Adding new category tags
- Understanding rating scales
- Creating new game entries

## Common Commands

### File Operations

**Add a new game:**
1. Create `games/{slug}.yaml` based on the template in schema.yaml
2. Use an existing game file as reference (e.g., `games/azul.yaml`)
3. Ensure the `id` field matches the filename slug

**Update game data:**
- Edit the YAML file directly
- Validate against schema.yaml if adding new categories

**Add images:**
- Place box art in `images/` folder
- Naming: `Game Name (Year).jpg`
- See `images/README.md` for official image sources and guidelines

### Validation

The project uses YAML structure only—no linting tools are configured. When editing:
- Maintain YAML syntax (proper indentation with spaces, not tabs)
- Keep field order consistent with the schema
- Ensure `categories[]` values exist in `schema.yaml`

### File Count & Status

**Tracking current work:**
- Check `SESSION_NOTES.md` for session history and TODO items
- 227 games have detailed entries; 773 remain from the master list

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
