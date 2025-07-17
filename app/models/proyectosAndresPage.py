# app/models/project.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.ext.declarative import declarative_base
from app.db.session import Base

Base = declarative_base() # O usa tu Base importada

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True) # Para la tarjeta/preview
    content = Column(JSONB, nullable=True) # Contenido detallado (array de ContentBlock)
    
    category = Column(String(100), nullable=True, index=True)
    author = Column(String(150), nullable=True) 
    
    status = Column(String(50), nullable=False) # Ej: 'Completado', 'En Progreso', 'Idea'
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=True)
    duration_text = Column(String(100), nullable=True) 
    display_date = Column(String(100), nullable=True)

    image_url = Column(Text, nullable=True) # Imagen para la tarjeta (podría ser la misma que hero)
    hero_image_url = Column(Text, nullable=True) # Imagen principal para la página de detalle
    hero_image_alt = Column(Text, nullable=True)
    
    project_url = Column(Text, nullable=True) # Enlace al demo o sitio en vivo
    repository_url = Column(Text, nullable=True) # Enlace al repositorio (GitHub, etc.)
    
    technologies_used = Column(ARRAY(Text), nullable=True)
    
    recommendation_links = Column(JSONB, nullable=True)
    
    priority = Column(Integer, nullable=True, server_default='100', index=True)
    # Eliminamos la columna is_active según tu solicitud para esta API/tabla

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Project(id={self.id}, slug='{self.slug}', title='{self.title[:30]}...')>"