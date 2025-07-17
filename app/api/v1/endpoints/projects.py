# app/api/v1/endpoints/projects.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

# Ajusta estas rutas de importación
from ....schemas.project import  ProjectDetail
from ....crud.crud_project import get_project_by_slug
from ....db.session import get_db

router = APIRouter()

# --- NUEVO ENDPOINT para obtener un proyecto completo por slug ---
@router.get("/project/{slug}", response_model=ProjectDetail)
def read_single_project(slug: str, db: Session = Depends(get_db)):
    """
    Obtiene un proyecto completo por su slug.
    """
    project = get_project_by_slug(db, slug=slug)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Proyecto con slug '{slug}' no encontrado."
        )
    return project # Pydantic serializará el objeto Project completo al schema ProjectDetail