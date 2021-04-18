.PHONY: init
init: _install_git_hooks


.PHONY: _install_git_hooks
_install_git_hooks:
	pre-commit install --install-hooks --hook-type pre-commit
	pre-commit install --install-hooks --hook-type pre-push


.PHONY: update
update: _update_dependencies


.PHONY: _update_dependencies
_update_dependencies:
	pre-commit autoupdate --freeze
