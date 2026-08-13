"""add user approval permission

Revision ID: 9bf968bd6565
Revises: 5ce439e0a90d
Create Date: 2026-08-13 09:57:22.969410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bf968bd6565'
down_revision: Union[str, Sequence[str], None] = '5ce439e0a90d'
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
                "permission_id": 3,
                "endpoint": "/admin/users/{user_id}/approve",
                "method": "PUT",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM permissions
        WHERE permission_id = 3
        """
    )