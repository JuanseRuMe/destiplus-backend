from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Restaurantes
class RestauranteBase(BaseModel):
    name: str
    items: Dict[str, Any] 
    calificacion: float
    precio_promedio: int
    img: str
    logo: str
    
class RestaurantesResponse(RestauranteBase):
    id: int
    
    class Config:
        from_attributes = True
        
# Bares
class BarBase(BaseModel):
    actividad: List[Dict[Any, Any]]
    logo: str
    
class BaresResponse(RestauranteBase):
    id:int
    
    class Config:
        from_attributes = True
        
# Tendencias
class TendenciasBase(BaseModel):
    img: str
    
class TendenciasResponse(TendenciasBase):
    id:int
    
    class Config:
        from_attributes = True
        
# Actividades
class ActividadesBase(BaseModel):
    actividad: List[Dict[Any, Any]]
    logo: str

class ActividadesRespone(ActividadesBase):
    id:int
    
    class Config:
        from_attributes = True
        
# Eventos
class EventosBase(BaseModel):
    logo: str
    coordenadas: Dict[Any, Any]
    evento: List[Dict[Any, Any]]

class EventosRespone(EventosBase):
    id:int
    
    class Config:
        from_attributes = True
    
# Alojamientos
class AlojamientosBase(BaseModel):
    logo: str
    alojamiento: List[Dict[Any, Any]]

class AlojamientosResponse(AlojamientosBase):
    id:int
    
    class Config:
        from_attributes = True

# Destino  
class DestinoResponse(BaseModel):
    id:int
    municipio: str
    departamento: str
    lat: float
    lng: float
    frase: str 
    descripcion: str 
    epocas: str
    clima: str 
    seguridad: str
    transporte: str 
    img: str
    calificacion: float 
    items: Dict[str, Any]
    imagenes: List[Dict[str, Any]]
    restaurantes: List[RestaurantesResponse]
    bares: List[BaresResponse]
    tendencias: List[TendenciasResponse]
    actividades: List[ActividadesRespone]
    eventos: List[EventosRespone]
    alojamientos: List[AlojamientosResponse]
    
    class Config:
        from_attributes = True