"""seed employee creation permission

Revision ID: 6748da7a221e
Revises: 3d6729a76261
Create Date: 2026-08-12 16:24:22.580373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6748da7a221e'
down_revision: Union[str, Sequence[str], None] = '3d6729a76261'
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
                "permission_id": 1,
                "endpoint": "/employees",
                "method": "POST",
            }
        ],
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM permissions WHERE permission_id = 1"
    )