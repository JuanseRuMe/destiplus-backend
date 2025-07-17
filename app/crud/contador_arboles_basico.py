from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from typing import List, Dict, Any, Optional
from ..models.destino import ArbolesPlantados, Usuario
from ..schemas.contador_arboles_basico import PlantadorInfo, DatosArbolesRuta
from datetime import datetime

class ArbolesCRUD:
    @staticmethod
    def get_arboles_info_por_ruta(db: Session, ruta_id: int) -> DatosArbolesRuta:
        """
        Obtiene información completa sobre árboles plantados en una ruta específica,
        incluyendo datos sobre quién los plantó.
        """
        # Obtener el total de árboles plantados en la ruta
        total_arboles = (db.query(func.count(ArbolesPlantados.id))
                     .filter(ArbolesPlantados.ruta_id == ruta_id)
                     .scalar()) or 0
         
        # Calcular CO2 estimado ahorrado
        co2_ahorrado = (db.query(func.sum(ArbolesPlantados.co2_estimado))
                    .filter(ArbolesPlantados.ruta_id == ruta_id)
                    .scalar()) or 0.0
         
        # Obtener información de los últimos 5 plantadores con sus datos
        ultimos_plantadores: List[PlantadorInfo] = []
         
        # Consulta SQL para obtener los últimos 5 árboles plantados con datos del plantador
        plantaciones_recientes = []
         
        try:
            plantaciones_recientes = (db.query(
                                ArbolesPlantados,
                                Usuario.id.label('usuario_id'),
                                Usuario.nombre,
                                Usuario.foto_perfil,
                                ArbolesPlantados.fecha_plantacion
                              )
                              .join(
                                  Usuario,
                                  ArbolesPlantados.plantador_id == Usuario.id,
                                  isouter=True  # Left join para incluir árboles sin plantador identificado
                              )
                              .filter(ArbolesPlantados.ruta_id == ruta_id)
                              .order_by(desc(ArbolesPlantados.fecha_plantacion))
                              .limit(5)
                              .all())
        except Exception as e:
            print(f"Error en la consulta de plantadores: {str(e)}")
            # Manejo de error para evitar que falle todo el endpoint
         
        for plantacion in plantaciones_recientes:
            # Crear objeto PlantadorInfo directamente
            plantador = PlantadorInfo(
                id=plantacion.usuario_id or 0,  # Si no hay ID, usar 0
                nombre=plantacion.nombre or "Anónimo",  # Si no hay nombre, usar "Anónimo"
                foto_perfil=plantacion.foto_perfil or "https://via.placeholder.com/40",  # Foto por defecto
                fecha=plantacion.fecha_plantacion
            )
            ultimos_plantadores.append(plantador)
         
        # Crear y devolver directamente un objeto DatosArbolesRuta
        return DatosArbolesRuta(
            total_arboles=total_arboles,
            co2_ahorrado_kg=float(co2_ahorrado),  # Asegúrate de que sea float
            ultimos_plantadores=ultimos_plantadores
        )