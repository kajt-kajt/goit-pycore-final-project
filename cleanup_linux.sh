#!/bin/sh
# Linux-only cleanup: remove venv and stored data
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

if [ -d "$VENV_DIR" ]; then
    echo "Removing virtual environment..."
    rm -rf "$VENV_DIR"
fi

if [ -f "$PROJECT_DIR/books.pkl" ]; then
    echo "Deleting books.pkl..."
    rm -f "$PROJECT_DIR/books.pkl"
fi

echo "Cleanup complete."
