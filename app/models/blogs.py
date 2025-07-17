from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB
from sqlalchemy.ext.declarative import declarative_base
from ..db.session import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    slug = Column(String(255), unique=True, nullable=False, index=True) # Alembic ya lo indexa por unique=True
    title = Column(Text, nullable=False)
    category = Column(String(100), nullable=True)
    author = Column(String(150), nullable=True)
    publication_date = Column(DateTime(timezone=True), nullable=False)
    display_date = Column(String(50), nullable=True)
    reading_time = Column(String(30), nullable=True)
    hero_image_url = Column(Text, nullable=True)
    hero_image_alt = Column(Text, nullable=True)
    excerpt = Column(Text, nullable=True) # Este es el campo que asumimos para "expert"
    meta_description = Column(Text, nullable=True)
    keywords = Column(ARRAY(Text), nullable=True)
    content = Column(JSONB, nullable=False)
    related_articles = Column(JSONB, nullable=True)
    
    prioridad = Column(Integer, nullable=True, default=100, index=True) 

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
