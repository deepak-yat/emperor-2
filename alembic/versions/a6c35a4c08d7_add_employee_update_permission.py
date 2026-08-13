"""add employee update permission

Revision ID: a6c35a4c08d7
Revises: 5a8b7fbd8c57
Create Date: 2026-08-13 09:40:17.637160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6c35a4c08d7'
down_revision: Union[str, Sequence[str], None] = '5a8b7fbd8c57'
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
                "permission_id": 5,
                "endpoint": "/employees/{employee_id}",
                "method": "PUT",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        """
        DELETE FROM permissions
        WHERE permission_id = 5
        """
    )