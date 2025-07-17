"""Crear los datos de los Eventos

Revision ID: ffadb4ab69f2
Revises: 89eba7c4ed2f
Create Date: 2024-10-15 22:35:37.676376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = 'ffadb4ab69f2'
down_revision: Union[str, None] = '89eba7c4ed2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
# Crear la tabla 'eventos' y asignar a una variable
    eventos_table = op.create_table(
        'eventos',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('oferente', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('items', postgresql.JSON, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('itinerario', sa.Text, nullable=False),
        sa.Column('logo', sa.Text, nullable=False),
        sa.Column('img', sa.Text, nullable=False),
        sa.Column('calificacion', sa.Float, nullable=False),
        sa.Column('fecha', sa.String(50), nullable=False),
        sa.Column('hora', sa.String(50), nullable=False),
        sa.Column('lugar', sa.String(255), nullable=False),
        sa.Column('precio', sa.Integer, nullable=False),
        sa.Column('metodosdepago', sa.Text, nullable=False),
        sa.Column('duracion', sa.Integer, nullable=False),
        sa.Column('requisitos', postgresql.JSON, nullable=False),
        sa.Column('cupos', sa.String(50), nullable=False),
        sa.Column('contacto', sa.BigInteger, nullable=False),
        sa.Column('address', sa.Text, nullable=False)
    )

    # Inserta los datos en la tabla 'eventos'
    op.bulk_insert(
        eventos_table,  # Usa la variable de la tabla aquí
        [
            {
                'oferente': 'Comunidad',
                'name': 'Viacrucis',
                'items': {
                    'Tipo': 'Religioso'
                },
                'description': 'Viacrucis de Semana Santa',
                'itinerario': 'El Viacrucis en Suesca, Cundinamarca, es una ceremonia profundamente arraigada en la comunidad católica local. El recorrido inicia en la plaza principal, donde los fieles se congregan para comenzar la procesión. A medida que se avanza por las calles empedradas del pueblo, los participantes hacen paradas en las estaciones que representan las etapas de la Pasión de Cristo.',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049637/2_ucal09.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049642/Viacrucis-2023_Post_trq82x.jpg',
                'calificacion': 4.8,
                'fecha': '12 Oct',
                'hora': '4:00 pm',
                'lugar': 'Parque de la Vida',
                'precio': 0,
                'metodosdepago': 'Sin costo de entrada',
                'duracion': 4,
                'requisitos': {
                    'Vestimenta': 'fiesta semaforo',
                    'Edad': 'No menores de edad'
                },
                'cupos': 'Ilimitados',
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D'
            },
            {
                'oferente': 'Comunidad',
                'name': 'Viacrucis',
                'items': {
                    'Tipo': 'Religioso'
                },
                'description': 'Viacrucis de Semana Santa',
                'itinerario': 'El Viacrucis en Suesca, Cundinamarca, es una ceremonia profundamente arraigada en la comunidad católica local. El recorrido inicia en la plaza principal, donde los fieles se congregan para comenzar la procesión. A medida que se avanza por las calles empedradas del pueblo, los participantes hacen paradas en las estaciones que representan las etapas de la Pasión de Cristo.',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049637/2_ucal09.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049642/Viacrucis-2023_Post_trq82x.jpg',
                'calificacion': 4.8,
                'fecha': '12 Oct',
                'hora': '4:00 pm',
                'lugar': 'Parque de la Vida',
                'precio': 0,
                'metodosdepago': 'Sin costo de entrada',
                'duracion': 4,
                'requisitos': {
                    'Vestimenta': 'fiesta semaforo',
                    'Edad': 'No menores de edad'
                },
                'cupos': 'Ilimitados',
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D'
            },
            {
                'oferente': 'Comunidad',
                'name': 'Viacrucis',
                'items': {
                    'Tipo': 'Religioso'
                },
                'description': 'Viacrucis de Semana Santa',
                'itinerario': 'El Viacrucis en Suesca, Cundinamarca, es una ceremonia profundamente arraigada en la comunidad católica local. El recorrido inicia en la plaza principal, donde los fieles se congregan para comenzar la procesión. A medida que se avanza por las calles empedradas del pueblo, los participantes hacen paradas en las estaciones que representan las etapas de la Pasión de Cristo.',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049637/2_ucal09.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729049642/Viacrucis-2023_Post_trq82x.jpg',
                'calificacion': 4.8,
                'fecha': '12 Oct',
                'hora': '4:00 pm',
                'lugar': 'Parque de la Vida',
                'precio': 0,
                'metodosdepago': 'Sin costo de entrada',
                'duracion': 4,
                'requisitos': {
                    'Vestimenta': 'fiesta semaforo',
                    'Edad': 'No menores de edad'
                },
                'cupos': 'Ilimitados',
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D'
            }
        ]
    )

def downgrade() -> None:
    pass
