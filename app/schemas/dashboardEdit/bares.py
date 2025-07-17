from pydantic import BaseModel
from typing import Dict, List, Any

class BaresUpdate(BaseModel):
    name: str
    items: Dict[str, str]
    concepto: str
    precio_promedio: int
    horario: Dict[str, str]
    contacto: int
    metodos_de_pago: str
    servicios: Dict[str, Any]
    img: str
    imgs: Dict[str, List[str]]
    logo: str
    coordenadas: Dict[str, float]
    antojos: List[Dict[str, Any]]
    bebidas: List[Dict[str, Any]]
    destacados: List[Dict[str, Any]]

class BaresResponse(BaresUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True