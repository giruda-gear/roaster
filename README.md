# run fastapi
uv run fastapi dev app/main.py

# alembic update
alembic revision --autogenerate -m "message"
alembic upgrade head