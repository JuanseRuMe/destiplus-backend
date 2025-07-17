from pydantic import BaseModel
from typing import Dict, Optional, List
from datetime import datetime

class UserVerify(BaseModel):
    email: str

class UserResponse(BaseModel):
    exists: bool
    message: str

class UserRegister(BaseModel):
    email: str
    nombre: str
    foto_perfil: str
    fecha_registro: datetime
    ultima_conexion: datetime
    estado: bool