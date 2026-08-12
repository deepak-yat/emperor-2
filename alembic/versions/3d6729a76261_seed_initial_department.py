"""seed initial department

Revision ID: 3d6729a76261
Revises: f156efd04998
Create Date: 2026-08-12 15:13:47.680551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d6729a76261'
down_revision: Union[str, Sequence[str], None] = 'f156efd04998'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "departments",
            sa.column("department_id", sa.Integer),
            sa.column("department_name", sa.String),
        ),
        [
            {
                "department_id": 1,
                "department_name": "Administration",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM departments "
        "WHERE department_id = 1"
    )