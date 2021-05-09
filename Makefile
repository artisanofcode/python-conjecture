# do any initial setup
setup:
	poetry install

# commands to run after git update
update:
	poetry install

# commands as run by CI
ci: lint
	HYPOTHESIS_PROFILE=slow poetry run pytest -vv --cov

# launch the interpreter in repl mode
repl:
	poetry run python

lint:
	poetry run isort --check-only .
	poetry run black --check .
	poetry run pydocstyle
	poetry run pylint src/conjecture
	poetry run pylint --disable=missing-function-docstring,duplicate-code tests
	poetry run mypy --strict  --pretty .

# run the tests  locally
test:
	poetry run pytest --testdox --cov --cov-report html

# automatically format codebase to pass linting rules
format:
	poetry run isort --atomic .
	poetry run black .

.PHONY: setup update ci repl test format