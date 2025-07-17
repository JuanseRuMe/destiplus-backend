# app/api/v1/endpoints/daily_learning.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

# Ajusta estas rutas de importación según tu estructura de proyecto
from ....schemas.daily_learning import DailyLearning # Solo necesitamos el schema de respuesta
from ....crud.learning_daily import get_daily_learning_items
from ....db.session import get_db

router = APIRouter()

@router.get("/questions/answers/fun/facts", response_model=List[DailyLearning])
def read_daily_learning_items(
    skip: int = 0, 
    limit: int = 10, 
    is_active: Optional[bool] = True, # Por defecto, solo trae los activos
    db: Session = Depends(get_db)
):
    """
    Obtiene una lista de Q&A y Datos Curiosos.
    Puedes filtrar por estado `is_active=True` (por defecto) o `is_active=False`.
    Para obtener todos, no pases el parámetro `is_active` o usa `is_active=None` (si la API lo permite así).
    En este caso, si el cliente no envía `is_active`, será `True`.
    Si el cliente envía `is_active=false`, se filtrará por inactivos.
    Si quieres todos (activos e inactivos) desde el cliente, tendrías que modificar cómo manejas el None aquí
    o el cliente tendría que hacer dos llamadas, o podrías añadir otro parámetro "include_inactive".
    Para mantenerlo simple, este endpoint ahora filtra por `is_active` si se provee, y si no, trae todos.
    O podemos hacer que `is_active: Optional[bool] = None` en CRUD y aquí `is_active: Optional[bool] = Query(True)`
    para que el default sea True si no se especifica.
    Por ahora, si el cliente no envía `is_active`, el CRUD no filtrará por ese campo.
    Si se envía `is_active=true` o `is_active=false`, sí filtrará.
    Para este endpoint, vamos a hacer que por defecto devuelva solo los activos si no se especifica.
    """
    items = get_daily_learning_items(db, skip=skip, limit=limit, is_active=is_active)
    return items
