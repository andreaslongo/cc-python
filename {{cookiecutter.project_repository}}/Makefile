###############################################################################
# Project
###############################################################################

.PHONY: venv
venv:
	pyenv virtualenv 3.9.5 {{cookiecutter.project_repository}}
	pyenv local {{cookiecutter.project_repository}}


.PHONY: init
init: _install_development _install_git_hooks
	# Generate project config files
	# TODO: Include in initial commit (don't rely on cookiecutter?)
	nitpick --offline fix


.PHONY: _install_development
_install_development:
	python -m pip install --no-deps --upgrade pip setuptools wheel
	python -m pip install --no-deps --editable .
	python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt  --requirement requirements-dev.txt


.PHONY: _install_git_hooks
_install_git_hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push


.PHONY: update
update: _update_dependencies _install_development


.PHONY: _update_dependencies
_update_dependencies:
	python -m pip install --upgrade pip setuptools wheel pip-tools
	python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements.in
	python -m piptools compile --upgrade --allow-unsafe --build-isolation --generate-hashes requirements-dev.in
	pre-commit autoupdate --freeze


.PHONY: install
install: _install_production


.PHONY: _install_production
_install_production:
	python -m pip install --no-deps --upgrade pip setuptools wheel
	python -m pip install --no-deps .
	python -m pip install --require-hashes --no-deps --upgrade --requirement requirements.txt


.PHONY: compile_dependencies
compile_dependencies:
	python -m pip install --upgrade pip setuptools wheel pip-tools
	python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements.in
	python -m piptools compile --allow-unsafe --build-isolation --generate-hashes requirements-dev.in


.PHONY: clean
clean:
	rm -rf .cache
	rm -rf __pycache__
	rm -rf test/__pycache__
	rm -rf src/{{cookiecutter.project_slug}}/__pycache__

###############################################################################
# Code
###############################################################################

.PHONY: test
test:
	pytest


.PHONY: report
report:
	pytest --cov-report html:.cache/coverage-report
	firefox .cache/coverage-report/index.html


.PHONY: lint
lint:
	nitpick --offline check
	mypy .
	flake8 .
	black . --check --diff --color --experimental-string-processing
	@#isort . --check-only --diff
