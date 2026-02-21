# Game Researcher Agent Memory

## Key Sources for Board Game Research
- Publisher websites are usually the best source for exact year, player count, playtime, and age
- Tabletop Bellhop (tabletopbellhop.com) gives reliable designer credits and mechanic breakdowns
- Meeple Mountain (meeplemountain.com) provides solid overview and publisher confirmation
- Menomonieminute.com has profiles on indie designers (e.g. Dave Beck of Paverson Games)

## Slug Formatting
- Lowercase, hyphen-separated: `distilled`, `ark-nova`, `pandemic-legacy-season-1`
- No special characters or punctuation in slugs

## Paverson Games
- Publisher of Distilled (2023), indie studio in Wisconsin
- Designer: Dave Beck (UW-Stout professor)
- Artist: Erik Evensen
- NOT in schema.yaml publishers list

## Research Log Caution
- The research-log.yaml file may be modified by other parallel agents between reads and writes
- Always re-read the file (or at least the tail) immediately before editing to get the current last entry
- Use the exact last entry text as the old_string anchor for Edit to avoid conflicts

## Common Mechanic Mappings
- "Push-your-luck" or "mitigate-your-luck" → `Press Your Luck` (schema tag)
- "Simultaneous action selection" → `Simultaneous Action` (schema tag)
- "Card drafting from market" → `Hand Management` + `Drafting` (check context)
- "Tableau expansion" → `Tableau Building` (schema tag)
- "Engine building" → `Engine Building` (schema tag)

## Food Theme Games
- Distilled (2023) — spirits/distilling theme → uses `Food Theme` category tag

## Invalid Category Tags (Common Mistakes)
- "Agriculture" is NOT a valid tag — use `Nature` for farming/animal themes
- "Animals" is NOT a valid tag — use `Nature` for animal-themed games
- Always verify every tag against Valid Categories before writing the file

## CRITICAL: Valid Tags Confirmed in Schema
The system prompt includes the complete valid tags list. Key ones that feel like they should exist but DO:
- `Agriculture`, `Animals` are NOT valid — use `Nature`
- `Pirates` IS valid (maritime pirate theme)
- `Dudes on a Map` IS valid (area-control wargame style)
- `Days of Wonder` IS a valid publisher tag
- `Fantasy Flight Games` IS a valid publisher tag
- `Portal Games` IS a valid publisher tag
- `Plaid Hat Games` IS a valid publisher tag
- `Capstone Games` IS a valid publisher tag

## Game Family Slugs for Common Series
- COIN Series (GMT): game_family: coin-series
- Axis & Allies variants: game_family: axis-and-allies
- BattleLore editions: game_family: battlelore
- Arkham Horror editions: game_family: arkham-horror
- Antike games: game_family: antike
- 51st State editions: game_family: 51st-state
- Bang! games: game_family: bang

## Publisher Naming
- Lookout Spiele (German name) = Lookout Games (English) — use "Lookout Games" in publisher field

## Workflow: File Already Exists
- Always check if games/{slug}.yaml exists before writing (use ls or Glob)
- If file exists and is mostly complete, just fix invalid tags rather than rewriting
- plays_tracked field: leave as-is in existing files; do NOT add it to new entries

## Agricola Game Family
- game_family: "agricola" links: agricola.yaml, agricola-revised-edition.yaml, agricola-all-creatures-big-and-small.yaml
- Agricola: All Creatures Big and Small is a standalone 2-player spinoff (not expansion), year 2012, Lookout Games

## German-Origin Euro Games
- Hans im Glück is original German publisher for many Euro games (Carcassonne, Marco Polo, etc.)
- Include both original German publisher + English publisher in `publisher` field
- Hans im Glück is NOT in schema categories — don't add as a tag
- German alternate titles go in `alternate_names[]`, not the slug (use English title for slug)

## Simone Luciani + Daniele Tascini
- Frequent co-designers (Marco Polo series, Grand Austria Hotel, etc.)
- Both have valid designer category tags in schema.yaml

## Party Game Patterns
- Party games: rules_complexity 0-1, strategic_depth 0-1, length 0-1
- Bluffing/social games evoke: Humor, Tension, Rivalry, Lucky, Persuasion
- true_counts for party games often skew toward higher player counts (more = merrier)

## Repos Production
- French/Belgian publisher (Brussels), NOT in schema.yaml categories list
- Published: Ca$h 'n Guns, Just One, So Clover!, 7 Wonders, Concept
- Slug for Ca$h 'n Guns: `cash-n-guns` (special chars stripped)

## Invalid Category Tags (additional)
- "Adventure" is NOT valid — use "Ameritrash" or "Fantasy" for adventure-style games
- "Star Wars" is NOT a valid theme tag — use "Sci-Fi" instead
- "Animals" is NOT valid — confirmed again

## Publisher Tags (valid in categories)
- Eagle-Gryphon Games: valid tag
- Chip Theory Games: valid tag
- Days of Wonder: valid tag
- Osprey Games: valid tag
- Czech Games Edition: valid tag
- Orange Nebula: NOT in schema — omit from categories
- Le Scorpion Masqué: NOT in schema — omit from categories (also spelled "Scorpion Masque")

## Non-English Title Slugs
- Use original language for slug if that is the primary title: "um-reifenbreite" (not English translation)
- Alternate/English names go in alternate_names[]

## Efficient Batch Research Workflow (20 games)
- Run 8-10 parallel WebSearch calls (2 games per call) to gather all data first
- Then create all YAML files in parallel Write calls
- Skip pipeline when WebSearch gives sufficient detail
- This approach completes 20 games in ~15 total tool calls

## Pipeline Limitation
- Pipeline often returns raw JavaScript from Wikipedia - the HTML preprocessor may fail on JS-heavy pages
- Better to use WebSearch directly for data and write YAML from gathered knowledge

## Confirmed Invalid Category Tags
- "Adventure" is NOT valid
- "Animals" is NOT valid — use `Nature`
- "Agriculture" is NOT valid — use `Nature` or `Agriculture` (wait, Agriculture IS in the valid list)
- "Educational" is NOT valid
- "Competition" is NOT an evoke — avoid it

## Agriculture Tag Correction
- `Agriculture` IS a valid theme tag in the schema — confirmed in agent instructions

## Slug Edge Cases
- Ampersand in title: "Heaven & Ale" → `heaven-and-ale`; "Donjons & Dominos" → `donjons-et-dominos`
- French game title with ampersand can use "et" (French "and")
- Accented chars stripped: "Drüber" → "druber"
- Parenthetical editions: "Fury of Dracula (Third Edition)" → `fury-of-dracula-third-edition`
- "Hey, That's My Fish!" → `hey-thats-my-fish` (punctuation stripped)

## Obscure/Problematic Games
- Dune Express (2009): print-and-play game, not commercial release — write minimal entry
- Doodletown (2022): very obscure, limited info available — write minimal entry
- Clash Royale: The Card Game: mobile game; physical version exists published by Ravensburger

## Good Non-BGG Sources
- Meeple Mountain: meeplemountain.com
- Board Game Quest: boardgamequest.com
- Opinionated Gamers: opinionatedgamers.com
- Board Game Bliss: boardgamebliss.com
- Dice Tower: dicetower.com
- Tric Trac (French): us.trictrac.net
- Board Game Guys: boardgameguys.com
- Tabletop Bellhop: tabletopbellhop.com
