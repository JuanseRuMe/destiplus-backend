# app/schemas/project.py
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Literal
from datetime import datetime

class ContentBlockSchema(BaseModel):
    type: Literal['paragraph', 'heading', 'image', 'list', 'quote', 'code_block']
    text: Optional[str] = None
    level: Optional[int] = None
    url: Optional[HttpUrl] = None # Pydantic validará que sea una URL
    alt: Optional[str] = None
    caption: Optional[str] = None
    items: Optional[List[str]] = None
    cite: Optional[str] = None
    code: Optional[str] = None
    language: Optional[str] = None

    class Config:
        from_attributes = True

# --- Esquema para Enlaces de Recomendación (Reutilizable) ---
class RecommendationLinkSchema(BaseModel):
    title: str
    url: HttpUrl
    description: Optional[str] = None
    icon_name: Optional[str] = None # El frontend mapeará esto a un ReactNode

    class Config:
        from_attributes = True

# --- Esquema para la Previsualización de Proyectos (ya lo teníamos) ---
class ProjectPreview(BaseModel):
    id: int
    slug: str
    title: str
    description: Optional[str] = None
    hero_image_url: Optional[HttpUrl] = None
    status: str
    repository_url: Optional[HttpUrl] = None
    project_url: Optional[HttpUrl] = None
    technologies_used: Optional[List[str]] = []

    class Config:
        from_attributes = True

# --- NUEVO: Esquema para el Detalle Completo del Proyecto ---
class ProjectDetail(BaseModel):
    id: int
    slug: str
    title: str
    description: Optional[str] = None
    content: Optional[List[ContentBlockSchema]] = [] # Contenido completo
    
    category: Optional[str] = None
    author: Optional[str] = None # Manteniendo por si lo usas
    
    status: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    duration_text: Optional[str] = None
    display_date: Optional[str] = None # Para fecha pre-formateada si la envías

    image_url: Optional[HttpUrl] = None # Podría ser la misma que hero_image_url o una específica para card
    hero_image_url: Optional[HttpUrl] = None # Imagen principal del detalle
    hero_image_alt: Optional[str] = None
    
    project_url: Optional[HttpUrl] = None
    repository_url: Optional[HttpUrl] = None
    
    technologies_used: Optional[List[str]] = []
    
    recommendation_links: Optional[List[RecommendationLinkSchema]] = []
    
    priority: Optional[int] = None
    # No incluimos is_active en la respuesta ya que la columna se eliminó/ignora

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True