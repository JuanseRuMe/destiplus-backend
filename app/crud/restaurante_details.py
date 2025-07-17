from sqlalchemy.orm import Session
from ..models.destino import Restaurante

class RestauranteCRUD:
    @staticmethod
    def get_detial_restaurant(db: Session, name: str):
        restaurant = db.query(Restaurante)\
            .filter(Restaurante.name == name)\
            .first()
            
        if not restaurant:
            return None
        
        return {
            "id": restaurant.id,
            "name": restaurant.name,
            "concepto": restaurant.concepto,
            "calificacion": restaurant.calificacion,
            "horario": restaurant.horario,
            "contacto": restaurant.contacto,
            "metodosdepago": restaurant.metodosdepago,
            "servicios": restaurant.servicios,
            "destacados": restaurant.destacados,
            "recurrentes": restaurant.recurrentes,
            "antojos": restaurant.antojos,
            "bebidas": restaurant.bebidas,
            "img": restaurant.img,
            "imgs": restaurant.imgs,
            "logo": restaurant.logo,
            "coordenadas": restaurant.coordenadas
        }