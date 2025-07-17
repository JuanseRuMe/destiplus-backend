from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .....db.session import get_db
from .....crud.dashboardEstablecimientos.alojamientos import AlojamientoCRUD
from .....schemas.dashboarEstablecimientos.alojamientos import AlojamientoDetailResponse

router = APIRouter()

@router.get("/dashboard/{usuario}/aloja", response_model = AlojamientoDetailResponse)
def get_alojamiento_detail(usuario, db: Session = Depends(get_db)):
    alojamiento = AlojamientoCRUD.get_detial_alojamiento(db, usuario)
    if not alojamiento:
        raise HTTPException(status_code=404, detail="Destino not found")
    return alojamiento
