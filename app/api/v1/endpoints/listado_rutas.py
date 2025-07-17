from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from enum import Enum

from ....db.session import get_db
from ....crud.lista_rutas import ListadoRutasCRUD
from ....schemas.listado_rutas import ListadoRutasDetailResponse

# Enum para validar categorías
class CategoriaEnum(str, Enum):
    senderismo = "Senderismo"
    bici_tour = "BiciTour"
    moto = "Moto"
    automovil = "Automovil"

router = APIRouter()

@router.get(
    "/rutas/{destino_id}/{categoria}/content",
    response_model=List[ListadoRutasDetailResponse],  # Nota: ahora es una lista
    description="Obtiene las rutas filtradas por destino y categoría"
)
def get_rutas_por_categoria(
    categoria: CategoriaEnum = Path(..., description="Categoría de la ruta"),
    destino_id: int = Path(..., description="ID del destino"),
    db: Session = Depends(get_db)
):
    listado_rutas = ListadoRutasCRUD.get_listado_rutas_content(
        db=db,
        categoria_tipo=categoria.value,
        destino_id=destino_id
    )
    
    if not listado_rutas:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron rutas para el destino {destino_id} en la categoría {categoria}"
        )
    
    return listado_rutas
