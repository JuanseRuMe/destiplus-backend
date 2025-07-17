from sqlalchemy.orm import Session
from ..models.destino import Bar

class BarCRUD:
    @staticmethod
    def get_detial_bar(db: Session, name: str):
        bar = db.query(Bar)\
            .filter(Bar.name == name)\
            .first()
            
        if not bar:
            return None
        
        return {
            "id": bar.id,
            "name": bar.name,
            "concepto": bar.concepto,
            "calificacion": bar.calificacion,
            "horario": bar.horario,
            "contacto": bar.contacto,
            "metodos_de_pago": bar.metodos_de_pago,
            "servicios": bar.servicios,
            "destacados": bar.destacados,
            "recurrente": bar.recurrente,
            "antojos": bar.antojos,
            "bebidas": bar.bebidas,
            "img": bar.img,
            "imgs": bar.imgs,
            "logo": bar.logo,
            "coordenadas": bar.coordenadas
        }