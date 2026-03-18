from datetime import datetime
import uuid
from sqlalchemy import TIMESTAMP, UUID, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from app.enums.user_role import UserRole


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid7
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.CUSTOMER)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
