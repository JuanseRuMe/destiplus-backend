"""Insertar resto de  datos en las tablas de la ruta

Revision ID: 413c59219208
Revises: aed0177381ba
Create Date: 2024-10-16 20:11:58.835785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '413c59219208'
down_revision: Union[str, None] = 'aed0177381ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
 # Insertar datos en la tabla categorias
    categorias_table = sa.table('categorias',
                                sa.column('ruta_id', sa.Integer),
                                sa.column('senderismo', sa.Boolean),
                                sa.column('bici_tour', sa.Boolean),
                                sa.column('moto', sa.Boolean),
                                sa.column('automovil', sa.Boolean))
    
    op.bulk_insert(categorias_table,
                   [
                       {'ruta_id': 1, 'senderismo': True, 'bici_tour': True, 'moto': True, 'automovil': False}
                   ])

    # Insertar datos en la tabla imagenes
    imagenes_table = sa.table('imagenes',
                              sa.column('ruta_id', sa.Integer),
                              sa.column('url', sa.String))
    
    op.bulk_insert(imagenes_table,
                   [
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123537/Lucas_ewfuoo.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123537/Lucas_ewfuoo.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123534/Virgen_De_Frente_rnj0c8.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123533/Mirador_Virgen2_rhfjaj.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123525/Mirador_Virgen_rrkym0.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123524/Mirador_fcwnyv.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123520/Final_Virgen_i51jcj.jpg'},
                       {'ruta_id': 1, 'url': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123520/Crucez_ptu6by.jpg'},
                   ])

    # Insertar datos en la tabla instrucciones
    instrucciones_table = sa.table('instrucciones',
                                   sa.column('ruta_id', sa.Integer),
                                   sa.column('recomendaciones', sa.String),
                                   sa.column('accesibilidad', sa.String),
                                   sa.column('conservacion', sa.String))
    
    op.bulk_insert(instrucciones_table,
                   [
                       {'ruta_id': 1, 'recomendaciones': 'Usa un casco y asegúrate de que tu bicicleta esté en buen estado antes de comenzar. Lleva suficiente agua, bloqueador solar y snacks.',
                        'accesibilidad': 'La ruta es accesible para ciclistas que sigan el camino principal, pero los atajos presentan mayor dificultad.',
                        'conservacion': 'Es fundamental contribuir a la conservación de la ruta y el monumento. Recoge la basura y no alteres la fauna.'}
                   ])

    # Insertar datos en la tabla emergencias
    emergencias_table = sa.table('emergencias',
                                 sa.column('ruta_id', sa.Integer),
                                 sa.column('tipo', sa.String),
                                 sa.column('numero', sa.String))
    
    op.bulk_insert(emergencias_table,
                   [
                       {'ruta_id': 1, 'tipo': 'Bomberos', 'numero': '3015081517'},
                       {'ruta_id': 1, 'tipo': 'Policia', 'numero': '3011234512'},
                       {'ruta_id': 1, 'tipo': 'Defensa civil', 'numero': '3011234512'},
                       {'ruta_id': 1, 'tipo': 'Ambulancia', 'numero': '3011234512'},                       
                   ])

    # Insertar datos en la tabla estaciones
    estaciones_table = sa.table('estaciones',
                                sa.column('ruta_id', sa.Integer),
                                sa.column('nombre', sa.String),
                                sa.column('dificultad', sa.String),
                                sa.column('lat', sa.Float),
                                sa.column('lng', sa.Float),
                                sa.column('img', sa.String))
    
    op.bulk_insert(estaciones_table,
                   [
                       {'ruta_id': 1, 'nombre': 'Parque principal', 'dificultad': 'Baja', 'lat': 5.103242, 'lng': -73.798712, 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123701/Parque-principal_ofo7lc.jpg'},
                       {'ruta_id': 1, 'nombre': 'Empezando la Z', 'dificultad': 'Alta', 'lat': 5.113875, 'lng': -73.804139, 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123740/Primer-Atajo_sozcz0.jpg'},
                       {'ruta_id': 1, 'nombre': 'Mirador', 'dificultad': 'Baja', 'lat': 5.114737, 'lng': -73.809393, 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123741/Chitiva-Abajo_xwou00.jpg'},
                       {'ruta_id': 1, 'nombre': 'Virgen de la Z', 'dificultad': 'Baja', 'lat': 5.116750, 'lng': -73.806383, 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123519/Panoramica-virgen2_iaathp.jpg'}

                   ])

    # Insertar datos en la tabla atajos
    atajos_table = sa.table('atajos',
                            sa.column('ruta_id', sa.Integer),
                            sa.column('nombre', sa.String),
                            sa.column('dificultad', sa.String),
                            sa.column('img', sa.String),
                            sa.column('lat', sa.Float),
                            sa.column('lng', sa.Float))
    
    op.bulk_insert(atajos_table,
                   [
                       {'ruta_id': 1, 'nombre': 'Saltando la Z', 'dificultad': 'Alta', 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123867/Atajo_1_qftyag.jpg', 'lat': 5.113973, 'lng': -73.803196},
                       {'ruta_id': 1, 'nombre': 'Por el bosque', 'dificultad': 'Alta', 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123868/Atajo_2_Por_Bosque_ue0x1s.jpg', 'lat': 5.113493, 'lng': -73.805893},
                       {'ruta_id': 1, 'nombre': 'Directo a la Virgen', 'dificultad': 'Alta', 'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123867/Atajo_Extremo_gtdmf0.jpg', 'lat': 5.115032, 'lng': -73.805580 } 
                   ])


def downgrade() -> None:
    pass
