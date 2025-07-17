"""Eliminar bares  de ejemplo

Revision ID: d45801b14794
Revises: 49e89c3213fc
Create Date: 2024-12-09 23:42:43.959415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd45801b14794'
down_revision: Union[str, None] = '49e89c3213fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Eliminar de la tabla bares
    op.execute("""
        DELETE FROM bares 
        WHERE id IN (4, 6)
    """)

    # Eliminar de la tabla actividades
    op.execute("""
        DELETE FROM actividades 
        WHERE id IN (4, 2)
    """)

    # Eliminar de la tabla alojamientos
    op.execute("""
        DELETE FROM alojamientos 
        WHERE id IN (4)
    """)

def downgrade() -> None:
    # Insertar en bares
    op.execute("""
        INSERT INTO bares (id) 
        VALUES (4), (6)
    """)

    # Insertar en actividades
    op.execute("""
        INSERT INTO actividades (id) 
        VALUES (4), (2)
    """)

    # Insertar en alojamientos
    op.execute("""
        INSERT INTO alojamientos (id) 
        VALUES (4)
    """)