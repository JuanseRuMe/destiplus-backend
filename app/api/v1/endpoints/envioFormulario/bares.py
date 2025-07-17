from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....schemas.envioFormulario.bares import BaresUpdate, BaresResponse
from .....db.session import get_db
from .....crud.envioFormulario.bares import update_bares, get_bares_by_email

router = APIRouter()

@router.put("/bares/register/formulario/{email}", response_model=BaresResponse)
def update_bares_info(
    email: str,
    bar: BaresUpdate,
    db: Session = Depends(get_db)
):
    db_bar = update_bares(db, email, bar)
    if not db_bar:
        raise HTTPException(
            status_code=404,
            detail="No se encontró un restaurante registrado con este email"
        )
    return db_bar