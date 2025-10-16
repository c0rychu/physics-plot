# Repository Guidelines

## Project Structure & Module Organization
- `src/physics_plot/` holds the package. `utils.py` exposes `Handles`, while `pp_base.mplstyle` defines the default Matplotlib theme and `py.typed` marks the package as typed.
- `examples/` contains runnable demos (`bode-plot.py`, `violin-plot.ipynb`) and reference images; use these to validate visual regressions before shipping changes.
- `uv.lock` captures the resolved dependency graph. Regenerate it only when you update dependencies with `uv`.

## Build, Test, and Development Commands
- `uv sync --group dev` installs runtime and development dependencies. If `uv` is unavailable, fall back to `python -m pip install -e .` and install test/format tools manually.
- `uv run python examples/bode-plot.py` executes the CLI example; use it to smoke-test style updates.
- `uv run pytest` runs the test suite once it exists; pass `-k <pattern>` to focus.
- `uv run ruff check src` and `uv run black --check src` guard linting/formatting. Run without `--check` to auto-fix.

## Coding Style & Naming Conventions
- Target Python 3.11+ and keep modules, functions, and files in `snake_case`; classes stay in `PascalCase`.
- Follow Black's 88-character line length and space indentation. Prefer double quotes (enforced by Ruff) and keep imports sorted.
- Annotate public APIs with type hints—the package ships `py.typed`, so downstream users rely on them.
- Document public interfaces with NumPy-style docstrings so contributors can extend utilities without guessing parameter semantics.

## Testing Guidelines
- Use `pytest` for unit and functional tests. Mirror package paths under `tests/` (e.g., `tests/test_utils.py`).
- Name tests `test_<behavior>` and parametrize when covering multiple inputs.
- For plotting changes, save comparison images in `examples/` or a dedicated `tests/data/` fixture directory and document the workflow in the PR.

## Commit & Pull Request Guidelines
- Keep commit subjects short, present-tense, and imperative (e.g., `update violin-plot filename`). Group related edits together.
- Reference issues or discussion threads in the PR description, summarize visual/test results, and attach before/after screenshots for plotting tweaks.
- Request review once CI passes, and respond to feedback with follow-up commits rather than force-pushes when possible.
