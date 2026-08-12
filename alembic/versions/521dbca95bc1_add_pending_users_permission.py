"""add pending users permission

Revision ID: 521dbca95bc1
Revises: 86e6c0e297dc
Create Date: 2026-08-12 17:01:31.893189

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '521dbca95bc1'
down_revision: Union[str, Sequence[str], None] = '86e6c0e297dc'
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
                "permission_id": 2,
                "endpoint": "/admin/pending-users",
                "method": "GET",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM permissions
        WHERE permission_id = 2
        """
    )
