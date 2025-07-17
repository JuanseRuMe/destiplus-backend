"""Borrar datos de la table burger batle

Revision ID: 2c4fa3bd0072
Revises: a2edcd101233
Create Date: 2025-06-19 12:02:30.942053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c4fa3bd0072'
down_revision: Union[str, None] = 'a2edcd101233'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Eliminar registros específicos de burger_battle_votes_2025"""
    
    # Conectar a la base de datos y ejecutar la eliminación
    connection = op.get_bind()
    
    # IDs a eliminar (10-28)
    ids_to_delete = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    
    # Crear la consulta de eliminación
    delete_query = sa.text("""
        DELETE FROM burger_battle_votes_2025 
        WHERE id IN :ids
    """)
    
    # Ejecutar la eliminación
    result = connection.execute(delete_query, {"ids": tuple(ids_to_delete)})
    
    print(f"Eliminados {result.rowcount} registros de burger_battle_votes_2025")


def downgrade() -> None:
    """No se puede deshacer la eliminación de datos sin backup"""
    pass