from setuptools import setup, find_packages

setup(
    name="{{ cookiecutter.project_slug }}",
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
