SHELL := /bin/bash
MAX_LINE_LENGTH := 119
POETRY_VERSION := $(shell poetry --version 2>/dev/null)

help: ## List all commands
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9 -]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check-poetry:
	@if [[ "${POETRY_VERSION}" == *"Poetry"* ]] ; \
	then \
		echo "Found ${POETRY_VERSION}, ok." ; \
	else \
		echo 'Please install poetry first, with e.g.:' ; \
		echo 'make install-poetry' ; \
		exit 1 ; \
	fi

install-poetry: ## install or update poetry
	@if [[ "${POETRY_VERSION}" == *"Poetry"* ]] ; \
	then \
		echo 'Update poetry v$(POETRY_VERSION)' ; \
		poetry self update ; \
	else \
		echo 'Install poetry' ; \
		curl -sSL "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" | python3 ; \
	fi

install: check-poetry ## install DragonPy via poetry
	poetry install

update: check-poetry ## Update the dependencies as according to the pyproject.toml file
	poetry update

lint: ## Run code formatters and linter
	poetry run flynt --fail-on-change --line_length=${MAX_LINE_LENGTH} dragonpy
	poetry run isort --check-only --recursive dragonpy
	poetry run flake8 dragonpy

fix-code-style: ## Fix code formatting
	poetry run flynt --line_length=${MAX_LINE_LENGTH} dragonpy
	poetry run autopep8 --ignore-local-config --max-line-length=${MAX_LINE_LENGTH} --aggressive --aggressive --in-place --recursive dragonpy
	poetry run isort --apply --recursive dragonpy

tox-listenvs: check-poetry ## List all tox test environments
	poetry run tox --listenvs

tox: check-poetry ## Run pytest via tox with all environments
	poetry run tox

tox-py36: check-poetry ## Run pytest via tox with *python v3.6*
	poetry run tox -e py36

tox-py37: check-poetry ## Run pytest via tox with *python v3.7*
	poetry run tox -e py37

tox-py38: check-poetry ## Run pytest via tox with *python v3.8*
	poetry run tox -e py38

pytest: check-poetry ## Run pytest
	poetry run pytest

update-rst-readme: ## update README.rst from README.creole
	poetry run update_rst_readme

publish: ## Release new version to PyPi
	poetry run publish

download-roms:  ## Download/Test only ROM files
	poetry run DragonPy download-roms

profile:  ## Profile the MC6809 emulation benchmark
	poetry run MC6809 profile

benchmark:  ## Run MC6809 emulation benchmark
	poetry run MC6809 benchmark

editor: check-poetry  ## Run only the BASIC editor
	poetry run DragonPy editor

Vectrex: check-poetry  ## Run GUI with Vectrex emulation (not working, yet!)
	poetry run DragonPy --machine Vectrex run

sbc09: check-poetry  ## Run GUI with sbc09 ROM emulation
	poetry run DragonPy --machine sbc09 run

Multicomp6809: check-poetry  ## Run GUI with Multicomp6809 ROM emulation
	poetry run DragonPy --machine Multicomp6809 run

Simple6809: check-poetry  ## Run GUI with Simple6809 ROM emulation
	poetry run DragonPy --machine Simple6809 run

CoCo2b: check-poetry  ## Run GUI with CoCo 2b emulation
	poetry run DragonPy --machine CoCo2b run

Dragon32: check-poetry  ## Run GUI with Dragon 32 emulation
	poetry run DragonPy --machine Dragon32 run

Dragon64: check-poetry  ## Run GUI with Dragon 64 emulation
	poetry run DragonPy --machine Dragon64 run

run: check-poetry ## *Run the DragonPy Emulator GUI*
	poetry run DragonPy

.PHONY: help install lint fix test publish