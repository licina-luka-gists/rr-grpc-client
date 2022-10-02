#!make

.PHONY: up stop

up:
	docker-compose up --build -d
stop:
	docker-compose stop
