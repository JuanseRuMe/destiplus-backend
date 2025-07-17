"""Modificar columnas de eventos y alojamientos
Revision ID: 6997069f96ab
Revises: 96ff44c8b177
Create Date: 2024-12-03 10:40:00.332714
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = '6997069f96ab'
down_revision = '96ff44c8b177'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Agregar nuevas columnas JSON para alojamientos y eventos
    op.add_column('alojamientos', sa.Column('alojamiento', postgresql.JSON(), server_default='[]', nullable=True))
    op.add_column('eventos', sa.Column('evento', postgresql.JSON(), server_default='[]', nullable=True))
    op.add_column('eventos', sa.Column('usuario', sa.String(), nullable=True))
    op.add_column('eventos', sa.Column('coordenadas', postgresql.JSON(), server_default='{}', nullable=True))

    # Eliminar columnas que se moverán al JSON
    op.drop_column('alojamientos', 'name')
    op.drop_column('alojamientos', 'img')
    op.drop_column('alojamientos', 'items')
    op.drop_column('alojamientos', 'description')
    op.drop_column('alojamientos', 'detalle')
    op.drop_column('alojamientos', 'calificacion')
    op.drop_column('alojamientos', 'precio')
    op.drop_column('alojamientos', 'servicios')
    op.drop_column('alojamientos', 'equipamento')
    op.drop_column('alojamientos', 'imgs')
    
    op.drop_column('eventos', 'name')
    op.drop_column('eventos', 'description')
    op.drop_column('eventos', 'itinerario')
    op.drop_column('eventos', 'img')
    op.drop_column('eventos', 'fecha')
    op.drop_column('eventos', 'hora')
    op.drop_column('eventos', 'lugar')
    op.drop_column('eventos', 'address')
    op.drop_column('eventos', 'precio')
    op.drop_column('eventos', 'duracion')
    op.drop_column('eventos', 'cupos')
    op.drop_column('eventos', 'items')
    op.drop_column('eventos', 'requisitos')
    op.drop_column('eventos', 'calificacion')

def downgrade() -> None:
    pass