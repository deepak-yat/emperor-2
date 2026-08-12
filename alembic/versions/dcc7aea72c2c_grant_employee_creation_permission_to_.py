"""grant employee creation permission to admin

Revision ID: dcc7aea72c2c
Revises: 6748da7a221e
Create Date: 2026-08-12 16:27:22.600345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dcc7aea72c2c'
down_revision: Union[str, Sequence[str], None] = '6748da7a221e'
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
                "permission_id": 1,
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE role_id = 1
        AND permission_id = 1
        """
    )
