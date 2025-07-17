from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .....db.session import get_db
from .....crud.dashboardEstablecimientos.actividad import ActividadCRUD
from .....schemas.dashboarEstablecimientos.actividades import ActividadDetailResponse

router = APIRouter()

@router.get("/{usuario}/dashboard/actividad", response_model=ActividadDetailResponse)
def get_actividad_detail(usuario: str, db: Session = Depends(get_db)):
    actividad = ActividadCRUD.get_detial_actividad(db, usuario)
    if not actividad:
        raise HTTPException(status_code=404, detail="Actividad not found")
    return actividad
