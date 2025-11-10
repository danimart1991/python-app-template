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

# Run with verbose logging
poetry run my-app -vv --text "Hello World"
```

## Features

- ✅ Modern Python application with Poetry dependency management
- ✅ Configurable logging levels (WARNING/INFO/DEBUG) with `-v` flags
- ✅ Flexible command-line interface with optional text processing
- ✅ Ruff for fast linting and formatting
- ✅ Pytest with 80% coverage requirement
- ✅ Pre-commit hooks with 17 automated checks
- ✅ GitHub Actions CI/CD workflow
- ✅ Dev Container support (Windows, Mac, Linux, Codespaces)
- ✅ Automated dependency updates (Dependabot)

## Requirements

**Local development:**

- Python 3.11+
- Poetry 2.0+

**Dev Container (optional but recommended):**

- VS Code with Dev Containers extension
- Docker OR GitHub Codespaces

## Installation

### Option 1: Using Poetry (local development)

```bash
poetry install
poetry run pre-commit install  # Enable git hooks
```

### Option 2: Development Container (recommended)

Open in VS Code → `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"

**Benefits:**

- ✅ Works on Windows, Mac, Linux, and GitHub Codespaces
- ✅ No local Python/Poetry installation needed
- ✅ Git authentication handled automatically by VS Code
- ✅ Everything pre-configured in ~2-3 minutes

> **Note:** When using Git inside the container, VS Code will handle authentication. Your Git credentials from the host are imported automatically.

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

# Process text (--text is optional, uses default text if not provided)
poetry run my-app --text "Your text here"

# Run without text argument (uses default)
poetry run my-app

# Verbose logging levels
poetry run my-app -v --text "text"     # INFO level
poetry run my-app -vv --text "text"    # DEBUG level
poetry run my-app --verbose --verbose --text "text"  # Same as -vv

# Or activate shell
poetry shell
my-app --text "Your text here"
my-app -vv  # Default text with DEBUG logging
```

### Logging Levels

The application supports different verbosity levels:

- **Default (no flag)**: WARNING level - shows only warnings and errors
- **`-v` or `--verbose`**: INFO level - shows informational messages
- **`-vv` or `--verbose --verbose`**: DEBUG level - shows detailed debug information

The `-v/--verbose` flag can be combined with any action (`--text`, `--version`, `--help`).

**Log format**: `YYYY-MM-DD HH:MM:SS,mmm - logger_name - LEVEL - message`

**Example output**:
```
$ poetry run my-app -v --text "Hello"
2025-11-10 12:00:00,000 - root - INFO - Processing text: Hello
Hello
```

### Command-Line Arguments

The application accepts one of these mutually exclusive actions:

- `--text TEXT`: Process and display the provided text
- `--version`: Show program version and exit
- `--help` or `-h`: Show help message and exit

If no action is provided, the application will process default text with a warning.

## Development

### Running Tests

```bash
# All tests
poetry run pytest

# With coverage
poetry run pytest --cov=src --cov-report=term-missing

# Only unit tests (excludes integration tests)
poetry run pytest -m "not integration"

# Only integration tests
poetry run pytest -m integration

# Verbose output
poetry run pytest -v

# Run specific test file
poetry run pytest tests/test_main.py -v
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

Runs automatically on every commit with 17 checks:

- File formatting, YAML/JSON/TOML validation
- Ruff linting and formatting (auto-fix)
- Python syntax validation
- Security checks
- Full test suite with 80% coverage

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

### Git Workflow

Trunk-based development: one `main` branch + short-lived feature branches

```bash
git checkout -b yourname/feature    # Create branch
git commit -m "feat: description"   # Pre-commit validates automatically
git push origin yourname/feature    # Create PR
# After merge: git checkout main && git pull
```

### CI/CD

**PR Workflow:** Validates PRs with all pre-commit hooks before merge
**Main Workflow:** Executes application on push to `main`
**Dependabot:** Weekly automated dependency updates (Python + GitHub Actions)

## VS Code Integration

Pre-configured settings included:

- Python interpreter auto-detection
- Ruff formatter and linter
- Debug configurations
- Test discovery
- Recommended extensions

**Tasks** (`Ctrl+Shift+P` → "Tasks: Run Task"): Run Application, Tests, Lint, Format

## Troubleshooting

| Issue                       | Solution                                                  |
| --------------------------- | --------------------------------------------------------- |
| Pre-commit fails first time | `poetry run pre-commit run --all-files` (downloads tools) |
| No `poetry.lock` file       | Normal for template - run `poetry install` to generate it |
| Poetry lock out of sync     | `poetry lock --no-update && poetry install`               |
| Import errors               | `poetry install` (reinstalls in editable mode)            |
| Tests fail locally          | `poetry install --sync` (ensures dependencies match)      |

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
