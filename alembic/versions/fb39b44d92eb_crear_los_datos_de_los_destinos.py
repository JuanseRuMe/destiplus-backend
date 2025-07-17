"""Crear los datos de los destinos

Revision ID: fb39b44d92eb
Revises: 2b2f4a1bcfd1
Create Date: 2024-10-16 12:49:40.003391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'fb39b44d92eb'
down_revision: Union[str, None] = '2b2f4a1bcfd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    destinos_table = op.create_table(
        'destinos',
        sa.Column('id', sa.Integer, primary_key = True, autoincrement = True),
        sa.Column('municipio', sa.String(100), nullable = False, unique = True),
        sa.Column('departamento', sa.Text, nullable = True),
        sa.Column('lat', sa.Float, nullable = True),
        sa.Column('lng', sa.Float, nullable = True)
    )
    
    op.bulk_insert(
        destinos_table, [
            {
                'municipio': 'Suesca',
                'departamento': 'Cundinamarca',
                'lat': 5.102989,
                'lng': -73.798836
            }
        ]
    )


def downgrade() -> None:
    pass
