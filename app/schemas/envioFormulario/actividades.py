from pydantic import BaseModel
from typing import Dict, List, Any

class ActividadesUpdate(BaseModel):
    destino_id: int
    oferente: str
    logo: str
    horario: Dict[str, Any]
    contacto: int
    metodosDePago: str
    coordenadas: Dict[str, Any]

class ActividadesResponse(ActividadesUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True