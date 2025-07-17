"""Modificar columnas de las tablas actividades y alojamientos, se me olvido eliminar la columna img

Revision ID: 96ff44c8b177
Revises: 1975722b1c13
Create Date: 2024-12-03 00:13:42.999178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96ff44c8b177'
down_revision: Union[str, None] = '1975722b1c13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('actividades', 'img')


def downgrade() -> None:
    pass
