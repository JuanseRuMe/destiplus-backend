from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .....schemas.envioFormulario.restaurantes import RestauranteUpdate, RestauranteResponse
from .....db.session import get_db
from .....crud.envioFormulario.restaurante import update_restaurante, get_restaurante_by_email

router = APIRouter()

@router.put("/restaurantes/register/formulario/{email}", response_model=RestauranteResponse)
def update_restaurante_info(
    email: str,
    restaurante: RestauranteUpdate,
    db: Session = Depends(get_db)
):
    db_restaurante = update_restaurante(db, email, restaurante)
    if not db_restaurante:
        raise HTTPException(
            status_code=404,
            detail="No se encontró un restaurante registrado con este email"
        )
    return db_restaurante