"""Modificar columna id

Revision ID: a42f4b00016c
Revises: 7a0db904b182
Create Date: 2024-10-15 16:38:51.690116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a42f4b00016c'
down_revision: Union[str, None] = '7a0db904b182'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('restaurantes', 'id')


def downgrade() -> None:
    pass
