"""Eliminar restaurantes de ejemplos

Revision ID: 54de3d1b0200
Revises: cc12f8bf9ad7
Create Date: 2024-12-11 00:51:40.589277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54de3d1b0200'
down_revision: Union[str, None] = 'cc12f8bf9ad7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        DELETE FROM restaurante
        WHERE id IN (9, 10)
    """)


def downgrade() -> None:
    # Since we're deleting data, we can't really restore it unless we know the original values
    pass