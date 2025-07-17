from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....db.session import get_db
from ....crud.coordenadas_ruta import RutaCoordenadaCRUD
from ....schemas.coordenadas_ruta import CoordenadasRutaResponse

router = APIRouter()

@router.get(
    "/ruta/mapa/{nombre}/content", 
    response_model=CoordenadasRutaResponse,
    summary="Obtener coordenadas y detalles de una ruta",
    description="Obtiene las coordenadas principales, estaciones, atajos y emergencias de una ruta específica"
)
def get_coordenada_content(
    nombre: str,
    db: Session = Depends(get_db)
):
    """
    Endpoint para obtener toda la información relacionada con las coordenadas de una ruta.
    
    Args:
        nombre: Nombre de la ruta a buscar
        db: Sesión de la base de datos
    
    Returns:
        CoordenadasRutaResponse: Información completa de la ruta incluyendo coordenadas,
        estaciones, atajos y emergencias
    
    Raises:
        HTTPException: Si la ruta no se encuentra (404)
    """
    ruta_coordenada = RutaCoordenadaCRUD.get_coordenada_content(db, nombre)
    if not ruta_coordenada:
        raise HTTPException(
            status_code=404, 
            detail=f"No se encontró la ruta con nombre: {nombre}"
        )
    return ruta_coordenada