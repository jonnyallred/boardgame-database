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
- [ ] **Add more detailed game entries** — many games remaining from master list
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

## File Counts
- `master_list.yaml`: Curated list from award winners and notable game lists
- `games/*.yaml`: 389 detailed entries
- Total categories defined: 70+
- Designer tags available: 28
- Publisher tags available: 22
