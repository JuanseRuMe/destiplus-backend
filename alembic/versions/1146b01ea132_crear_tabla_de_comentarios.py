"""Crear tabla de comentarios

Revision ID: 1146b01ea132
Revises: 458776d6278a
Create Date: 2025-03-17 11:38:37.927837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1146b01ea132'
down_revision: Union[str, None] = '458776d6278a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'comentarios_rutas',
        sa.Column('id', sa.Integer(), sa.Identity(), primary_key=True),
        sa.Column('ruta_id', sa.Integer(), nullable=False),
        sa.Column('usuario_id', sa.Integer(), nullable=False),
        sa.Column('comentario', sa.Text(), nullable=False),
        sa.Column('calificacion', sa.Integer(), nullable=True),
        sa.Column('fecha_creacion', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('estado', sa.String(length=20), server_default='pendiente', nullable=False),
        sa.Column('imagen', sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(['ruta_id'], ['rutas.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ondelete='CASCADE'),
        sa.CheckConstraint('calificacion >= 1 AND calificacion <= 5', name='check_calificacion_rango')
    )
    



def downgrade() -> None:
    pass