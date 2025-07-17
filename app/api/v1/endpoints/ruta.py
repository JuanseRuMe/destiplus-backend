from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ....db.session import get_db
from ....schemas.ruta import RutaCreate
from ....crud.ruta_crud import create_ruta

router = APIRouter()

@router.post("/new", response_model=RutaCreate, status_code=status.HTTP_201_CREATED)
def crear_ruta(ruta: RutaCreate, db: Session = Depends(get_db)):
    try:
        return create_ruta(db=db, ruta=ruta)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
