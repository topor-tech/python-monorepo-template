An example template service based on FastAPI framework

For local start run next commands

    services\dummy_fastapi> uv sync
    services\dummy_fastapi> uv run .\dummy_fastapi\app.py


For local linting run

    services\dummy_fastapi> uv sync --extra dev
    services\dummy_fastapi> uv run ruff check . --fix
    services\dummy_fastapi> uv run mypy .
