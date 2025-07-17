from pydantic import BaseModel
from typing import Dict, List

class RestauranteUpdate(BaseModel):
    destino_id: int
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

class RestauranteResponse(RestauranteUpdate):
    id: int
    usuario: str

    class Config:
        from_attributes = True