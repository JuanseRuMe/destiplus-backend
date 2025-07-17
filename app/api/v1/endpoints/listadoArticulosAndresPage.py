# app/api/v1/endpoints/articles.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

# Ajusta estas rutas de importación según tu estructura de proyecto
from ....schemas.listadoArticulosAndresPage import ArticlePreview # Usamos el schema de previsualización
from ....crud.listadoArticulosAndresPage import get_articles_for_preview
from ....db.session import get_db # Asumiendo que tienes get_db

router = APIRouter()

@router.get("/previews/andres/page", response_model=List[ArticlePreview])
def read_articles_for_preview(
    skip: int = Query(0, ge=0), 
    limit: int = Query(10, ge=1, le=100), # Límite por defecto y máximo
    featured: bool = Query(False), # Para carrusel de destacados
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista de artículos para previsualización.
    - `featured=true`: Ordena por prioridad para el carrusel del home (suele necesitar un `limit` pequeño, ej. 5).
    - `featured=false`: Ordena por fecha de publicación para la página de blog (usa `skip` y `limit` para paginación).
    """
    # Si es para 'featured', podrías querer un límite diferente por defecto
    actual_limit = 5 if featured and limit == 10 else limit # Ejemplo: si es featured y no se especifica limit, usa 5

    articles = get_articles_for_preview(
        db, 
        skip=skip, 
        limit=actual_limit, 
        featured=featured
    )
    if not articles:
        # Devolver una lista vacía es común y preferible a un 404 si la consulta es válida pero no hay resultados.
        return []
    return articles
