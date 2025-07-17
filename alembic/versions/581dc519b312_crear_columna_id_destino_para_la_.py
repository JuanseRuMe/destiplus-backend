"""Crear tablas para la relacion de las rutas

Revision ID: 581dc519b312
Revises: 9449cd9638d5
Create Date: 2024-10-16 17:59:16.381575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '581dc519b312'
down_revision: Union[str, None] = '9449cd9638d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
# Crear tabla rutas
    op.create_table(
        'rutas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('destino_id', sa.Integer(), nullable=True),
        sa.Column('nombre', sa.String(length=100), nullable=False),
        sa.Column('descripcion', sa.Text(), nullable=True),
        sa.Column('etiquetas', postgresql.JSON, nullable = True),
        sa.Column('distancia', sa.Float(), nullable=True),
        sa.Column('veces_recomendada', sa.Integer(), nullable=True),
        sa.Column('completaron_ruta', sa.Integer(), nullable=True),
        sa.Column('terreno', sa.String(length=50), nullable=True),
        sa.Column('items', postgresql.JSON, nullable=False),
        sa.Column('calificacion', sa.Float(), nullable=True),
        sa.Column('dificultad', sa.String(length=20), nullable=True),
        sa.Column('tiempo', sa.Integer(), nullable=True),
        sa.Column('img', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['destino_id'], ['destinos.id'])
    )
    
    # Crear tabla categorias
    op.create_table(
        'categorias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('senderismo', sa.Boolean(), nullable=True),
        sa.Column('bici_tour', sa.Boolean(), nullable=True),
        sa.Column('moto', sa.Boolean(), nullable=True),
        sa.Column('automovil', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )

    # Crear tabla imagenes
    op.create_table(
        'imagenes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('url', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )

    # Crear tabla instrucciones
    op.create_table(
        'instrucciones',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('recomendaciones', sa.Text(), nullable=True),
        sa.Column('accesibilidad', sa.Text(), nullable=True),
        sa.Column('conservacion', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )
    
    # Crear tabla emergencias
    op.create_table(
        'emergencias',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('tipo', sa.String(length=50), nullable=True),
        sa.Column('numero', sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )
    
    # Crear tabla estaciones
    op.create_table(
        'estaciones',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('nombre', sa.String(length=100), nullable=True),
        sa.Column('dificultad', sa.String(length=20), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('lng', sa.Float(), nullable=True),
        sa.Column('img', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )
    
    # Crear tabla atajos
    op.create_table(
        'atajos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('nombre', sa.String(length=100), nullable=True),
        sa.Column('dificultad', sa.String(length=20), nullable=True),
        sa.Column('img', sa.String(length=255), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('lng', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )
    
    # Crear tabla disponibilidad_atajos
    op.create_table(
        'disponibilidad_atajos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('atajo_id', sa.Integer(), nullable=True),
        sa.Column('senderismo', sa.Boolean(), nullable=True),
        sa.Column('bici_tour', sa.Boolean(), nullable=True),
        sa.Column('moto', sa.Boolean(), nullable=True),
        sa.Column('automovil', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['atajo_id'], ['atajos.id'])
    )
    
    # Crear tabla coordenadas_atajos
    op.create_table(
        'coordenadas_atajos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('atajo_id', sa.Integer(), nullable=True),
        sa.Column('cordenadas', postgresql.JSON, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['atajo_id'], ['atajos.id'])
    )
    
    # Crear tabla coordenadas_principales
    op.create_table(
        'coordenadas_principales',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('cordenadas', postgresql.JSON, nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'])
    )


def downgrade() -> None:
    pass
