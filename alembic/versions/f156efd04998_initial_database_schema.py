"""initial database schema

Revision ID: f156efd04998
Revises: 6f18f319cbae
Create Date: 2026-08-12 14:39:32.452677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f156efd04998'
down_revision: Union[str, Sequence[str], None] = '6f18f319cbae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "roles",
            sa.column("role_id", sa.Integer),
            sa.column("role_name", sa.String),
        ),
        [
            {
                "role_id": 1,
                "role_name": "Admin",
            },
            {
                "role_id": 2,
                "role_name": "Manager",
            },
            {
                "role_id": 3,
                "role_name": "HR",
            },
            {
                "role_id": 4,
                "role_name": "Employee",
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM roles WHERE role_id IN (1, 2, 3, 4)"
    )
