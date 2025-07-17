from sqlalchemy.orm import Session
from sqlalchemy import text 
from ..models.destino import Evento

class EventoCRUD:
    @staticmethod
    def get_detial_evento(db: Session, description: str):
        evento = db.query(Evento)\
            .filter(
                text(
                    "EXISTS (SELECT 1 FROM jsonb_array_elements(evento::jsonb) obj "
                    "WHERE obj->>'description' = :description)"
                )
            )\
            .params(description=description)\
            .first()
            
        if not evento:
            return None
        
        # Filtramos el evento específico del array
        evento_especifico = next(
            (item for item in evento.evento if item['description'] == description),
            None
        )
        
        return {
            "id": evento.id,
            "logo": evento.logo,
            "oferente": evento.oferente,
            "metodosdepago": evento.metodosdepago,
            "contacto": evento.contacto,
            "coordenadas": evento.coordenadas,
            "evento": [evento_especifico] if evento_especifico else []  # Devolvemos solo el evento que coincide
        }