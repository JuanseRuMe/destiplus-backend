# app/models/article.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.ext.declarative import declarative_base
from ..db.session import Base

Base = declarative_base() # O usa tu Base importada

class Article(Base):
    __tablename__ = 'articles_andres_page'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    slug = Column(String(255), unique=True, nullable=False, index=True)
    title = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    content = Column(JSONB, nullable=False) # Para ContentBlock[]
    category = Column(String(100), nullable=True, index=True)
    author = Column(String(150), nullable=True)
    published_date = Column(DateTime(timezone=True), nullable=False)
    reading_time_minutes = Column(Integer, nullable=True)
    hero_image_url = Column(Text, nullable=True)
    hero_image_alt = Column(Text, nullable=True)
    tags = Column(ARRAY(Text), nullable=True)
    
    meta_description = Column(Text, nullable=True)
    keywords = Column(ARRAY(Text), nullable=True)
    
    recommendation_links = Column(JSONB, nullable=True) # Para [{"title": ..., "url": ..., ...}]
    
    priority = Column(Integer, nullable=True, server_default='100', index=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<Article(id={self.id}, slug='{self.slug}', title='{self.title[:30]}...')>"