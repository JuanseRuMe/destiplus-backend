from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional

from ....crud.blogIndividual import get_article_by_slug
from ....schemas.blogIndividual import ArticleResponse
from ....db.session import get_db

router = APIRouter()

@router.get("/blog/{slug}", response_model=ArticleResponse)
def get_article(
    slug: str = Path(..., description="Slug of the article to retrieve"),
    db: Session = Depends(get_db)
):
    """
    Get a specific article by slug
    """
    article = get_article_by_slug(db, slug)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

