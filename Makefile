run-pre-commit-ruff-black:
	uv run pre-commit run --all-files
run-mkdocs-local-server:
	uv run mkdocs serve --livereload
