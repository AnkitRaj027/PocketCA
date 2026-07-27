from pathlib import Path

# Root directory
ROOT_DIR = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = ROOT_DIR / "data"
OFFICIAL_DOCS = DATA_DIR / "official_docs"
USER_UPLOADS = DATA_DIR / "user_uploads"

# Vector database
STORAGE_DIR = ROOT_DIR / "storage"
OFFICIAL_DB = STORAGE_DIR / "official_db"
SESSION_DB = STORAGE_DIR / "session_db"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 5