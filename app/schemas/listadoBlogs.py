from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime


class ArticlePreview(BaseModel):
    """Esquema para la previsualización de artículos"""
    slug: str
    title: str
    category: str 
    hero_image_url: str
    excerpt: str 
    prioridad: int

    class Config:
        from_attributes = True  # Para permitir la conversión automática de objetos SQLAlchemy a Pydantic
        populate_by_name = True  # Para permitir el uso de alias


class ArticlePreviewList(BaseModel):
    """Lista de previsualizaciones de artículos"""
    articles: List[ArticlePreview]