from __future__ import annotations

from typing import Any, Callable, TypeVar

import enum
from sqlalchemy import Enum as SAEnum

E = TypeVar("E", bound=enum.Enum)


def _enum_values(enum_cls: type[E]) -> list[str]:
    return [m.value for m in enum_cls]


def value_enum(
    enum_cls: type[E],
    *,
    name: str | None = None,
    **kwargs: Any,
) -> SAEnum:
    """
    SQLAlchemy Enum wrapper that persists enum `.value` strings.

    - Stores lowercase (or any) `.value` in DB, not member `.name`
    - Uses `native_enum=False` for easier migrations across DBs
    """

    kwargs.setdefault("native_enum", False)
    kwargs.setdefault("values_callable", _enum_values)
    kwargs.setdefault("validate_strings", True)
    kwargs.setdefault("create_constraint", True)

    # Give the enum a stable name for Alembic autogenerate.
    kwargs.setdefault("name", name or enum_cls.__name__.lower())

    return SAEnum(enum_cls, **kwargs)
