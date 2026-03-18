import datetime
from decimal import Decimal
from sqlalchemy import DateTime, Enum, ForeignKey, Integer, Numeric, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.enums.batch_status import BatchStatus
from app.models.roasted_bean import RoastedBean


class RoastingBatch(Base):
    __tablename__: "roasting_batches"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    roasted_bean_id: Mapped[int] = mapped_column(
        ForeignKey("roasted_beans.id"), nullable=False
    )
    input_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    yield_kg: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    status: Mapped[BatchStatus] = mapped_column(
        Enum(BatchStatus), default=BatchStatus.SCHEDULED
    )
    note: Mapped[str | None] = mapped_column(Text)
    roasted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    roasted_bean: Mapped[RoastedBean] = relationship(RoastedBean)
