"""Eliminar restaurantes de ejemplo

Revision ID: 49e89c3213fc
Revises: 871ca29ce3cb
Create Date: 2024-12-09 23:24:15.583376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49e89c3213fc'
down_revision: Union[str, None] = '871ca29ce3cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Eliminar los restaurantes con IDs específicos
    op.execute("""
        DELETE FROM restaurante 
        WHERE id IN (1, 8, 5, 6)
    """)

def downgrade() -> None:
    # Si necesitas revertir la operación, necesitarías los datos originales
    # Este es un ejemplo - ajusta los valores según los datos originales
    op.execute("""
        INSERT INTO restaurante (id) 
        VALUES (1), (8), (5), (6)
    """)