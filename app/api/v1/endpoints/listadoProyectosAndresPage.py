# app/api/v1/endpoints/projects.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

# Ajusta estas rutas de importación
from ....schemas.listadoProyectosAndresPage import ProjectPreview 
from ....crud.listadoProyectosAndresPage import get_projects_for_preview
from ....db.session import get_db

router = APIRouter()

@router.get("/previews/projects", response_model=List[ProjectPreview])
def read_projects_for_preview(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100), # Límite por defecto y máximo
    featured: bool = Query(False), # Para carrusel de destacados en home
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista de proyectos para previsualización.
    - `featured=true`: Ordena por prioridad (ideal para el carrusel del home, usar con un `limit` pequeño).
    - `featured=false`: Ordena por fecha (ideal para la página de listado de proyectos).
    No se aplica filtro de 'is_active'.
    """
    # Ajusta el límite si es 'featured' y el cliente no especifica un límite menor
    actual_limit = 6 if featured and limit == 10 else limit 

    projects = get_projects_for_preview(
        db, 
        skip=skip, 
        limit=actual_limit,
        featured=featured
    )
    if not projects:
        return [] # Devuelve lista vacía si no hay resultados
    return projects
