from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .....crud.dashboardEdit.bloquearFechas import get_fechas_bloqueadas, create_bloqueo, delete_bloqueo
from .....schemas.dashboardEdit.bloquearFechas import ReservaBloqueoCreate
from .....db.session import get_db
from datetime import datetime

router = APIRouter()

# 1. Obtener fechas bloqueadas
@router.get("/{alojamiento_id}/tipo/{tipo_alojamiento_id}/fechas-bloqueadas/")
async def obtener_fechas_bloqueadas(
    alojamiento_id: int,
    tipo_alojamiento_id: str,
    db: Session = Depends(get_db)
):
    try:
        fechas = get_fechas_bloqueadas(db, alojamiento_id, tipo_alojamiento_id)
        if not fechas:
            return {"fechas": []}
        return {"fechas": fechas}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

# 2. Bloquear fechas
@router.post("/bloquear/")
async def bloquear_fechas(
    bloqueo: ReservaBloqueoCreate,
    db: Session = Depends(get_db)
):
    return create_bloqueo(db, bloqueo)

# 3. Eliminar bloqueo
@router.delete("/bloqueos/{reserva_id}")
async def eliminar_bloqueo(
    reserva_id: int,
    db: Session = Depends(get_db)
):
    return delete_bloqueo(db, reserva_id)