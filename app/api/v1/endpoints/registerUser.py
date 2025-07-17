from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....schemas.registerUser import UserVerify, UserResponse, UserRegister
from ....crud.registerUser import register_user, verify_user
from ....db.session import get_db

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserRegister, db: Session = Depends(get_db)):
    try:
        # Primero verificamos si existe el usuario
        verify_result = verify_user(user.email, db)
        
        if verify_result["exists"]:
            return UserResponse(
                exists=True,
                message="Usuario ya registrado"
            )
        
        # Si no existe, lo registramos
        register_result = register_user(user, db)
        return UserResponse(
            exists=False,
            message="Usuario registrado exitosamente"
        )
    except Exception as e:
        print(f"Error en registro: {str(e)}")  # Para debugging
        raise HTTPException(500, f"Error en registro: {str(e)}")