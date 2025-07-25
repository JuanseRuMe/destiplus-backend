from pydantic import BaseModel
from typing import List, Dict, Any

class AlojamientoDetailBase(BaseModel):
    usuario: str
    destino_id: int
    oferente: str
    logo: str
    checkIn: str
    checkOut: str
    contacto: int
    metodosDePago: str 
    politicas: Dict[Any, Any]
    coordenadas: Dict[Any, Any]
    alojamiento: List[Dict[Any, Any]]
    
class AlojamientoDetailResponse(AlojamientoDetailBase):
    id: int
    
    class Config:
        from_attributes = True