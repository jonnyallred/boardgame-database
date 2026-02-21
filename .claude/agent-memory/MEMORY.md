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
