"""Crear los datos de los Alojamientos

Revision ID: 2b2f4a1bcfd1
Revises: ffadb4ab69f2
Create Date: 2024-10-15 22:56:26.498188

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision: str = '2b2f4a1bcfd1'
down_revision: Union[str, None] = 'ffadb4ab69f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
 # Crear la tabla 'alojamientos' y asignar a una variable
    alojamientos_table = op.create_table(
        'alojamientos',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('oferente', sa.String(255), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('logo', sa.Text, nullable=False),
        sa.Column('img', sa.Text, nullable=False),
        sa.Column('checkIn', sa.String(50), nullable=False),
        sa.Column('checkOut', sa.String(50), nullable=False),
        sa.Column('items', postgresql.JSON, nullable=False),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('detalle', sa.Text, nullable=False),
        sa.Column('calificacion', sa.Float, nullable=False),
        sa.Column('contacto', sa.BigInteger, nullable=False),
        sa.Column('address', sa.Text, nullable=False),
        sa.Column('precio', sa.Integer, nullable=False),
        sa.Column('metodosDePago', sa.Text, nullable=False),
        sa.Column('servicios', postgresql.JSON, nullable=False),
        sa.Column('equipamento', postgresql.JSON, nullable=False),
        sa.Column('politicas', postgresql.JSON, nullable=False),
        sa.Column('imgs', postgresql.JSON, nullable=False)
    )

    # Inserta los datos en la tabla 'alojamientos'
    op.bulk_insert(
        alojamientos_table,  # Usa la variable de la tabla aquí
        [
            {
                'oferente': 'Hotel Las Rocas',
                'name': 'Suite Vista al Lago',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051141/4_xur8jl.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051148/suite-vista-lago_xtunrr.jpg',
                'checkIn': '2:00 pm',
                'checkOut': '12:00 pm',
                'items': {
                    'Tipo': 'Suite',
                },
                'description': 'Habitación con vista al lago.',
                'detalle': 'La Suite Vista al Lago ofrece una cama doble king size, balcón privado con una vista impresionante al lago, y una decoración moderna con un toque rústico. El baño cuenta con jacuzzi y artículos de tocador de lujo. El hospedaje incluye desayuno continental diario y servicio a la habitación disponible 24 horas.',
                'calificacion': 4.7,
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D',
                'precio': 150000,
                'metodosDePago': 'Efectivo, tarjeta y billeteras digitales',
                'servicios': {
                    'servicios': [
                        'Wi-Fi',
                        'Baño privado',
                        'TV',
                        'Desayuno incluido',
                        'Petfriendly',
                        'Estacionamiento',
                        'Balcón privado',
                        'Jacuzzi'
                    ]    
                },
                'equipamento': {
                    'habitaciones': 2,
                    'camas': 4,
                    'baños': 2,
                },
                'politicas': {
                    'Cancelacion': 'Cancelación gratuita hasta 48 horas antes del check-in.',
                    'Check In': 'Check-in a partir de las 2:00 pm',
                    'Check Out': 'Check-out a las 12:00 pm',
                    'Masctotas': 'Se permiten mascotas con un cargo adicional'
                },
                'imgs': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051138/5_dwdwj1.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051119/10_rg744b.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051115/7_vozgxd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051114/6_zm0lrd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/8_if0r6j.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/9_ipsqtr.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051110/11_susia5.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051109/4_oemmnu.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/3_jw52na.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/2_w7vspc.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051089/1_gzqflu.webp'
                ]
            },
            {
                'oferente': 'Hotel Las Rocas',
                'name': 'Suite Vista al Lago',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051141/4_xur8jl.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051148/suite-vista-lago_xtunrr.jpg',
                'checkIn': '2:00 pm',
                'checkOut': '12:00 pm',
                'items': {
                    'Tipo': 'Suite',
                },
                'description': 'Habitación con vista al lago.',
                'detalle': 'La Suite Vista al Lago ofrece una cama doble king size, balcón privado con una vista impresionante al lago, y una decoración moderna con un toque rústico. El baño cuenta con jacuzzi y artículos de tocador de lujo. El hospedaje incluye desayuno continental diario y servicio a la habitación disponible 24 horas.',
                'calificacion': 4.7,
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D',
                'precio': 150000,
                'metodosDePago': 'Efectivo, tarjeta y billeteras digitales',
                'servicios': {
                    'servicios': [
                        'Wi-Fi',
                        'Baño privado',
                        'TV',
                        'Desayuno incluido',
                        'Petfriendly',
                        'Estacionamiento',
                        'Balcón privado',
                        'Jacuzzi'
                    ]    
                },
                'equipamento': {
                    'habitaciones': 2,
                    'camas': 4,
                    'baños': 2,
                },
                'politicas': {
                    'Cancelacion': 'Cancelación gratuita hasta 48 horas antes del check-in.',
                    'Check In': 'Check-in a partir de las 2:00 pm',
                    'Check Out': 'Check-out a las 12:00 pm',
                    'Masctotas': 'Se permiten mascotas con un cargo adicional'
                },
                'imgs': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051138/5_dwdwj1.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051119/10_rg744b.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051115/7_vozgxd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051114/6_zm0lrd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/8_if0r6j.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/9_ipsqtr.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051110/11_susia5.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051109/4_oemmnu.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/3_jw52na.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/2_w7vspc.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051089/1_gzqflu.webp'
                ]
            },
            {
                'oferente': 'Hotel Las Rocas',
                'name': 'Suite Vista al Lago',
                'logo': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051141/4_xur8jl.jpg',
                'img': 'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051148/suite-vista-lago_xtunrr.jpg',
                'checkIn': '2:00 pm',
                'checkOut': '12:00 pm',
                'items': {
                    'Tipo': 'Suite',
                },
                'description': 'Habitación con vista al lago.',
                'detalle': 'La Suite Vista al Lago ofrece una cama doble king size, balcón privado con una vista impresionante al lago, y una decoración moderna con un toque rústico. El baño cuenta con jacuzzi y artículos de tocador de lujo. El hospedaje incluye desayuno continental diario y servicio a la habitación disponible 24 horas.',
                'calificacion': 4.7,
                'contacto': 3015081517,
                'address': 'https://www.google.com/maps/@5.1032266,-73.7993305,180m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D',
                'precio': 150000,
                'metodosDePago': 'Efectivo, tarjeta y billeteras digitales',
                'servicios': {
                    'servicios': [
                        'Wi-Fi',
                        'Baño privado',
                        'TV',
                        'Desayuno incluido',
                        'Petfriendly',
                        'Estacionamiento',
                        'Balcón privado',
                        'Jacuzzi'
                    ]    
                },
                'equipamento': {
                    'habitaciones': 2,
                    'camas': 4,
                    'baños': 2,
                },
                'politicas': {
                    'Cancelacion': 'Cancelación gratuita hasta 48 horas antes del check-in.',
                    'Check In': 'Check-in a partir de las 2:00 pm',
                    'Check Out': 'Check-out a las 12:00 pm',
                    'Masctotas': 'Se permiten mascotas con un cargo adicional'
                },
                'imgs': [
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051138/5_dwdwj1.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051119/10_rg744b.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051115/7_vozgxd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051114/6_zm0lrd.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/8_if0r6j.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051112/9_ipsqtr.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051110/11_susia5.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051109/4_oemmnu.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/3_jw52na.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051090/2_w7vspc.webp',
                    'https://res.cloudinary.com/dmyq0gr14/image/upload/v1729051089/1_gzqflu.webp'
                ]
            },
        ]
    )

def downgrade() -> None:
    pass
