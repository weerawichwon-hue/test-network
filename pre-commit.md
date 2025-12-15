# Pre-commit configuration guide

This document shows a minimal example `.pre-commit-config.yaml` and how to use `pre-commit` in a Python project.

## Purpose

- Enforce code formatting (Black, isort)
- Run linters (ruff)
- Run type checks (mypy)

## Example `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4
    hooks:
      - id: ruff
        types_or: [ python, pyi ]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.14.1
    hooks:
      - id: mypy
        args: [ --ignore-missing-imports ]
        types: [ python ]
```

Notes:
- Adjust `rev` to the versions you prefer (use tags for reproducibility).
- `additional_dependencies` lets `mypy` include third-party types.

## Example: a local hook (optional)

If you want a quick custom local hook (runs a small script), add:

```yaml
  - repo: local
    hooks:
      - id: check-new-python
        name: Ensure new_python.py passes simple checks
        entry: python -m py_compile new_python.py
        language: system
        files: ^new_python\.py$
```

## Install and use

1. Install `pre-commit` (virtualenv recommended):

```bash
pip install pre-commit        # or pipx install pre-commit
```

2. Install the git hook in your repo:

```bash
pre-commit install
```

3. Run hooks against all files (useful in CI or to retro-fit):

```bash
pre-commit run --all-files
```

4. Update hooks to newer revisions:

```bash
pre-commit autoupdate
```

## CI usage (example for GitHub Actions step)

```yaml
- name: Run pre-commit
  uses: pre-commit/action@v4.4.0
  with:
    extra_args: --all-files
```

## Quick tips

- Keep `rev` pinned for reproducible behavior.
- Use `pre-commit run --files <file>` to test a single file.
- If a hook is slow in CI, consider running only a subset of hooks there.

---

Generated example targets Black, isort, ruff, and mypy. Tailor versions and args to your project.

## Code change for `example.py`

### Before

```python
import datetime


def add_numbers(a: int, b: int) -> str:
  result = a + b
  return str(result)  # intentionally wrong return type for mypy


def greet(name):
  message = "Hello, " + name
  print(message)
  return message
```

### After

```python
def add_numbers(a: int, b: int) -> int:
  result = a + b
  return result


def greet(name: str) -> str:
  message = "Hello, " + name
  print(message)
  return message
```