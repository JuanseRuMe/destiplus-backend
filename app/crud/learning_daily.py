# app/crud/crud_daily_learning.py
from sqlalchemy.orm import Session
from sqlalchemy.sql import func # Para RANDOM() o func.random()
from typing import List, Optional

from ..models.daily_learning import DailyLearningContent # Ajusta la ruta si es necesario

def get_daily_learning_item(db: Session, item_id: int) -> Optional[DailyLearningContent]:
    return db.query(DailyLearningContent).filter(DailyLearningContent.id == item_id).first()

def get_daily_learning_items(
    db: Session, 
    skip: int = 0, 
    limit: int = 5, 
    is_active: Optional[bool] = None # Permite filtrar por is_active
) -> List[DailyLearningContent]:
    query = db.query(DailyLearningContent)
    if is_active is not None:
        query = query.filter(DailyLearningContent.is_active == is_active)
    # Podrías añadir un orden por defecto, ej: .order_by(DailyLearningContent.created_at.desc())
    return query.offset(skip).limit(limit).all()

def get_active_daily_learning_item_random(db: Session) -> Optional[DailyLearningContent]:
    """
    Obtiene un único ítem activo de forma aleatoria.
    """
    return db.query(DailyLearningContent)\
             .filter(DailyLearningContent.is_active == True)\
             .order_by(func.random()) \
             .first() # Para PostgreSQL, func.random() funciona.

# No se necesitan funciones create, update, delete