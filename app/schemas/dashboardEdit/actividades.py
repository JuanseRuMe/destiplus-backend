from pydantic import BaseModel
from typing import Dict, List, Any

class ActividadesUpdate(BaseModel):
    oferente: str
    logo: str
    horario: Dict[str, Any]
    contacto: int
    metodosDePago: str
    actividad: List[Dict[str, Any]]


class ActividadesResponse(ActividadesUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True