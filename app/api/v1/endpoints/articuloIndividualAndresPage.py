# app/api/v1/endpoints/articles.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

# Ajusta rutas de importación
from ....schemas.blogIndividualAndresPage import ArticlePreview, ArticleDetail # Añadimos ArticleDetail
from ....crud.blogIndividualAndresPage import get_article_by_slug
from ....db.session import get_db

router = APIRouter()

# --- NUEVO ENDPOINT para obtener un artículo completo por slug ---
@router.get("/blog/andres/{slug}", response_model=ArticleDetail)
def read_single_article(slug: str, db: Session = Depends(get_db)):
    """
    Obtiene un artículo completo por su slug.
    Devuelve solo artículos activos por defecto.
    """
    article = get_article_by_slug(db, slug=slug) # Solo activos
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Artículo con slug '{slug}' no encontrado o no está activo."
        )
    return article # Pydantic se encarga de serializar todos los campos de ArticleDetail