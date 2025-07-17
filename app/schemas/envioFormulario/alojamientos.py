from pydantic import BaseModel
from typing import List, Dict, Any

class AlojamientoUpdate(BaseModel):
    destino_id: int
    oferente: str
    logo: str
    checkIn: str
    checkOut: str
    contacto: int
    metodosDePago: str 
    politicas: Dict[Any, Any]
    coordenadas: Dict[Any, Any]
    
class AlojamientoResponse(AlojamientoUpdate):
    id: int
    usuario: str
    
    class Config:
        from_attributes = True