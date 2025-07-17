# Asumo que este código está en tu archivo de esquemas, por ejemplo, schemas/blogIndividual.py
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

# Paso 1: Define un nuevo modelo Pydantic para la estructura de un artículo relacionado
class RelatedArticleItem(BaseModel):
    slug: str
    title: str
    category: Optional[str] = None
    imageUrl: Optional[str] = None # Basado en el 'input' del error

    class Config:
        from_attributes = True # Si estos datos también vienen de un modelo SQLAlchemy


class ArticleBase(BaseModel):
    slug: str
    title: str
    category: Optional[str] = None
    author: Optional[str] = None
    publication_date: datetime
    display_date: Optional[str] = None
    reading_time: Optional[str] = None
    hero_image_url: Optional[str] = None
    hero_image_alt: Optional[str] = None
    excerpt: Optional[str] = None
    meta_description: Optional[str] = None
    keywords: Optional[List[str]] = None
    content: Union[Dict[str, Any], List[Dict[str, Any]]]
    # Paso 2: Actualiza el tipo de related_articles
    related_articles: Optional[List[RelatedArticleItem]] = None # Cambiado de Dict a List[RelatedArticleItem]
    prioridad: Optional[int] = Field(default=100)


class ArticleInDB(ArticleBase):
    """Schema for returned Article with ID and timestamps"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ArticleResponse(ArticleInDB):
    """Public response schema for Article"""
    pass