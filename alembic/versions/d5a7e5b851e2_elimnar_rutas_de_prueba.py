"""Elimnar rutas de prueba

Revision ID: d5a7e5b851e2
Revises: 9ce6090b8eed
Create Date: 2024-11-14 18:02:04.723124

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5a7e5b851e2'
down_revision: Union[str, None] = '9ce6090b8eed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.execute("""
        BEGIN;
        
        -- Primero eliminamos todas las tablas relacionadas
        DELETE FROM categorias WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM coordenadas_principales WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM estaciones WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM imagenes WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM instrucciones WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM emergencias WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        DELETE FROM atajos WHERE ruta_id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);

        -- Finalmente eliminamos las rutas
        DELETE FROM rutas WHERE id IN (7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23);
        
        COMMIT;
    """)

def downgrade() -> None:
    pass
