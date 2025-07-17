# endpoints/destino.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ....schemas.destinoFiltros import DestinoFiltroResponse
from ....db.session import get_db
from ....crud.destinoFiltros import get_all_destinos

router = APIRouter()

@router.get("/destinos/filtros", response_model=List[DestinoFiltroResponse])
def read_destinos(db: Session = Depends(get_db)):
    destinos = get_all_destinos(db)
    if not destinos:
        raise HTTPException(status_code=404, detail="No se encontraron destinos")
    return destinos