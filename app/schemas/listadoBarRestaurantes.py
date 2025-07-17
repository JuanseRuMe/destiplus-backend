from pydantic import BaseModel
from typing import Dict, Any, List

class ListadoResponse(BaseModel):
    id: int
    name: str
    img: str
    calificacion: float
    precio_promedio: int
    items: Dict[str, Any]
    logo: str

    class Config:
        from_attributes = True