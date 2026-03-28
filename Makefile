API_DIR=apps/api
WEB_DIR=apps/web

.PHONY: api-install api-dev api-test api-migrate api-lint

api-install:
	cd $(API_DIR) && pip install -e .[dev]

api-dev:
	cd $(API_DIR) && uvicorn app.main:app --app-dir src --reload

api-test:
	cd $(API_DIR) && python3 -m pytest

api-migrate:
	cd $(API_DIR) && alembic upgrade head

api-lint:
	cd $(API_DIR) && ruff check src tests

