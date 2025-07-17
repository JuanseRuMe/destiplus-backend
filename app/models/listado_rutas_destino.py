from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON, Boolean, DateTime
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from ..db.session import Base
from ..models.destino import Usuario, Destino

class ListadoRutas(Base):
    __tablename__ = 'rutas'
    
    id = Column(Integer, primary_key=True, index=True)
    destino_id = Column(Integer, ForeignKey("destinos.id"))
    img = Column(String, index=True)
    nombre = Column(String)
    calificacion = Column(Float)
    dificultad = Column(String)
    tiempo = Column(Integer)
    terreno = Column(String)
    distancia = Column(Float)  # Agregué el tipo Float que faltaba
    descripcion = Column(String)
    etiquetas = Column(JSON)
    veces_recomendada = Column(Integer)
    completaron_ruta = Column(Integer)
    items = Column(JSON)
    
    destino = relationship("Destino", back_populates="rutas")
    categorias = relationship("Categorias", back_populates="ruta")
    instrucciones = relationship("Instrucciones", back_populates="ruta")
    imagenes = relationship("Imagenes", back_populates="ruta")
    estaciones = relationship("Estaciones", back_populates="ruta")
    emergencias = relationship("Emergencias", back_populates="ruta")
    coordenadas_principales = relationship("CoordenadasPrincipales", back_populates="ruta")
    atajos = relationship("Atajos", back_populates="ruta")
    comentarios = relationship("Comentarios_Rutas", back_populates="ruta")

class Categorias(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    senderismo = Column(Boolean)
    bici_tour = Column(Boolean)
    moto = Column(Boolean)
    automovil = Column(Boolean)
    
    ruta = relationship("ListadoRutas", back_populates="categorias")

class Instrucciones(Base):
    __tablename__ = 'instrucciones'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    recomendaciones = Column(String)
    accesibilidad = Column(String)
    conservacion = Column(String)
    
    ruta = relationship("ListadoRutas", back_populates="instrucciones")

class Imagenes(Base):
    __tablename__ = 'imagenes'

    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    url = Column(String)
    
    ruta = relationship("ListadoRutas", back_populates="imagenes")

class Estaciones(Base):
    __tablename__ = 'estaciones'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    nombre = Column(String)
    dificultad = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    img = Column(String)
    description = Column(String)
    numero_estacion = Column(Integer)
    
    ruta = relationship("ListadoRutas", back_populates="estaciones")

class Emergencias(Base):
    __tablename__ = 'emergencias'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    tipo = Column(String)
    numero = Column(Integer)
    
    ruta = relationship("ListadoRutas", back_populates="emergencias")

class Atajos(Base):
    __tablename__ = 'atajos'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    nombre = Column(String)
    dificultad = Column(String)
    img = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    description = Column(String)
    numero_atajo = Column(Integer)
    
    ruta = relationship("ListadoRutas", back_populates="atajos")
    disponibilidad = relationship("DisponibilidadAtajos", back_populates="atajo")
    coordenadas = relationship("CoordenadasAtajos", back_populates="atajo")

class DisponibilidadAtajos(Base):
    __tablename__ = 'disponibilidad_atajos'
    
    id = Column(Integer, primary_key=True, index=True)
    atajo_id = Column(Integer, ForeignKey("atajos.id"))
    senderismo = Column(Boolean)
    bici_tour = Column(Boolean)
    moto = Column(Boolean)
    automovil = Column(Boolean)
    
    atajo = relationship("Atajos", back_populates="disponibilidad")

class CoordenadasPrincipales(Base):
    __tablename__ = 'coordenadas_principales'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id"))
    cordenadas = Column(JSON)
    
    ruta = relationship("ListadoRutas", back_populates="coordenadas_principales")

class CoordenadasAtajos(Base):
    __tablename__ = 'coordenadas_atajos'
    
    id = Column(Integer, primary_key=True, index=True)
    atajo_id = Column(Integer, ForeignKey("atajos.id"))
    cordenadas = Column(JSON)
    
    atajo = relationship("Atajos", back_populates="coordenadas")


class Comentarios_Rutas(Base):
    __tablename__ = 'comentarios_rutas'
    
    id = Column(Integer, primary_key=True, index=True)
    ruta_id = Column(Integer, ForeignKey("rutas.id", ondelete="CASCADE"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    comentario = Column(String, nullable=False)
    calificacion = Column(Integer, nullable=True)
    fecha_creacion = Column(DateTime, server_default=sa.text('now()'), nullable=False)
    estado = Column(String(20), server_default='pendiente', nullable=False)
    imagen = Column(String(255), nullable=True)
    
    # Relaciones
    usuario = relationship("Usuario", back_populates="comentarios_rutas")
    ruta = relationship("ListadoRutas", back_populates="comentarios")

