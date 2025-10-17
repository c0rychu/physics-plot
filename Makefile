run-pre-commit-ruff-black:
	uv run pre-commit run --all-files
run-local-mkdocs-server:
	uv run mkdocs serve
