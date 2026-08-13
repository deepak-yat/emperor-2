"""grant employee update permission

Revision ID: 5ce439e0a90d
Revises: a6c35a4c08d7
Create Date: 2026-08-13 09:40:52.702056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ce439e0a90d'
down_revision: Union[str, Sequence[str], None] = 'a6c35a4c08d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "role_permissions",
            sa.column("role_id", sa.Integer),
            sa.column("permission_id", sa.Integer),
        ),
        [
            {
                "role_id": 1,
                "permission_id": 5,
            },
            {
                "role_id": 2,
                "permission_id": 5,
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE permission_id = 5
        AND role_id IN (1, 2)
        """
    )
    