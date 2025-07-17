from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from typing import List, Optional, Dict, Any

from ..models.blogs import Article

def get_article_by_slug(db: Session, slug: str) -> Optional[Article]:
    """Get article by slug"""
    return db.query(Article).filter(Article.slug == slug).first()

