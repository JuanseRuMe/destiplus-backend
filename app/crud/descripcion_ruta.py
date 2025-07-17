from sqlalchemy.orm import Session
from ..models.listado_rutas_destino import ListadoRutas
from typing import Optional, List

class RutasCRUD:
    @staticmethod
    def get_ruta_content(db: Session, nombre: str):
        ruta = db.query(ListadoRutas)\
            .filter(ListadoRutas.nombre == nombre)\
            .first()
            
        if not ruta:
            return None
            
        return {
            "id": ruta.id,
            "img": ruta.img,
            "nombre": ruta.nombre,
            "calificacion": ruta.calificacion,
            "dificultad": ruta.dificultad,
            "tiempo": ruta.tiempo,
            "terreno": ruta.terreno,
            "distancia": ruta.distancia,
            "descripcion": ruta.descripcion,
            "etiquetas": ruta.etiquetas,
            "veces_recomendada": ruta.veces_recomendada,
            "completaron_ruta": ruta.completaron_ruta,
            "instrucciones": ruta.instrucciones,
            "imagenes": ruta.imagenes,
            "estaciones": ruta.estaciones,
            "emergencias": ruta.emergencias,
            "atajos": ruta.atajos
        }