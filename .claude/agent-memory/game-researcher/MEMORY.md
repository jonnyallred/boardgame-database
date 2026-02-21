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
- CMYK publishes party/social games (Wavelength, Spots, Lacuna, Hot Streak, Wilmot's Warehouse, Magical Athlete)\n- cmyk.games/products/{slug} is JS-gated (Locksmith protection) — pipeline yields JSON noise, not text; use WebSearch summaries\n- Magical Athlete (2025): originally Takashi Ishida (Z-Man 2003), updated by Richard Garfield; artist Angela Kirkwood; 2-6p, 30 min, age 6+
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
- Use "Thames & Kosmos" as publisher name for English-edition KOSMOS games; list both Kosmos and Thames & Kosmos in publisher field
- store.thamesandkosmos.com is the authoritative source for player count, playtime, age, and year
- KOSMOS is NOT in schema.yaml publishers list — no publisher tag applies
- Legends of Andor (2012): German cooperative adventure by Michael Menzel (both designer and illustrator)
  Original title: Die Legenden von Andor; Kennerspiel des Jahres 2013 winner; 2-4 players, 10+, 60-120 min
- EXIT: The Game series: first published Germany 2016; won Kennerspiel 2017
  - Slug: exit-the-game for series-level entry; individual titles get own slugs if needed
  - game_family: exit-the-game for all titles; each title uses base_game: exit-the-game
  - One-time use (cards are cut/folded during play) — mention in description
  - 1-4 players, best 2-3; 45-90 min; age 12+; Cooperative + Puzzle Solving + Deduction tags

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
- Donald X. Vaccarino IS in schema.yaml designers list — apply "Donald X. Vaccarino" tag in categories
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

## Holy Grail Games Notes
- Holy Grail Games is NOT in schema.yaml publishers list — no publisher tag applies
- French publisher (Paris); games often have English and French editions
- Dominations: Road to Civilization (2019): Designers Olivier Melison & Eric Dubus; triangular domino tile placement civ game
- americantabletopawards.com confirms game details (publisher, designers) for award nominees

## Civilization Building Euro Games Rating Pattern
- Dominations: Road to Civilization (2019): length=2, complexity=2, depth=3, feel=2, value=3
  (60-120 min medium, moderate rules with 6 knowledge domains + tech tree, deep optimization puzzle, moderate competition, premium MSRP)
- Triangular domino tile placement is a unique variant of Tile Placement mechanic
- Use Tech Tree tag when game has a branching mastery/technology card system

## Thunderworks Games Notes
- Thunderworks Games is NOT in schema.yaml publishers list — no publisher tag applies
- thunderworksgames.com product pages are Shopify-based and return JS/CSS noise in pipeline
- WebSearch summaries are sufficient for Thunderworks titles; Board Game Arena pages are clean
- FlipToons (2025): Designers Jordy Adan & Renato Simoes; Artist Diego Sa; small-box deckbuilder
- FlipToons: length=0, complexity=1, depth=1, feel=2, value=1
  (15-30 min snack; simple deckbuilder; light grid-flip scoring decisions; moderate competition; ~$20 budget price)

## Off The Page Games Notes
- Off The Page Games is NOT in schema.yaml publishers list — no publisher tag applies
- offthepagegames.com product pages are heavily CSS/JS-laden (pipeline yields mostly font boilerplate)
- Kickstarter project page (kickstarter.com/projects/mindmgmt/...) is a better pipeline source
- meeplemountain.com reviews are reliable for mechanics details on their titles
- Harrow County: Gothic Conflict (2024): Designers Jay Cormier + Shad Miller; cube tower combat built into box lid
- Fair Folk expansion scales game from 3 to 4 players and adds factions
- Harrow County: Gothic Conflict (2024): length=1, complexity=2, depth=2, feel=3, value=3
  (45-75 min short asymmetric horror, moderate rules with cube tower + mason jar action drafting, tactical route building, competitive but contained, premium IP production)

## Classic Children's/Family Games (1980s era)
- Spiel des Jahres winners like Enchanted Forest are best sourced from Wikipedia + opinionatedgamers.com
- Ravensburger IS in schema.yaml publishers list — apply "Ravensburger" tag in categories
- For roll-and-move memory games: Dice Rolling + Family + Fantasy are the core tags
- Artist credits are often unverifiable for 1980s games — use `artist: []` (empty list)
- Enchanted Forest (Sagaland): year=1982, ages 6+, 2-6 players, designers Alex Randolph + Michel Matschoss
- Pipeline often returns CSS/JS noise for Ravensburger product pages — rely on search result summaries
- opinionatedgamers.com SdJ re-reviews are a reliable source for historical SdJ mechanics details

## Pegasus Spiele Publisher Notes
- Pegasus Spiele is NOT in schema.yaml publishers list — no publisher tag applies
- German-language publisher; games often co-published in English by Thames & Kosmos or other regional partners
- Dorfromantik: The Board Game (2022): published by Pegasus Spiele, designed by Lukas Zach & Michael Palm
- Winner of 2023 Spiel des Jahres; artist: Michaela Kienle
- Slug: dorfromantik-the-board-game (keep subtitle "The Board Game" to distinguish from video game)

## Asmadi Games Publisher Notes
- Asmadi Games is NOT in schema.yaml publishers list — no publisher tag applies
- asmadigames.com hosts rulebook PDFs for their games
- Innovation (2010): Carl Chudyk's cult classic card game; also published in French by Iello (2011)
- Iello/IELLO is NOT in schema.yaml publishers list — no publisher tag applies
- geekyhobbies.com is a reliable source for Innovation artist credits (Anders Olausson, Robin Olausson, etc.)
- Innovation: length=2, complexity=3, depth=3, feel=3, value=2
  (45-120 min medium, complex unique card powers per card, deep asymmetric combos, polite competitive, ~$30-40 fair deal)

## Cooperative Tile Placement Puzzle Games Rating Pattern
- Dorfromantik: The Board Game (2022): length=1, complexity=1, depth=1, feel=1, value=2
  (45-90 min short, elementary rules, light tactical tile placement, fully cooperative, ~$50 fair deal)
- true_counts: 1-4 (box supports 1-6 but community consensus optimal at 1-4)
- Campaign mode does not raise length rating if individual sessions are under 90 min

## Eagle-Gryphon Games Notes
- Eagle-Gryphon Games IS in schema.yaml publishers list — apply "Eagle-Gryphon Games" tag in categories
- eagle-gryphon.com product pages are Shopify-based and return mostly JS/CSS noise in pipeline — rely on search result summaries
- Federation (2022): Designers Dimitri Perrier & Matthieu Verdier; double-sided worker placement voting mechanic
- Federation: length=2, complexity=2, depth=3, feel=2, value=3
  (60-120 min medium euro, moderate rules, deep strategic planning with vote manipulation, moderately competitive, premium sci-fi production)

## Invalid Mechanic Tags (common mistakes)
- "Voting" — NOT a valid tag; describe voting mechanic in description text only
- Always cross-check against valid categories list before writing YAML

## Eagle-Gryphon Games Notes
- Eagle-Gryphon Games IS in schema.yaml publishers list — apply "Eagle-Gryphon Games" tag in categories
- eaglegames.net and eagle-gryphon.com are both their domains (eaglegames.net redirects to eagle-gryphon.com)
- For Sale (1997): classic Stefan Dorra auction filler; multiple editions (Ravensburger 1997, Überplay, Gryphon 2009, Eagle-Gryphon current)
- Use original publication year (1997) even when listing current publisher

## Classic Auction/Bidding Filler Rating Pattern
- For Sale (1997): length=0, complexity=1, depth=1, feel=2, value=2
  (20-30 min snack, simple 2-phase bid/reveal rules, light bluffing decisions, moderate competition, standard MSRP)
- possible_counts for 3-6; true_counts favor 4-5 for best auction dynamics
- Tags: Auctions/Bidding, Hand Management, Bluffing, Simultaneous Action, Set Collection, Family, Filler, Gateway

## Stratego-Style 2-Player Hidden Identity Duel Pattern
- Lord of the Rings: The Confrontation (2002): length=1, complexity=1, depth=2, feel=3, value=2
  (15-45 min short, simple rules, moderate tactical bluffing, competitive duel, standard FFG MSRP)
- Fantasy Flight Games IS in schema.yaml publishers list — apply "Fantasy Flight Games" tag
- Reiner Knizia IS in schema.yaml designers list — apply "Reiner Knizia" tag
- Tags: Hidden Movement, Bluffing, Hand Management, Asymmetric, Variable Player Powers, 1 vs Many
- Both "Lord of the Rings" AND "Fantasy" theme tags are appropriate for LOTR-themed games
- Original publisher was Kosmos (Germany); FFG published English edition also in 2002
- Deluxe Edition (2005) had improved components but same mechanics — same slug, same entry

## Cephalofair Games Notes
- Cephalofair Games IS in schema.yaml publishers list — apply "Cephalofair Games" tag in categories
- Isaac Childres IS in schema.yaml designers list — apply "Isaac Childres" tag in categories
- Gloomhaven series: game_family=gloomhaven covers the full family (Gloomhaven, Jaws of the Lion, Frosthaven)
- Jaws of the Lion is standalone but compatible_with gloomhaven (characters are cross-game compatible)
- Artists: Alexandr Elichev, Josh T. McDowell, Biboun (shared across Gloomhaven / JotL)
- tabletopbellhop.com is a reliable detailed comparison/review source for the Gloomhaven series
- Jaws of the Lion: 1-4 players, 25 scenarios, learn-as-you-play tutorial for first 5 scenarios
- Dungeon crawl cooperative: feel=1 (Light/Cooperative), true_counts=[2,3] per community consensus
- Per-scenario playtime 60-150 min; use playtime_minutes=105 (median)

## Pandasaurus Games Publisher Notes
- Pandasaurus Games is NOT in schema.yaml publishers list — no publisher tag applies
- pandasaurusgames.com Shopify store pages return mostly JS noise from pipeline — rely on search summaries
- Machi Koro (2012): designer Masao Suganuma, artist Noboru Hotta, originally published by Grounding Inc. (Japan)
  US edition by IDW Games (first), then Pandasaurus Games (current 5th Anniversary edition)
- Machi Koro: length=1, complexity=1, depth=1, feel=2, value=2

## Argentum Verlag Publisher Notes
- Argentum Verlag is NOT in schema.yaml publishers list — no publisher tag applies
- German publisher of Hansa Teutonica (2009); game later co-published in English by Z-Man Games (Big Box 2020)
- Designer: Andreas Steding; Artist: Andreas Resch

## Network Building Euro Games Rating Pattern
- Hansa Teutonica (2009): length=2, complexity=2, depth=3, feel=3, value=2
  (45-90 min medium; moderate rules with 5 upgradeable skill tracks; deep route-network optimization; competitive blocking/bumping; standard MSRP)
- Network-building games: true_counts typically [3, 4] for 2-5 player games (5 players = too chaotic; 2 = too direct)
- boardgameguys.com returns raw JS/CSS from pipeline — use search result summaries instead

## Feuerland Spiele Publisher Notes
- Feuerland Spiele is the original German publisher of Terra Mystica and Gaia Project
- Capstone Games IS in schema.yaml publishers list — apply "Capstone Games" tag when they are the English publisher
- Z-Man Games held English rights to Feuerland titles before Capstone Games took over
- digidiced.com (DIGIDICED) is the digital adaptation studio for Feuerland games; confirms designers/year
- icv2.com is reliable for tracking publisher rights changes (e.g., Capstone picking up Feuerland titles)
- Dennis Lohausen is the artist for many Feuerland titles including Gaia Project and Terra Mystica

## Heavy Asymmetric Eurogame Rating Pattern (Terra Mystica style)
- Gaia Project (2017): length=3, complexity=4, depth=4, feel=3, value=3
  (60-150 min long, PhD-level interacting systems, master-plan faction optimization, politely competitive, premium ~$100 MSRP)
- 14 asymmetric factions, hex grid, tech tracks, power bowl management
- Tags: Area Control, Variable Player Powers, Tech Tree, Network Building, Resource Management, Modular Board, Variable Setup, Action Points, Hex Map
- true_counts excludes solo for optimal (3-4 best for interaction)
- Wikipedia may lack dedicated board game articles — pipeline returns nothing; rely on other sources

## Gen42 Games Publisher Notes
- Gen42 Games is NOT in schema.yaml publishers list — no publisher tag applies
- gen42.com/product/{slug} is the official product page; often returns JS/cookie consent noise
- Wikipedia is a reliable primary source for Gen42 titles (Hive, etc.)
- discoverwildlife.com is useful for review-style overviews of Gen42 games

## Abstract Strategy 2-Player Games Rating Pattern
- Hive (2001): length=0, complexity=1, depth=3, feel=3, value=2
  (15-30 min snack, simple rules, deep tactical strategy, politely competitive 2-player duel, standard MSRP)
- Pure abstract games with no randomness: do NOT use "Dice Rolling" or "Press Your Luck" tags
- For boardless games: "Tile Placement" is still the right mechanic tag (pieces form the board)
- true_counts: [2] for pure 2-player abstract games — no optimal count variance
- feel=3 (Competitive) rather than feel=4 (Fierce) for polite abstract duels without direct take-that
- Mensa Select award is worth noting in descriptions for abstract games

## Tablescope Publisher Notes
- Tablescope is NOT in schema.yaml publishers list — no publisher tag applies
- lightspeedarena.com is the official site but returns heavy CSS noise in pipeline
- Ares Games distributes Tablescope games at retail (aresgames.eu)
- Light Speed: Arena (2025): Kickstarter 2024, retail 2025; list "Tablescope" as publisher (Ares is distributor only)
- Slug for "Light Speed: Arena" → light-speed-arena (colon-space becomes hyphen, per slug convention)
- Designers: Leonardo Alese, James Ernest, Tom Jolly, Emanuele Santellani (none in schema list)
- opinionatedgamers.com review (2025-11-16) is reliable for this game's mechanics detail

## App-Integrated Real-Time Tile Placement Games
- Light Speed: Arena (2025): length=0, complexity=1, depth=2, feel=3, value=2
  (15-20 min snack; simple tile placement; moderate real-time positional tactics; competitive arena; standard MSRP)
- App handles all combat resolution — rate rules_complexity=1 even though underlying math is complex
- Tags: Tile Placement, Simultaneous Action, Real-time, Area Control, Sci-Fi, Space, Family, Filler

## App-Integrated Cooperative Adventure Games (Bluetooth Tower)
- Return to Dark Tower (2022): length=3, complexity=2, depth=2, feel=1, value=3
  (90-120 min long; moderate resource/engine rules; tactical hero coordination; fully cooperative; premium $100+ production with motorised Bluetooth tower)
- Designers: Isaac Childres + Rob Daviau + Noah Cohen + Brian Neff + Justin D. Jacobson
- Restoration Games IS in schema.yaml publishers list — apply "Restoration Games" tag in categories
- Isaac Childres IS in schema.yaml designers list — apply "Isaac Childres" tag in categories
- Rob Daviau IS in schema.yaml designers list — apply "Rob Daviau" tag in categories
- Kickstarter campaign Jan 2020; delivery/retail 2022
- game_family: dark-tower (covers original 1981 Milton Bradley Dark Tower and the 2022 reimagining)
- Tags: Cooperative, Engine Building, Resource Management, Variable Player Powers, Modular Board, Campaign Mode, Fantasy, Ameritrash

## Days of Wonder Publisher Notes
- Days of Wonder IS in schema.yaml publishers list — apply "Days of Wonder" tag in categories
- daysofwonder.com product pages return JSON-LD/JS metadata from pipeline — rely on search summaries
- Richard Borg is NOT in schema.yaml designers list — do not apply a designer tag for him
- Memoir '44 (2004): 2-player WWII Command and Colors system game; slug: memoir-44
  - Won 2004 International Gamers Award (General Strategy, 2-player)
  - Overlord mode supports up to 8 players but requires 2 copies — true_counts stays [2] for base game

## Command & Colors (Richard Borg) System
- Tags: Hex Map, Dice Rolling, Hand Management, Card Drafting, Modular Board, Variable Setup, Wargame
- Memoir '44: length=1, complexity=1, depth=2, feel=3, value=2
  (30-60 min short, simple card-driven activation rules, moderate tactical decisions, competitive 2-player, standard MSRP)

## Pipeline Noise Pattern Reminder
- When pipeline returns JSON/JS blobs instead of clean text (Days of Wonder, Meeple Mountain, etc.),
  the WebSearch result summaries are usually sufficient for well-known commercial games
- Do not retry the pipeline — work with what the search results provide

## Spielworxx Publisher Notes
- Spielworxx is NOT in schema.yaml publishers list — no publisher tag applies
- gamefound.com/en/projects/spielworxx/{slug} is a reliable campaign page source
- Known for Kickstarter/Gamefound campaigns with sometimes inconsistent component quality
- Oranienburger Kanal (2023): Designer Uwe Rosenberg; 1-2 players, 45-90 min, age 12+
  Won International Gamers Award 2023 (two-player category)

## Uwe Rosenberg 1-2 Player Heavy Euro Rating Pattern
- Oranienburger Kanal (2023): length=2, complexity=3, depth=3, feel=2, value=2
  (45-90 min medium, complex card activation + bridge/route network systems, deep spatial planning, moderately competitive, standard MSRP)
- Dual-trigger card activation: structure fires when surrounded by routes AND again when bridged to 2+ neighbors
- Uwe Rosenberg IS in schema.yaml designers list — apply "Uwe Rosenberg" tag in categories

## Zoch Verlag Publisher Notes
- Zoch Verlag (also "Zoch zum Spielen") is NOT in schema.yaml publishers list — no publisher tag applies
- Rio Grande Games IS in schema.yaml publishers list — apply "Rio Grande Games" tag when they are the English publisher
- zoch-verlag.com product pages are heavily JS-laden (cookie consent, Salesforce scripts) — pipeline yields minimal useful text
- gambiter.com and en.wikipedia.org are the most reliable pipeline sources for older Zoch titles

## Classic Spiel des Jahres Family Games Rating Pattern (Niagara style)
- Niagara (2004): length=1, complexity=1, depth=1, feel=2, value=2
  (30-45 min short, simple simultaneous paddle reveal, light tactical decisions, moderate competition, standard MSRP)
- Simultaneous revealed paddle tiles that affect whole table = "Simultaneous Action" tag
- Winner: 2005 Spiel des Jahres, 2005 Mensa Mind Games
- possible_counts [3,4,5]; true_counts [4,5] for best race dynamics
- Artist: Franz Vohwinkel (confirmed for Niagara)

## Hurrican Publisher Notes
- Hurrican is NOT in schema.yaml publishers list — no publisher tag applies
- brunocathala.com designer site is an excellent source for Hurrican game metadata (year, co-designer, illustrator, playtime, age)
- Mr. Jack (2006): Designers Bruno Cathala + Ludovic Maublanc; Artist Pierô (Pierre Lechevalier)
- Mr. Jack: 2-player asymmetric deduction, Whitechapel 1889, 8 characters, ~30 min, ages 9+
- Illustrator "Pierô" is a pseudonym for Pierre Lechevalier

## Asymmetric 2-Player Deduction/Hidden Identity Pattern
- Mr. Jack (2006): length=1, complexity=1, depth=2, feel=3, value=2
  (20-40 min short, elementary rules, moderate deduction tactics, politely competitive cat-and-mouse, standard MSRP)
- Tags: Deduction, Hidden Movement, Asymmetric, Variable Player Powers, Hex Map, Mystery, Historical
- Designer Bruno Cathala IS in schema.yaml designers list — apply "Bruno Cathala" tag
- For "Jack the Ripper" 1889 London setting: use "Historical" theme tag (not just Mystery)
- game_family: mr-jack (original game + Mr. Jack Pocket + Mr. Jack New York variants)
- Research log (sources/research-log.yaml): file is 6700+ lines, exceeds 256KB Read limit
  Use `tail -5` to check end-of-file format, then `cat >>` bash append (not Edit tool)

## Eerie Idol Games Publisher Notes
- Eerie Idol Games is NOT in schema.yaml publishers list — no publisher tag applies
- eerieidolgames.com is the official site (Wix-based — pipeline yields JS/JSON framework noise, not useful)
- Gamefound (gamefound.com) is a reliable source for their campaign update posts with mechanic details
- The Old King's Crown (2025): card-driven area control with simultaneous card play; designer Pablo Clark (also artist)
- Solo mode by Richard Wilkins (acclaimed solo specialist: Pax Pamir 2e, John Company 2e, Oath)
- Songs of Home expansion adds factions and neutral Kingdom cards
- wargamer.com is a detailed review source for this game; playerelimination.com covers area control well

## Area Control Bluffing Games Rating Pattern
- The Old King's Crown (2025): length=2, complexity=2, depth=3, feel=3, value=3
  (60-120 min medium, moderate rules with faction upgrade cards, deep simultaneous bluffing/combo planning, competitive conquest, premium indie production)
- Simultaneous card placement to regions: use both "Simultaneous Action" + "Bluffing" tags together
- Kingdom card bidding = "Auctions/Bidding" tag
- 4 asymmetric factions with faction-specific upgrade cards: "Asymmetric" + "Variable Player Powers"
- Slug: old-kings-crown (drop "The", apostrophe dropped, no other special handling needed)

## CMON Publisher Notes
- CMON IS in schema.yaml publishers list — apply "CMON" tag in categories
- cmon.com/products/{slug} is the official product page but often returns JS/CSS noise in pipeline — use review sites instead
- Artipia Games is a Greek publisher (not in schema.yaml) that co-published Project: ELITE with CMON
- Project: ELITE (2020): co-published by CMON + Artipia Games; original 2015 version was by Drawlab Entertainment
  Designers: Konstantinos Kokkinis, Marco Portugal, Sotirios Tsantilas; 1-6 players, ages 14+, 30-60 min
  Slug: project-elite (colon stripped per slug punctuation convention)
  length=1, complexity=2, depth=2, feel=2, value=3
- Real-time cooperative games: feel=2 (Moderate) when tension is team-coordination-based, not player-vs-player

## Ferti Publisher Notes
- Ferti is a French publisher (en.ferti-games.com); NOT in schema.yaml publishers list — no publisher tag
- Eagle-Gryphon Games IS in schema.yaml — apply "Eagle-Gryphon Games" tag when they are North American distributor
- en.ferti-games.com returns Wix JavaScript noise — rely on search result summaries

## PitchCar (1995) Rating Calibration
- PitchCar (1995): length=1, complexity=0, depth=1, feel=3, value=3
  (20-45 min short, preschool-level "flick the disc" rule, light physical skill decisions, competitive racing, premium all-wood components)
  Designer: Jean du Poël; Publisher: Ferti (France), Eagle-Gryphon Games (North America)
  2-8 players; true_counts=[4,5,6]; 9 expansions add track element variety

## Floodgate Games Publisher Notes
- Floodgate Games is NOT in schema.yaml publishers list — no publisher tag applies
- floodgate.games product pages are Shopify-based and return JS/CSS noise — pipeline yields minimal useful text
- Rely on Wikipedia and search result summaries for Floodgate titles

## Sagrada-Specific Notes
- Designers: Adrian Adamescu and Daryl Andrews (neither in schema.yaml designer tag list)
- Publisher: Floodgate Games (not in schema.yaml publishers list)
- Artist: Conor McGoey
- Solo mode is included in the base game (1-4 players, 1 is valid in possible_counts)
- Best at 2-3 players per community consensus; supports 1-4
- Sagrada (2017): length=1, complexity=1, depth=2, feel=2, value=2
  (30-45 min short dice drafting, simple adjacency rules, moderate optimization of objectives, moderate competition, standard MSRP)
- Expansions: sagrada-5-6-player-expansion, sagrada-artisans, sagrada-panorama
- Tags: Drafting, Dice Rolling, Pattern Building, Set Collection, Hand Management, Family, Gateway

## Classic Tile Rummy Games (Rummikub)
- Rummikub (1977): Designed by Ephraim Hertzano in the 1940s; first sold commercially in Israel 1977
- Won Spiel des Jahres 1980; original publisher Lemada Light Industries; US publisher Pressman Toy Corporation
- Pressman Toy Corporation is NOT in schema.yaml publishers list — no publisher tag applies
- Ravensburger IS in schema.yaml publishers list — apply "Ravensburger" tag if using the German edition entry
- Use year: 1977 for original edition (despite 1940s design; 1977 is first commercial publication year)
- Artist typically uncredited on classic editions — use `artist: []` (empty list)
- Tags: Set Collection, Hand Management, Tile Placement, Family, Abstract, Gateway
- Rummikub: length=1, complexity=1, depth=1, feel=2, value=1
  (30-60 min short, simple rules, light tactical tableau manipulation, moderately competitive, budget MSRP)
- true_counts: [3, 4] — more interaction/fun with more players; 2-player works but feels flat
- pagat.com/rummy/rummikub.html is an excellent detailed rules source for classic tile/card games
