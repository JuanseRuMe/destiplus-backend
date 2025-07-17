from pydantic import BaseModel
from typing import List, Dict, Any

class ListadoRutasDetailBase(BaseModel):
    nombre: str
    calificacion: float
    dificultad: str
    distancia: float
    tiempo: int
    terreno: str
    items: Dict[str, Any]
    img: str

class ListadoRutasDetailResponse(ListadoRutasDetailBase):
    id: int
    
    class Config:
        from_attributes = True