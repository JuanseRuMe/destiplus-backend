from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...models.destino import Bar
from ...schemas.envioFormulario.bares import BaresUpdate

def update_bares(db: Session, email: str, bares: BaresUpdate):
    try:
        db_bares = db.query(Bar).filter(Bar.usuario == email).first()
        if not db_bares:
            return None

        # Actualizar todos los campos
        for key, value in bares.model_dump().items():
            setattr(db_bares, key, value)

        db.commit()
        db.refresh(db_bares)
        return db_bares
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_bares_by_email(db: Session, email: str):
    return db.query(Bar).filter(Bar.usuario == email).first()
