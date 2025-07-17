from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...models.destino import Alojamiento
from ...schemas.dashboardEdit.alojamientos import AlojamientoUpdate

def update_alojamientos(db: Session, email: str, alojamientos: AlojamientoUpdate):
    try:
        db_alojamientos = db.query(Alojamiento).filter(Alojamiento.usuario == email).first()
        if not db_alojamientos:
            return None

        # Actualizar todos los campos
        for key, value in alojamientos.model_dump().items():
            setattr(db_alojamientos, key, value)

        db.commit()
        db.refresh(db_alojamientos)
        return db_alojamientos
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_alojamientos_by_email(db: Session, email: str):
    return db.query(Alojamiento).filter(Alojamiento.usuario == email).first()
