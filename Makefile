# Project Chimera — Developer Commands

.PHONY: help setup install test demo docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make setup         Create environment + install deps (uv)"
	@echo "  make install       Install project locally"
	@echo "  make test          Run pytest suite"
	@echo "  make demo          Run Chimera pipeline demo"
	@echo "  make docker-build  Build Docker image"
	@echo "  make docker-run    Run tests inside Docker"

# Golden Environment Setup (Challenge Requirement)
setup:
	uv venv
	uv pip install -e .

install:
	uv pip install -e .

test:
	uv run pytest -v

demo:
	uv run python demo/run_demo.py

docker-build:
	docker build -t chimera .

docker-run:
	docker run chimera
