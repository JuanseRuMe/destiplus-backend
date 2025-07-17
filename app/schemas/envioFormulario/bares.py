from pydantic import BaseModel
from typing import Dict, List, Any

class BaresUpdate(BaseModel):
    destino_id: int
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

class BaresResponse(BaresUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True