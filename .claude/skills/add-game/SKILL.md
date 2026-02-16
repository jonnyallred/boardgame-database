---
name: add-game
description: Create a detailed YAML entry for a board game. Use when adding new games to the database.
argument-hint: "[game name]"
disable-model-invocation: false
context: fork
model: sonnet
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash(ls *)
---

# Add Board Game Entry

Create a detailed YAML file for the board game: **$ARGUMENTS**

When finished, respond with ONLY a brief summary in this format (no other output):

```
Created {slug}.yaml — {Game Name} ({year})
Designers: {list}
Players: {possible_counts}, best at {true_counts}
Ratings: length={n} complexity={n} depth={n} feel={n} value={n}
Categories: {all tags applied}
Sources: {number of URLs logged}
```

If the file already exists, respond with only: `Skipped — {slug}.yaml already exists`.

## Steps

1. **Check for duplicates** — Search existing games by name (including alternate_names) to avoid duplicates. Read all game files in `games/` and check if the game name matches any existing `name` or `alternate_names` field.
2. **Search the web** for the game using publisher sites, Wikipedia, retailers, and review sites. **DO NOT use boardgamegeek.com** — use `blocked_domains: ["boardgamegeek.com"]` on all WebSearch calls.
3. **Read the schema** at `schema.yaml` for valid category values and rating scale definitions.
4. **Read an existing game** (e.g., `games/azul.yaml`) as a formatting reference.
5. **Create the YAML file** at `games/{slug}.yaml` following the exact format below.
6. **Log sources** — append all URLs consulted to `sources/research-log.yaml` (see Source Logging below).

## Preferred Sources (in priority order)

1. **Publisher product pages** (e.g., stonemaier-games.com, fantasyflightgames.com)
2. **Wikipedia** game articles
3. **Retailer pages** (Amazon, Miniature Market, Gamenerdz, etc.)
4. **Review sites** (Dice Tower, Shut Up & Sit Down, Ars Technica)
5. **Rules PDFs** from publisher sites
6. **Designer/studio blogs and interviews**

**Blocked sources:** Do NOT use boardgamegeek.com for any research.

## Research Checklist

Gather all of the following from the preferred sources above:
- Full game name and publication year
- **Alternate names** — other titles for the same game (translations, regional names like "Adel Verpflichtet" / "Hoity Toity")
- Designer(s), publisher(s), and artist(s)
- Player count range and best/recommended counts (from publisher info, reviews, community consensus)
- Playtime (min, max, and average)
- Minimum age
- Core mechanics, themes, and style
- Whether it's part of a game family, has expansions, or is an expansion itself
- Artist(s) / illustrator(s)
- A concise description of the game (3-5 sentences covering theme and key mechanics)

## Rating Guidelines

Use these scales (0-4) based on your research:

| Rating | 0 | 1 | 2 | 3 | 4 |
|--------|---|---|---|---|---|
| **length** | Snack (10 min) | Appetizer (30 min) | Main Course (1 hr) | Feast (3 hrs) | Marathon (6+ hrs) |
| **rules_complexity** | Preschool | Elementary | Junior High/HS | College | PhD |
| **strategic_depth** | Reflex | Basic | Tactics | Strategy | Master Plan |
| **feel** | Solitary | Cooperative | Party | Polite | Fierce |
| **value** | Impulse | Bargain | Fair Deal | Splurge | Heirloom |

### rules_complexity Guidelines

Judge based on how the game feels to learn and teach:

| Score | Label | How to identify |
|-------|-------|-----------------|
| 0 | Preschool | 1-2 rules, explain in one sentence |
| 1 | Elementary | Simple rules, teach in 2-3 minutes |
| 2 | Junior High/HS | Multiple mechanics, 10-15 min to teach |
| 3 | College | Complex interlocking mechanics, 20-30 min to teach |
| 4 | PhD | Intricate rules with exceptions, 30+ min to teach |

## Source Logging

After creating the game file, append all URLs you consulted to `sources/research-log.yaml`. Read the file first, then write it back with new entries appended to the `entries` list.

Each entry format:
```yaml
  - timestamp: "YYYY-MM-DDTHH:MM:SSZ"
    game_id: {slug}
    url: "https://..."
    description: "Brief note on what data was gathered"
```

## YAML Format

Use this exact structure. Add a comment after each rating with the label:

```yaml
id: {slug}
name: "{Full Name}"
alternate_names:
  - "{Other Title 1}"
  - "{Other Title 2}"
year: {year}

# Relationships
game_family: {family-slug or null}
edition: {edition or null}
base_game: {base-game-slug or null}
expansions: []
compatible_with: []

# Ratings (0-4 scale)
length: {0-4}  # {label}
rules_complexity: {0-4}  # {label}
strategic_depth: {0-4}  # {label}
feel: {0-4}  # {label}
value: {0-4}  # {label}

# Personal ratings (leave null until rated)
affinity: null
hotness: null

# Tags
categories:
  - {Mechanic/Style/Theme from schema.yaml ONLY}

# Player counts
possible_counts: [{supported counts}]
true_counts: [{best counts}]

# Metadata
designer:
  - {Designer Full Name}
publisher:
  - {Publisher Full Name}
artist:
  - {Artist Full Name}
playtime_minutes: {average}
min_playtime: {min}
max_playtime: {max}
min_age: {age}

# Description
description: |
  {3-5 sentence description}

# Upgrades
upgrades: []

# Play tracking
plays_tracked:
  total_plays: 0
  configs: []
```

## Rules

- **Check for duplicates first** — Read existing game files and check if the game name matches any `name` or `alternate_names` field. If found, skip creation.
- **Only use categories that exist in `schema.yaml`**. Do not invent new tags.
- **`affinity` and `hotness` must be `null`** — these are personal ratings.
- **`alternate_names`** — List any other titles for the same game (translations, regional names). Use an empty list `[]` if none.
- **Slug/ID must match the filename** (lowercase, hyphen-separated).
- **Do not modify any existing files** — only create the new game file (and append to `sources/research-log.yaml`).
- Use 2-space indentation. No tabs.
- Check if the file already exists by filename before creating — skip if it does.
- **`game_family`**: Only set this if multiple related games exist (editions, sequels, spinoffs). Use a shared slug (e.g., `brass` for Brass: Birmingham and Brass: Lancashire). If the game is standalone with no related titles, use `null`.
- **`compatible_with`**: Only for games whose components can be physically combined (e.g., mixing card pools). Do not use for standalone sequels or games that merely share a universe.
