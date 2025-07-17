# app/schemas/project.py
from pydantic import BaseModel, HttpUrl
from typing import Optional, List
from datetime import datetime # Aunque no la uses directamente en Preview, es bueno tenerla si la necesitas en otros esquemas.

# Esquema para la previsualización de proyectos
class ProjectPreview(BaseModel):
    id: int
    slug: str
    title: str
    description: Optional[str] = None # Mapea a 'summary' en tu frontend
    hero_image_url: Optional[HttpUrl] = None # O image_url, decide cuál usar para el preview
    status: str
    repository_url: Optional[HttpUrl] = None
    project_url: Optional[HttpUrl] = None
    technologies_used: Optional[List[str]] = [] # Incluido porque es útil para tarjetas

    class Config:
        from_attributes = True