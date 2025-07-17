"""Crear los datos de los bares

Revision ID: 6868be3c303d
Revises: c6176e65cee6
Create Date: 2024-10-15 20:20:48.985096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '6868be3c303d'
down_revision: Union[str, None] = 'c6176e65cee6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bares_table = sa.Table(
        'bares',
        sa.MetaData(),
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('items', postgresql.JSON, nullable=False),
        sa.Column('concepto', sa.Text, nullable=False),
        sa.Column('calificacion', sa.Float, nullable=False),
        sa.Column('precio_promedio', sa.Integer, nullable=False),
        sa.Column('horario', postgresql.JSON, nullable=False),
        sa.Column('address', sa.Text, nullable=False),
        sa.Column('contacto', sa.BigInteger, nullable=False),
        sa.Column('servicios', postgresql.JSON, nullable=False),
        sa.Column('metodos_de_pago', sa.Text, nullable=False),
        sa.Column('destacados', postgresql.JSON, nullable=False),
        sa.Column('recurrente', postgresql.JSON, nullable=False),
        sa.Column('antojos', postgresql.JSON, nullable=False),
        sa.Column('bebidas', postgresql.JSON, nullable=False),
        sa.Column('img', sa.Text, nullable=False),
        sa.Column('imgs', postgresql.JSON, nullable=False),
        sa.Column('logo', sa.Text, nullable=False)
    )
     
    op.bulk_insert(
        'bares',
        [
            {
                'name': 'Bar El Rincón',
                'items': {"Tipo": 'Discoteca', "Descripcion": 'La mejor fiesta'},
                'concepto': 'Un bar acogedor con música en vivo.',
                'calificacion': 4.5,
                'precio_promedio': 30000,
                'horario': {"abren": '8:10 am', "cierran": "11:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3112345678,
                'servicios': { "cover": 5000, "reservas": 'Disponible', "parking": 'No disponible'},
                'metodos_de_pago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'destacados': [
                    {
                        "nombre": "Burguer texana",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Texas BBQ Ribs",
                        "img": "https://images.unsplash.com/photo-1544025162-d76694265947",
                        "costo": 28000,
                        "descripcion": "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        "nombre": "Brisket Sandwich",
                        "img": "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        "costo": 18000,
                        "descripcion": "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                "recurrente": [
                    {
                        "nombre": "Plato del dia",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Desayuno",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                "antojos": [
                    {
                        "nombre": "Chicharrones",
                        "descripcion": 'Entrada chicharron carnudo',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Empanadas",
                        "descripcion": 'Canasta x6',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        "costo": 14000,
                    },
                ],
                "bebidas": [
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    }
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg',
                'imgs': {
                    "imagenes": [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/mauros-pub_gwjoff.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/la-movida_l2focs.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044408/el-sotano_ge8put.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044407/cueva-jazz_r0sbuw.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044406/bar-texas_tic21v.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg", 
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044259/3_p6y2qm.jpg'
            },
            {
                'name': 'Bar El Rincón',
                'items': {"Tipo": 'Discoteca', "Descripcion": 'La mejor fiesta'},
                'concepto': 'Un bar acogedor con música en vivo.',
                'calificacion': 4.5,
                'precio_promedio': 30000,
                'horario': {"abren": '8:10 am', "cierran": "11:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3112345678,
                'servicios': { "cover": 5000, "reservas": 'Disponible', "parking": 'No disponible'},
                'metodos_de_pago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'destacados': [
                    {
                        "nombre": "Burguer texana",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Texas BBQ Ribs",
                        "img": "https://images.unsplash.com/photo-1544025162-d76694265947",
                        "costo": 28000,
                        "descripcion": "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        "nombre": "Brisket Sandwich",
                        "img": "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        "costo": 18000,
                        "descripcion": "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                "recurrente": [
                    {
                        "nombre": "Plato del dia",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Desayuno",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                "antojos": [
                    {
                        "nombre": "Chicharrones",
                        "descripcion": 'Entrada chicharron carnudo',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Empanadas",
                        "descripcion": 'Canasta x6',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        "costo": 14000,
                    },
                ],
                "bebidas": [
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    }
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg',
                'imgs': {
                    "imagenes": [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/mauros-pub_gwjoff.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/la-movida_l2focs.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044408/el-sotano_ge8put.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044407/cueva-jazz_r0sbuw.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044406/bar-texas_tic21v.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg", 
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044259/3_p6y2qm.jpg'
            },
            {
                'name': 'Bar El Rincón',
                'items': {"Tipo": 'Discoteca', "Descripcion": 'La mejor fiesta'},
                'concepto': 'Un bar acogedor con música en vivo.',
                'calificacion': 4.5,
                'precio_promedio': 30000,
                'horario': {"abren": '8:10 am', "cierran": "11:30 pm"},
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': 3112345678,
                'servicios': { "cover": 5000, "reservas": 'Disponible', "parking": 'No disponible'},
                'metodos_de_pago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'destacados': [
                    {
                        "nombre": "Burguer texana",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Texas BBQ Ribs",
                        "img": "https://images.unsplash.com/photo-1544025162-d76694265947",
                        "costo": 28000,
                        "descripcion": "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        "nombre": "Brisket Sandwich",
                        "img": "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        "costo": 18000,
                        "descripcion": "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                "recurrente": [
                    {
                        "nombre": "Plato del dia",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        "nombre": "Desayuno",
                        "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        "costo": 14000,
                        "descripcion": "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                "antojos": [
                    {
                        "nombre": "Chicharrones",
                        "descripcion": 'Entrada chicharron carnudo',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Empanadas",
                        "descripcion": 'Canasta x6',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        "costo": 14000,
                    },
                ],
                "bebidas": [
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Coca cola",
                        "descripcion": '250 ml',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        "costo": 14000,
                    },
                    {
                        "nombre": "Jugo natural",
                        "descripcion": 'En agua o en leche',
                        "img": "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        "costo": 14000,
                    }
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg',
                'imgs': {
                    "imagenes": [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/mauros-pub_gwjoff.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044411/la-movida_l2focs.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044408/el-sotano_ge8put.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044407/cueva-jazz_r0sbuw.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044406/bar-texas_tic21v.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044321/bar-texas_rngomu.jpg", 
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729044259/3_p6y2qm.jpg'
            },
        ]
    )


def downgrade() -> None:
    pass
