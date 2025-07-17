from sqlalchemy.orm import Session
from ...models.destino import Actividad

class ActividadCRUD:
    @staticmethod
    def get_detial_actividad(db: Session, usuario: str):
        actividad = db.query(Actividad)\
            .filter(Actividad.usuario == usuario)\
            .first()
            
        if not actividad:
            return None
        
        return {
            "id": actividad.id,
            "logo": actividad.logo,
            "oferente": actividad.oferente,
            "horario": actividad.horario,
            "contacto": actividad.contacto,
            "metodosDePago": actividad.metodosDePago,
            "actividad": actividad.actividad,
            "usuario": actividad.usuario,
            "destino_id": actividad.destino_id,
            "coordenadas": actividad.coordenadas
        }