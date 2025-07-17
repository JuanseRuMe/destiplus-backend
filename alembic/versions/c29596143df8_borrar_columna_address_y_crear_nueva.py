"""Borrar columna address y crear nueva

Revision ID: c29596143df8
Revises: bc9367a1bda0
Create Date: 2024-11-28 15:56:03.501518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = 'c29596143df8'
down_revision: Union[str, None] = 'bc9367a1bda0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('restaurante', 'address')
    op.add_column('restaurante', sa.Column('coordenadas', postgresql.JSON, nullable=True))

    op.drop_column('actividades', 'address')
    op.add_column('actividades', sa.Column('coordenadas', postgresql.JSON, nullable=True))

    op.drop_column('alojamientos', 'address')
    op.add_column('alojamientos', sa.Column('coordenadas', postgresql.JSON, nullable=True))

    op.drop_column('bares', 'address')
    op.add_column('bares', sa.Column('coordenadas', postgresql.JSON, nullable=True))

def downgrade() -> None:
    op.drop_column('restaurante', 'coordenadas')
    op.add_column('restaurante', sa.Column('address', sa.String(), nullable=True))
