.PHONY: up down logs ps build restart

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

build:
	docker compose build

restart:
	docker compose restart
