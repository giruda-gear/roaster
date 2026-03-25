import uuid
from sqlalchemy import UUID, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, TimestampMixin
from app.db_enums import value_enum
from app.enums.user_role import UserRole


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid7
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(
        value_enum(UserRole, name="user_role"),
        default=UserRole.CUSTOMER,
    )
