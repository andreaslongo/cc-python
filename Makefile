.PHONY: init
init: _install-git-hooks


.PHONY: _install-git-hooks
_install-git-hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push


.PHONY: update
update: _update-dependencies


.PHONY: _update-dependencies
_update-dependencies:
	pre-commit autoupdate --freeze
