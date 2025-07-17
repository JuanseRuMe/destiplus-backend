"""Elimnar rutas de prueba 2

Revision ID: bc9367a1bda0
Revises: d5a7e5b851e2
Create Date: 2024-11-15 18:33:05.588259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bc9367a1bda0'
down_revision: Union[str, None] = 'd5a7e5b851e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        BEGIN;
        
        -- Primero eliminamos todas las tablas relacionadas
        DELETE FROM categorias WHERE ruta_id IN (24,25);
        DELETE FROM coordenadas_principales WHERE ruta_id IN (24,25);
        DELETE FROM estaciones WHERE ruta_id IN (24,25);
        DELETE FROM imagenes WHERE ruta_id IN (24,25);
        DELETE FROM instrucciones WHERE ruta_id IN (24,25);
        DELETE FROM emergencias WHERE ruta_id IN (24,25);
        DELETE FROM atajos WHERE ruta_id IN (24,25);

        -- Finalmente eliminamos las rutas
        DELETE FROM rutas WHERE id IN (24,25);
        
        COMMIT;
    """)


def downgrade() -> None:
    pass
