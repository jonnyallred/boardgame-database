# Game Researcher Agent Memory

## Key Sources for Research
- Publisher sites (rprod.com for Repos Production, stonemaier-games.com, etc.) are the best primary source
- Press pages (e.g., rprod.com/en/press/{game}) often have publication date, designer, artist confirmed
- Asmodee store (store.asmodee.com) is useful for Repos Production / Asmodee-distributed titles
- Meeple Mountain and Geeks Under Grace are reliable review sites with detailed mechanics

## Repos Production Games
- Publisher slug: "Repos Production" (not a schema tag — no publisher tag exists for them)
- Asmodee distributes Repos Production games in North America
- Press pages at rprod.com/en/press/{game-slug} confirm publication month/year

## Schema Notes
- No publisher tag exists for Repos Production or Asmodee in schema.yaml
- "Take That" is a valid mechanic tag in schema.yaml
- "Filler" is a valid style tag (use for ~15 min games)
- For pure 2-player duels: feel=4 (Fierce) is appropriate
- "Maritime" is a valid theme tag (use for sea/ocean/pirate themes)
- "Phil Walker-Harding" is a valid designer tag in schema.yaml

## Slug Conventions
- Simple game names: direct lowercase hyphenated slug (e.g., "Toy Battle" -> toy-battle)
- Special characters like & become "and": "Sea Salt & Paper" -> sea-salt-and-paper
- "Silver & Gold" -> silver-and-gold
- Second editions: append "-second-edition" to base slug
- Game families: use game_family field to link editions (e.g., saint-petersburg)

## WizKids Games
- WizKids is not in schema.yaml publishers list — no publisher tag to apply
- Noble Knight Games (nobleknight.com) is a good retailer for confirming publication year
- ICv2 (icv2.com) is useful for tracking expansion announcements and release dates

## Release Year Ambiguity
- Some games straddle late 2024/early 2025 release windows; check multiple sources
- Noble Knight and retailer listings often match the original intended year (e.g., 2024)
- Memory Alpha (memory-alpha.fandom.com) is a reliable fan wiki for Star Trek games
- If user specifies a year in their request, lean toward that year if confirmed by any source

## Research Log
- The pipeline's `--log` flag handles all research-log.yaml appending automatically.
- Do NOT manually read or append to sources/research-log.yaml — it is handled by the pipeline.

## Randolph (French Publisher)
- Not in schema.yaml publishers list — no publisher tag to apply

## Calliope Games
- Not in schema.yaml publishers list — no publisher tag for them
- Rob Daviau is a valid designer tag in schema.yaml

## Arcane Wonders
- Not in schema.yaml publishers list — no publisher tag for them
- CMON acquired rights to Sheriff of Nottingham but Arcane Wonders published original English edition

## Space Cowboys
- Not in schema.yaml publishers list — no publisher tag for them
- Asmodee label; publishes Sherlock Holmes: Consulting Detective since 2016

## Pipeline Notes
- Some URLs return empty sources (JS-heavy SPAs, Shopify stores, etc.)
- Always have 3 candidate URLs ready; only the ones that parse successfully appear in output
- rprod.com/en/games/{slug} often fails (JS-heavy); rprod.com/en/press/{slug} is better
- Wikipedia is the most reliable single source — always include it first

## Handling Multiple Editions
- When user requests both original and second edition, create two separate files
- Link them via game_family field (same value for both)
- Original: edition: first; Second: edition: second
- expansions[] on original points to second-edition slug (if it's more than a reprint)
- Only use expansions[] for genuine expansions/editions, not if the 2nd ed fully replaces 1st

## Sherlock Holmes: Consulting Detective
- Original published 1981 by Sleuth Productions; won Spiel des Jahres 1985
- Current publisher: Space Cowboys (Asmodee); multiple standalone volumes exist
- Each volume is a separate game, not an expansion — they share game_family

## Cooperative/Deduction Genre Notes
- Scotland Yard (1983): first SdJ with hidden movement; 6 designers including first female SdJ winner
- Sherlock Holmes CD: no board/dice/tokens — purely narrative; 1-8 players works well solo

## Sidereal Confluence
- Designer name is "TauCeti Deichmann" (stylized, single string)
- WizKids published original 2017; Renegade Game Studios published Remastered Edition
- For the 2017 original: publisher is WizKids

## Evokes Field — Common Mistake
- "Puzzle Solving" is a CATEGORY tag, NOT a valid evoke value — never put it in evokes[]
- Valid evokes are: Agency, Clever, Complete, Connection, Creative, Discovery, Dread, Humor, Lucky, Masterful, Mystery, Persuasion, Powerful, Progress, Rivalry, Tension, Unique, Wonder

## Notable Publishers NOT in Schema
- Runaway Parade Games (Smug Owls publisher) — no publisher tag
- Big Potato Games (Snakesss! publisher) — no publisher tag
- Schmidt Spiele (Taverns of Tiefenthal publisher) — no publisher tag
- Gamewright (Sushi Go! publisher) — no publisher tag
- Alderac Entertainment Group (AEG) — no publisher tag in schema (they publish Space Base, Tiny Towns)
- Mayfair Games (original Catan English publisher) — no publisher tag

## Catan Naming
- Original 1995 name: "The Settlers of Catan"; slug: settlers-of-catan
- Alternate names include "Catan" (current name) and "Die Siedler von Catan" (German original)
- Use game_family: catan to link Catan base game and expansions

## Summoner Wars Second Edition
- slug: summoner-wars-second-edition; game_family: summoner-wars; edition: second
- Designer: Colby Dauch; Publisher: Plaid Hat Games; year: 2021
- Plaid Hat Games IS a valid schema publisher tag
