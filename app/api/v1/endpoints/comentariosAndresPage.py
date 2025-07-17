# app/api/v1/endpoints/comments.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

# Ajusta estas rutas de importación
from ....schemas.comentariosAndresPage import CommentCreate, CommentRead 
from ....crud.comentariosAndresPage import create_comment, get_comments_by_parent
from ....db.session import get_db # Asumiendo que tienes get_db

router = APIRouter()

@router.post("/crear/comentario/", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
def create_new_comment(
    comment_in: CommentCreate, 
    db: Session = Depends(get_db)
):
    """
    Crea un nuevo comentario.
    El frontend debe enviar `parent_type` ('blog' o 'project') y `parent_slug`.
    """
    # Aquí podrías añadir validaciones extra, como verificar si el parent_slug existe
    # antes de crear el comentario, pero para mantenerlo simple, lo omitimos por ahora.
    created_comment = create_comment(db=db, comment_in=comment_in)
    return created_comment

@router.get("/comentarios/{parent_type}/{parent_slug}", response_model=List[CommentRead])
def read_comments_for_parent(
    parent_type: str, # 'blog' o 'project'
    parent_slug: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100), # Límite por defecto y máximo
    # approved_only: bool = Query(True), # Descomenta si quieres controlarlo desde el cliente
    db: Session = Depends(get_db)
):
    """
    Obtiene los comentarios para un artículo o proyecto específico.
    Por defecto, solo devuelve comentarios aprobados.
    """
    if parent_type not in ["blog", "project"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid parent_type. Must be 'blog' or 'project'."
        )
    
    # Siempre traer solo aprobados para la vista pública
    comments = get_comments_by_parent(
        db, 
        parent_type=parent_type, 
        parent_slug=parent_slug, 
        skip=skip, 
        limit=limit,
        approved_only=True 
    )
    return comments