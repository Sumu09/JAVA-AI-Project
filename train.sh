#!/usr/bin/env bash
# ==============================================================================
# Butterfly Species Classifier — Model Training Script
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================"
echo " Butterfly Species Classifier — Training Engine"
echo "================================================"

# Check if .venv exists, otherwise create it using uv
if [ ! -f ".venv/bin/python" ]; then
    echo "Virtual environment not found. Initializing .venv with Python 3.12..."
    if command -v uv >/dev/null 2>&1; then
        uv venv --python 3.12 .venv
        uv pip install --python .venv/bin/python tensorflow
    else
        echo "Error: .venv not found and 'uv' is not installed to create it."
        exit 1
    fi
fi

echo "Launching training pipeline..."
.venv/bin/python train_model.py "$@"
