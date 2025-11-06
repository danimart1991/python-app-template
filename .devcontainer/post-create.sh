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
    else
        echo "  ℹ️  Host .gitconfig not available (this is normal for fresh clones)"
        echo "  → You can set your Git identity with:"
        echo "     git config --global user.name 'Your Name'"
        echo "     git config --global user.email 'your@email.com'"
    fi
fi

if [ -n "$(git config --global user.name)" ]; then
    echo "  ✅ Git user.name: $(git config --global user.name)"
else
    echo "  ⚠️  Git user.name not found"
fi

if [ -n "$(git config --global user.email)" ]; then
    echo "  ✅ Git user.email: $(git config --global user.email)"
else
    echo "  ⚠️  Git user.email not found"
fi

# Configure editor (safe to always set)
git config --global core.editor 'code --wait'

# Mark workspace as safe directory
git config --global --add safe.directory "${PWD}"

# Configure SSH for GitHub if keys are mounted from host (skip in Codespaces)
if [ -z "${CODESPACES}" ] && [ -d "$HOME/.ssh-host" ] && [ -n "$(ls -A "$HOME/.ssh-host" 2>/dev/null)" ]; then
    echo "🔑 Configuring SSH keys from host..."
    mkdir -p "$HOME/.ssh"
    cp -r "$HOME/.ssh-host/"* "$HOME/.ssh/" 2>/dev/null || true
    chmod 700 "$HOME/.ssh"
    chmod 600 "$HOME/.ssh/"id_* 2>/dev/null || true
    chmod 644 "$HOME/.ssh/"*.pub 2>/dev/null || true
    chmod 644 "$HOME/.ssh/known_hosts" 2>/dev/null || true
    chmod 600 "$HOME/.ssh/config" 2>/dev/null || true
    echo "  ✅ SSH keys configured"
else
    if [ -z "${CODESPACES}" ]; then
        echo "  ℹ️  No SSH keys found in host (this is normal if you use HTTPS)"
    fi
fi

if command -v gh &> /dev/null; then
    echo "🔑 Checking GitHub CLI authentication..."
    if gh auth status &> /dev/null; then
        echo "  ✅ GitHub CLI authenticated"
    else
        echo "  ℹ️  GitHub CLI not authenticated"
        if [ -n "${CODESPACES}" ]; then
            echo "  → Run 'gh auth login' to authenticate"
        else
            echo "  → Run 'gh auth login' to authenticate (optional)"
        fi
    fi
fi

echo "📦 Installing Python dependencies with Poetry..."
poetry install

echo "📂 Ensuring the virtual environment is activated and detected by VS Code..."
VENV_PATH="$(poetry env info --path)"
echo "  → Virtual environment path: ${VENV_PATH}"

echo "🐍 Verifing pytest is installed..."
if poetry run python -c "import pytest" 2>/dev/null; then
    echo "  ✅ pytest is available in the virtual environment"
else
    echo "  ⚠️  pytest not found, check your dependencies"
fi

echo "🪝 Installing pre-commit hooks..."
if [ -d ".git" ]; then
    poetry run pre-commit install
    echo "✅ Pre-commit hooks installed successfully"
else
    echo "⚠️  Warning: Not a git repository, skipping pre-commit installation"
fi

echo "✨ Dev container setup complete!"
