from decimal import Decimal
from sqlalchemy import ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, TimestampMixin
from app.models.green_bean import GreenBean
from app.models.roasting_batch import RoastingBatch


class RoastedBean(TimestampMixin, Base):
    __tablename__ = "roasted_beans"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    green_bean_id: Mapped[int] = mapped_column(
        ForeignKey("green_beans.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    size_g: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    green_bean: Mapped[GreenBean] = relationship(GreenBean)
    batches: Mapped[list[RoastingBatch]] = relationship(RoastingBatch)
