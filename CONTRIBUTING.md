# Contributing to Python App Template

Thank you for your interest in contributing! This guide will help you get started.

## Development Model

We use **trunk-based development**:

- Single main branch: `main`
- Short-lived feature branches (1-2 days max)
- Fast integration through Pull Requests
- No `develop`, `release`, or long-lived branches

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR-USERNAME/python-app-template.git
cd python-app-template
```

### 2. Install Dependencies

```bash
poetry install
poetry run pre-commit install
```

### 3. Create a Branch

```bash
git checkout main
git pull origin main
git checkout -b yourname/short-description
```

**Branch naming**: `yourname/feature-description` or `yourname/fix-issue-123`

## Development Workflow

### 1. Make Changes

```bash
# Edit code
vim src/main.py

# Run tests frequently
poetry run pytest -v

# Check formatting
poetry run ruff check src tests
poetry run ruff format src tests
```

### 2. Commit

Pre-commit hooks run automatically:

```bash
git add .
git commit -m "feat: add new feature"
```

If pre-commit fails:

- Review the output
- Fix the issues (some are auto-fixed)
- Run `git add .` if files were modified
- Commit again

### 3. Keep Branch Updated

```bash
# Rebase on main (recommended)
git fetch origin
git rebase origin/main

# Or merge
git merge origin/main
```

### 4. Push and Create PR

```bash
git push origin yourname/short-description
```

Then create a Pull Request on GitHub targeting `main`.

### 5. After Merge

```bash
git checkout main
git pull origin main
git branch -d yourname/short-description
```

## Code Standards

### Python Style

- Follow PEP 8
- Maximum line length: 100 characters
- Use type hints for all public functions
- Write docstrings for modules, classes, and functions

### Code Quality Tools

We use **Ruff** for both linting and formatting:

```bash
# Lint with auto-fix
poetry run ruff check --fix src tests

# Format code
poetry run ruff format src tests

# Or run everything
poetry run pre-commit run --all-files
```

### Testing

**All changes must include tests.**

```bash
# Run all tests
poetry run pytest -v

# Run with coverage (minimum 80% required)
poetry run pytest --cov=src --cov-report=term-missing --cov-fail-under=80

# Run specific test types
poetry run pytest -m unit      # Unit tests only
poetry run pytest -m integration  # Integration tests only
```

**Test structure:**

- Unit tests: `tests/test_*.py` with `@pytest.mark.unit`
- Integration tests: `tests/test_integration.py` with `@pytest.mark.integration`
- Use fixtures in `tests/conftest.py`

## Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Add or modify tests
- `refactor`: Code refactoring
- `style`: Code style changes (formatting, no logic change)
- `chore`: Maintenance tasks (dependencies, config, etc.)
- `ci`: CI/CD changes

**Examples:**

```bash
git commit -m "feat: add new functionality"
git commit -m "fix: handle empty text argument"
git commit -m "docs: update README installation steps"
git commit -m "test: add unit tests for parser"
git commit -m "chore: update dependencies"
```

## Pull Request Process

### Before Creating PR

1. ✅ All tests pass locally
2. ✅ Pre-commit checks pass
3. ✅ Code coverage ≥ 80%
4. ✅ Branch is up-to-date with `main`
5. ✅ Commit messages follow convention

### PR Description Template

```markdown
## Description

Brief description of changes

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing

Describe how you tested the changes

## Checklist

- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Pre-commit hooks pass
- [ ] No breaking changes (or documented)
```

### Review Process

1. Create PR to `main`
2. CI/CD automatically runs all checks
3. Wait for review (if collaborators exist)
4. Address feedback
5. Once approved and green, merge via GitHub
6. Delete your branch

## Pre-commit Hooks

Pre-commit runs these checks automatically:

### File Checks

- Remove trailing whitespace
- Fix end-of-file
- Validate YAML/JSON/TOML syntax
- Detect merge conflicts
- Detect case conflicts (Windows/Linux)
- Prevent large files (>500KB)

### Python Checks

- Validate Python syntax (AST)
- Check docstring positioning
- Detect debug statements (`print`, `pdb`)
- Ruff linting and formatting
- Validate Poetry configuration

### Security & Tests

- GitHub Actions security scan (zizmor)
- Full test suite with 80% coverage

### Manual Execution

```bash
# Run all hooks
poetry run pre-commit run --all-files

# Run specific hook
poetry run pre-commit run ruff-check --all-files
poetry run pre-commit run pytest-check --all-files

# Update hooks to latest versions
poetry run pre-commit autoupdate
```

### Bypass (Emergency Only)

```bash
git commit --no-verify -m "emergency fix"
```

⚠️ **Warning**: CI will still validate everything!

## Local Development Tips

### Use VS Code Tasks

Press `Ctrl+Shift+P` and select "Tasks: Run Task":

- **Run Application** - Execute the app
- **Run Tests** - Run pytest
- **Run Tests with Coverage** - Full coverage report
- **Lint Code** - Run Ruff check
- **Format Code** - Run Ruff format
- **Install Dependencies** - Run poetry install

### Debug Configuration

Launch configurations available:

- **Python: Debug App** - Debug the application
- **Python: Debug Tests** - Debug test suite
- **Python: Debug Current File** - Debug open file

### Common Commands

```bash
# Install/update dependencies
poetry install
poetry update

# Add new dependency
poetry add requests
poetry add --group dev pytest-mock

# Remove dependency
poetry remove requests

# Show installed packages
poetry show
poetry show --tree

# Run app in development
poetry run my-app --text "test"

# Activate shell
poetry shell
my-app --text "test"
```

## Troubleshooting

### Pre-commit fails to install

```bash
# Ensure you're in a git repository
git init  # If needed
poetry run pre-commit install
```

### Poetry lock issues

```bash
# Regenerate lock file
poetry lock --no-update
poetry install
```

### Import errors in tests

```bash
# Reinstall project
poetry install
```

### Coverage below 80%

```bash
# See which lines aren't covered
poetry run pytest --cov=src --cov-report=html
# Open htmlcov/index.html in browser
```

### Tests pass locally but fail in CI

```bash
# Sync dependencies exactly
poetry install --sync

# Run pre-commit like CI does
poetry run pre-commit run --all-files
```

## Questions or Issues?

- **Bugs**: [Open an issue](https://github.com/yourusername/python-app-template/issues)
- **Questions**: [GitHub Discussions](https://github.com/yourusername/python-app-template/discussions)
- **Security**: See [SECURITY.md](SECURITY.md)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
