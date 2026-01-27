const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const GAMES_DIR = path.join(__dirname, '../../games');
const IMAGES_DIR = path.join(__dirname, '../../images');

let gamesCache = null;

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
 * Clear the games cache (useful after file updates)
 */
function clearCache() {
  gamesCache = null;
}

module.exports = {
  loadAllGames,
  getGameById,
  checkImageExists,
  getExpectedImageFilename,
  getImageUrl,
  clearCache,
  GAMES_DIR,
  IMAGES_DIR
};
