"""seed initial departments

Revision ID: 86e6c0e297dc
Revises: dcc7aea72c2c
Create Date: 2026-08-12 16:47:09.791550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86e6c0e297dc'
down_revision: Union[str, Sequence[str], None] = 'dcc7aea72c2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "departments",
            sa.column("department_id", sa.Integer),
            sa.column("department_name", sa.String),
        ),
        [
            {
                "department_id": 2,
                "department_name": "Engineering",
            },
            {
                "department_id": 3,
                "department_name": "Human Resources",
            },
            {
                "department_id": 4,
                "department_name": "Finance",
            },
        ],
    )