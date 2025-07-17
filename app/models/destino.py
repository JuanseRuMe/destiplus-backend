from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..db.session import Base

__all__ = ['Restaurante', 'Bar', 'Actividad', 'Alojamiento']

class Destino(Base):
    __tablename__ = 'destinos'
    
    id = Column(Integer, primary_key = True, index = True)
    municipio = Column(String, index = True)
    departamento = Column(String, index = True)
    lat = Column(Float)
    lng = Column(Float)
    frase = Column(String)
    descripcion = Column(String)
    epocas = Column(String)
    clima = Column(String)
    seguridad = Column(String)
    transporte = Column(String)
    img = Column(String)
    calificacion = Column(Float)
    items = Column(JSON)
    imagenes = Column(JSON)
    completado = Column(Boolean)

    restaurantes = relationship('Restaurante', back_populates='destino')
    bares = relationship('Bar', back_populates='destino')
    tendencias = relationship('Tendencia', back_populates='destino')
    actividades = relationship('Actividad', back_populates='destino')
    eventos = relationship('Evento', back_populates='destino')
    alojamientos = relationship('Alojamiento', back_populates='destino')
    rutas = relationship('ListadoRutas', back_populates='destino')
    
class Restaurante(Base):
    __tablename__ = 'restaurante'
    
    id = Column(Integer, primary_key = True)
    usuario = Column(String)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    name = Column(String)
    items = Column(JSON)
    calificacion = Column(Float)
    precio_promedio = Column(Integer)
    img = Column(String)
    logo = Column(String)
    concepto = Column(String)
    horario = Column(JSON)
    contacto = Column(Integer)
    metodosdepago = Column(String)
    servicios = Column(JSON)
    destacados = Column(JSON)
    recurrentes = Column(JSON)
    antojos = Column(JSON)
    bebidas = Column(JSON)
    imgs = Column(JSON)
    coordenadas = Column(JSON)
    
    destino = relationship("Destino", back_populates = "restaurantes")

class Bar(Base):
    __tablename__ = 'bares'
    
    id = Column(Integer, primary_key = True, index = True)
    usuario = Column(String)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    name = Column(String, index = True)
    items = Column(JSON, index = True)
    calificacion = Column(Float, index = True)
    precio_promedio = Column(Integer, index = True)
    img = Column(String, index = True)
    logo = Column(String, index = True)
    concepto = Column(String, index = True)
    horario = Column(JSON, index = True)
    contacto = Column(String, index = True)
    metodos_de_pago = Column(String, index = True)
    servicios = Column(JSON, index = True)
    destacados = Column(JSON, index = True)
    recurrente = Column(JSON, index = True)
    antojos = Column(JSON, index = True)
    bebidas = Column(JSON, index = True)
    imgs = Column(JSON, index = True)
    coordenadas = Column(JSON)
    
    destino = relationship("Destino", back_populates = "bares")


class Tendencia(Base):
    __tablename__ = 'tendencias'
    
    id = Column(Integer, primary_key=True, index=True)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    img = Column(String)
    
    destino = relationship("Destino", back_populates="tendencias")

class Actividad(Base):
    __tablename__ = 'actividades'
    
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    logo = Column(String)
    oferente = Column(String)
    horario = Column(JSON)
    contacto = Column(Integer)
    metodosDePago = Column(String)
    actividad = Column(JSON)
    coordenadas = Column(JSON)
    
    destino = relationship("Destino", back_populates="actividades")

class Evento(Base):
    __tablename__ = 'eventos'
    
    id = Column(Integer, primary_key=True, index=True)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    logo = Column(String)
    oferente = Column(String)
    metodosdepago = Column(String)
    contacto = Column(Integer)
    evento = Column(JSON)
    coordenadas = Column(JSON)

    destino = relationship("Destino", back_populates="eventos")

class Alojamiento(Base):
    __tablename__ = 'alojamientos'
    
    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    oferente = Column(String)
    logo = Column(String)
    checkIn = Column(String)
    checkOut = Column(String)
    contacto = Column(Integer)
    metodosDePago = Column(String)
    politicas = Column(JSON)
    coordenadas = Column(JSON)
    alojamiento = Column(JSON)
    
    reservas = relationship("Reserva", back_populates="alojamiento")
    destino = relationship("Destino", back_populates="alojamientos")
    
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    email = Column(String)
    whatsapp = Column(Integer)
    ciudad = Column(String)
    edad = Column(Integer)
    foto_perfil = Column(String)

    reservas = relationship("Reserva", back_populates="usuario")
    comentarios_rutas = relationship("Comentarios_Rutas", back_populates="usuario")


class Reserva(Base):
    __tablename__ = 'reservas'

    id = Column(Integer, primary_key=True, index=True)
    alojamiento_id = Column(Integer, ForeignKey("alojamientos.id"))
    tipo_alojamiento_id = Column(String)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)  # Nullable para bloqueos
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    total_pagado = Column(Float, nullable=True)  # Nullable para bloqueos
    metodo_pago = Column(String, nullable=True)  # Nullable para bloqueos
    estado = Column(String) 
    huespedes = Column(Integer, nullable=True)  # Nullable para bloqueos
    destino_id = Column(Integer)
    
    alojamiento = relationship("Alojamiento", back_populates="reservas")
    usuario = relationship("Usuario", back_populates="reservas")

class ArbolesDonados(Base):
    __tablename__ = 'donaciones_arboles'

    id = Column(Integer, primary_key=True, index=True)
    donante_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    donante_nombre = Column(String(255), nullable=False)
    fecha_donacion = Column(DateTime, nullable=False)
    cantidad_total = Column(Integer, nullable=False)
    descripcion = Column(String, nullable=True)
    estado = Column(String(50), nullable=False, server_default='activa')
    
    # Relaciones
    arboles = relationship("ArbolesPlantados", back_populates="donacion")

class ArbolesPlantados(Base):
    __tablename__ = 'arboles_plantados'

    id = Column(Integer, primary_key=True, index=True)
    donacion_id = Column(Integer, ForeignKey("donaciones_arboles.id"), nullable=True)
    plantador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    fecha_plantacion = Column(DateTime, nullable=False)
    ubicacion_geografica = Column(String(100), nullable=True)  # Formato: 'lat,long'
    ruta_id = Column(Integer, ForeignKey("rutas.id", ondelete="SET NULL"), nullable=True)
    nombre_ubicacion = Column(String(255), nullable=True)
    region = Column(String(100), nullable=True)
    pais = Column(String(100), nullable=True)
    especie = Column(String(255), nullable=True)
    estado_actual = Column(String(50), nullable=False, server_default='plantado')
    imagen_url = Column(String(512), nullable=True)
    descripcion = Column(String, nullable=True)
    co2_estimado = Column(Float, nullable=True)
    
    # Relaciones
    donacion = relationship("ArbolesDonados", back_populates="arboles")