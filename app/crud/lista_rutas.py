from sqlalchemy.orm import Session
from ..models.listado_rutas_destino import ListadoRutas, Categorias
from typing import Optional, List

class ListadoRutasCRUD:
    @staticmethod
    def get_listado_rutas_content(
        db: Session, 
        categoria_tipo: str,
        destino_id: int
    ) -> Optional[List[dict]]:
        # Mapeo de nombres de categorías a columnas de la base de datos
        categoria_map = {
            "Senderismo": Categorias.senderismo,
            "BiciTour": Categorias.bici_tour,
            "Moto": Categorias.moto,
            "Automovil": Categorias.automovil
        }
        
        # Obtener la columna correspondiente a la categoría
        categoria_columna = categoria_map.get(categoria_tipo)
        if not categoria_columna:
            return None
            
        # Consulta con join y filtros
        listado_rutas = db.query(ListadoRutas)\
            .join(ListadoRutas.categorias)\
            .filter(
                ListadoRutas.destino_id == destino_id,
                categoria_columna == True
            )\
            .all()
            
        if not listado_rutas:
            return None
            
        # Transformar los resultados al formato deseado
        return [
            {
                "id": ruta.id,
                "calificacion": ruta.calificacion,
                "nombre": ruta.nombre,
                "dificultad": ruta.dificultad,
                "distancia": ruta.distancia,
                "tiempo": ruta.tiempo,
                "terreno": ruta.terreno,
                "items": ruta.items,
                "img": ruta.img
                
            }
            for ruta in listado_rutas
        ]