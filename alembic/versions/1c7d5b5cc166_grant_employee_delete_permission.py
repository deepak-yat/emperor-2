"""grant employee delete permission

Revision ID: 1c7d5b5cc166
Revises: 7f1335a82650
Create Date: 2026-08-14 11:32:35.007558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c7d5b5cc166'
down_revision: Union[str, Sequence[str], None] = '7f1335a82650'
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
                "permission_id": 6,
            },
            {
                "role_id": 3,
                "permission_id": 6,
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE permission_id = 6
        AND role_id IN (1, 3)
        """
    )