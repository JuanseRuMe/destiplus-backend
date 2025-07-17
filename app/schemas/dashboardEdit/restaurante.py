from pydantic import BaseModel
from typing import Dict, List, Any

class RestauranteUpdate(BaseModel):
    name: str
    items: Dict[str, str]
    concepto: str
    precio_promedio: int
    horario: Dict[str, str]
    contacto: int
    metodosdepago: str
    servicios: Dict[str, str]
    img: str
    imgs: Dict[str, List[str]]
    logo: str
    coordenadas: Dict[str, float]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    destacados: List[Dict[str, Any]]
    recurrentes: List[Dict[str, Any]]

class RestauranteResponse(RestauranteUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True