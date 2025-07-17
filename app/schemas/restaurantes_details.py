from pydantic import BaseModel
from typing import List, Dict, Any

class RestaurateDetailBase(BaseModel):
    name: str
    concepto: str
    calificacion: float
    horario: Dict[str, Any]
    contacto: int
    metodosdepago: str
    servicios: Dict[str, Any]
    destacados: List[Dict[str, Any]]
    recurrentes: List[Dict[str, Any]]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    img: str
    imgs: Dict[str, List]
    logo: str
    coordenadas: Dict[str, Any]
    

class RestauranteDetailResponse(RestaurateDetailBase):
    id: int
    
    class Config:
        from_attributes = True
        
