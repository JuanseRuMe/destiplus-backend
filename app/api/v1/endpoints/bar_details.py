from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.bares_details import BarCRUD
from ....schemas.bares_details import BarDetailResponse

router = APIRouter()

@router.get("/bares/{name}/content", response_model = BarDetailResponse)
def get_bar_detail(name, db: Session = Depends(get_db)):
    bar = BarCRUD.get_detial_bar(db, name)
    if not bar:
        raise HTTPException(status_code=404, detail="Destino not found")
    return bar
