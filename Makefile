lint:
	flake8 app/
test:
	pytest -ra

prepare:
	make lint
	make test

run:
	sudo docker-compose up --build