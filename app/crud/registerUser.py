from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Dict
from ..models.destino import Usuario
from ..schemas.registerUser import UserRegister

def verify_user(email: str, db: Session) -> Dict:
    """
    Solo verifica si existe el email
    Retorna 200 OK en ambos casos con el mensaje correspondiente
    """
    user = db.query(Usuario).filter(Usuario.email == email).first()
    return {
        "exists": True if user else False,
        "message": "Usuario ya registrado" if user else "Usuario no encontrado"
    }

def register_user(user_data: UserRegister, db: Session) -> Dict:
    """
    Verifica y registra usuario si no existe
    Retorna 200 OK en ambos casos con el mensaje correspondiente
    """
    # Verifica si existe
    existing_user = db.query(Usuario).filter(Usuario.email == user_data.email).first()
    if existing_user:
        return {
            "exists": True,
            "message": "Usuario ya registrado"
        }

    # Si no existe, registra
    try:
        new_user = Usuario(**user_data.dict())
        db.add(new_user)
        db.commit()
        
        return {
            "exists": False,
            "message": "Usuario registrado exitosamente"
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(500, f"Error al registrar usuario: {str(e)}")