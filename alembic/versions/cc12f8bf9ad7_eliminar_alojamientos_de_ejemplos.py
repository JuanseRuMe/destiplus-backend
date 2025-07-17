"""Eliminar alojamientos de ejemplos

Revision ID: cc12f8bf9ad7
Revises: d45801b14794
Create Date: 2024-12-10 22:14:28.788630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc12f8bf9ad7'
down_revision: Union[str, None] = 'd45801b14794'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Eliminar los alojamientos con IDs específicos
    op.execute("""
        DELETE FROM alojamientos 
        WHERE id IN (3, 1, 2, 5)
    """)

def downgrade() -> None:
    # Si necesitas revertir la operación
    op.execute("""
        INSERT INTO alojamientos (id) 
        VALUES (3), (1), (2), (5)
    """)
