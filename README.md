# run fastapi
uv run fastapi dev app/main.py

# alembic update
uv run alembic revision --autogenerate -m "message"
uv run alembic upgrade head