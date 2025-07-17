"""Crear los datos de los restaurantes

Revision ID: 7546d06cb4d9
Revises: a42f4b00016c
Create Date: 2024-10-15 16:50:24.106200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7546d06cb4d9'
down_revision: Union[str, None] = 'a42f4b00016c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('restaurantes', sa.Column('contacto', sa.String(), nullable=True))
    op.bulk_insert(
        sa.table('restaurantes',
            sa.column('name', sa.String),
            sa.column('items', sa.JSON),
            sa.column('concepto', sa.Text),
            sa.column('calificacion', sa.Float),
            sa.column('precio_promedio', sa.Integer),
            sa.column('address', sa.String),
            sa.column('contacto', sa.String),
            sa.column('metodosdepago', sa.String),
            sa.column('horario', sa.JSON),
            sa.column('servicios', sa.JSON),
            sa.column('destacados', sa.JSON),
            sa.column('recurrentes', sa.JSON),
            sa.column('antojos', sa.JSON),
            sa.column('bebidas', sa.JSON),
            sa.column('img', sa.String),
            sa.column('imgs', sa.JSON(sa.String)),
            sa.column('logo', sa.String),     
        ),
        [
            {
                'name': 'Burger Texas',
                'items': {
                    'Tipo': 'Parrilla',
                    'Descripcion': 'Delicioso asado a la parrilla'
                },
                'concepto': 'Burger Texas es más que un restaurante; es una auténtica experiencia de sabor texano en el corazón de la ciudad. Fusionamos las técnicas tradicionales de ahumado y parrilla del sur de Estados Unidos con ingredientes locales de primera calidad.',
                'calificacion': 4.2,
                'precio_promedio': 50000,
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': '3015081517',
                'metodosdepago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'horario': {
                    'abren': '8:10 am', 
                    'cierran': '7:30 pm'},
                'servicios': {
                    'delivery': 'Disponible',
                    'reservas': 'Disponible',
                    'parking': 'No disponible'
                },
                'destacados': [
                    {
                        'nombre': "Burguer texana",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Texas BBQ Ribs",
                        'img': "https://images.unsplash.com/photo-1544025162-d76694265947",
                        'costo': 28000,
                        'descripcion': "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        'nombre': "Brisket Sandwich",
                        'img': "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        'costo': 18000,
                        'descripcion': "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                'recurrentes': [
                    {
                        'nombre': "Plato del dia",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Desayuno",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                'antojos': [
                    {
                        'nombre': "Chicharrones",
                        'descripcion': 'Entrada chicharron carnudo',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Empanadas",
                        'descripcion': 'Canasta x6',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        'costo': 14000,
                    },
                ],
                'bebidas': [
                    {
                        'nombre': "Coca cola",
                        'descripcion': '250 ml',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Jugo natural",
                        'descripcion': 'En agua o en leche',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        'costo': 14000,
                    },
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/plato1_bhhyqb.jpg',
                'imgs': {
                    'imagenes': [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026408/par3_dkwzad.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026400/par1_eoxbyk.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026396/par4_l53ny6.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026393/par5_v5hdhg.webp",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026390/par6_ktinlx.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026387/par7_bzrs1d.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026384/par2_mvov1u.jpg",
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026354/2_fsgjz4.jpg',
            },
            {
                'name': 'Burger Texas',
                'items': {
                    'Tipo': 'Parrilla',
                    'Descripcion': 'Delicioso asado a la parrilla'
                },
                'concepto': 'Burger Texas es más que un restaurante; es una auténtica experiencia de sabor texano en el corazón de la ciudad. Fusionamos las técnicas tradicionales de ahumado y parrilla del sur de Estados Unidos con ingredientes locales de primera calidad.',
                'calificacion': 4.2,
                'precio_promedio': 50000,
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': '3015081517',
                'metodosdepago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'horario': {
                    'abren': '8:10 am', 
                    'cierran': '7:30 pm'},
                'servicios': {
                    'delivery': 'Disponible',
                    'reservas': 'Disponible',
                    'parking': 'No disponible'
                },
                'destacados': [
                    {
                        'nombre': "Burguer texana",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Texas BBQ Ribs",
                        'img': "https://images.unsplash.com/photo-1544025162-d76694265947",
                        'costo': 28000,
                        'descripcion': "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        'nombre': "Brisket Sandwich",
                        'img': "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        'costo': 18000,
                        'descripcion': "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                'recurrentes': [
                    {
                        'nombre': "Plato del dia",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Desayuno",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                'antojos': [
                    {
                        'nombre': "Chicharrones",
                        'descripcion': 'Entrada chicharron carnudo',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Empanadas",
                        'descripcion': 'Canasta x6',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        'costo': 14000,
                    },
                ],
                'bebidas': [
                    {
                        'nombre': "Coca cola",
                        'descripcion': '250 ml',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Jugo natural",
                        'descripcion': 'En agua o en leche',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        'costo': 14000,
                    },
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/plato1_bhhyqb.jpg',
                'imgs': {
                    'imagenes': [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026408/par3_dkwzad.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026400/par1_eoxbyk.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026396/par4_l53ny6.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026393/par5_v5hdhg.webp",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026390/par6_ktinlx.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026387/par7_bzrs1d.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026384/par2_mvov1u.jpg",
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026354/2_fsgjz4.jpg',
            },
                        {
                'name': 'Burger Texas',
                'items': {
                    'Tipo': 'Parrilla',
                    'Descripcion': 'Delicioso asado a la parrilla'
                },
                'concepto': 'Burger Texas es más que un restaurante; es una auténtica experiencia de sabor texano en el corazón de la ciudad. Fusionamos las técnicas tradicionales de ahumado y parrilla del sur de Estados Unidos con ingredientes locales de primera calidad.',
                'calificacion': 4.2,
                'precio_promedio': 50000,
                'address': 'https://maps.app.goo.gl/g976EgJprQZgAfzFA',
                'contacto': '3015081517',
                'metodosdepago': 'Efectivo, Nequi y Daviplara, no reciben tarjetas',
                'horario': {
                    'abren': '8:10 am', 
                    'cierran': '7:30 pm'},
                'servicios': {
                    'delivery': 'Disponible',
                    'reservas': 'Disponible',
                    'parking': 'No disponible'
                },
                'destacados': [
                    {
                        'nombre': "Burguer texana",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Texas BBQ Ribs",
                        'img': "https://images.unsplash.com/photo-1544025162-d76694265947",
                        'costo': 28000,
                        'descripcion': "Costillas de cerdo ahumadas. Servidas con elote a la parrilla y coleslaw tradicional.",
                    },
                    {
                        'nombre': "Brisket Sandwich",
                        'img': "https://images.unsplash.com/photo-1610440042657-612c34d95e9f",
                        'costo': 18000,
                        'descripcion': "Jugoso brisket ahumado por 16 horas, cebollas caramelizadas y pepinillos caseros.",
                    }
                ],
                'recurrentes': [
                    {
                        'nombre': "Plato del dia",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                    {
                        'nombre': "Desayuno",
                        'img': "https://images.unsplash.com/photo-1568901346375-23c9450c58cd",
                        'costo': 14000,
                        'descripcion': "Carne doble, queso derretido, bacon, vegetales frescos y papas fritas doradas."
                    },
                ],
                'antojos': [
                    {
                        'nombre': "Chicharrones",
                        'descripcion': 'Entrada chicharron carnudo',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026404/chicharron_dvxkvw.jpg",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Empanadas",
                        'descripcion': 'Canasta x6',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/empanada_skt7jw.webp",
                        'costo': 14000,
                    },
                ],
                'bebidas': [
                    {
                        'nombre': "Coca cola",
                        'descripcion': '250 ml',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026376/bebida1_uxqrhh.webp",
                        'costo': 14000,
                    },
                    {
                        'nombre': "Jugo natural",
                        'descripcion': 'En agua o en leche',
                        'img': "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/bebida2_vqn3pt.webp",
                        'costo': 14000,
                    },
                ],
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026380/plato1_bhhyqb.jpg',
                'imgs': {
                    'imagenes': [
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026408/par3_dkwzad.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026400/par1_eoxbyk.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026396/par4_l53ny6.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026393/par5_v5hdhg.webp",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026390/par6_ktinlx.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026387/par7_bzrs1d.jpg",
                        "https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026384/par2_mvov1u.jpg",
                    ]
                },
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729026354/2_fsgjz4.jpg',
            }
        ]
    )

def downgrade() -> None:
    pass
