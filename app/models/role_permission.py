from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.role_id"),
        primary_key=True
    )

    permission_id: Mapped[int] = mapped_column(
        ForeignKey("permissions.permission_id"),
        primary_key=True
    )

    role = relationship(
        "Role",
        back_populates="permissions"
    )

    permission = relationship(
        "Permission",
        back_populates="roles"
    )