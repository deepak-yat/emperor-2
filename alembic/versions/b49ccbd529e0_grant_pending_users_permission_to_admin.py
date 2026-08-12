"""grant pending users permission to admin

Revision ID: b49ccbd529e0
Revises: 521dbca95bc1
Create Date: 2026-08-12 17:02:09.112065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b49ccbd529e0'
down_revision: Union[str, Sequence[str], None] = '521dbca95bc1'
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
                "permission_id": 2,
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE role_id = 1
        AND permission_id = 2
        """
    )