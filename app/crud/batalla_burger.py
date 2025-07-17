from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError # Para capturar errores de constraints
from typing import Optional

from ..models.batalla_burguer import BurgerVote
from ..schemas.batalla_burger import VoteCreate

def create_vote(db: Session, vote: VoteCreate, ip_address: Optional[str]):
    """
    Crea un nuevo registro de voto en la base de datos.
    """
    # Crear instancia del modelo SQLAlchemy desde el schema Pydantic
    # Los campos `id` y `voted_at` no se incluyen aquí, se generan en la DB
    db_vote = BurgerVote(
        email=vote.email,
        full_name=vote.full_name,
        rating=vote.rating,
        recommendations=vote.recommendations,
        origin=vote.origin,
        burger_name=vote.burger_name,
        restaurant_name=vote.restaurant_name,
        burger_id=vote.burger_id,
        latitude=vote.latitude,
        longitude=vote.longitude,
        ip_address=ip_address # Añadir IP obtenida del request
    )
    db.add(db_vote)
    try:
        db.commit() # Intentar guardar en la base de datos
        db.refresh(db_vote) # Refrescar para obtener ID y voted_at generados
        return db_vote
    except IntegrityError as e:
        db.rollback() # Deshacer la transacción si falla (ej. por unique constraint)
        print(f"Error de Integridad al guardar voto: {e}")
        # Podríamos analizar el error 'e' para ver si es por la constraint única
        # y devolver un error específico o lanzar una excepción personalizada.
        # Por ahora, devolvemos None o relanzamos/lanzamos una excepción específica.
        raise ValueError("Error al guardar el voto, posible duplicado (email/burger).") # Lanzar excepción para manejar en el endpoint


def get_vote(db: Session, vote_id: int):
    return db.query(BurgerVote).filter(BurgerVote.id == vote_id).first()

def get_votes_by_burger(db: Session, burger_id: int) -> int:
    count = db.query(BurgerVote).filter(BurgerVote.burger_id == burger_id).count()
    return count