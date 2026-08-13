"""grant user approval permission to admin

Revision ID: 7747dd785586
Revises: 9bf968bd6565
Create Date: 2026-08-13 09:57:59.957376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7747dd785586'
down_revision: Union[str, Sequence[str], None] = '9bf968bd6565'
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
                "permission_id": 3,
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM role_permissions
        WHERE role_id = 1
        AND permission_id = 3
        """
    )