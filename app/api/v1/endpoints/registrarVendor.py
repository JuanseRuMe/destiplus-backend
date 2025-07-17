from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....schemas.registrarVendor import UserVerify, UserResponse, UserRegister
from ....crud.registrarVendor import register_user, verify_user
from ....db.session import get_db

router = APIRouter()

@router.post("/{type}/register", response_model=UserResponse)
def register(type: str, user: UserRegister, db: Session = Depends(get_db)):
    try:
        # Verificamos solo en el tipo específico de negocio
        verify_result = verify_user(user.email, type, db)
        
        if verify_result["exists"]:
            return UserResponse(
                exists=True,
                type=type,
                message="Usuario ya registrado"
            )
        
        # Si no existe en ese tipo, lo registramos
        register_result = register_user(user.email, type, db)
        return UserResponse(
            exists=False,
            type=type,
            message="Registro exitoso"
        )
    except Exception as e:
        print(f"Error en registro: {str(e)}")  # Para debugging
        raise
