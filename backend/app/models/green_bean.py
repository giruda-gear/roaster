from decimal import Decimal
from sqlalchemy import Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, TimestampMixin


class GreenBean(TimestampMixin, Base):
    __tablename__ = "green_beans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    origin: Mapped[str] = mapped_column(String(100))
    region: Mapped[str] = mapped_column(String(100))
    variety: Mapped[str] = mapped_column(String(100))
    process: Mapped[str] = mapped_column(String(100))
    stock_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), default=0)
    price_per_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    description: Mapped[str | None] = mapped_column(Text)
