from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...models.destino import Actividad
from ...schemas.dashboardEdit.actividades import ActividadesUpdate

def update_actividades(db: Session, email: str, actividades: ActividadesUpdate):
    try:
        db_actividades = db.query(Actividad).filter(Actividad.usuario == email).first()
        if not db_actividades:
            return None

        # Actualizar todos los campos
        for key, value in actividades.model_dump().items():
            setattr(db_actividades, key, value)

        db.commit()
        db.refresh(db_actividades)
        return db_actividades
    except SQLAlchemyError as e:
        db.rollback()
        raise e

def get_actividades_by_email(db: Session, email: str):
    return db.query(Actividad).filter(Actividad.usuario == email).first()
