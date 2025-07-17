from pydantic import BaseModel
from typing import List, Dict, Any

class DestinoFiltrolBase(BaseModel):
    municipio: str
    departamento: str
    frase: str
    items: Dict[str, Any]
    img: str
    calificacion: float
    lat: float
    lng: float
    completado: bool

class DestinoFiltroResponse(DestinoFiltrolBase):  
    id: int

    class Config:
        from_attributes = True