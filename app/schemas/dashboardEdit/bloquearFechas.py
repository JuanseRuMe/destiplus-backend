from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class ReservaBloqueoBase(BaseModel):
    alojamiento_id: int
    tipo_alojamiento_id: str
    usuario_id: Optional[int] = None
    fecha_inicio: datetime
    fecha_fin: datetime
    total_pagado: Optional[float] = None
    metodo_pago: Optional[str] = None
    estado: Optional[str] = None  # Hacerlo opcional
    huespedes: Optional[int] = None
    destino_id: int

class ReservaBloqueoCreate(ReservaBloqueoBase):
    pass

class ReservaBloqueoUpdate(BaseModel):
    estado: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None

class ReservaBloqueoResponse(ReservaBloqueoBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True