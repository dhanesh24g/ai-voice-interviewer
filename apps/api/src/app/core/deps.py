from collections.abc import Generator

from app.db.session import SessionLocal
from app.services.container import ServiceContainer, get_container


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_services() -> ServiceContainer:
    return get_container()
