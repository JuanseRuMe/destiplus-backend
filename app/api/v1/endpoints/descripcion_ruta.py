from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.descripcion_ruta import RutasCRUD
from ....schemas.descripcion_ruta import RutaResponse

router = APIRouter()

@router.get("/caracteristicas/{nombre}/content", response_model = RutaResponse)
def get_ruta_content(
    nombre: str,
    db: Session = Depends(get_db)
):
    ruta = RutasCRUD.get_ruta_content(db, nombre)
    if not ruta:
        raise HTTPException(status_code=404, detail="Ruta not found")
    return ruta