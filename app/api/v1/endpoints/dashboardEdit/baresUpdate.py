from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....schemas.dashboardEdit.bares import BaresUpdate, BaresResponse
from .....db.session import get_db
from .....crud.dashboardEdit.bares import update_bar, get_bar_by_email

router = APIRouter()

@router.put("/bares/update/{email}", response_model=BaresResponse)
def update_bar_info(
    email: str,
    bar: BaresUpdate,
    db: Session = Depends(get_db)
):
    db_bar = update_bar(db, email, bar)
    if not db_bar:
        raise HTTPException(
            status_code=404,
            detail="No se encontró un bar registrado con este email"
        )
    return {
        **db_bar.__dict__,
        "message": "Bar actualizado exitosamente"
    }