"""Descargar data Burger battle

Revision ID: cb2545579989
Revises: 2c4fa3bd0072
Create Date: 2025-06-20 12:03:34.122891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb2545579989'
down_revision: Union[str, None] = '2c4fa3bd0072'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
