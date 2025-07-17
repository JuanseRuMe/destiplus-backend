"""Eliminar columna contacto

Revision ID: bfd5ede32360
Revises: 22faa6c2ea23
Create Date: 2024-11-04 13:17:36.639910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfd5ede32360'
down_revision: Union[str, None] = '22faa6c2ea23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
