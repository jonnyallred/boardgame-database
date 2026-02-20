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
