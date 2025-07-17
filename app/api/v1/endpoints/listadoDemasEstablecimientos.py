from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ....schemas.listadoDemasEstablecimientos import ItemResponse
from ....db.session import get_db
from ....crud.listadoDemasEstablecimientos import get_items_by_destino

router = APIRouter()

@router.get("/listados/demas/{destino_id}/{tipo}", response_model=List[ItemResponse])
async def get_listado(
   destino_id: int,
   tipo: str,
   db: Session = Depends(get_db)
):
   if tipo not in ["eventos", "actividades", "alojamientos"]:
       raise HTTPException(status_code=400, detail="Tipo no válido")
       
   return get_items_by_destino(db, destino_id, tipo)