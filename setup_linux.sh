#!/bin/sh
# Linux-only setup: create venv, install deps, and launch the assistant immediately
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

echo "Project directory: $PROJECT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 is not installed or not in PATH."
    exit 1
fi

if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "Creating virtual environment..."
    rm -rf "$VENV_DIR"
    python3 -m venv "$VENV_DIR"
    if [ ! -f "$VENV_DIR/bin/activate" ]; then
        echo "Failed to create virtual environment at $VENV_DIR."
        exit 1
    fi
fi

. "$VENV_DIR/bin/activate"
python3 -m pip install --upgrade pip
python3 -m pip install -r "$PROJECT_DIR/requirements.txt"

echo "Starting assistant..."
python3 "$PROJECT_DIR/main.py"

deactivate
