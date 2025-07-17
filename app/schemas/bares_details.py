from pydantic import BaseModel
from typing import List, Dict, Any

class BarDetailBase(BaseModel):
    name: str
    concepto: str
    calificacion: float
    horario: Dict[str, Any]
    contacto: int
    metodos_de_pago: str
    servicios: Dict[str, Any]
    destacados: List[Dict[str, Any]]
    recurrente: List[Dict[str, Any]]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    img: str
    imgs: Dict[str, List]
    logo: str
    coordenadas: Dict[str, Any]
    

class BarDetailResponse(BarDetailBase):
    id: int
    
    class Config:
        from_attributes = True