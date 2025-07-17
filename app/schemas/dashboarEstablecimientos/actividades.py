from pydantic import BaseModel
from typing import List, Dict, Any

class ActividadDetailBase(BaseModel):
    usuario: str
    destino_id: int
    logo: str
    oferente: str
    horario: Dict[str, Any]
    contacto: int
    metodosDePago: str
    actividad: List[Dict[Any, Any]]
    coordenadas: Dict[str, Any] 

class ActividadDetailResponse(ActividadDetailBase):  
    id: int

    class Config:
        from_attributes = True