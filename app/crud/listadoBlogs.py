from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import desc

from ..models.blogs import Article
from ..schemas.listadoBlogs import ArticlePreview


def get_article_previews(
    db: Session, 
) -> List[Article]:
    
    query = db.query(Article)

    
    # Aplicar paginación
    articles = query.all()
    
    return articles
