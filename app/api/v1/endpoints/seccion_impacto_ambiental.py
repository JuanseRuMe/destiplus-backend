from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from ....db.session import get_db
from ....models import listado_rutas_destino
from ....schemas.seccion_impacto_ambiental import ArbolesInfoResponse
from ....crud import seccion_impacto_ambiental

router = APIRouter()

@router.get("/arboles-info", response_model=ArbolesInfoResponse)
def get_arboles_info(
    ruta_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Obtiene información completa de árboles plantados con todos sus detalles.
    
    Args:
        ruta_id: Filtrar por una ruta específica (opcional)
        db: Sesión de base de datos
        
    Returns:
        Información completa de árboles plantados y estadísticas
    """
    # Verificar que la ruta existe si se proporciona un ID
    if ruta_id is not None:
        ruta = db.query(listado_rutas_destino).filter(listado_rutas_destino.id == ruta_id).first()
        if ruta is None:
            raise HTTPException(status_code=404, detail="Ruta no encontrada")
    
    # Obtener datos completos
    return seccion_impacto_ambiental.get_arboles_info_completa(db, ruta_id=ruta_id)