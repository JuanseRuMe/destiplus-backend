"""Modificar columnas de las tablas actividades y alojamientos

Revision ID: 1975722b1c13
Revises: 3de5716749cf
Create Date: 2024-12-02 23:35:04.301600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1975722b1c13'
down_revision: Union[str, None] = '3de5716749cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add new actividades column
    op.add_column('actividades', sa.Column('actividad', postgresql.JSON, nullable=True, server_default='[]'))
    
    # Drop old columns
    op.drop_column('actividades', 'items')
    op.drop_column('actividades', 'name')
    op.drop_column('actividades', 'duracion')
    op.drop_column('actividades', 'dificultad')
    op.drop_column('actividades', 'capacidad')
    op.drop_column('actividades', 'description')
    op.drop_column('actividades', 'itinerario')
    op.drop_column('actividades', 'imgs')
    op.drop_column('actividades', 'calificacion')
    op.drop_column('actividades', 'requisitosRecomendaciones')
    op.drop_column('actividades', 'precio')

def downgrade() -> None:
    # Recreate original columns
    op.add_column('actividades', sa.Column('items', postgresql.JSON, nullable=True))
    op.add_column('actividades', sa.Column('name', sa.String(), nullable=True))
    op.add_column('actividades', sa.Column('duracion', sa.Integer(), nullable=True))
    op.add_column('actividades', sa.Column('dificultad', sa.String(), nullable=True))
    op.add_column('actividades', sa.Column('capacidad', sa.Integer(), nullable=True))
    op.add_column('actividades', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('actividades', sa.Column('itinerario', sa.Text(), nullable=True))
    op.add_column('actividades', sa.Column('imgs', postgresql.JSON, nullable=True))
    op.add_column('actividades', sa.Column('calificacion', sa.Float(), nullable=True))
    op.add_column('actividades', sa.Column('requisitosRecomendaciones', postgresql.JSON, nullable=True))
    op.add_column('actividades', sa.Column('precio', sa.Integer(), nullable=True))