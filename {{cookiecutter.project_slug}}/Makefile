install:
	poetry install

collectstatic:
	cd src/ && ./manage.py collectstatic

migrate:
	cd src/ && ./manage.py migrate

lint:
	dotenv-linter src/app/.env.ci
	flake8 src
	cd src && mypy

check-no-dead-fixtures:
	cd src && pytest --dead-fixtures

test:
	cd src && pytest -x
