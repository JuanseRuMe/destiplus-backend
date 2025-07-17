"""Crear tabla de arboles plantados y donaciones

Revision ID: 0ad66e93a359
Revises: 1146b01ea132
Create Date: 2025-03-17 21:19:32.549929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0ad66e93a359'
down_revision: Union[str, None] = '1146b01ea132'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear tabla de donaciones de árboles
    op.create_table(
        'donaciones_arboles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('donante_id', sa.Integer(), nullable=True),
        sa.Column('donante_nombre', sa.String(length=255), nullable=False),
        sa.Column('fecha_donacion', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('cantidad_total', sa.Integer(), nullable=False),
        sa.Column('descripcion', sa.Text(), nullable=True),
        sa.Column('estado', sa.String(length=50), nullable=False, server_default='activa'),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['donante_id'], ['usuarios.id'], name='fk_donante_usuario'),
    )
    
    # Crear índices para optimizar búsquedas
    op.create_index('idx_donaciones_donante', 'donaciones_arboles', ['donante_id'], unique=False)
    op.create_index('idx_donaciones_estado', 'donaciones_arboles', ['estado'], unique=False)
    
    # Crear tabla de árboles plantados
    op.create_table(
        'arboles_plantados',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('donacion_id', sa.Integer(), nullable=True),
        sa.Column('plantador_id', sa.Integer(), nullable=True),
        sa.Column('fecha_plantacion', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('ubicacion_geografica', sa.String(length=100), nullable=True),  # Formato: 'lat,long'
        sa.Column('ruta_id', sa.Integer(), nullable=True),
        sa.Column('nombre_ubicacion', sa.String(length=255), nullable=True),
        sa.Column('region', sa.String(length=100), nullable=True),
        sa.Column('pais', sa.String(length=100), nullable=True),
        sa.Column('especie', sa.String(length=255), nullable=True),
        sa.Column('estado_actual', sa.String(length=50), nullable=False, server_default='plantado'),
        sa.Column('imagen_url', sa.String(length=512), nullable=True),
        sa.Column('descripcion', sa.Text(), nullable=True),
        sa.Column('co2_estimado', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['donacion_id'], ['donaciones_arboles.id'], name='fk_arbol_donacion'),
        sa.ForeignKeyConstraint(['plantador_id'], ['usuarios.id'], name='fk_arbol_plantador'),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'], name='fk_arbol_ruta', ondelete='SET NULL')
    )
    
    # Crear índices para optimizar búsquedas
    op.create_index('idx_arboles_donacion', 'arboles_plantados', ['donacion_id'], unique=False)
    op.create_index('idx_arboles_plantador', 'arboles_plantados', ['plantador_id'], unique=False)
    op.create_index('idx_arboles_ruta', 'arboles_plantados', ['ruta_id'], unique=False)
    op.create_index('idx_arboles_fecha', 'arboles_plantados', ['fecha_plantacion'], unique=False)
    op.create_index('idx_arboles_estado', 'arboles_plantados', ['estado_actual'], unique=False)
    op.create_index('idx_arboles_ubicacion', 'arboles_plantados', ['pais', 'region'], unique=False)


def downgrade() -> None:
    # Eliminar tablas en orden inverso para respetar las restricciones de clave foránea
    op.drop_table('arboles_plantados')
    op.drop_table('donaciones_arboles')