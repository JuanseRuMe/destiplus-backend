"""Borrar datos de tabla burger_battle_votes_2025

Revision ID: a2edcd101233
Revises: 6b9a92f0be62
Create Date: 2025-06-01 19:49:17.729161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2edcd101233'
down_revision: Union[str, None] = '6b9a92f0be62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Eliminar registros específicos de burger_battle_votes_2025"""
    
    # Conectar a la base de datos y ejecutar la eliminación
    connection = op.get_bind()
    
    # IDs a eliminar
    ids_to_delete = [1, 5, 6, 8, 9]
    
    # Crear la consulta de eliminación
    delete_query = sa.text("""
        DELETE FROM burger_battle_votes_2025 
        WHERE id IN :ids
    """)
    
    # Ejecutar la eliminación
    result = connection.execute(delete_query, {"ids": tuple(ids_to_delete)})


def downgrade() -> None:
    pass