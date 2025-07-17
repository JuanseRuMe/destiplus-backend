# schemas.py
from pydantic import BaseModel, EmailStr, constr, conint, confloat
from typing import Optional, Text # 'Text' no es un tipo Pydantic, usar 'str'
from datetime import datetime

# --- Esquema Base ---
# Campos que se reciben y se devuelven (comunes)
class VoteBase(BaseModel):
    email: str
    full_name: str
    rating: int 
    recommendations: Optional[str] = None
    origin: str 

    # Datos de la hamburguesa (recibidos del frontend)
    burger_name: str
    restaurant_name: str
    burger_id: int

    latitude: Optional[float] = None
    longitude: Optional[float] = None


# Lo que se espera en el cuerpo de la solicitud POST
class VoteCreate(VoteBase):
    pass


# --- Esquema para Leer/Devolver ---
# Lo que la API devolverá después de crear/consultar un voto
class Vote(VoteBase):
    id: int 
    voted_at: datetime 
    ip_address: Optional[str] = None 

    class Config:
        from_attributes = True


class VoteCount(BaseModel):
    burger_id: int
    vote_count: int