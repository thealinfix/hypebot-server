.PHONY: run dev install test

install:
   pip install -r requirements.txt

dev:
   python -m src.main

test:
   pytest tests/

run:
   docker-compose -f infrastructure/docker/docker-compose.yml up
