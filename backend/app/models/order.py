import datetime
from decimal import Decimal
import uuid
from sqlalchemy import UUID, Enum, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, TimestampMixin
from app.enums.order import OrderStatus
from app.models.order_item import OrderItem
from app.models.user import User


class Order(TimestampMixin, Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid7
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.ORDER_PLACED
    )
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    address: Mapped[str] = mapped_column(String(255))

    user: Mapped[User] = relationship(User)
    items: Mapped[list["OrderItem"]] = relationship(OrderItem)
