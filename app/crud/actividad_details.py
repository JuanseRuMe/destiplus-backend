from sqlalchemy.orm import Session
from sqlalchemy import text 
from ..models.destino import Actividad

class ActividadCRUD:
    @staticmethod
    def get_detial_actividad(db: Session, description: str):
        actividad = db.query(Actividad)\
            .filter(
                text(
                    "EXISTS (SELECT 1 FROM jsonb_array_elements(actividad::jsonb) obj "
                    "WHERE obj->>'description' = :description)"
                )
            )\
            .params(description=description)\
            .first()
            
        if not actividad:
            return None
        
        # Filtramos la actividad específica del array
        actividad_especifica = next(
            (item for item in actividad.actividad if item['description'] == description),
            None
        )
        
        return {
            "id": actividad.id,
            "logo": actividad.logo,
            "oferente": actividad.oferente,
            "horario": actividad.horario,
            "contacto": actividad.contacto,
            "metodosDePago": actividad.metodosDePago,
            "actividad": [actividad_especifica] if actividad_especifica else [],  # Devolvemos solo la actividad que coincide
            "usuario": actividad.usuario,
            "destino_id": actividad.destino_id,
            "coordenadas": actividad.coordenadas
        }