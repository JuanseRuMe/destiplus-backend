# app/crud/crud_article.py
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc # Para ordenar
from typing import List, Optional

from ..models.articulosAndresPage import Article

def get_articles_for_preview(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    featured: bool = False # Para determinar el orden
) -> List[Article]:
    """
    Obtiene una lista de artículos para previsualización.
    Si 'featured' es True, ordena por 'priority' y luego por 'published_date'.
    Si no, ordena solo por 'published_date'.
    """
    query = db.query(Article)

    if featured:
        query = query.order_by(asc(Article.priority), desc(Article.published_date))
    else:
        query = query.order_by(desc(Article.published_date))
    
    return query.offset(skip).limit(limit).all()
