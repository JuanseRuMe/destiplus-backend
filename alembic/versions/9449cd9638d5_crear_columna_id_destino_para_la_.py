"""Crear columna id_destino para la relacion

Revision ID: 9449cd9638d5
Revises: fb39b44d92eb
Create Date: 2024-10-16 13:07:01.289197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = '9449cd9638d5'
down_revision: Union[str, None] = 'fb39b44d92eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('restaurantes', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    op.add_column('tendencias', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    op.add_column('eventos', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    op.add_column('bares', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    op.add_column('alojamientos', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    op.add_column('actividades', sa.Column('destino_id', sa.Integer, sa.ForeignKey('destinos.id'), nullable = True))
    
    op.execute("""
        UPDATE restaurantes SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
        UPDATE tendencias SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
        UPDATE eventos SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
        UPDATE bares SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
        UPDATE alojamientos SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
        UPDATE actividades SET destino_id = (SELECT id FROM destinos WHERE municipio = 'Suesca');
    """)

def downgrade() -> None:
    pass
