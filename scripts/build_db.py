#!/usr/bin/env python3
"""Build a SQLite database from YAML game files.

Reads all games/*.yaml files and produces games.db — a normalized
SQLite database for querying, searching, and sorting across the
entire collection. YAML remains the source of truth; this DB is
a derived read cache that can be rebuilt at any time.

Usage:
    python3 scripts/build_db.py
"""

import glob
import os
import sqlite3
import sys

import yaml

GAMES_DIR = os.path.join(os.path.dirname(__file__), '..', 'games')
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'games.db')

SCHEMA_SQL = """
-- Core game table: one row per game, scalar fields only
CREATE TABLE games (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    year INTEGER,
    edition TEXT,
    game_family TEXT,
    base_game TEXT,
    playtime_minutes INTEGER,
    min_playtime INTEGER,
    max_playtime INTEGER,
    min_age INTEGER,
    length INTEGER,
    rules_complexity INTEGER,
    strategic_depth INTEGER,
    feel INTEGER,
    value INTEGER,
    affinity INTEGER,
    hotness INTEGER,
    description TEXT,
    total_plays INTEGER DEFAULT 0
);

-- Array tables
CREATE TABLE game_alternate_names (
    game_id TEXT NOT NULL REFERENCES games(id),
    name TEXT NOT NULL
);

CREATE TABLE game_designers (
    game_id TEXT NOT NULL REFERENCES games(id),
    name TEXT NOT NULL
);

CREATE TABLE game_publishers (
    game_id TEXT NOT NULL REFERENCES games(id),
    name TEXT NOT NULL
);

CREATE TABLE game_artists (
    game_id TEXT NOT NULL REFERENCES games(id),
    name TEXT NOT NULL
);

CREATE TABLE game_categories (
    game_id TEXT NOT NULL REFERENCES games(id),
    category TEXT NOT NULL
);

CREATE TABLE game_evokes (
    game_id TEXT NOT NULL REFERENCES games(id),
    evoke TEXT NOT NULL
);

CREATE TABLE game_possible_counts (
    game_id TEXT NOT NULL REFERENCES games(id),
    count TEXT NOT NULL
);

CREATE TABLE game_true_counts (
    game_id TEXT NOT NULL REFERENCES games(id),
    count TEXT NOT NULL
);

CREATE TABLE game_expansions (
    game_id TEXT NOT NULL REFERENCES games(id),
    expansion_id TEXT NOT NULL
);

CREATE TABLE game_compatible_with (
    game_id TEXT NOT NULL REFERENCES games(id),
    compatible_id TEXT NOT NULL
);

-- Nested table for upgrades
CREATE TABLE game_upgrades (
    game_id TEXT NOT NULL REFERENCES games(id),
    name TEXT,
    year INTEGER,
    type TEXT,
    publisher TEXT,
    notes TEXT
);

-- Indexes for common queries
CREATE INDEX idx_categories_category ON game_categories(category);
CREATE INDEX idx_evokes_evoke ON game_evokes(evoke);
CREATE INDEX idx_designers_name ON game_designers(name);
CREATE INDEX idx_games_year ON games(year);
CREATE INDEX idx_games_rules_complexity ON games(rules_complexity);
CREATE INDEX idx_games_strategic_depth ON games(strategic_depth);
CREATE INDEX idx_games_length ON games(length);
CREATE INDEX idx_games_feel ON games(feel);
CREATE INDEX idx_games_value ON games(value);
CREATE INDEX idx_games_name ON games(name);
"""


def load_yaml_files():
    """Load all YAML game files and return a list of dicts."""
    pattern = os.path.join(GAMES_DIR, '*.yaml')
    files = sorted(glob.glob(pattern))
    games = []
    for path in files:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        if data and 'id' in data:
            games.append(data)
    return games


def insert_game(cursor, game):
    """Insert a single game into all relevant tables."""
    # Extract total_plays from nested plays_tracked
    total_plays = 0
    plays_tracked = game.get('plays_tracked')
    if isinstance(plays_tracked, dict):
        total_plays = plays_tracked.get('total_plays', 0) or 0

    # Insert into main games table
    cursor.execute("""
        INSERT INTO games (
            id, name, year, edition, game_family, base_game,
            playtime_minutes, min_playtime, max_playtime, min_age,
            length, rules_complexity, strategic_depth, feel, value,
            affinity, hotness, description, total_plays
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        game['id'],
        game['name'],
        game.get('year'),
        game.get('edition'),
        game.get('game_family'),
        game.get('base_game'),
        game.get('playtime_minutes'),
        game.get('min_playtime'),
        game.get('max_playtime'),
        game.get('min_age'),
        game.get('length'),
        game.get('rules_complexity'),
        game.get('strategic_depth'),
        game.get('feel'),
        game.get('value'),
        game.get('affinity'),
        game.get('hotness'),
        game.get('description', '').strip() if game.get('description') else None,
        total_plays,
    ))

    game_id = game['id']

    # Array fields: (yaml_key, table_name, column_name)
    array_fields = [
        ('alternate_names', 'game_alternate_names', 'name'),
        ('designer', 'game_designers', 'name'),
        ('publisher', 'game_publishers', 'name'),
        ('artist', 'game_artists', 'name'),
        ('categories', 'game_categories', 'category'),
        ('evokes', 'game_evokes', 'evoke'),
        ('possible_counts', 'game_possible_counts', 'count'),
        ('true_counts', 'game_true_counts', 'count'),
        ('expansions', 'game_expansions', 'expansion_id'),
        ('compatible_with', 'game_compatible_with', 'compatible_id'),
    ]

    for yaml_key, table, col in array_fields:
        items = game.get(yaml_key) or []
        for item in items:
            cursor.execute(
                f"INSERT INTO {table} (game_id, {col}) VALUES (?, ?)",
                (game_id, str(item))
            )

    # Upgrades (nested objects)
    for upgrade in (game.get('upgrades') or []):
        if isinstance(upgrade, dict):
            cursor.execute("""
                INSERT INTO game_upgrades (game_id, name, year, type, publisher, notes)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                game_id,
                upgrade.get('name'),
                upgrade.get('year'),
                upgrade.get('type'),
                upgrade.get('publisher'),
                upgrade.get('notes'),
            ))


def build_database():
    """Build the SQLite database from YAML files."""
    games = load_yaml_files()
    if not games:
        print("No YAML files found in games/", file=sys.stderr)
        sys.exit(1)

    # Remove existing DB for clean rebuild
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    cursor = conn.cursor()

    # Create schema
    cursor.executescript(SCHEMA_SQL)

    # Insert all games
    for game in games:
        try:
            insert_game(cursor, game)
        except Exception as e:
            print(f"Error inserting {game.get('id', '???')}: {e}", file=sys.stderr)

    conn.commit()

    # Print summary
    counts = {}
    for table in ['games', 'game_categories', 'game_evokes', 'game_designers',
                   'game_publishers', 'game_artists', 'game_upgrades']:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        counts[table] = cursor.fetchone()[0]

    conn.close()

    print(f"Built {DB_PATH}: "
          f"{counts['games']} games, "
          f"{counts['game_categories']} categories, "
          f"{counts['game_evokes']} evokes, "
          f"{counts['game_designers']} designers, "
          f"{counts['game_publishers']} publishers, "
          f"{counts['game_artists']} artists, "
          f"{counts['game_upgrades']} upgrades")


if __name__ == '__main__':
    build_database()
