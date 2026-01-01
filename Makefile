.PHONY: help install test test-html lint format fix clean all \
	docker-build docker-test docker-test-html docker-shell docker-clean

help:
	@echo "Available commands:"
	@echo ""
	@echo "Local:"
	@echo "  make install        - Install dependencies with uv (including dev tools)"
	@echo "  make test           - Run Locust load tests (without HTML/CSV reports)"
	@echo "  make test-html      - Run Locust load tests with HTML and CSV reports"
	@echo "  make lint           - Run Ruff lint checks"
	@echo "  make format         - Format code with Ruff"
	@echo "  make fix            - Auto-fix lint issues and format code"
	@echo "  make clean          - Remove cache artifacts, reports, and logs"
	@echo "  make all            - Install, format, lint, and test (full workflow)"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build      - Build Docker image"
	@echo "  make docker-test       - Run load tests in Docker (without HTML/CSV reports)"
	@echo "  make docker-test-html  - Run load tests in Docker with HTML and CSV reports"
	@echo "  make docker-shell      - Open shell in Docker container"
	@echo "  make docker-clean      - Remove Docker containers and images"

install:
	uv sync

test:
	mkdir -p logs
	uv run python -m locust --config=config.yml

test-html:
	mkdir -p reports logs
	rm -rf reports/* 2>/dev/null || true
	uv run python -m locust --config=config.yml --html=reports/report.html --csv=reports/stats

lint:
	uv run ruff check data/ tests/ utils/ locustfile.py

format:
	uv run ruff format data/ tests/ utils/ locustfile.py

fix:
	uv run ruff check --fix data/ tests/ utils/ locustfile.py
	uv run ruff format data/ tests/ utils/ locustfile.py

all: install format lint test

clean:
	@echo "Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .ruff_cache
	rm -rf .vscode
	rm -rf reports
	rm -rf logs
	@echo "Cleanup complete!"

docker-build:
	mkdir -p logs
	docker compose build

docker-test:
	mkdir -p logs
	docker compose run --rm -v $(CURDIR)/logs:/app/logs -v $(CURDIR)/data:/app/data tests uv run python -m locust --config=config.yml

docker-test-html:
	mkdir -p reports logs
	rm -rf reports/* 2>/dev/null || true
	docker compose run --rm -v $(CURDIR)/logs:/app/logs -v $(CURDIR)/data:/app/data -v $(CURDIR)/reports:/app/reports -e HTML_REPORT=true tests sh -c "rm -rf reports/* 2>/dev/null || true && uv run python -m locust --config=config.yml --html=reports/report.html --csv=reports/stats"

docker-shell:
	mkdir -p logs
	docker compose run --rm -v $(CURDIR)/logs:/app/logs -v $(CURDIR)/data:/app/data tests /bin/bash

docker-clean:
	docker compose down --rmi local --volumes --remove-orphans || true
