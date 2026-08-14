"""grant employee delete permission

Revision ID: 0d486b4b5300
Revises: 1c7d5b5cc166
Create Date: 2026-08-14 11:33:36.214489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d486b4b5300'
down_revision: Union[str, Sequence[str], None] = '1c7d5b5cc166'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
