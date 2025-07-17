from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class CategoriaBase(BaseModel):
    ruta_id: Optional[int] = None
    ruta_id: int
    senderismo: bool
    bici_tour: bool
    moto: bool
    automovil: bool

class InstruccionesBase(BaseModel):
    ruta_id: Optional[int] = None
    recomendaciones: str
    accesibilidad: str
    conservacion: str

class ImagenBase(BaseModel):
    ruta_id: Optional[int] = None
    url: str

class EstacionBase(BaseModel):
    ruta_id: Optional[int] = None
    nombre: str
    dificultad: str
    lat: float
    lng: float
    img: str
    description: str
    numero_estacion: int

class CoordenadasPrincipalesBase(BaseModel):
    ruta_id: Optional[int] = None
    cordenadas: List[Dict[str, Any]]

class RutaCreate(BaseModel):
    destino_id: int
    img: str
    nombre: str
    calificacion: float = 0
    dificultad: str
    tiempo: int
    terreno: str
    distancia: float
    descripcion: str
    etiquetas: Dict[str, List[str]]
    veces_recomendada: int = 0
    completaron_ruta: int = 0
    items: Dict[str, Any]
    categoria: CategoriaBase
    instrucciones: InstruccionesBase
    imagenes: List[ImagenBase]
    estaciones: List[EstacionBase]
    coordenadas_principales: CoordenadasPrincipalesBase

    class Config:
        from_attributes = True