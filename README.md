# Doebus Django Template

I use this repository as a starter modern API Django template in my projects. This repository is forked from [@fandsdev/django](https://github.com/fandsdev/django) and was originally created by [@f213.](https://github.com/f213)

## What’s inside

* [Flake8](https://flake8.pycqa.org/en/latest/) (`.flake8`) for linting, lots of plugins included
* [Isort](https://pycqa.github.io/isort/) (`.isort.cfg`) to sort import statements
* [Django Rest Framework](https://www.django-rest-framework.org/) with JWT support
* [Poetry](https://python-poetry.org) (`pyproject.toml`) to manage dependencies
* [Celery](https://docs.celeryq.dev/en/stable/) to run background tasks
* Multiple settings sections using [django-split-settings](https://github.com/wemake-services/django-split-settings)
* Checking for stale fixtures with [pytest-dead-fixtures](https://github.com/jllorencetti/pytest-deadfixtures)
* A tool that makes custom migration names mandatory (`app.management.commands.makemigrations`)
* Postgres as local development DB
* RabbitMQ as local Celery message broker

## How to install

1. [Install Poetry.](https://python-poetry.org/docs/#installation)

2. [Install Cookiecutter.](https://cookiecutter.readthedocs.io/en/stable/installation.html)

3. [Install Docker and Docker Compose.](https://docs.docker.com/get-docker/)

4. Open up a background terminal and run `docker-compose up postgres redis rabbitmq`

5. Run the following command: `cookiecutter gh:vsevolod-skripnik/doebus-django`
