"""add employee delete permission

Revision ID: 7f1335a82650
Revises: 12bb836d589d
Create Date: 2026-08-14 11:10:08.103385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f1335a82650'
down_revision: Union[str, Sequence[str], None] = '12bb836d589d'
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
                "permission_id": 6,
                "endpoint": "/employees/{employee_id}",
                "method": "DELETE",
            }
        ],
    )
def downgrade() -> None:
    op.execute(
        """
        DELETE FROM permissions
        WHERE permission_id = 6
        """
    )