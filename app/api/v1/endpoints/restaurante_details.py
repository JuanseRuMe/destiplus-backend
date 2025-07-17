from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.restaurante_details import RestauranteCRUD
from ....schemas.restaurantes_details import RestauranteDetailResponse

router = APIRouter()

@router.get("/restaurante/{name}/content", response_model = RestauranteDetailResponse)
def get_restaurant_detail(name, db: Session = Depends(get_db)):
    restaurante = RestauranteCRUD.get_detial_restaurant(db, name)
    if not restaurante:
        raise HTTPException(status_code=404, detail="Destino not found")
    return restaurante
