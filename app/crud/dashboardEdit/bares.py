from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...models.destino import Bar
from ...schemas.dashboardEdit.bares import BaresUpdate

def update_bar(db: Session, email: str, bar: BaresUpdate):
    try:
        db_bar = db.query(Bar).filter(Bar.usuario == email).first()
        if not db_bar:
            return None

        # Actualizar todos los campos
        for key, value in bar.model_dump().items():
            setattr(db_bar, key, value)

        db.commit()
        db.refresh(db_bar)
        return db_bar
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_bar_by_email(db: Session, email: str):
    return db.query(Bar).filter(Bar.usuario == email).first()
