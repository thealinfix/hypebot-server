.PHONY: help install dev prod test migrate clean

help:
	@echo "Available commands:"
	@echo "  install  - Install dependencies"
	@echo "  dev      - Run development server"
	@echo "  prod     - Run production server"
	@echo "  test     - Run tests"
	@echo "  migrate  - Run database migrations"
	@echo "  clean    - Clean up cache files"

install:
	pip install -r requirements.txt

dev:
	python -m src.main

prod:
	docker-compose -f infrastructure/docker/docker-compose.yml up

test:
	pytest tests/

migrate:
	alembic upgrade head

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
