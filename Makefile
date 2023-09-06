install:
	poetry install

lint:
	poetry run flake8 server --exclude=migrations,server/settings.py

start:
	poetry run python manage.py runserver 127.0.0.1:8000

test:
	poetry run python manage.py test

test_coverage:
	poetry run coverage run --source='server' manage.py test
	poetry run coverage xml
	poetry run coverage report