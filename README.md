### 🚀 run fastapi
```bash
uv run fastapi dev app/main.py
```

### 👉 alembic update
```bash
uv run alembic revision --autogenerate -m "message"
uv run alembic upgrade head
```


### ✅ How to Update Enum Members
Using `native_enum=False` avoids PostgreSQL's rigid Type constraints, allowing for safer and more flexible Enum member updates. Enums are actually stored as VARCHAR with a Check Constraint in PostgreSQL.
1. Generate an empty revision.
2. Manually **Drop** and **Create** the constraint as shown below:

```python
def upgrade():
    # 1. Drop the existing check constraint
    op.drop_constraint('order_status', 'orders', type_='check')
    
    # 2. Create the updated check constraint with the new value list
    op.create_check_constraint(
        'order_status',
        'orders',
        "status IN ('placed', 'preparing', 'shipped', 'delivered', 'cancelled', 'returned')"
    )
```