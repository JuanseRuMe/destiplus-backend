from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class InstruccionesBase(BaseModel):
    recomendaciones: str
    accesibilidad: str
    conservacion: str

class InstruccionesResponse(InstruccionesBase):
    id: int
    
    class Config:
        from_attributes = True

class ImagenesBase(BaseModel):
    url: str

class ImagenesResponse(ImagenesBase):
    id: int
    
    class Config:
        from_attributes = True
    
class EstacionesBase(BaseModel):
    nombre: str
    dificultad: str   
    
class EstacionesResponse(EstacionesBase):
    id: int
    
    class Config:
        from_attributes = True
        
class EmergenciasBase(BaseModel):
    tipo:str
    numero: int
    
class EmergenciasResponse(EmergenciasBase):
    id: int
    
    class Config:
        from_attributes = True
        
class AtajosBase(BaseModel):
    nombre: str
    dificultad: str  

class AtajosResponse(AtajosBase):
    id: int
    disponibilidad: List["DisponibilidadAtajosResponse"]
    
    class Config:
        from_attributes = True
        
        
class DisponibilidadAtajosBase(BaseModel):
    senderismo: bool
    bici_tour: bool
    moto: bool
    automovil: bool       
         
class DisponibilidadAtajosResponse(DisponibilidadAtajosBase):
    id: int
    
    class Config:
        from_attributes = True        
         
# Descripcion Ruta 
class RutaResponse(BaseModel):
    id:int
    img: str
    nombre: str
    calificacion: float
    dificultad: str
    tiempo: int
    terreno: str
    distancia: float # Agregué el tipo Float que faltaba
    descripcion: str
    etiquetas: Dict[str, List[str]]
    veces_recomendada: int
    completaron_ruta: int
    instrucciones: List[InstruccionesResponse]
    imagenes: List[ImagenesResponse]
    estaciones: List[EstacionesResponse]
    emergencias: List[EmergenciasResponse]
    atajos: List[AtajosResponse]
    
    class Config:
        from_attributes = True