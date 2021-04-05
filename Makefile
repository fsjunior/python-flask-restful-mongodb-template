.PHONY: generate-migrations
include .env
export

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f .coverage.NB-SBDEV*

check-lint:
	poetry run isort app --check-only
	poetry run flake8 app
	poetry run black app --check --line-length 120

fix-lint:
	poetry run isort app
	poetry run black app --line-length 120
	poetry run flake8 app

check-typing:
	poetry run mypy app

check-security:
	poetry run bandit --ini setup.cfg

test: clean
	poetry run pytest test
	poetry run pytest --dead-fixtures --dup-fixtures test

coverage: clean
	poetry run pytest --dead-fixtures --dup-fixtures test
	poetry run pytest test --cov --cov-fail-under=99 --cov-report=term-missing

coverage-update: coverage
	poetry run codecov

check-all: check-lint check-typing check-security coverage

run-dev:
	poetry run python run.py

generate-migrations:
	pymongo-migrate generate -u $(MONGODB_URI) -m migrations
	echo "Migration template generated in 'migrations' directory. Please review the generated file."

migrate-dev:
	pymongo-migrate migrate -u $(MONGODB_URI) -m migrations
