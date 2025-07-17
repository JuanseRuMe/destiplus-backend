from typing import Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from ....db.session import get_db
from ....crud.listadoBlogs  import get_article_previews
from ....schemas.listadoBlogs import ArticlePreview, ArticlePreviewList

router = APIRouter()


@router.get("/previews", response_model=ArticlePreviewList)
def read_article_previews(
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista paginada de previsualizaciones de artículos.
    Opcionalmente se puede filtrar por categoría.
    """
    articles = get_article_previews(
        db=db, 
    )
    
    # Convertir los artículos en previsualizaciones usando el esquema Pydantic
    article_previews = [
        ArticlePreview(
            slug=article.slug,
            title=article.title,
            category=article.category,
            hero_image_url=article.hero_image_url,
            excerpt=article.excerpt,
            prioridad=article.prioridad
        ) 
        for article in articles
    ]
    
    return ArticlePreviewList(articles=article_previews)
