"""Crear los datos de las actividades

Revision ID: 89eba7c4ed2f
Revises: 355e0355901b
Create Date: 2024-10-15 22:10:25.188363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '89eba7c4ed2f'
down_revision: Union[str, None] = '355e0355901b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    actividades_table = op.create_table(
        'actividades',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('oferente', sa.String(255), nullable=False),
        sa.Column('items', postgresql.JSON, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('duracion', sa.Integer, nullable=False),
        sa.Column('dificultad', sa.String(50), nullable=False),
        sa.Column('capacidad', sa.Integer, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('itinerario', sa.Text, nullable=False),
        sa.Column('horario', postgresql.JSON, nullable=False),
        sa.Column('address', sa.Text, nullable=False),
        sa.Column('contacto', sa.BigInteger, nullable=False),
        sa.Column('logo', sa.Text, nullable=False),
        sa.Column('img', sa.Text, nullable=False),
        sa.Column('imgs', postgresql.JSON, nullable=False),
        sa.Column('calificacion', sa.Float, nullable=False),
        sa.Column('requisitosRecomendaciones', postgresql.JSON, nullable=False),
        sa.Column('precio', sa.Integer, nullable=False),
        sa.Column('metodosDePago', sa.Text, nullable=False)
    )

    # Inserta los datos en la tabla 'actividades'
    op.bulk_insert(
        actividades_table,
        [
            {
                'oferente': 'Suesca Aventura',
                'items': {"Tipo": "Cabalgata"},
                'name': 'Cabalgata',
                'duracion': 45,
                'dificultad': 'facil',
                'capacidad': 5,
                'description': 'Cabalgata en las Rocas',
                'itinerario': 'Disfruta de una emocionante cabalgata por los impresionantes paisajes de Suesca, recorriendo senderos que te llevan a través de montañas y rocas icónicas. A lo largo del trayecto, sentirás la conexión con la naturaleza mientras atraviesas bosques, praderas y miradores naturales que ofrecen vistas espectaculares.',
                'horario': {"abren": "8:10 am", "cierran": "7:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3015081517,
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048641/4_f17eqi.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048648/cabalgata_fxdzzh.jpg',
                'imgs': {
                    'Imagenes': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/1_wpkowy.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/6_svznmf.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/5_ksylco.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/7_ymw6al.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/2_oalcz7.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/4_oxttxb.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/3_wmaunr.jpg'
                    ]
                },
                'calificacion': 4.5,
                'requisitosRecomendaciones': {
                    'edad': 'Sin limite de edad',
                    'experiencia': 'No requiere experiencia previa',
                    'incluye': 'Guia, equipo y seguro turistico',
                    'recomendaciones': 'Llevar ropa comoda, bloqueador solar e hidratación'
                },
                'precio': 35000,
                'metodosDePago': 'Efectivo, Nequi y Daviplata, no reciben tarjetas'
            },
            {
                'oferente': 'Suesca Aventura',
                'items': {"Tipo": "Cabalgata"},
                'name': 'Cabalgata',
                'duracion': 45,
                'dificultad': 'facil',
                'capacidad': 5,
                'description': 'Cabalgata en las Rocas',
                'itinerario': 'Disfruta de una emocionante cabalgata por los impresionantes paisajes de Suesca, recorriendo senderos que te llevan a través de montañas y rocas icónicas. A lo largo del trayecto, sentirás la conexión con la naturaleza mientras atraviesas bosques, praderas y miradores naturales que ofrecen vistas espectaculares.',
                'horario': {"abren": "8:10 am", "cierran": "7:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3015081517,
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048641/4_f17eqi.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048648/cabalgata_fxdzzh.jpg',
                'imgs': {
                    'Imagenes': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/1_wpkowy.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/6_svznmf.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/5_ksylco.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/7_ymw6al.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/2_oalcz7.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/4_oxttxb.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/3_wmaunr.jpg'
                    ]
                },
                'calificacion': 4.5,
                'requisitosRecomendaciones': {
                    'edad': 'Sin limite de edad',
                    'experiencia': 'No requiere experiencia previa',
                    'incluye': 'Guia, equipo y seguro turistico',
                    'recomendaciones': 'Llevar ropa comoda, bloqueador solar e hidratación'
                },
                'precio': 35000,
                'metodosDePago': 'Efectivo, Nequi y Daviplata, no reciben tarjetas'
            },
            {
                'oferente': 'Suesca Aventura',
                'items': {"Tipo": "Cabalgata"},
                'name': 'Cabalgata',
                'duracion': 45,
                'dificultad': 'facil',
                'capacidad': 5,
                'description': 'Cabalgata en las Rocas',
                'itinerario': 'Disfruta de una emocionante cabalgata por los impresionantes paisajes de Suesca, recorriendo senderos que te llevan a través de montañas y rocas icónicas. A lo largo del trayecto, sentirás la conexión con la naturaleza mientras atraviesas bosques, praderas y miradores naturales que ofrecen vistas espectaculares.',
                'horario': {"abren": "8:10 am", "cierran": "7:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3015081517,
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048641/4_f17eqi.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048648/cabalgata_fxdzzh.jpg',
                'imgs': {
                    'Imagenes': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/1_wpkowy.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/6_svznmf.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/5_ksylco.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/7_ymw6al.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/2_oalcz7.jpg',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048632/4_oxttxb.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729048631/3_wmaunr.jpg'
                    ]
                },
                'calificacion': 4.5,
                'requisitosRecomendaciones': {
                    'edad': 'Sin limite de edad',
                    'experiencia': 'No requiere experiencia previa',
                    'incluye': 'Guia, equipo y seguro turistico',
                    'recomendaciones': 'Llevar ropa comoda, bloqueador solar e hidratación'
                },
                'precio': 35000,
                'metodosDePago': 'Efectivo, Nequi y Daviplata, no reciben tarjetas'
            }
        ]
    )



def downgrade() -> None:
    pass
