###############################################################################
# Environment
###############################################################################

.PHONY: venv init update install-dev install-prod git-hooks update-deps compile-deps

venv:
	pyenv virtualenv 3.9.1 {{cookiecutter.project_repository}}
	pyenv local {{cookiecutter.project_repository}}

init: install-dev git-hooks

update: update-deps install-dev

install-dev:
	python -m pip install --no-deps --upgrade pip setuptools wheel
	python -m pip install --no-deps --editable .
	python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt  --requirement requirements-dev.txt

install-prod:
	python -m pip install --no-deps --upgrade pip setuptools wheel
	python -m pip install --no-deps .
	python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt

git-hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push

update-deps:
	python -m pip install --upgrade pip setuptools wheel pip-tools
	python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements.in
	python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements-dev.in
	pre-commit autoupdate --freeze

compile-deps:
	python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements.in
	python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements-dev.in


###############################################################################
# Code
###############################################################################

.PHONY: test coverage report lint

test: lint
	pytest --cov --cov-report term-missing

coverage:
	pytest --cov --cov-report term-missing --cov-report html

report: coverage
	firefox htmlcov/index.html

lint:
	mypy .
	@#black . --check
	flake8 .
	@#isort . --check-only --diff
