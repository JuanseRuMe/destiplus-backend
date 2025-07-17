from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Union

from .....db.session import get_db
from .....crud.dashboardEstablecimientos.restauranteBar import RestauranteCRUD, BaresCRUD
from .....schemas.dashboarEstablecimientos.restauranteBar import RestauranteDetailResponse, BarDetailResponse

router = APIRouter()

@router.get("/{tipo}/{usuario}/dashboard", response_model=Union[RestauranteDetailResponse, BarDetailResponse])
def get_establishment_detail(tipo: str, usuario: str, db: Session = Depends(get_db)):
    if tipo.lower() == "restaurante":
        establishment = RestauranteCRUD.get_detial_restaurant(db, usuario)
        response_model = RestauranteDetailResponse
    elif tipo.lower() == "bar":
        establishment = BaresCRUD.get_detial_bares(db, usuario)
        response_model = BarDetailResponse
    else:
        raise HTTPException(status_code=400, detail="Invalid establishment type")
        
    if not establishment:
        raise HTTPException(status_code=404, detail="Establishment not found")
        
    return establishment
