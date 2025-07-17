from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....schemas.envioFormulario.alojamientos import AlojamientoUpdate, AlojamientoResponse
from .....db.session import get_db
from .....crud.envioFormulario.alojamientos import update_alojamientos, get_alojamientos_by_email

router = APIRouter()

@router.put("/alojamientos/register/formulario/{email}", response_model=AlojamientoResponse)
def update_alojamientos_info(
    email: str,
    alojamientos: AlojamientoUpdate,
    db: Session = Depends(get_db)
):
    db_actividades = update_alojamientos(db, email, alojamientos)
    if not db_actividades:
        raise HTTPException(
            status_code=404,
            detail="No se encontró un restaurante registrado con este email"
        )
    return db_actividades