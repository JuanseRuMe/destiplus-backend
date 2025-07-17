from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.eventos_detail import EventoCRUD
from ....schemas.eventos_details import EventosDetailResponse

router = APIRouter()

@router.get("/evento/{description}/content", response_model = EventosDetailResponse)
def get_evento_detail(description, db: Session = Depends(get_db)):
    evento = EventoCRUD.get_detial_evento(db, description)
    if not evento:
        raise HTTPException(status_code=404, detail="Destino not found")
    return evento
