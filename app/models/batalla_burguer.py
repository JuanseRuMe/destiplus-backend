# models.py
from sqlalchemy import (Column, Integer, String, Float, Text, TIMESTAMP, 
                        CheckConstraint, UniqueConstraint, Index) # Import Index if needed separately, usually handled in Column
from sqlalchemy.sql import func # Para func.now()
from sqlalchemy.dialects.postgresql import INET # Opcional para IP

from ..db.session import Base

class BurgerVote(Base):
    __tablename__ = 'burger_battle_votes_2025' # Nombre exacto de la tabla creada con Alembic

    # --- Columnas ---
    id = Column(Integer, primary_key=True, comment='Identificador único del voto')

    # Datos del Votante
    email = Column(String(255), nullable=False, index=True, comment='Correo electrónico del votante')
    full_name = Column(String(255), nullable=False, comment='Nombre completo del votante')
    rating = Column(Integer, nullable=False, comment='Calificación de 1 a 10')
    recommendations = Column(Text, nullable=True, comment='Comentarios o recomendaciones')
    origin = Column(String(255), nullable=True, comment='Lugar de origen/visita del votante')

    # Datos de la Hamburguesa
    burger_name = Column(String(255), nullable=False, comment='Nombre de la hamburguesa votada')
    restaurant_name = Column(String(255), nullable=False, comment='Nombre del restaurante')
    burger_id = Column(Integer, nullable=False, index=True, comment='ID de la hamburguesa votada (para referencia)')

    # Datos de Geolocalización y Auditoría
    latitude = Column(Float, nullable=True, comment='Latitud del votante al momento de votar')
    longitude = Column(Float, nullable=True, comment='Longitud del votante al momento de votar')
    # ip_address = Column(INET, nullable=True, comment='Dirección IP del votante') # Si usas INET
    ip_address = Column(String(100), nullable=True, comment='Dirección IP del votante') # Alternativa con String

    # Marca de Tiempo
    voted_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(), # Gestionado por la DB
        comment='Fecha y hora en que se registró el voto'
    )

    # --- Restricciones definidas en Alembic (no es necesario repetirlas aquí para la operación,
    # pero es bueno tenerlas documentadas o referenciadas) ---
    # CheckConstraint('rating >= 1 AND rating <= 10', name='ck_burger_battle_votes_2025_rating')
    # UniqueConstraint('email', 'burger_id', name='uq_burger_battle_votes_2025_email_burger_id')

    def __repr__(self):
        return f"<BurgerVote(id={self.id}, email='{self.email}', burger_id={self.burger_id}, rating={self.rating})>"