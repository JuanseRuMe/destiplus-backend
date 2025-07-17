"""Eliminar restaurantes de ejemplos, alojamientos y eventos

Revision ID: 305fb84515c3
Revises: 54de3d1b0200
Create Date: 2024-12-18 11:34:19.735917

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '305fb84515c3'
down_revision: Union[str, None] = '54de3d1b0200'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Eliminar de la tabla alojamientos
    op.execute("DELETE FROM alojamientos WHERE id = 13")
    
    # Eliminar de la tabla restaurante
    op.execute("DELETE FROM restaurante WHERE id = 13")
    
    # Eliminar de la tabla eventos
    op.execute("DELETE FROM eventos WHERE id IN (1, 2)")


def downgrade() -> None:
    pass
