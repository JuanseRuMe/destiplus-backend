from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.actividad_details import ActividadCRUD
from ....schemas.actividad_details import ActividadDetailResponse

router = APIRouter()

@router.get("/actividad/{description}/content", response_model = ActividadDetailResponse)
def get_actividad_detail(description, db: Session = Depends(get_db)):
    actividad = ActividadCRUD.get_detial_actividad(db, description)
    if not actividad:
        raise HTTPException(status_code=404, detail="Destino not found")
    return actividad
