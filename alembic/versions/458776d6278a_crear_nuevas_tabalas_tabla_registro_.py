"""Crear nuevas tabalas => tabla registro usuarios, tabla reservas

Revision ID: 458776d6278a
Revises: 305fb84515c3
Create Date: 2025-02-18 16:03:50.340277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '458776d6278a'
down_revision: Union[str, None] = '305fb84515c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Paso 1: Eliminar la tabla usuarios existente (si tiene datos, ¡haz backup primero!)
    op.drop_table('usuarios')  # <--- Eliminar antes de crear la nueva
    
    # Paso 2: Crear la nueva tabla usuarios
    op.create_table('usuarios',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nombre', sa.Text, nullable=False),
        sa.Column('email', sa.Text, nullable=False, unique=True),
        sa.Column('whatsapp', sa.Text),
        sa.Column('ciudad', sa.Text),
        sa.Column('edad', sa.Integer),
        sa.Column('fecha_registro', sa.TIMESTAMP, server_default=sa.text('now()'))
    )
    
    # Paso 3: Crear tabla reservas
    op.create_table('reservas',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('alojamiento_id', sa.Integer, nullable=False),
        sa.Column('tipo_alojamiento_id', sa.String(20), nullable=False),
        sa.Column('usuario_id', sa.Integer, sa.ForeignKey('usuarios.id', ondelete='SET NULL')),
        sa.Column('fecha_inicio', sa.Date, nullable=False),
        sa.Column('fecha_fin', sa.Date, nullable=False),
        sa.Column('fecha_creacion', sa.TIMESTAMP, server_default=sa.text('now()')),
        sa.Column('total_pagado', sa.Integer, nullable=False),
        sa.Column('metodo_pago', sa.String(50)),
        sa.Column('estado', sa.String(20), nullable=False, server_default='pendiente'),
        sa.Column('huespedes', sa.Integer, nullable=False),
        sa.CheckConstraint(
            "estado IN ('pendiente', 'confirmada', 'cancelada', 'bloqueado')",
            name='estado_valido'
        )
    )
    
    # Índices
    op.create_index('idx_tipo_alojamiento', 'reservas', ['tipo_alojamiento_id'])
    op.create_index('idx_fechas_reserva', 'reservas', ['fecha_inicio', 'fecha_fin'])


def downgrade() -> None:
    # Eliminar en orden inverso (reservas primero por la FK)
    op.drop_table('reservas')
    op.drop_table('usuarios')