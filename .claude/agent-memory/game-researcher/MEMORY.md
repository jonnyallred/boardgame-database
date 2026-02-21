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

## Slug Conventions
- Simple game names: direct lowercase hyphenated slug (e.g., "Toy Battle" -> toy-battle)

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
- Randolph publishes games in French first; look for French alternate names
- Distributed by Hachette Boardgames in North America
- philibertnet.com (French retailer) is useful for confirming original French titles

## Schema Categories
- Press Your Luck (not "Push Your Luck") — exact tag in schema
- Bag Building — valid mechanic tag
- Nature, Animals — valid theme tags
- Family, Filler, Gateway — valid style tags

## Rating Calibration Examples
- Toy Battle (2025): length=0, complexity=1, depth=2, feel=4, value=1
  (15 min snack, elementary rules, tactical area control, fierce 2-player duel, ~$33 filler)
- Star Trek: Captain's Chair (2024): length=2, complexity=3, depth=3, feel=4, value=2
  (60-120 min, college-level rules with many keywords, strategic deckbuilder, $59.99 MSRP)
- Seaside (2024): length=0, complexity=1, depth=1, feel=3, value=2
  (20 min snack, elementary rules, basic set-collection, polite competitive, $32 fair deal)
- Nucleum (2023): length=2, complexity=3, depth=4, feel=3, value=3
  (60-150 min heavy euro, college-level interconnected systems, master-plan strategic depth, polite competitive, $70 MSRP splurge)

## Board&Dice Publisher Notes
- Board&Dice is NOT in schema.yaml publishers list — no publisher tag applies
- Their games often have strong Simone Luciani / Dávid Turczi designer credits
- Simone Luciani HAS a designer tag in schema.yaml — apply it when relevant
- gamenerdz.com is reliable for Board&Dice artist credits (Andreas Resch, etc.)

## Adam's Apple Games
- Adam's Apple Games is NOT in schema.yaml publishers list — no publisher tag applies
- gamenerdz.com and meeplemountain.com/boardgame/{slug} are reliable for full credits
- Artist "Yoma" credited for Planet Unknown
- meeplemountain.com/boardgame/{slug} lists full mechanics and all publishers (global co-publishers)

## Simultaneous Action Games
- When a game uses simultaneous play as its CORE differentiator, apply "Simultaneous Action" tag
- Planet Unknown (2022): length=2, complexity=2, depth=3, feel=3, value=3
  (60-80 min, junior-high-level rules, strategic depth with asymmetric tech trees, polite competitive, $79 splurge)

## Osprey Games Notes
- Osprey Games IS in schema.yaml publishers list — apply "Osprey Games" tag
- ospreypublishing.com has publisher product pages AND design diary blog posts
- ospreypublishing.com/us/osprey-blog/ has compatibility articles and designer diaries
- Imperium series (Classics, Legends, Horizons) uses game_family: imperium
- Imperium games are standalones that are compatible with each other (use compatible_with field)

## Imperium Series (Osprey Games)
- Designers: Nigel Buckle, Dávid Turczi; Artist: Mihajlo Dimitrievski
- Imperium: Horizons (2024): standalone with 14 civilizations, trade module innovation
- Compatible with Imperium: Classics and Imperium: Legends (not yet in DB as of 2026-02-19)
- Best at 2 players per community consensus; supports 1-4

## Rating Calibration Examples (continued)
- Imperium: Horizons (2024): length=2, complexity=3, depth=3, feel=3, value=3
  (40 min/player up to 180 min, college-level asymmetric deck builder, strategic long-term planning, polite trade routes, $58-80 splurge)
- boop. (2022): length=1, complexity=1, depth=2, feel=3, value=2
  (20-30 min appetizer, elementary rules, tactical pattern building, polite competitive, $35 fair deal)

## Slug Punctuation
- Strip ALL punctuation from slugs: "boop." -> `boop`
- Periods, colons, exclamation marks are all dropped

## Smirk & Dagger / Smirk & Laughter Games
- Smirk & Laughter is an imprint of Smirk & Dagger Games
- Neither appears in schema.yaml publishers list — no publisher category tag applies

## Research Log - Parallel Agent Conflicts
- Use `cat >>` bash append to avoid Edit tool conflicts when multiple agents are active
- `tail -5` first to verify end of file, then append

## CMYK Games Notes
- CMYK is NOT in schema.yaml publishers list — no publisher tag applies
- CMYK publishes party/social games (Wavelength, Spots, Lacuna, Hot Streak, Wilmot's Warehouse)
- cmyk.games/products/{slug} is the primary source for designer credits, player count, age
- Reviews published May 2025 confirm Hot Streak (2025) release year despite mid-March 2026 reprint shipping

## Rating Calibration Examples (continued)
- Hot Streak (2025): length=0, complexity=1, depth=1, feel=2, value=2
  (20 min snack, elementary betting/racing rules, basic decisions before race runs itself, party vibe, $44.99 fair deal with miniatures)

## Office Dog Games Notes
- Office Dog Games is Asmodee North America's in-house development studio
- NOT in schema.yaml publishers list — no publisher tag applies
- officedoggames.com is the primary source for their titles
- meeplemountain.com and opinionatedgamers.com are reliable for mechanics details
- legendofthefiverings.com covers their L5R-licensed games

## Kinson Key Games
- Small indie publisher from Tennessee; not in schema.yaml publishers list — no publisher tag
- Galactic Cruise (2025) is their flagship title; distributed by Allplay/Asmodee North America
- Board Game Arena (en.boardgamearena.com/gamepanel?game=X) is reliable for designers, artist, year
- coopboardgames.com includes competitive game reviews with useful complexity ratings

## Thames & Kosmos / KOSMOS Games
- Use "Thames & Kosmos" as publisher name for English-edition KOSMOS games
- store.thamesandkosmos.com is the authoritative source for player count, playtime, age, and year
- KOSMOS is NOT in schema.yaml publishers list — no publisher tag applies

## Cooperative Poker / Deduction Card Games
- Use Hand Management (not Trick-taking) for cooperative poker mechanic
- Bluffing + Simultaneous Action are appropriate companion tags
- The Gang (2024): length=0, complexity=1, depth=1, feel=1, value=1
  (20 min snack, elementary rules, basic cooperative deduction, $15 MSRP bargain)
- Artist credits: some games credit a design studio rather than individual (e.g., Fiore GmbH)

## American Tabletop Awards
- americantabletopawards.com confirms award winners with publisher details
- Useful for establishing publication year and confirming publisher names

## Academy Games / Birth of America Series
- Academy Games is NOT in schema.yaml publishers list — no publisher tag applies
- Birth of America series: 1754: Conquest, 1775: Rebellion, 1812: The Invasion of Canada
- Use game_family: birth-of-america when adding any title in this series
- All games share mechanics: Area Control, Dice Rolling, Hand Management, Teams, Wargame, Dudes on a Map
- Armchair General (armchairgeneral.com) has TLS cert issues — use search result summaries only

## Artist Credits - Unknown
- When artist cannot be confirmed from any source, use `artist: []` (empty list), not null
- Historical wargames often use period artwork without credited illustrators

## Far Off Games Notes
- Far Off Games is NOT in schema.yaml publishers list — no publisher tag applies
- faroffgames.com is the primary source; product pages show pricing and component count
- Arydia uses "green legacy" branding — resettable campaign, no permanent destruction
- Mr. Cuddington (Lina Cossette + David Forest) is a frequent board game art studio
- boardgameguys.com is a useful source for artist credits on Kickstarter games

## Rating Calibration Examples (continued)
- 1775: Rebellion (2013): length=2, complexity=2, depth=2, feel=4, value=2
  (60-120 min medium wargame, junior-high-level rules with 6 pages, area control tactics, fierce competitive team play, fair deal components)
- Arydia: The Paths We Dare Tread (2025): length=3, complexity=3, depth=3, feel=1, value=4
  (60-120 min sessions, 40+ hr campaign; college-level interlocking systems; strategy-level open-world planning; pure co-op; $240 heirloom all-in with 60+ pre-painted minis)
- Burning Banners: Rage of the Witch Queen (2024): length=3, complexity=3, depth=3, feel=4, value=3
  (30 min-4 hr scenario-based hex wargame; college-level two-tier rules; strategic faction play; fierce kingdom conquest; $95-119 splurge with 4 mounted maps)

## Compass Games Notes
- Compass Games is NOT in schema.yaml publishers list — no publisher tag applies
- nobleknight.com is reliable for Compass Games titles (year, price, player count)
- playerelimination.com is a useful wargame-focused review site
- theboardgameschronicle.com is a reliable review source for wargames and heavy euros

## Chip Theory Games Notes
- Chip Theory Games IS in schema.yaml publishers list — apply "Chip Theory Games" tag
- chiptheorygames.com/products/{slug} is primary source for designer credits and pricing
- Known for premium neoprene/poker chip components; prices $100-$250+
- Multi-designer teams common (4-6 co-designers on Elder Scrolls)
- Gamefound (gamefound.com) is useful for their campaign update posts with mechanic details

## Licensed Video Game IP Slugs
- Drop "The" from start of slug only if it's a standalone article
- "The Elder Scrolls: Betrayal of the Second Era" → elder-scrolls-betrayal-of-the-second-era
  (kept "elder-scrolls" prefix, dropped leading "The", subtitle included in full)
- Colon+space in titles → hyphen in slug, drop colon

## Campaign Game Ratings
- Multi-session campaign cooperative games: length=4 (Marathon), feel=1 (Light/cooperative)
- Premium licensed games with $200+ price: value=4 (Heirloom)
- true_counts = all possible_counts for fully cooperative games (any count is "optimal")

## Rating Calibration Examples (continued)
- Elder Scrolls: Betrayal of the Second Era (2025): length=4, complexity=3, depth=3, feel=1, value=4
  (3-session ~2-3 hr/session cooperative campaign, complex skill/dice systems, $224+ premium production)
- The Lord of the Rings: Fate of the Fellowship (2025): length=2, complexity=2, depth=2, feel=0, value=3
  (60-120 min medium cooperative, moderate Pandemic-system rules, tactical coordination, pure co-op, Z-Man premium box)

## Z-Man Games Notes
- Z-Man Games IS in schema.yaml publishers list — apply "Z-Man Games" tag in categories
- Matt Leacock IS in schema.yaml designers list — apply "Matt Leacock" tag in categories
- Pandemic System games: feel=0 (Cooperative/Solitary), true_counts covers all player counts (any is "optimal" for co-op)

## Lord of the Rings Theme
- "Lord of the Rings" is a valid theme tag in schema.yaml categories
- "Fantasy" is also appropriate as a companion theme tag

## Bombyx (Studio Bombyx) Publisher Notes
- Bombyx is NOT in schema.yaml publishers list — no publisher tag applies
- studiobombyx.com is the official publisher site; product pages often return CSS noise from pipeline
- Thames & Kosmos distributes Bombyx games in North America; list "Bombyx" as primary publisher name
- store.thamesandkosmos.com pages often return mostly CSS/font boilerplate — low pipeline value

## Dexterity Games Rating Pattern
- length=0 (Snack) for games under 30 min
- rules_complexity=1 (Simple) for games with a single die-roll placement rule
- strategic_depth=1 (Light) for pure dexterity with minimal planning
- true_counts skews toward larger groups (more fun with more people for social dexterity games)
- Catch the Moon (2017): length=0, complexity=1, depth=1, feel=2, value=2
  (15-30 min, elementary ladder-placement rules, 1-6 players best with groups, $30-40 fair deal)

## Ystari Games Notes
- Ystari Games is NOT in schema.yaml publishers list — no publisher category tag applies
- Rio Grande Games IS in schema.yaml publishers list — apply "Rio Grande Games" tag when they are the English publisher
- gambiter.com is a clean secondary source for box specs (player count, age, playtime, mechanics)
- bombardgames.com returns 403 errors — exclude from pipeline URL lists

## AEG (Alderac Entertainment Group) Publisher Notes
- AEG is NOT in schema.yaml publishers list — no publisher tag applies
- alderac.com/{game-slug} is the official publisher product page
- AEG publishes accessible family/gateway games (Cubitos, Smash Up, Tiny Towns, etc.)

## Dice-Building Racing Game Pattern (Cubitos)
- Cubitos (2021): length=1, complexity=1, depth=2, feel=2, value=2
  (30-45 min short, elementary press-your-luck rules, moderate dice-pool engine decisions, moderate competitive racing, $48 fair deal)
- Designer: John D. Clair; Publisher: AEG
- Use tags: Dice Rolling, Bag Building, Press Your Luck, Racing, Engine Building, Variable Setup, Family, Gateway

## Classic Euro Worker Placement Ratings (2000s era)
- Caylus (2005): length=3, complexity=3, depth=4, feel=2, value=3
  (60-180 min long game; complex interlocking Provost/Bailiff systems; master-plan strategic depth; politely competitive but heavy analysis; premium out-of-print production)
- Near-absent randomness games: omit Dice Rolling tag; use Variable Setup only if board setup IS randomized
- "Cult Classic" style tag is appropriate for genre-defining games (Caylus defined worker placement)

## Obscure/Small Publisher Games (2000s era)
- Small publisher games (Mystics, etc.) often have very limited web presence — pipeline may yield mostly JS noise
- For obscure 2-player abstract games: eBay listings are useful for year and publisher confirmation
- IGA winners page (internationalgamersawards.net/winners/{year}-winners) often returns JS noise — search results are more useful
- Day & Night (2008): 2-player abstract strategy by van den Roovaart & Eekels, published by Mystics
  Won IGA 2009 (2-player category); asymmetric Lady Day vs Lady Night dueling for temple placement

## Restoration Games Notes
- Restoration Games IS in schema.yaml publishers list — apply "Restoration Games" tag in categories
- restorationgames.com/shop/{slug} is the primary source, but often returns CSS noise — rely on search summaries
- For revival editions: use the revival year in `year:`, set `edition:` to "YYYY Restoration Games"
- Use game_family when reviving a named series (e.g., game_family: crossbows-and-catapults)
- Crossbows & Catapults: Fortress War (2024): 2-player dexterity siege game, 20-40 min, ages 7+
  Designers: Stephen Baker (original), Noah Cohen, Rob Daviau, Justin D. Jacobson, Brian Neff
  Filed under slug: crossbows-and-catapults (drop "Fortress War" subtitle from slug)
  length=1, complexity=1, depth=1, feel=3, value=2

## Blue Orange Games Publisher Notes
- Blue Orange Games is NOT in schema.yaml publishers list — no publisher tag applies
- blueorangegames.com hosts PDF rulebooks for their games
- Detective Club (2018): Designer Oleksandr Nevskiy (also co-designed Mysterium)
- Social deduction party games: feel=3 (Competitive), length=1 (Short)
- Detective Club: length=1, complexity=1, depth=1, feel=3, value=2
  (30-45 min short party game, elementary rules, light deduction decisions, social competition, ~$35 fair deal)

## Lucky Duck Games Notes
- Lucky Duck Games is NOT in schema.yaml publishers list — no publisher tag applies
- luckyduckgames.com is the official site but is very JS-heavy (pipeline yields mostly JSON/script noise)
- boardgamewikia.com and coopboardgames.com are good alternatives for Lucky Duck games
- Chronicles of Crime (2018): app-integrated QR code mystery game, designer David Cicurel
- Won As d'Or at Festival International des Jeux de Cannes 2019

## App-Integrated Mystery/Investigation Games
- Valid tags: Cooperative, Deduction, Narrative Heavy, Mystery, Variable Setup, Family, Gateway
- Do NOT use "Storytelling" or "Time Track" — not in valid categories list
- App drives most rules complexity; rate rules_complexity=1 despite apparent sophistication
- For QR-scan investigation games: feel=1 (Light cooperative)

## Kids Table Board Gaming (KTBG) Notes
- KTBG is NOT in schema.yaml publishers list — no publisher tag applies
- Based in Toronto, Ontario, Canada; focus on games playable across full family age range
- Diced Veggies (2023): premiered Gen Con 2023; won Origins Award 2024 Best Children's & Family Board Game
- gamingtrend.com/news/ and thefamilygamers.com are useful sources for KTBG releases

## Origins Awards Notes
- Origins Award year is the ceremony year (announced at Origins Game Fair), not the game publication year
- Diced Veggies published 2023, won "Origins Award 2024" (ceremony held June 2024)
- icv2.com/articles/news/ is reliable for Origins Award winner coverage
