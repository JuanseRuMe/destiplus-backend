# app/schemas/daily_learning.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# --- Esquema Base (campos que se devuelven) ---
class DailyLearningBase(BaseModel):
    question: str
    answer: str
    fun_fact: str
    category: str
    icon_name: Optional[str] = None # Mantenemos Optional por si algunos no lo tienen
    color_hex: Optional[str] = None
    is_active: bool # Siempre se devolverá

# --- Esquema para Leer/Devolver ---
# Lo que la API devolverá
class DailyLearning(DailyLearningBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Para Pydantic V2 (era orm_mode = True en V1)