from sqlalchemy.orm import Session
from ..models.destino import Destino

class DestinoCRUD:
    @staticmethod
    def get_destino_content(db: Session, municipio: str  = "Suesca"):
        destino = db.query(Destino)\
            .filter(Destino.municipio == municipio)\
            .first()
            
        if not destino:
            return None
        
        return {
            "id": destino.id,
            "municipio": destino.municipio,
            "departamento": destino.departamento,
            "lat": destino.lat,
            "lng": destino.lng,
            "frase": destino.frase,
            "descripcion": destino.descripcion,
            "epocas": destino.epocas,
            "clima": destino.clima,
            "seguridad": destino.seguridad,
            "transporte": destino.transporte,
            "img": destino.img,
            "calificacion": destino.calificacion,
            "items": destino.items,
            "imagenes": destino.imagenes,
            "restaurantes": destino.restaurantes,
            "bares": destino.bares,
            "tendencias": destino.tendencias,
            "actividades": destino.actividades,
            "eventos": destino.eventos,
            "alojamientos": destino.alojamientos
        }