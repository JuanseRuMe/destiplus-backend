from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....schemas.envioFormulario.actividades import ActividadesUpdate, ActividadesResponse
from .....db.session import get_db
from .....crud.envioFormulario.actividades import update_actividades, get_actividades_by_email

router = APIRouter()

@router.put("/actividades/register/formulario/{email}", response_model=ActividadesResponse)
def update_actividades_info(
    email: str,
    actividades: ActividadesUpdate,
    db: Session = Depends(get_db)
):
    db_actividades = update_actividades(db, email, actividades)
    if not db_actividades:
        raise HTTPException(
            status_code=404,
            detail="No se encontró un restaurante registrado con este email"
        )
    return db_actividades