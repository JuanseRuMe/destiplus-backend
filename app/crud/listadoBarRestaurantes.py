from sqlalchemy.orm import Session
from typing import List
from ..models.destino import Bar, Restaurante

class ListadoCRUD:
    @staticmethod
    def get_listado(db: Session, destino_id: int, tipo: str) -> List:
        if tipo == "restaurantes":
            return db.query(Restaurante).filter(
                Restaurante.destino_id == destino_id
            ).with_entities(
                Restaurante.id,
                Restaurante.name,
                Restaurante.img,
                Restaurante.calificacion,
                Restaurante.precio_promedio,
                Restaurante.items,
                Restaurante.logo
            ).all()
            
        elif tipo == "bares":
            return db.query(Bar).filter(
                Bar.destino_id == destino_id
            ).with_entities(
                Bar.id,
                Bar.name,
                Bar.img,
                Bar.calificacion,
                Bar.precio_promedio,
                Bar.items,
                Bar.logo
            ).all()