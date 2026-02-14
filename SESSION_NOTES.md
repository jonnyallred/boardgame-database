# Board Game Database - Session Notes

**Date:** January 24, 2026
**Session:** Initial Setup & First 25 Games

---

## What Was Accomplished

### 1. Project Structure Created
- `/games/` - Individual YAML files for each game
- `/images/` - Folder for box art (with README guide)
- `schema.yaml` - Complete schema documentation
- `master_list.yaml` - 1,000 games from BGG rankings

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
- 1,000 games from BGG top rankings
- Includes name, year, and BGG rank
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
- Games now cover a wide range of BGG top-ranked titles including editions, expansions, and variants
- Added `/add-game` skill for automated game entry via Claude Code subagent
- Refined skill to use Sonnet model for cost-efficient research

### Add-Game Skill (`/.claude/skills/add-game/`)
- Forked subagent that researches and creates game YAML files
- Uses WebSearch + WebFetch for BGG/publisher data
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

## TODO - Future Sessions

### High Priority
- [ ] **Add more detailed game entries** - 773 games remaining from master list
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
- BoardGameGeek (game lists only, per user request)
- Publisher websites (Roxley, Stonemaier, Cephalofair, FFG, etc.)
- Wikipedia (for verification)
- Official product pages

### Notes for Next Session
- Data was gathered from official publisher sources where possible
- `affinity` and `hotness` fields are intentionally blank for personal ratings
- Game family relationships established (brass, dominion, gloomhaven, etc.)
- Designer tags only applied where accurate (per user request)

---

## File Counts
- `master_list.yaml`: 1,000 games (all with `id` slugs)
- `games/*.yaml`: 227 detailed entries
- Total categories defined: 70+
- Designer tags available: 28
- Publisher tags available: 22
