# app/models/comment.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from app.db.session import Base

Base = declarative_base() # O usa tu Base importada

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    parent_type = Column(String(50), nullable=False, index=True) # 'blog' o 'project'
    parent_slug = Column(String(255), nullable=False, index=True) # Slug del artículo o proyecto
    
    author_name = Column(String(150), nullable=False)
    content = Column(Text, nullable=False)
    avatar_color = Column(String(20), nullable=True) 

    is_approved = Column(Boolean, nullable=False, server_default=func.true()) # Por defecto, aprobados
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    # updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False) # Opcional para comentarios simples

    def __repr__(self):
        return f"<Comment(id={self.id}, author_name='{self.author_name}', parent_slug='{self.parent_slug}')>"