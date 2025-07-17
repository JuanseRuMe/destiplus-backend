from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComentarioRutaResponse(BaseModel):
    id: int
    ruta_id: int
    usuario_id: int
    comentario: str
    calificacion: Optional[float] = None
    fecha_creacion: datetime
    estado: str
    imagen: Optional[str] = None
    
    # Para incluir el nombre del usuario si quieres mostrarlo
    nombre_usuario: Optional[str] = None
    foto_usuario: Optional[str] = None

    class Config:
        from_attributes = True