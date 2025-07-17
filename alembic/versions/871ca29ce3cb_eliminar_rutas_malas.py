"""Eliminar rutas malas

Revision ID: 871ca29ce3cb
Revises: 6997069f96ab
Create Date: 2024-12-09 11:13:32.103664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# Identificadores de revisión, usados por Alembic
revision: str = '871ca29ce3cb'
down_revision: Union[str, None] = '6997069f96ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # IDs de las rutas a eliminar
    ruta_id = [5, 6, 28, 29, 3]
    
    # Crear una conexión para ejecutar SQL directo
    connection = op.get_bind()

    # Primero eliminar registros de las tablas hijas
    for table in ['categorias', 'coordenadas_principales', 'estaciones', 
                  'imagenes', 'instrucciones', 'emergencias']:
        connection.execute(
            sa.text(f"""
                DELETE FROM {table}
                WHERE ruta_id IN :ruta_id
            """),
            {"ruta_id": tuple(ruta_id)}
        )

    # Finalmente eliminar las rutas
    connection.execute(
        sa.text("""
            DELETE FROM rutas
            WHERE id IN :ruta_id
        """),
        {"ruta_id": tuple(ruta_id)}
    )


def downgrade() -> None:
    # Nota: Los datos no se pueden restaurar en el downgrade ya que fueron eliminados
    pass