#!/bin/sh -e

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place src --exclude=__init__.py
isort src --profile black
black src
mypy src