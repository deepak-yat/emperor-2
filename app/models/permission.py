from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Permission(Base):
    __tablename__ = "permissions"

    permission_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    endpoint: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    method: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    roles = relationship(
        "RolePermission",
        back_populates="permission"
    )