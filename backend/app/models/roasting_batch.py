import datetime
from decimal import Decimal
from sqlalchemy import DateTime, Enum, ForeignKey, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, TimestampMixin
from app.enums.batch_status import BatchStatus
from app.models.roasted_bean import RoastedBean


class RoastingBatch(TimestampMixin, Base):
    __tablename__: "roasting_batches"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    roasted_bean_id: Mapped[int] = mapped_column(
        ForeignKey("roasted_beans.id"), nullable=False
    )
    charge_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    roasted_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[BatchStatus] = mapped_column(
        Enum(BatchStatus), default=BatchStatus.SCHEDULED
    )
    note: Mapped[str | None] = mapped_column(Text)
    roasted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    roasted_bean: Mapped[RoastedBean] = relationship(RoastedBean)
