#!/usr/bin/env python3
"""
Cross-reference board games from major retailers against our master list.
Finds games sold at Barnes & Noble and Target that we might be missing.
"""

import csv
import re
from difflib import SequenceMatcher
from pathlib import Path

# ── Scraped data from Barnes & Noble and Target (Feb 2026) ──────────────

BN_SHOP_ALL = [
    "Qawale", "Steam Up A Feast of Dim Sum", "You Think You Know Me",
    "A Place For All My Books", "Kurt Vonnegut's GHQ: The Lost Board Game",
    "Harmonies", "The Lord of the Rings: The Fellowship of the Ring: Trick-Taking Game",
    "Telestrations", "Floristry", "Let's Go! To Japan", "Not So Neighborly",
    "Finest Fish", "Gnome Hollow", "Garden Guests", "Hardback", "Wyrmspan",
    "Wingspan", "Heroes of Barcadia", "Art Society", "Hues and Cues", "Finspan",
    "Catan", "Mistborn Deckbuilding Game", "EXIT: The Enchanted Forest",
    "EXIT: The Professor's Last Riddle", "EXIT: Venice Conspiracy",
    "EXIT: Adventures on Catan", "EXIT: The Disappearance of Sherlock Holmes",
    "EXIT: The Magical Academy", "EXIT: Nightfall Manor", "EXIT: The Deserted Lighthouse",
    "Wavelength", "Horrible Therapist", "The Couples Game",
    "We're Not Really Strangers", "Things in Rings", "Beat The System",
    "Trash Talk", "Priorities Fourth Wing", "Act Your Age",
    "What Were You Thinking? Pop Culture Edition", "Cards Against Humanity",
    "Brick Like This", "Exploding Kittens: The Board Game",
    "Ticket to Ride", "Comic Hunters", "RISK: Dune", "Wicked Game",
    "Heroscape Age of Annihilation", "Masters of Crime: Vendetta",
    "Masters of Crime: Shadows", "Monkey Palace", "Survivor: The Tribe Has Spoken",
    "Taco Cat Goat Cheese Pizza", "UNO: Harry Potter",
    "Poetry for Neanderthals", "Dungeons & Dragons Dungeon Board Game",
    "Coup", "Rivals for Catan", "Blitz Bowl Ultimate",
    "Catan: New Energies", "Agueda: City of Umbrellas",
    "Happy Little Dinosaurs", "One Night Ultimate Werewolf",
    "UNO No Mercy", "Flip 7", "Bananagrams", "Murdle",
    "Sushi Go!", "Mancala", "Monopoly Deal", "Dutch Blitz",
    "Faraway", "May Contain Butts",
]

BN_STRATEGY = [
    "BattleTech Inner Sphere Direct Fire Lance", "Trekking the National Parks",
    "Final Girl: Once Upon a Full Moon", "Munchkin Deluxe",
    "Root", "Alice is Missing", "Choose Your Own Adventure",
    "EXIT: Prison Break", "Agatha Christie: Death on the Cards",
    "EXIT: The Hunt Through Amsterdam", "Splendor Duel",
    "Night Cage", "Wingspan: Oceania Expansion",
    "Wrath of Ashardalon", "SPY - Pack O Game",
]

BN_FAMILY = [
    "Disney Villainous", "Othello", "Codenames: Duet", "Parks",
    "Scrabble", "Exploding Kittens", "7 Wonders Duel", "Azul",
    "Ticket to Ride", "Jenga", "Forbidden Island", "King of Tokyo",
    "My City", "Planet", "Boss Monster", "Love Letter",
    "Disney Hocus Pocus", "Carcassonne", "Splendor",
]

BN_PARTY = [
    "Bet on Your Friends", "For The Girls", "Extreme Personal Questions",
    "Let's Get Deep", "Psycho Killer", "Our Family Is So Weird",
    "What Do You Meme?", "Disturbed Friends", "Shit Happens",
    "Joking Hazard", "Red Flags", "New Phone, Who Dis?",
    "P For Pizza", "First to Worst", "I Should Have Known That!",
    "Grab The Mic",
]

TARGET_GAMES = [
    "Catan", "Muffin Time", "Wavelength", "Sorry!",
    "Tower Stack Game", "Connect 4", "Ticket to Ride",
    "Everdell", "Exploding Kittens Survivor: The Tribe Has Spoken",
    "Trouble", "Candy Land", "Chutes and Ladders",
    "Clue", "Game of Life", "Guess Who?", "Monopoly",
    "Operation", "Risk", "Scrabble", "Stratego",
    "Trivial Pursuit", "Yahtzee", "Battleship", "Boggle",
    "Cranium", "Pictionary", "Taboo", "Apples to Apples",
    "Blokus", "Sequence", "Codenames", "Splendor",
    "Pandemic", "Carcassonne", "Azul", "Wingspan",
    "7 Wonders", "Ticket to Ride: Europe", "Settlers of Catan",
    "King of Tokyo", "Sagrada", "Photosynthesis",
    "Terraforming Mars", "Spirit Island", "Gloomhaven",
    "Villainous", "Unstable Unicorns", "Exploding Kittens",
    "Bears vs Babies", "Throw Throw Burrito",
    "What Do You Meme?", "Telestrations", "Dixit",
    "Mysterium", "Betrayal at House on the Hill",
    "Arkham Horror", "Dominion", "Star Wars: Rebellion",
]

# ── GameNerdz bestsellers (Feb 2026, pages 1-10) ──────────────

GAMENERDZ_GAMES = [
    "Wandering Towers", "Terra Nova", "Forest Shuffle",
    "Heat: Pedal to the Metal", "Dorfromantik: The Board Game",
    "Cascadia", "Nucleum", "Arcs", "The White Castle",
    "World Wonders", "Fiction", "QE", "Wyrmspan", "Evacuation",
    "Horseless Carriage", "Daybreak", "Foundations of Metropolis",
    "Through the Desert", "Civolution", "Distilled",
    "Praga Caput Regni", "Harmonies", "Windmill Valley", "Scout",
    "Medici", "Sail", "Expeditions", "Earth", "The Gang", "Ark Nova",
    "SETI: Search for Extraterrestrial Intelligence",
    "The Vale of Eternity", "Freelancers: A Crossroads Game",
    "Minos: Dawn of the Bronze Age", "Witchcraft!",
    "Rebel Princess", "Stardew Valley: The Board Game", "Knarr",
    "Wingspan", "Meadow", "Targi", "boop.", "Age of Innovation",
    "Slay the Spire: The Board Game", "Brass: Birmingham",
    "Dune: War for Arrakis", "Castle Combo", "Root",
    "Jekyll & Hyde vs Scotland Yard",
    "Lost Ruins of Arnak", "Apiary", "The Crew: Mission Deep Sea",
    "Cascadia", "Hansa Teutonica", "Carnegie", "Ready Set Bet",
    "Hegemony: Lead Your Class to Victory", "Zoo Vadis",
    "First Rat", "Courtisans", "Bus", "Orichalcum",
    "Sea Salt & Paper", "Flamecraft", "Azul",
    "That Time You Killed Me", "King of Tokyo", "Nidavellir",
    "Mind MGMT", "Camel Up", "Sleeping Gods",
    "Sky Team", "MicroMacro: Crime City", "Scythe",
    "Century: Golem Edition", "Dune Imperium", "Viticulture",
    "El Grande", "Turing Machine", "Great Western Trail",
    "Gloomhaven: Jaws of the Lion", "Dwellings of Eldervale",
    "Splendor Duel", "So Clover!", "Cockroach Poker",
    "Food Chain Magnate", "Finca", "Fort", "The Red Cathedral",
    "Inis", "Beyond the Sun", "Heroscape: Age of Annihilation",
    "Hanamikoji", "Mycelia", "Acquire", "Finspan",
    "Dune: The Board Game", "Spirit Island",
    "Planet Unknown", "Cubitos", "Roll for the Galaxy",
    "Caldera Park", "EOS: Island of Angels", "Pandemic",
    "Botanicus", "Jump Drive", "Spots", "Radlands",
    "Under Falling Skies", "War of the Worlds: The New Wave",
    "Imperium: Classics", "Eclipse: Second Dawn for the Galaxy",
    "Sagrada", "Libertalia: Winds of Galecrest",
    "Canvas", "Deception: Murder in Hong Kong", "Ahoy",
    "Resist!", "Salton Sea", "Galactic Cruise",
    "No Thanks!", "Forbidden Jungle", "Mille Fiori",
    "Black Forest", "Fit to Print", "Hickory Dickory",
    "Long Shot: The Dice Game", "Unconscious Mind",
    "River of Gold", "Circus Flohcati",
    "Star Trek: Captain's Chair", "River Valley Glassworks",
    "Evenfall", "Fromage", "Legacy of Yu",
    "Scholars of the South Tigris", "Revive",
    "Lure", "Daitoshi", "Akropolis",
    "Monster Hunter World: The Board Game",
    "Moon Colony Bloodbath", "Dreadful Meadows",
    "Mythwind", "Bomb Busters",
]

# ── Amazon Best Sellers in Board Games (Feb 2026, top 100) ──────────────
# Extracted game names from verbose Amazon product titles

AMAZON_GAMES = [
    "Connect 4", "Candy Land", "Trouble", "Sorry!", "Wavelength",
    "Tapple", "Monopoly", "Hues and Cues", "Scrabble", "Catan",
    "Don't Break the Ice", "Twister", "Codenames", "Battleship",
    "Sequence", "Blank Slate", "I Should Have Known That!",
    "The Chameleon", "Zingo", "Herd Mentality",
    "Ticket to Ride", "Azul", "Guess Who?",
    "Telestrations", "Wingspan", "One Night Ultimate Werewolf",
    "Pictionary", "Qwirkle", "Clue", "Sky Team",
    "Game of Life", "Blokus", "Taboo",
    "Hungry Hungry Hippos", "Monopoly: Pokemon Edition",
    "Jenga", "Operation", "Tenzi", "Carcassonne",
    "You Can't Say Umm", "First to Worst",
    "Brick Like This", "Hedbanz", "Outfoxed",
    "Pretty Pretty Princess", "Catch Phrase",
    "Match Madness", "Ticket to Ride: First Journey",
    "Super Skills", "Catan 5-6 Player Extension",
    "Scrabble Junior", "Rock Em Sock Em Robots",
    "UNO Flip", "Skip-Bo", "Murder Mystery Party",
]

# ── Walmart Board Games (Feb 2026) ──────────────
# Filtered to actual board games from their "Games & Puzzles" category

WALMART_GAMES = [
    "Don't Break the Ice", "Jenga", "Operation",
    "Monopoly", "Catan", "Hedbanz",
    "Hungry Hungry Hippos", "Rock Em Sock Em Robots",
    "Tenzi", "Simon", "Tower Stack Game",
    "UNO Flip", "Skip-Bo", "Greedy Granny",
    "Jurassic World Ravenous Raptors", "Murder Mystery Party",
]


def clean_name(name: str) -> str:
    """Normalize a game name for fuzzy matching."""
    name = re.sub(r'\s*\(.*?\)\s*', ' ', name)  # remove parentheticals
    name = re.sub(r'\s*by\s+.*$', '', name, flags=re.IGNORECASE)  # remove "by Author"
    name = re.sub(r'\s*[-–—:]\s*(B&N|Target).*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\bEXIT:\s*The Game\s*[-–—]\s*', 'EXIT: ', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def normalize_for_match(name: str) -> str:
    """Further normalize for comparison."""
    name = clean_name(name)
    name = name.lower()
    name = re.sub(r'[^a-z0-9 ]', '', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name


def is_board_game(name: str) -> bool:
    """Filter out non-board-game items."""
    skip_patterns = [
        r'plush', r'playing cards?$', r'rubik', r'puzzle cube',
        r'brainteaser', r'dice set', r'folio', r'spellbook',
        r'bingo$', r'chess & checkers', r'^uno\b',
        r'kanoodle', r'iq fit', r'icosa',
    ]
    lower = name.lower()
    return not any(re.search(p, lower) for p in skip_patterns)


def load_master_list(path: Path) -> set[str]:
    """Load master_list.csv and return normalized names."""
    names = set()
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get('name', '').strip()
            if name:
                names.add(normalize_for_match(name))
    return names


def fuzzy_match(name: str, master_names: set[str]) -> tuple[str, float] | None:
    """Check if name fuzzy-matches anything in master list.

    Uses a dynamic threshold: stricter for short names (which are prone
    to false positives) and slightly looser for long, distinctive names.
    """
    norm = normalize_for_match(name)
    if norm in master_names:
        return (norm, 1.0)

    # Dynamic threshold based on name length
    if len(norm) <= 6:
        threshold = 0.95  # very strict for short names (catan, risk, etc.)
    elif len(norm) <= 12:
        threshold = 0.88  # strict for medium names
    else:
        threshold = 0.82  # slightly looser for long distinctive names

    best_score = 0.0
    best_match = None
    for master in master_names:
        # Skip if lengths are wildly different (no point comparing)
        if abs(len(norm) - len(master)) > max(len(norm), len(master)) * 0.5:
            continue
        score = SequenceMatcher(None, norm, master).ratio()
        if score > best_score:
            best_score = score
            best_match = master

    if best_score >= threshold:
        return (best_match, best_score)
    return None


def main():
    project_root = Path(__file__).parent.parent
    master_path = project_root / 'master_list.csv'

    if not master_path.exists():
        print(f"ERROR: {master_path} not found")
        return

    master_names = load_master_list(master_path)
    print(f"Master list: {len(master_names)} games")

    # Combine all retailer data, deduplicate
    all_retailer = set()
    for source_list in [BN_SHOP_ALL, BN_STRATEGY, BN_FAMILY, BN_PARTY, TARGET_GAMES,
                        GAMENERDZ_GAMES, AMAZON_GAMES, WALMART_GAMES]:
        for name in source_list:
            if is_board_game(name):
                all_retailer.add(clean_name(name))

    print(f"Retailer games (after filtering): {len(all_retailer)}")
    print()

    # Find games NOT in our master list
    missing = []
    matched = []
    for name in sorted(all_retailer):
        result = fuzzy_match(name, master_names)
        if result:
            match, score = result
            matched.append((name, match, score))
        else:
            missing.append(name)

    print(f"Matched to master list: {len(matched)}")
    print(f"NOT in master list:     {len(missing)}")
    print()

    if missing:
        print("═" * 60)
        print("MISSING FROM MASTER LIST (potential additions)")
        print("═" * 60)
        for name in missing:
            print(f"  • {name}")

    print()
    print("═" * 60)
    print("MATCHED (already in master list)")
    print("═" * 60)
    for name, match, score in sorted(matched):
        if normalize_for_match(name) != match:
            print(f"  ✓ {name}  →  {match}  ({score:.0%})")
        else:
            print(f"  ✓ {name}")


if __name__ == '__main__':
    main()
