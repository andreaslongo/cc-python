from shlex import split
from subprocess import run


if __name__ == "__main__":
    if "yes" in "{{ cookiecutter.git_init|lower }}":
        run(split("git init"))
        run(split("git remote add origin {{ cookiecutter.github_repository }}"))
        run(split("git add ."))
        run(split('git commit -m "Initial commit"'))

    if "yes" in "{{ cookiecutter.git_hooks|lower }}":
        run(split("make git-hooks"))

    if "yes" in "{{ cookiecutter.create_venv|lower }}":
        run(split("make venv"))
