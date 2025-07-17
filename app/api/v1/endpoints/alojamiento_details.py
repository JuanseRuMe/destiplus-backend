from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.alojamiento_details import AlojamientoCRUD
from ....schemas.alojamientos_detail import AlojamientoDetailResponse

router = APIRouter()

@router.get("/alojamiento/{name}/content", response_model = AlojamientoDetailResponse)
def get_alojamiento_detail(name, db: Session = Depends(get_db)):
    alojamiento = AlojamientoCRUD.get_detial_alojamiento(db, name)
    if not alojamiento:
        raise HTTPException(status_code=404, detail="Destino not found")
    return alojamiento
