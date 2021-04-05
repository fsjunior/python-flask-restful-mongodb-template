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

test: clean
	poetry run pytest test
	poetry run pytest --dead-fixtures --dup-fixtures test

check-all: coverage
	pre-commit run --all-files

coverage: clean
	poetry run pytest --dead-fixtures --dup-fixtures test
	poetry run pytest test --cov --cov-fail-under=99 --cov-report=term-missing

coverage-update: coverage
	poetry run codecov

run-dev:
	poetry run python run.py

generate-migrations:
	pymongo-migrate generate -u $(MONGODB_URI) -m migrations
	echo "Migration template generated in 'migrations' directory. Please review the generated file."

apply-migrations:
	pymongo-migrate migrate -u $(MONGODB_URI) -m migrations

