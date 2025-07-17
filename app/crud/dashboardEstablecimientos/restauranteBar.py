from sqlalchemy.orm import Session
from ...models.destino import Restaurante, Bar

class RestauranteCRUD:
    @staticmethod
    def get_detial_restaurant(db: Session, usuario: str):
        restaurant = db.query(Restaurante)\
            .filter(Restaurante.usuario == usuario)\
            .first()
            
        if not restaurant:
            return None
        
        return {
            "id": restaurant.id,
            "name": restaurant.name,
            "items": restaurant.items,
            "concepto": restaurant.concepto,
            "usuario": restaurant.usuario,
            "calificacion": restaurant.calificacion,
            "precio_promedio": restaurant.precio_promedio,
            "horario": restaurant.horario,
            "metodosdepago": restaurant.metodosdepago,
            "servicios": restaurant.servicios,
            "destacados": restaurant.destacados,
            "recurrentes": restaurant.recurrentes,
            "antojos": restaurant.antojos,
            "bebidas": restaurant.bebidas,
            "img": restaurant.img,
            "imgs": restaurant.imgs,
            "logo": restaurant.logo,
            "contacto": restaurant.contacto,
            "coordenadas": restaurant.coordenadas,
        }

class BaresCRUD:
    @staticmethod
    def get_detial_bares(db: Session, usuario: str):
        bar = db.query(Bar)\
            .filter(Bar.usuario == usuario)\
            .first()
            
        if not bar:
            return None
        
        return {
            "id": bar.id,
            "name": bar.name,
            "items": bar.items,
            "concepto": bar.concepto,
            "usuario": bar.usuario,
            "calificacion": bar.calificacion,
            "precio_promedio": bar.precio_promedio,
            "horario": bar.horario,
            "metodos_de_pago": bar.metodos_de_pago,
            "servicios": bar.servicios,
            "destacados": bar.destacados,
            "recurrente": bar.recurrente,
            "antojos": bar.antojos,
            "bebidas": bar.bebidas,
            "img": bar.img,
            "imgs": bar.imgs,
            "logo": bar.logo,
            "contacto": bar.contacto,
            "coordenadas": bar.coordenadas,
        }
    