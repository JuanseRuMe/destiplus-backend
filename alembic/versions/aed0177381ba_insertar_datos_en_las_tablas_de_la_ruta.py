from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'aed0177381ba'
down_revision = '581dc519b312'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Insertar datos en la tabla rutas
    rutas_table = sa.table('rutas',
                           sa.column('destino_id', sa.Integer),
                           sa.column('nombre', sa.String),
                           sa.column('descripcion', sa.String),
                           sa.column('etiquetas', sa.JSON(sa.String)),
                           sa.column('distancia', sa.Integer),
                           sa.column('veces_recomendada', sa.Integer),
                           sa.column('completaron_ruta', sa.Integer),
                           sa.column('terreno', sa.String),
                           sa.column('items', sa.JSON),
                           sa.column('calificacion', sa.Float),
                           sa.column('dificultad', sa.String),
                           sa.column('tiempo', sa.Integer),
                           sa.column('img', sa.String)
                           )
    
    op.bulk_insert(rutas_table,
                   [
                       {'destino_id': 1,
                        'nombre': 'Virgen de la Z',
                        'descripcion': 'El Alto de la Virgen es un lugar sagrado en la cima de una montaña, ofreciendo vistas impresionantes de la sabana. Es perfecto para locales y turistas que buscan una experiencia espiritual, reflexionar, tomar fotos y relajarse en un entorno sereno.',
                        'etiquetas': { 'etiquetas': ["Pet Friendly", "Monumento", "Bosque", "Camino Irregular", "Paisajes", "Montaña"]},
                        'distancia': 10,
                        'veces_recomendada': 150,
                        'completaron_ruta': 160,
                        'terreno': 'Montañoso',
                        'items': {"Duración": "corta", "Tipo": "Monumento"},
                        'calificacion': 4.5,
                        'dificultad': 'Alta',
                        'tiempo': 30,
                        'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729123518/Panoramica_Virgen3_d6tvb6.jpg'}
                   ])