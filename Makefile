.PHONY: init sync test lint format check run db

init:
	uv sync
	uv run pre-commit install

sync:
	uv sync --all-groups

test:
	uv run --group test pytest

lint:
	uv run ruff check --fix .

format:
	uv run ruff format .

check:
	uv run ruff check .
	uv run ruff format --check .
	uv run --group test pytest

run:
	uv run python src/french_verb_trainer/main.py