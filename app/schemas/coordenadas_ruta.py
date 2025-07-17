from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class EstacionesBase(BaseModel):
    nombre: str
    dificultad: str
    lat: float
    lng: float
    img: str
    description: str
    numero_estacion: int

class EstacionesResponse(EstacionesBase):
    id: int
    
    class Config:
        from_attributes = True

class CoordenadasAtajosBase(BaseModel):
    cordenadas: List[Dict[str, Any]]

class CoordenadasAtajosResponse(CoordenadasAtajosBase):
    id: int
    
    class Config:
        from_attributes = True


class AtajosBase(BaseModel):
    nombre: str
    dificultad: str
    lat: float
    lng: float
    img: str
    description: str
    numero_atajo: int

class AtajosResponse(AtajosBase):
    id: int
    coordenadas: Optional[List[CoordenadasAtajosResponse]]
    
    class Config:
        from_attributes = True

class EmergenciasBase(BaseModel):
    tipo: str
    numero: int

class EmergenciasResponse(EmergenciasBase):
    id: int
    
    class Config:
        from_attributes = True

class CoordenadasPrincipalesBase(BaseModel):
    cordenadas: List[Dict[str, Any]]

class CoordenadasPrincipalesResponse(CoordenadasPrincipalesBase):
    id: int
    
    class Config:
        from_attributes = True

class CoordenadasRutaResponse(BaseModel):
    id: int
    coordenadas_principales: List[CoordenadasPrincipalesResponse]
    estaciones: List[EstacionesResponse]
    atajos: List[AtajosResponse]
    emergencias: List[EmergenciasResponse]
    
    class Config:
        from_attributes = True