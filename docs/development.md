<!-- # Development

This guide outlines how to set up a local development environment, run checks, and contribute improvements to Physics Plot.

## Environment Setup

```bash
uv sync --group dev
```

The command installs runtime dependencies along with development tooling such as Ruff and Black.

## Quality Gates

- `uv run ruff check src` keeps imports sorted and enforces the style guide.
- `uv run black --check src` validates formatting (run without `--check` to auto-format).
- `uv run pytest` executes the test suite once it exists.

Run the commands before opening a pull request so CI stays green.

## Visual Regression Checklist

1. Rebuild figures under `examples/` (start with the Bode plot CLI).
2. Compare the generated images against the versions committed to the repository.
3. Document notable deltas in the pull request description and attach screenshots.

## Documentation

The documentation is built with MkDocs Material:

```bash
uv run mkdocs serve
```

The command starts a live-reloading preview at `http://127.0.0.1:8000`. Commit relevant doc updates alongside code changes to keep users informed.

!!! tip
    The project uses `mkdocstrings` to render API docs from docstrings. If you manage dependencies manually, install `mkdocstrings[python]` in addition to `mkdocs-material`.

## Releasing

1. Bump the version in `pyproject.toml`.
2. Regenerate `uv.lock` if dependencies changed (`uv lock --upgrade-package physics-plot`).
3. Build the distribution with `uv build`.
4. Publish via `uv publish` or `twine upload dist/*`.

Coordinate releases through GitHub issues so maintainers can review changes and test across platforms. -->

