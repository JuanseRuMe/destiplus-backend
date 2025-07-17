# app/crud/crud_comment.py
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Optional

# Ajusta las rutas de importación según tu estructura
from ..models.comentariosAndresPage import Comment as CommentModel 
from ..schemas.comentariosAndresPage import CommentCreate

def create_comment(db: Session, comment_in: CommentCreate) -> CommentModel:
    """
    Crea un nuevo comentario en la base de datos.
    """
    db_comment = CommentModel(
        parent_type=comment_in.parent_type,
        parent_slug=comment_in.parent_slug,
        author_name=comment_in.author_name,
        content=comment_in.content,
        avatar_color=comment_in.avatar_color
        # is_approved usará el server_default (True)
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_parent(
    db: Session, 
    parent_type: str, 
    parent_slug: str, 
    skip: int = 0, 
    limit: int = 20,
    approved_only: bool = True # Por defecto, solo comentarios aprobados
) -> List[CommentModel]:
    """
    Obtiene los comentarios para un 'parent' específico (artículo o proyecto),
    ordenados por fecha de creación (más recientes primero).
    """
    query = db.query(CommentModel)\
              .filter(CommentModel.parent_type == parent_type, CommentModel.parent_slug == parent_slug)
    
    if approved_only:
        query = query.filter(CommentModel.is_approved == True)
        
    return query.order_by(desc(CommentModel.created_at)).offset(skip).limit(limit).all()

# No se necesitan get_comment_by_id, update, o delete para la versión "extremadamente sencilla" de solo enviar y leer lista.