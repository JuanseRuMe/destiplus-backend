from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class RestaurateDetailBase(BaseModel):
    name: str
    items: Dict[str, Any]
    concepto: str
    usuario: str
    calificacion: float
    precio_promedio: int
    horario: Dict[str, Any]
    metodosdepago: str
    servicios: Dict[str, Any]
    destacados: List[Dict[str, Any]]
    recurrentes: List[Dict[str, Any]]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    img: str
    imgs: Dict[str, List]
    logo: str
    contacto: int
    coordenadas: Dict[str, float] 
    

class RestauranteDetailResponse(RestaurateDetailBase):
    id: int
    
    class Config:
        from_attributes = True
        

class BarDetailBase(BaseModel):
    name: str
    items: Dict[str, Any]
    concepto: str
    usuario: str
    calificacion: float
    precio_promedio: int
    horario: Dict[str, Any]
    metodos_de_pago: str
    servicios: Dict[str, Any]
    destacados: List[Dict[str, Any]]
    recurrente: List[Dict[str, Any]]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    img: str
    imgs: Dict[str, List]
    logo: str
    contacto: int
    coordenadas: Dict[str, float] 
    
class BarDetailResponse(BarDetailBase):
    id: int
    
    class Config:
        from_attributes = True
