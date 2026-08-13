"""add employee list permission


Revision ID: f1d5f210b986
Revises: b49ccbd529e0
Create Date: 2026-08-13 09:29:54.599561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1d5f210b986'
down_revision: Union[str, Sequence[str], None] = 'b49ccbd529e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "permissions",
            sa.column("permission_id", sa.Integer),
            sa.column("endpoint", sa.String),
            sa.column("method", sa.String),
        ),
        [
            {
                "permission_id": 4,
                "endpoint": "/employees",
                "method": "GET",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM permissions
        WHERE permission_id = 4
        """
    )