init: git-hooks

update: update-deps

git-hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push

update-deps:
	pre-commit autoupdate --freeze

.PHONY: init update git-hooks update-deps
