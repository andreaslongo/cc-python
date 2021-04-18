from setuptools import setup, find_packages


setup(
    name="{{ cookiecutter.project_repository }}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3'
)
