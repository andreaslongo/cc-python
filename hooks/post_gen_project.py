from shlex import split
from subprocess import run


if __name__ == "__main__":
    if "{{ cookiecutter.create_git_repository | lower }}" == "y":
        run(split("git init"))
        run(split("git remote add origin {{ cookiecutter.github_repository }}"))
        run(split("git add ."))
        run(split('git commit -m "Initial commit"'))

    if "{{ cookiecutter.install_git_hooks | lower }}" == "y":
        run(split("make _install_git_hooks"))

    if "{{ cookiecutter.create_python_virtual_environment | lower }}" == "y":
        run(split("make venv"))
