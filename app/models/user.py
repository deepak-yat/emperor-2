from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    user_email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("employees.id"),
        unique=True,
        nullable=False
    )

    role_id: Mapped[int | None] = mapped_column(
        ForeignKey("roles.role_id"),
        nullable=True
    )

    is_approved: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    employee = relationship(
        "Employee"
    )

    role = relationship(
        "Role",
        back_populates="users"
    )