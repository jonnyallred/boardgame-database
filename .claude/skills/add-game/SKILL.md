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
```

If the file already exists, respond with only: `Skipped — {slug}.yaml already exists`.

## Steps

1. **Search the web** for the game on BoardGameGeek and publisher sites to gather accurate data.
2. **Read the schema** at `schema.yaml` for valid category values and rating scale definitions.
3. **Read an existing game** (e.g., `games/azul.yaml`) as a formatting reference.
4. **Create the YAML file** at `games/{slug}.yaml` following the exact format below.

## Research Checklist

Gather all of the following from official sources:
- Full game name and publication year
- Designer(s), publisher(s), and artist(s)
- Player count range and best/recommended counts (from BGG polls)
- Playtime (min, max, and average)
- Minimum age
- Core mechanics, themes, and style
- Whether it's part of a game family, has expansions, or is an expansion itself
- Artist(s) / illustrator(s)
- A concise description of the game (3-5 sentences covering theme and key mechanics)

## Rating Guidelines

Use these scales (0-4) based on your research. Be accurate — use BGG weight, playtime, and community data:

| Rating | 0 | 1 | 2 | 3 | 4 |
|--------|---|---|---|---|---|
| **length** | Snack (10 min) | Appetizer (30 min) | Main Course (1 hr) | Feast (3 hrs) | Marathon (6+ hrs) |
| **rules_complexity** | Preschool | Elementary | Junior High/HS | College | PhD |
| **strategic_depth** | Reflex | Basic | Tactics | Strategy | Master Plan |
| **feel** | Solitary | Cooperative | Party | Polite | Fierce |
| **value** | Impulse | Bargain | Fair Deal | Splurge | Heirloom |

Map BGG weight to rules_complexity roughly: <1.5→0, 1.5-2.2→1, 2.2-3.0→2, 3.0-3.8→3, >3.8→4

## YAML Format

Use this exact structure. Add a comment after each rating with the label:

```yaml
id: {slug}
name: "{Full Name}"
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

- **Only use categories that exist in `schema.yaml`**. Do not invent new tags.
- **`affinity` and `hotness` must be `null`** — these are personal ratings.
- **Slug/ID must match the filename** (lowercase, hyphen-separated).
- **Do not modify any existing files** — only create the new game file.
- Use 2-space indentation. No tabs.
- Check if the file already exists before creating — skip if it does.
- **`game_family`**: Only set this if multiple related games exist (editions, sequels, spinoffs). Use a shared slug (e.g., `brass` for Brass: Birmingham and Brass: Lancashire). If the game is standalone with no related titles, use `null`.
- **`compatible_with`**: Only for games whose components can be physically combined (e.g., mixing card pools). Do not use for standalone sequels or games that merely share a universe.
