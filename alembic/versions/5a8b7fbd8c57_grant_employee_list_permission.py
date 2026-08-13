"""grant employee list permission

Revision ID: 5a8b7fbd8c57
Revises: f1d5f210b986
Create Date: 2026-08-13 09:30:39.971596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5a8b7fbd8c57'
down_revision: Union[str, Sequence[str], None] = 'f1d5f210b986'
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
                "permission_id": 4,
            },
            {
                "role_id": 2,
                "permission_id": 4,
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE permission_id = 4
        AND role_id IN (1, 2)
        """
    )