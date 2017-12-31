build:
	docker-compose build simple-messenger

run-dev:
	ENV=dev docker-compose up -d

run:
	docker-compose up -d

clean:
	docker-compose down
