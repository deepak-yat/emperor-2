"""grant employee permission to hr

Revision ID: 12bb836d589d
Revises: 7747dd785586
Create Date: 2026-08-13 10:31:21.780540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12bb836d589d'
down_revision: Union[str, Sequence[str], None] = '7747dd785586'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "role_permissions",
            sa.column("role_id",sa.Integer),
            sa.column("permission_id",sa.Integer),
        ),
        [
            {
                "role_id":3,
                "permission_id":1
            },
            {
                "role_id":3,
                "permission_id":4
            },
            {
                "role_id":3,
                "permission_id":5
            }
        ]
    )
    


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE role_id = 3
        AND permission_id IN (1, 4, 5)
        """
    )