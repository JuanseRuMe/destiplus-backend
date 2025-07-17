# app/crud/crud_article.py
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List, Optional

from ..models.articulosAndresPage import Article # Ajusta la ruta de importación

# --- NUEVA FUNCIÓN para obtener un artículo por slug ---
def get_article_by_slug(db: Session, slug: str) -> Optional[Article]:
    """
    Obtiene un único artículo por su slug.
    Por defecto, solo devuelve artículos activos.
    """
    query = db.query(Article).filter(Article.slug == slug)
    return query.first()

