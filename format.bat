@echo off
py -m ruff check . --fix
py -m black .
echo Done.