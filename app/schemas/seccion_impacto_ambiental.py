from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PlantadorInfo(BaseModel):
    id: int
    nombre: str
    foto_perfil: str
    
    class Config:
        from_attributes = True

class DonanteInfo(BaseModel):
    id: int
    nombre: str
    fecha_donacion: datetime
    cantidad_total: int
    descripcion: str
    estado: str
    
    class Config:
        from_attributes = True

class RutaInfo(BaseModel):
    id: int
    nombre: str
    
    class Config:
        from_attributes = True

class ArbolPlantadoInfo(BaseModel):
    id: int
    donacion_id: int
    plantador_id: int
    fecha_plantacion: datetime
    ubicacion_geografica: Optional[str] = None
    ruta_id: int
    nombre_ubicacion: str
    region: str
    pais: str
    especie: str
    estado_actual: str
    imagen_url: str
    descripcion: str
    co2_estimado: float
    donante: Optional[DonanteInfo] = None
    plantador: Optional[PlantadorInfo] = None
    ruta: Optional[RutaInfo] = None
    
    class Config:
        from_attributes = True

class ArbolesInfoResponse(BaseModel):
    cantidad_total: int
    co2_total: float
    m2_reforestados: int
    arboles: List[ArbolPlantadoInfo]
    
    class Config:
        from_attributes = True