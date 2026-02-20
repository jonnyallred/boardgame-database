# Board Game Database - Session Notes

**Date:** January 24, 2026
**Session:** Initial Setup & First 25 Games

---

## What Was Accomplished

### 1. Project Structure Created
- `/games/` - Individual YAML files for each game
- `/images/` - Folder for box art (with README guide)
- `schema.yaml` - Complete schema documentation
- `master_list.yaml` - 1,000 games from online rankings

### 2. Schema Defined
Full rating system implemented:
- **Length** (0-4): Snack → Marathon
- **Rules Complexity** (0-4): Preschool → PhD
- **Strategic Depth** (0-4): Reflex → Master Plan
- **Feel** (0-4): Solitary → Fierce
- **Affinity** (0-4): Personal rating (left blank)
- **Hotness** (0-4): Personal rating (left blank)
- **Value** (0-4): Impulse → Heirloom

### 3. Categories Organized
70+ tags across:
- Mechanics (Worker Placement, Deck Building, etc.)
- Styles (Euro, Ameritrash, Party, etc.)
- Themes (Sci-Fi, Fantasy, Historical, etc.)
- Designers (Knizia, Rosenberg, Stegmaier, etc.)
- Publishers (Stonemaier, FFG, Leder Games, etc.)

### 4. Master List Compiled
- 1,000 games from online rankings
- Includes name, year, and rank
- Covers base games, expansions, and editions

### 5. Detailed Game Files Created (25 games)
| Game | Year | Designer(s) |
|------|------|-------------|
| Brass: Birmingham | 2018 | Wallace, Brown, Tolman |
| Ark Nova | 2021 | Wigge |
| Pandemic Legacy: Season 1 | 2015 | Leacock, Daviau |
| Gloomhaven | 2017 | Childres |
| Dune: Imperium | 2020 | Dennen |
| Twilight Imperium 4 | 2017 | Petersen, Konieczka, Beltrami |
| Terraforming Mars | 2016 | Fryxelius |
| Spirit Island | 2017 | Reuss |
| Scythe | 2016 | Stegmaier |
| Root | 2018 | Wehrle |
| Wingspan | 2019 | Hargrave |
| Concordia | 2013 | Gerdts |
| Dominion | 2008 | Vaccarino |
| Everdell | 2018 | Wilson |
| 7 Wonders Duel | 2015 | Bauza, Cathala |
| War of the Ring 2E | 2011 | Di Meglio, Maggi, Nepitello |
| Star Wars: Rebellion | 2016 | Konieczka |
| Gaia Project | 2017 | Drogemuller, Ostertag |
| Twilight Struggle | 2005 | Gupta, Matthews |
| The Castles of Burgundy | 2011 | Feld |
| Great Western Trail | 2016 | Pfister |
| Nemesis | 2018 | Kwapinski |
| A Feast for Odin | 2016 | Rosenberg |
| Agricola | 2007 | Rosenberg |
| Azul | 2017 | Kiesling |

---

## Session 2 - Bulk Game Entry

**Date:** January/February 2026

### What Was Accomplished

- Added 202 new detailed game entries (25 → 227 total)
- Games now cover a wide range of top-ranked titles including editions, expansions, and variants
- Added `/add-game` skill for automated game entry via Claude Code subagent
- Refined skill to use Sonnet model for cost-efficient research

### Add-Game Skill (`/.claude/skills/add-game/`)
- Forked subagent that researches and creates game YAML files
- Uses WebSearch + WebFetch for publisher data
- Pinned to Sonnet model (structured data collection doesn't need Opus)

---

## Session 3 - Progress Tracking System

**Date:** February 2026

### What Was Accomplished

- Added `id` slugs to all 1,000 entries in `master_list.yaml` (links entries to `games/` files)
- Created `scripts/progress.py` — shows completion stats and next games to work on
- Created `/progress` Claude Code skill as a quick shorthand
- Migration script: `scripts/generate_master_ids.py` (kept for reference)

---

## Session 4 - Bulk Game Entry (Ranks 188-327)

**Date:** February 14, 2026

### What Was Accomplished

- Added 100 new detailed game entries (227 → 327 total)
- Covers ranks 188-327 from the original master list
- Used parallel subagents for efficient batch creation
- Updated CLAUDE.md game count

### Notable Games Added
- Heavy Euros: Tiletum, Hallertau, Kanban: Driver's Edition, Bora Bora, Bitoku
- Classics: Glory to Rome, The Princes of Florence, 1830, Battle Line, Goa
- Party/Family: Monikers, Skull King, Kingdomino, Love Letter (2019)
- Civilization: Tapestry, Endless Winter: Paleoamericans
- Wargames: Dune: War for Arrakis, 1960: The Making of the President, Kemet: Blood and Sand
- Deck Builders: Hero Realms, Star Realms: Frontiers, Aeon's End: The New Age
- Worker Placement: Viticulture, Apiary, Unconscious Mind
- Other: Galaxy Trucker, Santorini, Turing Machine, Mind MGMT, Marvel United

---

## Session 5 - Source Restructuring & Master List Rebuild

**Date:** February 15, 2026

### What Was Accomplished

- **Restructured data sources** — removed all third-party ranking site dependencies
  - Stripped weight reference comments from 128 game YAML files
  - Rewrote `/add-game` skill to use publisher sites, Wikipedia, retailers, and review sites
  - Added subjective rules_complexity guidelines
- **Built new master list** from award winners and notable game lists
  - Compiled from: Spiel des Jahres, Kennerspiel des Jahres, As d'Or, International Gamers Award, Origins Awards, Dice Tower People's Choice, Wikipedia game lists, publisher catalogs
  - New format uses `source` field (provenance) instead of ranking
  - Alphabetical by ID instead of ranked
  - All 389 existing game files included
- **Created source provenance system**
  - `sources/research-log.yaml` — chronological log of all URLs consulted
  - `/add-game` skill now appends to this log automatically
- **Archived original data**
  - `archive/games-v1/` — snapshot of all game files pre-change
  - `archive/master-list-v1.yaml` — original master list
- **Updated tooling**
  - `scripts/progress.py` — shows source instead of ranking
  - `/progress` skill — updated output description
- **Updated documentation**
  - CLAUDE.md — added Blocked Sources and Source Provenance sections
  - SESSION_NOTES.md — this entry

---

## TODO - Future Sessions

### High Priority
- [x] **Build source lists** — Add curated game lists to `sources/lists/`
  - [x] Spiel des Jahres Winners (1979-present) — 47 games
  - [x] Kennerspiel des Jahres Winners (2011-present) — 15 games
  - [x] Golden Geek Awards Winners — 15 games (incomplete, needs Medium/Light categories)
  - [x] Deutscher Spiele Preis Winners — 11 games (incomplete, many missing years)
  - [ ] Dicebreaker Top 100
  - [ ] Shut Up & Sit Down Recommendations
  - [ ] No Pun Included Best Games
  - [ ] BoardGameQuest Top Games
  - [ ] Reiner Knizia collection
  - [ ] Uwe Rosenberg collection
  - [ ] Stonemaier Games collection
  - [ ] Gateway Games Classics
- [ ] **Complete Golden Geek and Deutscher Spiele Preis** — Fill in missing years/categories
- [ ] **Add game entries for award winners** — 20/75 complete (55 remaining)
- [ ] **Obtain box art images** - See `/images/README.md` for sources
  - Contact publishers for press kits
  - Download from official websites
  - Naming: `Game Name (Year).jpg`

### Medium Priority
- [ ] **Add expansion files** - Create separate YAML for major expansions
  - Dominion expansions (Intrigue, Seaside, Prosperity, etc.)
  - Terraforming Mars expansions
  - Spirit Island expansions
  - Gloomhaven: Forgotten Circles, Jaws of the Lion
- [ ] **Add edition variants** - Track different editions
  - Dominion Second Edition
  - Great Western Trail Second Edition
  - Agricola Revised Edition
- [ ] **Verify/update data** - Cross-reference with publisher sites
  - Some playtimes may need adjustment
  - Verify player counts against official sources

### Lower Priority
- [ ] **Add upgrade entries** - Populate upgrade sections
  - Metal coins, playmats, inserts, etc.
- [ ] **Create query tools** - Scripts to filter/search the database
- [ ] **Add more designers to tags** - Expand designer category list
- [ ] **Add plays tracking** - Structure for logging game sessions

### Data Sources Used
- Publisher websites (Roxley, Stonemaier, Cephalofair, FFG, etc.)
- Wikipedia (award lists, game articles)
- Retailer pages (Amazon, Miniature Market, etc.)
- Review sites (Dice Tower, Shut Up & Sit Down, etc.)
- Official product pages

### Notes for Next Session
- Data is gathered from official publisher sources where possible
- See CLAUDE.md "Blocked Sources" section for restricted sites
- All research URLs are logged in `sources/research-log.yaml`
- `affinity` and `hotness` fields are intentionally blank for personal ratings
- Game family relationships established (brass, dominion, gloomhaven, etc.)
- Designer tags only applied where accurate (per user request)

---

## Session 6 - Fresh Start: Source Lists & Initial Game Entries

**Date:** February 16, 2026

### What Was Accomplished

- **Created 4 award source lists** in `sources/lists/`:
  - Spiel des Jahres Winners (47 games, 1979-2025)
  - Kennerspiel des Jahres Winners (15 games, 2011-2025)
  - Golden Geek Awards Winners (15 games, 2010-2024, incomplete)
  - Deutscher Spiele Preis Winners (11 games, 1990-2025, incomplete)
  - **Total: 75 unique games across all lists**

- **Added 20 detailed game entries** (0 → 20 total):
  - Used parallel `/add-game` skill subagents for efficient batch creation
  - Prioritized games appearing in multiple awards
  - All entries fully researched from publisher sites, Wikipedia, retailers, and review sites
  - All research URLs logged to `sources/research-log.yaml`

- **Implemented `alternate_names` field** — Architectural change to handle multilingual games:
  - Added `alternate_names: []` to schema template for tracking translations and regional names
  - Updated `scripts/progress.py` to check both primary and alternate names when detecting duplicates
  - Updated `/add-game` skill to research and record alternate names
  - Updated documentation in CLAUDE.md and schema.yaml
  - Example: "Adel Verpflichtet" also known as "Hoity Toity", "Fair Means or Foul", "By Hook or By Crook"
  - Prevents duplicate entries when source lists use different names for the same game
  - Fixed 5 game file IDs to match source list conventions (removed unnecessary year suffixes)

### Games Added (20)
| Game | Year | Designers | Awards |
|------|------|-----------|--------|
| Wingspan | 2019 | Elizabeth Hargrave | 3 awards 🏆🏆🏆 |
| Adel Verpflichtet | 1990 | Klaus Teuber | 2 awards |
| Ark Nova | 2021 | Mathias Wigge | 2 awards |
| El Grande | 1995 | Wolfgang Kramer, Richard Ulrich | 2 awards |
| SETI | 2024 | Tomáš Holek | 2 awards |
| 7 Wonders | 2010 | Antoine Bauza | 1 award |
| Alhambra | 2003 | Dirk Henn | 1 award |
| Auf Achse | 1987 | Wolfgang Kramer | 1 award |
| Azul | 2017 | Michael Kiesling | 1 award |
| Barbarossa | 1988 | Klaus Teuber | 1 award |
| Bomb Busters | 2025 | Hisashi Hayashi | 1 award |
| Brass: Birmingham | 2018 | Wallace, Brown, Tolman | 1 award |
| Broom Service | 2015 | Pelikan, Pfister | 1 award |
| Café International | 1989 | Rudi Hoffmann | 1 award |
| Call My Bluff | 1993 | Richard Borg | 1 award |
| Camel Up | 2014 | Steffen Bogen | 1 award |
| Carcassonne | 2000 | Klaus-Jürgen Wrede | 1 award |
| Challengers! | 2022 | Krenner, Slawitscheck | 1 award |
| Codenames | 2016 | Vlaada Chvátil | 1 award |
| Colt Express | 2014 | Christophe Raimbault | 1 award |

### Progress
- **Completion: 20/75 games (26.7%)**
- **Remaining: 55 games** from award lists
- **No orphan games** after ID standardization

### Architecture Notes
- **alternate_names field** added to schema for handling games with multiple titles (translations, regional names)
- Duplicate detection now checks both primary name and alternate names across all existing games
- This prevents creating duplicate entries when source lists use different names for the same game

### Next Steps
- [ ] Complete Golden Geek and Deutscher Spiele Preis lists (fill missing years)
- [ ] Add remaining 8 source lists (review sites, designers, publishers)
- [ ] Continue adding game entries for remaining 55 award winners

---

## Session 7 - Wikidata Scraper & Additional Game Entries

**Date:** February 19, 2026

### What Was Accomplished

- **Built Wikidata SPARQL scraper** (`scripts/scrape_wikidata.py`)
  - Queries Wikidata's free public endpoint — no API key required
  - Fetches 10,000 board games per run, resumable via `wikidata_state.json`
  - Outputs to `master_list.csv` (columns: bgg_id, name, year, type)
  - Also retained `scripts/scrape_bgg.py` (BGG XML API, now requires bearer token)
  - BGG API now requires registration — Wikidata selected as alternative
- **Added ~99 new game YAML entries** (covering BGG ranks ~51–118 range)
  - Note: some of these overlap with existing entries on remote; remote versions preferred

### Notes
- `master_list.csv` is a bulk discovery catalog, separate from the `sources/lists/` workflow
- The Wikidata scraper does not replace the award-source-list approach; it supplements it
- Some game files added locally had parallel versions on remote; remote versions (more refined) were kept

---

## File Counts

Run `python3 scripts/progress.py 0` for live stats. Snapshot as of February 2026:

- `sources/lists/*.yaml`: 20 source list files (348 unique games)
- `games/*.yaml`: 168 detailed entries (140 matched to source lists + 47 orphans)
- `master_list.csv`: bulk Wikidata catalog (header only — run scraper to populate)
- Total categories defined: 151
- Designer tags available: 28
- Publisher tags available: 22
