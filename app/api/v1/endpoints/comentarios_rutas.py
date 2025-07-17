from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.comentarios_rutas import get_comentarios_by_ruta
from ....schemas.comentarios_rutas import ComentarioRutaResponse

router = APIRouter()

@router.get("/ruta/comentarios/{ruta_id}", response_model=List[ComentarioRutaResponse])
def read_comentarios_by_ruta(
    ruta_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Obtiene todos los comentarios de una ruta específica"""
    comentarios = get_comentarios_by_ruta(db, ruta_id=ruta_id, skip=skip, limit=limit)
    return comentarios