from sqlalchemy.orm import Session
from ...models.destino import Alojamiento

class AlojamientoCRUD:
    @staticmethod
    def get_detial_alojamiento(db: Session, usuario: str):
        alojamiento = db.query(Alojamiento)\
            .filter(Alojamiento.usuario == usuario)\
            .first()
            
        if not alojamiento:
            return None
        
        return {
            "id": alojamiento.id,
            "usuario": alojamiento.usuario,
            "destino_id": alojamiento.destino_id,
            "oferente": alojamiento.oferente,
            "logo": alojamiento.logo,
            "checkIn": alojamiento.checkIn,
            "checkOut": alojamiento.checkOut,
            "contacto": alojamiento.contacto,
            "metodosDePago": alojamiento.metodosDePago,
            "politicas": alojamiento.politicas,
            "coordenadas": alojamiento.coordenadas,
            "alojamiento": alojamiento.alojamiento
        }