from sqlalchemy.orm import Session
from ..models.destino import Destino

def get_all_destinos(db: Session):
    return db.query(
        Destino.id, 
        Destino.municipio,
        Destino.departamento,
        Destino.frase,
        Destino.items,
        Destino.img,
        Destino.calificacion,
        Destino.lat,
        Destino.lng,
        Destino.completado
    ).filter(
        Destino.completado == True  # Aquí agregamos el filtro
    ).all()