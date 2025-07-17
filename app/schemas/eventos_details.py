from pydantic import BaseModel
from typing import List, Dict, Any

class EventosDetailBase(BaseModel):
    logo: str
    oferente: str 
    metodosdepago: str 
    contacto: int
    coordenadas: Dict[Any, Any]
    evento: List[Dict[Any, Any]]

class EventosDetailResponse(EventosDetailBase):
    id: int
    
    class Config:
        from_attributes = True