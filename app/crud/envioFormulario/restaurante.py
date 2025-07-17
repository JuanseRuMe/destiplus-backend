from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...models.destino import Restaurante
from ...schemas.envioFormulario.restaurantes import RestauranteUpdate

def update_restaurante(db: Session, email: str, restaurante: RestauranteUpdate):
    try:
        db_restaurante = db.query(Restaurante).filter(Restaurante.usuario == email).first()
        if not db_restaurante:
            return None

        # Actualizar todos los campos
        for key, value in restaurante.model_dump().items():
            setattr(db_restaurante, key, value)

        db.commit()
        db.refresh(db_restaurante)
        return db_restaurante
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_restaurante_by_email(db: Session, email: str):
    return db.query(Restaurante).filter(Restaurante.usuario == email).first()
