import os
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = BASE_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

os.environ["DATABASE_URL"] = f"sqlite:///{BASE_DIR / 'test.db'}"
os.environ["TINYFISH_USE_MOCK"] = "true"

import pytest
from fastapi.testclient import TestClient

from app.db.init_db import init_db
from app.main import app


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    init_db()


@pytest.fixture
def client():
    return TestClient(app)
