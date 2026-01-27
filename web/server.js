const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const cors = require('cors');
const sharp = require('sharp');
const yamlHandler = require('./lib/yaml-handler');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Configure multer for file uploads (store in memory)
const upload = multer({
  storage: multer.memoryStorage(),
  limits: {
    fileSize: 20 * 1024 * 1024 // 20MB limit
  },
  fileFilter: (req, file, cb) => {
    const allowedMimes = ['image/jpeg', 'image/png', 'image/webp'];
    const allowedExts = ['.jpg', '.jpeg', '.png', '.webp'];

    const ext = path.extname(file.originalname).toLowerCase();
    const mime = file.mimetype.toLowerCase();

    if (allowedMimes.includes(mime) && allowedExts.includes(ext)) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type. Only JPG, PNG, WEBP allowed.'));
    }
  }
});

// ============ API Endpoints ============

/**
 * GET /api/games
 * Return all games with metadata and image status
 */
app.get('/api/games', async (req, res) => {
  try {
    const games = await yamlHandler.loadAllGames();
    res.json(games);
  } catch (err) {
    console.error('Error fetching games:', err);
    res.status(500).json({
      error: true,
      message: 'Failed to load games',
      code: 'LOAD_ERROR'
    });
  }
});

/**
 * GET /api/games/:id
 * Return single game details
 */
app.get('/api/games/:id', async (req, res) => {
  try {
    const game = await yamlHandler.getGameById(req.params.id);

    if (!game) {
      return res.status(404).json({
        error: true,
        message: 'Game not found',
        code: 'NOT_FOUND'
      });
    }

    // Add image URL if exists
    const imageUrl = await yamlHandler.getImageUrl(req.params.id);
    res.json({ ...game, image_url: imageUrl });
  } catch (err) {
    console.error('Error fetching game:', err);
    res.status(500).json({
      error: true,
      message: 'Failed to load game',
      code: 'LOAD_ERROR'
    });
  }
});

/**
 * POST /api/games/:id/upload
 * Upload image for a specific game
 * Image will be named: {Game Name} ({Year}).{ext}
 */
app.post('/api/games/:id/upload', upload.single('image'), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({
        error: true,
        message: 'No file provided',
        code: 'NO_FILE'
      });
    }

    // Get game metadata
    const game = await yamlHandler.getGameById(req.params.id);
    if (!game) {
      return res.status(404).json({
        error: true,
        message: 'Game not found',
        code: 'NOT_FOUND'
      });
    }

    // Validate image with sharp
    try {
      const metadata = await sharp(req.file.buffer).metadata();

      // Warn if dimensions are small
      if (metadata.width < 500 || metadata.height < 500) {
        console.warn(
          `Image for ${game.name} is small: ${metadata.width}x${metadata.height}px`
        );
      }
    } catch (err) {
      return res.status(400).json({
        error: true,
        message: 'Invalid image file',
        code: 'INVALID_IMAGE'
      });
    }

    // Generate filename from game metadata
    const ext = path.extname(req.file.originalname).toLowerCase();
    const filename = `${game.name} (${game.year})${ext}`;

    // Sanitize filename (prevent path traversal)
    const sanitized = filename.replace(/[^a-zA-Z0-9\s().-]/g, '_');
    const filepath = path.join(yamlHandler.IMAGES_DIR, sanitized);

    // Write file to disk
    fs.writeFileSync(filepath, req.file.buffer);

    // Clear cache so next request reflects new image
    yamlHandler.clearCache();

    res.json({
      success: true,
      filename: sanitized,
      path: `/api/images/${encodeURIComponent(sanitized)}`,
      message: 'Image uploaded successfully'
    });
  } catch (err) {
    console.error('Error uploading image:', err);
    res.status(500).json({
      error: true,
      message: 'Failed to upload image',
      code: 'UPLOAD_ERROR',
      details: err.message
    });
  }
});

/**
 * GET /api/images/:filename
 * Serve images from the images directory
 */
app.get('/api/images/:filename', (req, res) => {
  try {
    const filename = decodeURIComponent(req.params.filename);
    const filepath = path.join(yamlHandler.IMAGES_DIR, filename);

    // Prevent path traversal
    const normalized = path.normalize(filepath);
    if (!normalized.startsWith(yamlHandler.IMAGES_DIR)) {
      return res.status(403).json({
        error: true,
        message: 'Access denied',
        code: 'ACCESS_DENIED'
      });
    }

    // Check if file exists
    if (!fs.existsSync(filepath)) {
      return res.status(404).json({
        error: true,
        message: 'Image not found',
        code: 'NOT_FOUND'
      });
    }

    // Send file with appropriate content type
    res.sendFile(filepath);
  } catch (err) {
    console.error('Error serving image:', err);
    res.status(500).json({
      error: true,
      message: 'Failed to serve image',
      code: 'SERVE_ERROR'
    });
  }
});

/**
 * GET /api/health
 * Health check endpoint
 */
app.get('/api/health', async (req, res) => {
  try {
    const games = await yamlHandler.loadAllGames();
    res.json({
      status: 'healthy',
      games_loaded: games.length,
      images_directory: yamlHandler.IMAGES_DIR
    });
  } catch (err) {
    res.status(500).json({
      status: 'unhealthy',
      error: err.message
    });
  }
});

// ============ Error Handling ============

app.use((err, req, res, next) => {
  console.error('Error:', err);

  if (err instanceof multer.MulterError) {
    if (err.code === 'FILE_TOO_LARGE') {
      return res.status(400).json({
        error: true,
        message: 'File too large. Maximum 20MB allowed.',
        code: 'FILE_TOO_LARGE'
      });
    }
  }

  if (err.message && err.message.includes('Invalid file type')) {
    return res.status(400).json({
      error: true,
      message: err.message,
      code: 'INVALID_FILE_TYPE'
    });
  }

  res.status(500).json({
    error: true,
    message: 'Internal server error',
    code: 'INTERNAL_ERROR'
  });
});

// ============ Server Start ============

app.listen(PORT, () => {
  console.log(`
╔════════════════════════════════════════════════════════════╗
║  Board Game Database - Web Interface                       ║
╚════════════════════════════════════════════════════════════╝

Server running at http://localhost:${PORT}

Instructions:
  1. Open browser to http://localhost:${PORT}
  2. Drag images onto game cards
  3. Images will be saved to: ${yamlHandler.IMAGES_DIR}

API Endpoints:
  GET    /api/games              - List all games
  GET    /api/games/:id          - Get single game
  POST   /api/games/:id/upload   - Upload image for game
  GET    /api/images/:filename   - Serve image
  GET    /api/health             - Health check

Press Ctrl+C to stop the server
  `);
});
