"""Crear tabla de votaciones batalla de hamburguesas 2025

Revision ID: 69b521c501ff
Revises: 0ad66e93a359
Create Date: 2025-04-28 17:56:08.966089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '69b521c501ff'
down_revision: Union[str, None] = '0ad66e93a359' # El ID de la migración anterior
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Nombre de la tabla para consistencia
TABLE_NAME = 'burger_battle_votes_2025'

def upgrade() -> None:
    """
    Define la estructura de la tabla de votos.
    Se ejecuta al aplicar la migración (alembic upgrade head).
    """
    op.create_table(
        TABLE_NAME,
        # Clave Primaria
        sa.Column('id', sa.Integer, primary_key=True, comment='Identificador único del voto'),

        # Datos del Votante (del formulario)
        sa.Column('email', sa.String(255), nullable=False, index=True, comment='Correo electrónico del votante'),
        sa.Column('full_name', sa.String(255), nullable=False, comment='Nombre completo del votante'),
        sa.Column('rating', sa.Integer, nullable=False, comment='Calificación de 1 a 10'),
        sa.Column('recommendations', sa.Text, nullable=True, comment='Comentarios o recomendaciones'),
        sa.Column('origin', sa.String(255), nullable=True, comment='Lugar de origen/visita del votante'),

        # Datos de la Hamburguesa (contexto)
        sa.Column('burger_name', sa.String(255), nullable=False, comment='Nombre de la hamburguesa votada'),
        sa.Column('restaurant_name', sa.String(255), nullable=False, comment='Nombre del restaurante'),
        sa.Column('burger_id', sa.Integer, nullable=False, index=True, comment='ID de la hamburguesa votada (para referencia)'),

        # Datos de Geolocalización y Auditoría (obtenidos por frontend/backend)
        sa.Column('latitude', sa.Float, nullable=True, comment='Latitud del votante al momento de votar'),
        sa.Column('longitude', sa.Float, nullable=True, comment='Longitud del votante al momento de votar'),
        sa.Column('ip_address', sa.String(100), nullable=True, comment='Dirección IP del votante'),
        # Podrías usar postgresql.INET si tienes la dependencia y prefieres ese tipo:
        # sa.Column('ip_address', postgresql.INET, nullable=True, comment='Dirección IP del votante'),

        # Marca de Tiempo (gestionada por la DB)
        sa.Column(
            'voted_at',
            sa.TIMESTAMP(timezone=True), # Importante usar timezone=True
            nullable=False,
            server_default=sa.func.now(), # PostgreSQL asignará la hora actual automáticamente
            comment='Fecha y hora en que se registró el voto'
        ),

        # Restricciones adicionales
        sa.CheckConstraint('rating >= 1 AND rating <= 10', name=f'ck_{TABLE_NAME}_rating'),
        # Comentarios en las columnas (añadidos con comment=...)
    )

    # Crear un índice único para evitar que el mismo email vote más de una vez POR LA MISMA hamburguesa
    op.create_unique_constraint(
        f'uq_{TABLE_NAME}_email_burger_id', # Nombre de la restricción única
        TABLE_NAME,
        ['email', 'burger_id'] # Columnas que deben ser únicas en combinación
    )
    print(f"Tabla '{TABLE_NAME}' creada exitosamente con restricciones e índices.")


def downgrade() -> None:
    """
    Revierte los cambios hechos en upgrade.
    Se ejecuta al revertir la migración (alembic downgrade <revision_anterior>).
    """
    # Es buena práctica eliminar restricciones explícitamente antes de borrar la tabla
    print(f"Eliminando restricción única 'uq_{TABLE_NAME}_email_burger_id'...")
    op.drop_constraint(f'uq_{TABLE_NAME}_email_burger_id', TABLE_NAME, type_='unique')

    # Las CheckConstraints suelen eliminarse al borrar la tabla, pero si se creó explícitamente
    # podrías necesitar eliminarla explícitamente también en algunos casos:
    # op.drop_constraint(f'ck_{TABLE_NAME}_rating', TABLE_NAME, type_='check')

    print(f"Eliminando tabla '{TABLE_NAME}'...")
    op.drop_table(TABLE_NAME)
    print(f"Tabla '{TABLE_NAME}' eliminada exitosamente.")