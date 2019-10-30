all: help

help:
	@echo 'make up              bring up the servers'
	@echo 'make test            run tests and show coverage report'
	@echo 'make makemigrations'
	@echo 'make migrate'
	@echo 'make shell'
	@echo 'make build           rebuild the images'

up:
	docker-compose up -d

test:
	docker-compose run --rm django python manage.py test

makemigrations:
	docker-compose run --rm django python manage.py makemigrations

migrate:
	docker-compose run --rm django python manage.py migrate

shell:
	docker-compose run --rm django python manage.py shell

build:
	docker-compose build django
