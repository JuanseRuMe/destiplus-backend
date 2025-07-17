from sqlalchemy.orm import Session
from sqlalchemy import text 
from ..models.destino import Alojamiento

class AlojamientoCRUD:
    @staticmethod
    def get_detial_alojamiento(db: Session, description: str):
        alojamiento = db.query(Alojamiento)\
            .filter(
                text(
                    "EXISTS (SELECT 1 FROM jsonb_array_elements(alojamiento::jsonb) obj "
                    "WHERE obj->>'description' = :description)"
                )
            )\
            .params(description=description)\
            .first()
            
        if not alojamiento:
            return None
        
        # Filtramos el alojamiento específico del array
        alojamiento_especifico = next(
            (item for item in alojamiento.alojamiento if item['description'] == description),
            None
        )
            
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
            "alojamiento": [alojamiento_especifico] if alojamiento_especifico else []  # Devolvemos solo el alojamiento que coincide
        }