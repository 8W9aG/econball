#!/bin/sh

set -e

echo "Formatting..."
echo "--- Ruff ---"
ruff format econball
echo "--- isort ---"
isort econball

echo "Checking..."
echo "--- Flake8 ---"
flake8 econball
echo "--- pylint ---"
pylint econball
echo "--- mypy ---"
mypy econball
echo "--- Ruff ---"
ruff check econball
echo "--- pyright ---"
pyright econball
