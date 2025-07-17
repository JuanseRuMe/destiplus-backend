from sqlalchemy.orm import Session
from ..models.destino import Evento, Actividad, Alojamiento

def get_items_by_destino(db: Session, destino_id: int, tipo: str):
   modelo_map = {
       "eventos": Evento,
       "actividades": Actividad, 
       "alojamientos": Alojamiento
   }
   
   items = db.query(modelo_map[tipo]).filter_by(destino_id=destino_id).all()
   
   response = []
   for item in items:
       data = item.evento if tipo == "eventos" else \
              item.actividad if tipo == "actividades" else \
              item.alojamiento
              
       for d in data:
           response.append({
               "name": d["name"],
               "description": d["description"],
               "img": d["img"],
               "calificacion": d.get("calificacion", 0),
               "precio": d["precio"],
               "items": d["items"],
               "logo": item.logo,
               "fecha": d.get("fecha") if tipo == "eventos" else None,
               "equipamento": d.get("equipamento") if tipo == "alojamientos" else None
           })
           
   return response