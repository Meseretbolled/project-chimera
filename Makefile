# Project Chimera — Developer Commands

.PHONY: help install test demo docker-build docker-run

help:
	@echo "Available commands:"
	@echo "  make install       Install project locally"
	@echo "  make test          Run pytest suite"
	@echo "  make demo          Run Chimera pipeline demo"
	@echo "  make docker-build  Build Docker image"
	@echo "  make docker-run    Run tests inside Docker"

install:
	pip install -e .

test:
	pytest -v

demo:
	python demo/run_demo.py

docker-build:
	docker build -t chimera .

docker-run:
	docker run chimera
