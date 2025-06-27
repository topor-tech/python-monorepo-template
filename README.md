# python-monorepo-template
template for python projects

## Development Setup

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The following hooks are configured:

- **ruff**: Fast Python linter and formatter
- **mypy**: Static type checker
- **pre-commit-hooks**: General file checks (trailing whitespace, YAML validation, etc.)

#### Installation

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install the git hooks:
   ```bash
   pre-commit install
   ```

3. (Optional) Run against all files:
   ```bash
   pre-commit run --all-files
   ```

#### Manual Usage

- Run all hooks: `pre-commit run`
- Run specific hook: `pre-commit run ruff`
- Run against staged files: `pre-commit run --files <file>`

The hooks will automatically run on every commit and can also be run manually as needed.
