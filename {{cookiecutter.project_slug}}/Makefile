install:
	poetry install

collectstatic:
	cd src/ && ./manage.py collectstatic --no-input

migrate:
	cd src/ && ./manage.py migrate

lint-ci:
	dotenv-linter src/app/.env.ci

lint-python:
	cd src/ && flake8

check-no-dead-fixtures:
	cd src/ && pytest --dead-fixtures

check-type-annotations:
	cd src/ && mypy

test:
	cd src/ && pytest -x
