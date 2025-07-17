from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PlantadorInfo(BaseModel):
    id: int
    nombre: str
    foto_perfil: str
    fecha: datetime
    
    class Config:
        from_attributes = True

class DatosArbolesRuta(BaseModel):
    total_arboles: int
    co2_ahorrado_kg: float
    ultimos_plantadores: List[PlantadorInfo]
    
    class Config:
        from_attributes = True