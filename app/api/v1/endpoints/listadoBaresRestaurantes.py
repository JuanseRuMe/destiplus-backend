from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from enum import Enum

from ....db.session import get_db
from ....schemas.listadoBarRestaurantes import ListadoResponse
from ....crud.listadoBarRestaurantes import ListadoCRUD

class TipoListado(str, Enum):
    restaurantes = "restaurantes"
    bares = "bares"

router = APIRouter()

@router.get(
    "/listados/{destino_id}/{tipo}",
    response_model=List[ListadoResponse],
    description="Obtiene listado de restaurantes o bares por destino"
)
def get_listado(
    destino_id: int = Path(..., description="ID del destino"),
    tipo: TipoListado = Path(..., description="Tipo de listado"),
    db: Session = Depends(get_db)
):
    listado = ListadoCRUD.get_listado(db, destino_id, tipo.value)
    if not listado:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontró listado de {tipo} para el destino {destino_id}"
        )
    return listado