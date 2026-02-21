---
name: add-game
description: Create a detailed YAML entry for a board game. Use when adding new games to the database.
argument-hint: "[game name]"
disable-model-invocation: false
context: fork
model: sonnet
allowed-tools: Read, Write, Glob, Grep, WebSearch, Bash(ls *), Bash(python3 scripts/game_pipeline.py *)
---

# Add Board Game Entry

Create a detailed YAML file for the board game: **$ARGUMENTS**

When finished, respond with ONLY:

```
Created {slug}.yaml — {Game Name} ({year})
Designers: {list}
Players: {possible_counts}, best at {true_counts}
Ratings: length={n} complexity={n} depth={n} feel={n} value={n}
Categories: {all tags applied}
Evokes: {top 5 feelings}
Sources: {number of URLs logged}
```

If the file already exists: `Skipped — {slug}.yaml already exists`.

## Steps

1. **Check duplicates** — Glob `games/*.yaml`, grep for the game name across `name` and `alternate_names` fields. Skip if found.
2. **Read schema** — Read `schema.yaml` for valid categories, rating scales, and evokes.
3. **Read a reference game** — e.g., `games/azul.yaml` for formatting.
4. **Collect URLs** (WebSearch ≤3) — Target publisher site, Wikipedia, one retailer/review. **Never use boardgamegeek.com** (`blocked_domains: ["boardgamegeek.com"]`). Do not use WebFetch.
5. **Run pipeline**:
   ```bash
   python3 scripts/game_pipeline.py "Game Name" --urls url1 url2 url3
   ```
   Returns JSON with `sources[]` (each: `url`, `source_type`, `text`). Extract all metadata from the clean text.
6. **Create YAML** at `games/{slug}.yaml` using the format below. Gather: name, alternate names, year (this edition), designers, publishers, artists, player counts (box + optimal), playtime, min age, mechanics, family/expansion relationships, and a 3-5 sentence description.
7. **Log sources** — Read `sources/research-log.yaml`, then append entries:
   ```yaml
     - timestamp: "YYYY-MM-DDTHH:MM:SSZ"
       game_id: {slug}
       url: "https://..."
       description: "Brief note"
   ```

## Rating Scales (0-4)

| Rating | 0 | 1 | 2 | 3 | 4 |
|--------|---|---|---|---|---|
| length | Snack (10min) | Appetizer (30min) | Main Course (1hr) | Feast (3hr) | Marathon (6+hr) |
| rules_complexity | Preschool | Elementary | Junior High | College | PhD |
| strategic_depth | Reflex | Basic | Tactics | Strategy | Master Plan |
| feel | Solitary | Cooperative | Party | Polite | Fierce |
| value | Impulse | Bargain | Fair Deal | Splurge | Heirloom |

`rules_complexity` guide: 0=one sentence, 1=teach 2-3min, 2=teach 10-15min, 3=teach 20-30min, 4=30+min with exceptions.

## YAML Format

```yaml
id: {slug}
name: "{Full Name}"
alternate_names:
  - "{Other Title}"
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
  - {from schema.yaml ONLY}

# Evokes (top 5)
evokes:
  - {from schema.yaml evokes list}

# Player counts
possible_counts: [{supported}]
true_counts: [{best}]

# Metadata
designer:
  - {name}
publisher:
  - {name}
artist:
  - {name}
playtime_minutes: {avg}
min_playtime: {min}
max_playtime: {max}
min_age: {age}

# Description
description: |
  {3-5 sentences: theme, mechanics, what makes it notable}

# Upgrades
upgrades: []

# Play tracking
plays_tracked:
  total_plays: 0
  configs: []
```

## Rules

- Categories must exist in `schema.yaml`. Do not invent tags.
- Exactly 5 evokes from schema.yaml's evokes list.
- `affinity` and `hotness` must be `null`.
- Slug must match filename (lowercase, hyphen-separated).
- `game_family`: only set if multiple related games exist. `null` for standalone.
- `compatible_with`: only for physically combinable components, not shared universe.
- 2-space indentation. No tabs.
- Do not modify existing files except appending to `sources/research-log.yaml`.
