# app/schemas/article.py
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Esquema para la previsualización de artículos (campos limitados)
class ArticlePreview(BaseModel):
    id: int
    slug: str
    title: str
    summary: Optional[str] = None
    hero_image_url: Optional[str] = None
    hero_image_alt: Optional[str] = None
    category: Optional[str] = None
    published_date: datetime 
    reading_time_minutes: Optional[int] = None

    class Config:
        from_attributes = True # Para Pydantic V2 (era orm_mode = True en V1)

