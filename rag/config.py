from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent


DATA_DIR = ROOT_DIR / "data"
OFFICIAL_DOCS = DATA_DIR / "official_docs"
USER_UPLOADS = DATA_DIR / "user_uploads"


STORAGE_DIR = ROOT_DIR / "storage"
OFFICIAL_DB = STORAGE_DIR / "official_db"
SESSION_DB = STORAGE_DIR / "session_db"


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 5