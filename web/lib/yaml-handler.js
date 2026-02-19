const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const GAMES_DIR = path.join(__dirname, '../../games');
const IMAGES_DIR = path.join(__dirname, '../../images');
const SOURCES_LISTS_DIR = path.join(__dirname, '../../sources/lists');

let gamesCache = null;
let masterListCache = null;

/**
 * Load all game files from the games directory
 * Returns an array of game objects with metadata
 */
async function loadAllGames() {
  if (gamesCache) {
    return gamesCache;
  }

  try {
    const files = fs.readdirSync(GAMES_DIR).filter(f => f.endsWith('.yaml'));
    const games = [];

    for (const file of files) {
      try {
        const filePath = path.join(GAMES_DIR, file);
        const content = fs.readFileSync(filePath, 'utf8');
        const gameData = yaml.load(content);

        if (gameData && gameData.id) {
          // Check if image exists for this game
          const hasImage = checkImageExists(gameData);

          games.push({
            id: gameData.id,
            name: gameData.name,
            year: gameData.year,
            designer: gameData.designer || [],
            publisher: gameData.publisher || [],
            categories: gameData.categories || [],
            description: gameData.description,
            has_image: hasImage,
            playtime_minutes: gameData.playtime_minutes,
            min_age: gameData.min_age,
            possible_counts: gameData.possible_counts || [],
            true_counts: gameData.true_counts || [],
            rules_complexity: gameData.rules_complexity,
            strategic_depth: gameData.strategic_depth,
            feel: gameData.feel,
            length: gameData.length,
            value: gameData.value,
            affinity: gameData.affinity,
            hotness: gameData.hotness
          });
        }
      } catch (err) {
        console.error(`Error loading game file ${file}:`, err.message);
      }
    }

    // Sort by name
    games.sort((a, b) => a.name.localeCompare(b.name));
    gamesCache = games;
    return games;
  } catch (err) {
    console.error('Error loading games directory:', err.message);
    return [];
  }
}

/**
 * Get a single game by ID
 */
async function getGameById(gameId) {
  const games = await loadAllGames();
  return games.find(g => g.id === gameId);
}

/**
 * Check if an image exists for a game using naming convention
 * Images are named: {Game Name} ({Year}).{ext}
 */
function checkImageExists(gameData) {
  if (!gameData.name || !gameData.year) {
    return false;
  }

  try {
    const files = fs.readdirSync(IMAGES_DIR);
    const baseName = `${gameData.name} (${gameData.year})`;

    // Check for any file matching the pattern (case-insensitive)
    return files.some(file => {
      const nameWithoutExt = path.parse(file).name;
      return nameWithoutExt.toLowerCase() === baseName.toLowerCase();
    });
  } catch (err) {
    return false;
  }
}

/**
 * Get the expected image filename for a game
 */
function getExpectedImageFilename(gameData) {
  if (!gameData.name || !gameData.year) {
    return null;
  }

  try {
    const files = fs.readdirSync(IMAGES_DIR);
    const baseName = `${gameData.name} (${gameData.year})`;

    // Find matching file (case-insensitive)
    const matching = files.find(file => {
      const nameWithoutExt = path.parse(file).name;
      return nameWithoutExt.toLowerCase() === baseName.toLowerCase();
    });

    return matching || null;
  } catch (err) {
    return null;
  }
}

/**
 * Get image URL for a game
 */
async function getImageUrl(gameId) {
  const game = await getGameById(gameId);
  if (!game) {
    return null;
  }

  const filename = getExpectedImageFilename(game);
  if (!filename) {
    return null;
  }

  return `/api/images/${encodeURIComponent(filename)}`;
}

/**
 * Load all source lists and return merged master list with research status
 */
async function loadMasterList() {
  if (masterListCache) return masterListCache;

  try {
    const listFiles = fs.readdirSync(SOURCES_LISTS_DIR)
      .filter(f => f.endsWith('.yaml'))
      .sort();

    const gameMap = new Map(); // id -> {id, name, year, sources: []}

    for (const file of listFiles) {
      try {
        const filePath = path.join(SOURCES_LISTS_DIR, file);
        const content = fs.readFileSync(filePath, 'utf8');
        const listData = yaml.load(content);

        if (!listData || !Array.isArray(listData.games)) continue;

        const sourceName = listData.source || file;

        for (const game of listData.games) {
          if (!game.id) continue;

          if (!gameMap.has(game.id)) {
            gameMap.set(game.id, {
              id: game.id,
              name: game.name || game.id,
              year: game.year || null,
              sources: []
            });
          }

          const entry = gameMap.get(game.id);
          if (!entry.sources.includes(sourceName)) {
            entry.sources.push(sourceName);
          }
        }
      } catch (err) {
        console.error(`Error loading source list ${file}:`, err.message);
      }
    }

    // Check which games have been researched
    const existingGameIds = new Set(
      fs.readdirSync(GAMES_DIR)
        .filter(f => f.endsWith('.yaml'))
        .map(f => path.parse(f).name)
    );

    const games = Array.from(gameMap.values()).map(game => ({
      ...game,
      source_count: game.sources.length,
      researched: existingGameIds.has(game.id)
    }));

    // Sort by source count desc, then name asc
    games.sort((a, b) => {
      if (b.source_count !== a.source_count) return b.source_count - a.source_count;
      return a.name.localeCompare(b.name);
    });

    const result = {
      total: games.length,
      researched: games.filter(g => g.researched).length,
      games
    };

    masterListCache = result;
    return result;
  } catch (err) {
    console.error('Error loading master list:', err.message);
    return { total: 0, researched: 0, games: [] };
  }
}

/**
 * Clear the games cache (useful after file updates)
 */
function clearCache() {
  gamesCache = null;
  masterListCache = null;
}

module.exports = {
  loadAllGames,
  getGameById,
  loadMasterList,
  checkImageExists,
  getExpectedImageFilename,
  getImageUrl,
  clearCache,
  GAMES_DIR,
  IMAGES_DIR
};
