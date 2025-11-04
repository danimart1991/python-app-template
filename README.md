# Python App Template

[![CI/CD](https://github.com/yourusername/python-app-template/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/yourusername/python-app-template/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-2.0+-blue.svg)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A modern Python application template with Poetry, Ruff, Pytest, pre-commit hooks, and CI/CD. Perfect starting point for APP tools, APIs, or any Python project.

## Quick Start

```bash
# Use as template on GitHub (click "Use this template")
# Or clone
git clone https://github.com/yourusername/python-app-template.git my-project
cd my-project

# Customize the project (see "Customization" section below)
# Then install
poetry install

# Run the app
poetry run my-app --text "Hello World"
```

## Features

- ✅ Modern Python application with argparse
- ✅ Poetry for dependency management
- ✅ Ruff for linting and formatting (replaces black, isort, flake8)
- ✅ Pytest with 80% coverage requirement
- ✅ Pre-commit hooks with 17 checks (including security)
- ✅ GitHub Actions CI/CD (PR validation + main execution)
- ✅ Trunk-based development workflow
- ✅ Dev Container support (Docker + Codespaces)
- ✅ Automated dependency updates (Dependabot)

## Requirements

- Python 3.11+
- Poetry 2.0+
- (Optional) Docker Desktop for devcontainer

## Installation

### Option 1: Using Poetry (local development)

```bash
poetry install
poetry run pre-commit install  # Enable git hooks
```

### Option 2: Development Container (recommended for multi-machine/Codespaces)

**Prerequisites:**

- VS Code with "Dev Containers" extension
- Docker Desktop (for local) OR GitHub Codespaces (cloud)

**Usage:**

1. Open the project in VS Code
2. Press `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
3. Wait for the container to build (first time: ~2-3 minutes)
4. Everything is pre-configured: Python, Poetry, pre-commit, extensions

**Benefits:**

- ✅ Same environment on Windows, Mac, Linux, and Codespaces
- ✅ No need to install Python or Poetry on your machine
- ✅ Isolated from your system
- ✅ Instant setup on new machines

```bash
# Inside the container, everything is ready:
poetry run pytest
poetry run my-app --help
```

## Customization

After cloning/using this template, customize it for your project:

1. **Update `pyproject.toml`:**

   - Change `name = "python-app-template"` to your project name
   - Update `description`, `authors`, `repository`, `homepage`
   - Update `keywords` to match your project
   - Rename script: `my-app = "src.main:main"` → `your-app = "src.main:main"`

2. **Update code files:**

   - `src/main.py`: Implement your application logic (update `__version__` if needed)
   - `tests/test_*.py`: Update tests for your functionality

3. **Update documentation:**

   - `README.md`: Replace with your project details
   - `CONTRIBUTING.md`: Update command examples
   - `CHANGELOG.md`: Start fresh with your version 0.1.0

4. **Reinstall:**
   ```bash
   poetry install
   ```

## Usage

```bash
# Show help
poetry run my-app --help

# Show version
poetry run my-app --version

# Process text
poetry run my-app --text "Your text here"

# Or activate shell
poetry shell
my-app --text "Your text here"
```

## Development

### Running Tests

```bash
# All tests
poetry run pytest

# With coverage
poetry run pytest --cov=src --cov-report=term-missing

# Only unit tests
poetry run pytest -m unit

# Only integration tests
poetry run pytest -m integration
```

### Code Quality

```bash
# Lint and format (automatic fix)
poetry run ruff check --fix src tests
poetry run ruff format src tests

# Run all pre-commit checks
poetry run pre-commit run --all-files

# Validate Poetry config
poetry check
```

### Pre-commit Hooks

Pre-commit runs automatically on every commit and includes:

- File formatting checks (whitespace, EOF, etc.)
- YAML/JSON/TOML validation
- Python syntax validation
- Ruff linting and formatting
- GitHub Actions security analysis (zizmor)
- Poetry configuration validation
- Full test suite with 80% coverage

If a check fails, fix the issues and commit again. Pre-commit will auto-fix some issues (like formatting).

## Project Structure

```
python-app-template/
├── .devcontainer/           # Dev container config (Docker)
├── .github/
│   ├── workflows/
│   │   ├── ci-cd.yml        # PR validation
│   │   └── run-app.yml      # Main branch execution
│   └── dependabot.yml       # Dependency updates
├── .vscode/                 # VS Code configuration
├── src/
│   ├── main.py              # Main entry point
│   └── py.typed             # Type hints marker
├── tests/
│   ├── test_main.py         # Unit tests
│   └── test_integration.py  # Integration tests
├── .pre-commit-config.yaml  # Pre-commit hooks
├── pyproject.toml           # Project config
├── CONTRIBUTING.md          # Development guide
└── CHANGELOG.md             # Version history
```

## Workflows

### Trunk-Based Development

This project follows trunk-based development:

- One main branch: `main`
- Short-lived feature branches for PRs
- Fast integration (daily merges)

**Workflow:**

```bash
# 1. Create branch from main
git checkout main && git pull
git checkout -b yourname/short-description

# 2. Make changes (pre-commit validates automatically)
git add .
git commit -m "feat: description"

# 3. Push and create PR to main
git push origin yourname/short-description

# 4. After merge, clean up
git checkout main && git pull
git branch -d yourname/short-description
```

### CI/CD

**PR Workflow** (`.github/workflows/ci-cd.yml`):

- Triggers on PRs to `main`
- Runs all pre-commit hooks
- Validates application functionality
- Must pass before merge

**Main Workflow** (`.github/workflows/run-app.yml`):

- Triggers on push to `main`
- Installs production dependencies only
- Executes the application
- Manual trigger available

### Dependabot

Automated dependency updates run weekly (Mondays at 9:00 AM):

- Python packages (pip ecosystem)
- GitHub Actions versions

Pull requests are automatically created with:

- 5 max concurrent PRs per ecosystem
- CI validation before merge
- Labels: `dependencies`, `python`, `github-actions`

## VS Code Integration

Included configuration:

- Python interpreter setup
- Ruff as default formatter
- Debug configurations
- Task runner for common commands
- Recommended extensions

**Available tasks** (Ctrl+Shift+P → "Tasks: Run Task"):

- Run Application
- Run Tests
- Run Tests with Coverage
- Lint Code
- Format Code
- Install Dependencies

## Troubleshooting

### Pre-commit fails on first run

```bash
# Pre-commit downloads tools on first run
poetry run pre-commit run --all-files
```

### Poetry lock file out of sync

```bash
poetry lock --no-update
poetry install
```

### Tests fail locally but pass in CI

```bash
# Ensure you have the latest dependencies
poetry install --sync
```

### Import errors

```bash
# Reinstall project in editable mode
poetry install
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Development workflow
- Code standards
- Commit message format
- PR process
- Testing requirements

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- **Repository**: [GitHub](https://github.com/yourusername/python-app-template)
- **Issues**: [GitHub Issues](https://github.com/yourusername/python-app-template/issues)
- **Changelog**: [CHANGELOG.md](CHANGELOG.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
