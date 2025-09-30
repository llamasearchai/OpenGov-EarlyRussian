# Makefile for OpenGov-EarlyRussian
# Author: Nik Jois <nikjois@llamasearch.ai>

.PHONY: help install test test-cov lint format type clean run demo docker-build docker-run all

help:
	@echo "OpenGov-EarlyRussian - Available Commands"
	@echo "=========================================="
	@echo "install      - Install package and dependencies"
	@echo "test         - Run test suite"
	@echo "test-cov     - Run tests with coverage report"
	@echo "lint         - Run code linting"
	@echo "format       - Format code with black"
	@echo "type         - Run type checking"
	@echo "clean        - Clean build artifacts"
	@echo "run          - Start API server"
	@echo "demo         - Run demo script"
	@echo "docker-build - Build Docker image"
	@echo "docker-run   - Run Docker container"
	@echo "all          - Run format, lint, type, and test"

install:
	@echo "Installing OpenGov-EarlyRussian..."
	python3 -m venv .venv || true
	. .venv/bin/activate && pip install -e ".[dev]"
	@echo "Installation complete!"

test:
	@echo "Running test suite..."
	. .venv/bin/activate && pytest -v

test-cov:
	@echo "Running tests with coverage..."
	. .venv/bin/activate && pytest --cov=opengov_earlyrussian --cov-report=term-missing --cov-report=html

lint:
	@echo "Running linter..."
	. .venv/bin/activate && ruff check opengov_earlyrussian tests || true

format:
	@echo "Formatting code..."
	. .venv/bin/activate && black opengov_earlyrussian tests examples

type:
	@echo "Running type checker..."
	. .venv/bin/activate && mypy opengov_earlyrussian tests || true

clean:
	@echo "Cleaning build artifacts..."
	rm -rf .venv
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache
	rm -rf htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + || true
	find . -type f -name "*.pyc" -delete
	@echo "Clean complete!"

run:
	@echo "Starting API server..."
	. .venv/bin/activate && uvicorn opengov_earlyrussian.api.main:app --reload --host 0.0.0.0 --port 8000

demo:
	@echo "Running demo..."
	chmod +x demo.sh
	. .venv/bin/activate && ./demo.sh

docker-build:
	@echo "Building Docker image..."
	docker build -t opengov-earlyrussian:latest .

docker-run:
	@echo "Running Docker container..."
	docker-compose up

all: format lint type test
	@echo "All checks passed!"

