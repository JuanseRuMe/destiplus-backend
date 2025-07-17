# app/schemas/article.py
from pydantic import BaseModel, HttpUrl # HttpUrl para validar URLs
from typing import Optional, List, Literal, Union # Literal para el type de ContentBlock
from datetime import datetime

# --- Esquema para Bloques de Contenido ---
class ContentBlockSchema(BaseModel):
    type: Literal['paragraph', 'heading', 'image', 'list', 'quote', 'code_block']
    text: Optional[str] = None
    level: Optional[int] = None # Para 'heading' (ej: 2 para H2)
    url: Optional[HttpUrl] = None # Para 'image'
    alt: Optional[str] = None
    caption: Optional[str] = None
    items: Optional[List[str]] = None # Para 'list'
    cite: Optional[str] = None # Para 'quote'
    code: Optional[str] = None # Para 'code_block'
    language: Optional[str] = None # Para 'code_block'

    class Config:
        from_attributes = True

# --- Esquema para Enlaces de Recomendación ---
class RecommendationLinkSchema(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None
    icon_name: Optional[str] = None # ej: "FaBook", el frontend lo mapeará

    class Config:
        from_attributes = True

# --- Esquema para la Previsualización de Artículos (ya lo teníamos) ---
class ArticlePreview(BaseModel):
    id: int
    slug: str
    title: str
    summary: Optional[str] = None
    hero_image_url: Optional[HttpUrl] = None
    hero_image_alt: Optional[str] = None
    category: Optional[str] = None
    published_date: datetime
    reading_time_minutes: Optional[int] = None
    # tags: Optional[List[str]] = None # Descomenta si la API de preview devuelve tags

    class Config:
        from_attributes = True

# --- NUEVO: Esquema para el Detalle Completo del Artículo ---
class ArticleDetail(BaseModel): # Podría heredar de ArticlePreview si muchos campos coinciden
    id: int
    slug: str
    title: str
    summary: Optional[str] = None
    content: List[ContentBlockSchema] # Contenido completo como lista de bloques
    category: Optional[str] = None
    author: Optional[str] = None
    published_date: datetime
    display_date: Optional[str] = None # Fecha formateada, opcional si el frontend la calcula
    reading_time_minutes: Optional[int] = None
    hero_image_url: Optional[HttpUrl] = None
    hero_image_alt: Optional[str] = None
    tags: Optional[List[str]] = None
    meta_description: Optional[str] = None
    keywords: Optional[List[str]] = None
    recommendation_links: Optional[List[RecommendationLinkSchema]] = None # Nueva sección
    priority: Optional[int] = None # Si quieres devolverlo

    # Campos de auditoría (opcional incluirlos en la respuesta)
    # created_at: datetime
    # updated_at: datetime

    class Config:
        from_attributes = True