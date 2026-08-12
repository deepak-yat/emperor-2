from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    department_name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    employees = relationship(
        "Employee",
        back_populates="department"
    )