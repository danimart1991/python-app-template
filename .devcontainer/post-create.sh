#!/bin/bash
set -e

echo "🔧 Configuring Git..."

if [ -n "${CODESPACES}" ]; then
    echo "  → Running in GitHub Codespaces"
else
    echo "  → Running in local Dev Container"
    if [ -f "$HOME/.gitconfig-host" ]; then
        echo "  → Importing Git configuration from host..."
        cp "$HOME/.gitconfig-host" "$HOME/.gitconfig" 2>/dev/null || true
        echo "  ✅ Git config imported from host"
    fi
fi

echo "  → Configuring editor..."
git config --global core.editor 'code --wait'

echo "  → Marking workspace as safe directory..."
git config --global --add safe.directory "${PWD}"

if [ -n "$(git config --global user.name)" ]; then
    echo "  ✅ Git user.name: $(git config --global user.name)"
else
    echo "  ⚠️  Git user.name not configured"
    echo "     → Set with: git config --global user.name 'Your Name'"
fi

if [ -n "$(git config --global user.email)" ]; then
    echo "  ✅ Git user.email: $(git config --global user.email)"
else
    echo "  ⚠️  Git user.email not configured"
    echo "     → Set with: git config --global user.email 'your@email.com'"
fi

echo ""
echo "📦 Poetry & Python"
echo "  → Configuring Poetry to create virtual environments inside the project..."
poetry config virtualenvs.in-project true
echo "  → Installing Python dependencies with Poetry..."
poetry install --with dev

echo "📂 Ensuring the virtual environment is activated and detected by VS Code..."
VENV_PATH="$(poetry env info --path)"
echo "  ✅ Virtual environment path: ${VENV_PATH}"

echo "🐍 Verifing pytest is installed..."
if poetry run python -c "import pytest" 2>/dev/null; then
    echo "  ✅ pytest is available in the virtual environment"
else
    echo "  ⚠️  pytest not found, check your dependencies"
fi

echo ""
echo "🪝 Installing pre-commit hooks..."
if [ -d ".git" ]; then
    poetry run pre-commit install
    echo "✅ Pre-commit hooks installed successfully"
else
    echo "⚠️  Warning: Not a git repository, skipping pre-commit installation"
fi

echo ""
echo "✨ Dev container setup complete!"
