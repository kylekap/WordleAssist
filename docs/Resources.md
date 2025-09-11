# Overview of useful python resources & common commands

## Resources

- [PEP-8](https://realpython.com/python-pep8/)
- [Writing Structure](https://docs.python-guide.org/writing/structure/)
- [Google's Python Writing Guide](https://google.github.io/styleguide/pyguide.htm)

## Common Commands

### To create virtual environment

>py -m venv env

### To activate

>env\Scripts\activate

### To install

>py -m pip install .

### To install including development tags

>py -m pip install .[dev]

## Ruff

### Format all files in the current directory

>ruff format

### Format all files in `path/to/code` (and any subdirectories)

>ruff format path/to/code/

### Format a single file

>ruff format path/to/file.py

## Pre-commit

### Install

>pre-commit install

### Run

>pre-commit run --all-files

### Get it to autoupdate

>pre-commit autoupdate
