# app/schemas/comment.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# --- Esquema Base para campos comunes ---
class CommentBase(BaseModel):
    author_name: str = Field(..., min_length=1, max_length=150)
    content: str = Field(..., min_length=1)
    avatar_color: Optional[str] = Field(None, max_length=20)

# --- Esquema para Crear un Comentario ---
# Datos que se esperan en el cuerpo de la solicitud POST
class CommentCreate(CommentBase):
    parent_type: str = Field(..., min_length=1, max_length=50) # 'blog' o 'project'
    parent_slug: str = Field(..., min_length=1, max_length=255)
    # is_approved no se incluye aquí, se manejará con el server_default o por un admin

# --- Esquema para Leer/Devolver un Comentario ---
# Lo que la API devolverá
class CommentRead(CommentBase):
    id: int
    parent_type: str
    parent_slug: str
    created_at: datetime # Corresponde a 'timestamp' en tu frontend
    is_approved: bool # Para saber si es visible

    class Config:
        from_attributes = True