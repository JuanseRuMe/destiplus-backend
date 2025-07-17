from sqlalchemy.orm import Session, joinedload
from typing import Optional, Dict, Any
from ..models.listado_rutas_destino import ListadoRutas, Atajos
from operator import itemgetter

class RutaCoordenadaCRUD:
    @staticmethod
    def get_coordenada_content(db: Session, nombre: str) -> Optional[Dict[str, Any]]:
        try:
            ruta_coordenada = (
                db.query(ListadoRutas)
                .options(
                    joinedload(ListadoRutas.coordenadas_principales),
                    joinedload(ListadoRutas.estaciones),
                    joinedload(ListadoRutas.atajos).joinedload(Atajos.coordenadas),
                    joinedload(ListadoRutas.emergencias)
                )
                .filter(ListadoRutas.nombre.ilike(f"%{nombre}%"))
                .first()
            )
            
            if not ruta_coordenada:
                return None
            
            # Sort estaciones by numero_estacion
            sorted_estaciones = sorted(
                [
                    {
                        "id": estacion.id,
                        "nombre": estacion.nombre,
                        "dificultad": estacion.dificultad,
                        "lat": estacion.lat,
                        "lng": estacion.lng,
                        "img": estacion.img,
                        "description": estacion.description,
                        "numero_estacion": estacion.numero_estacion
                    } for estacion in ruta_coordenada.estaciones
                ],
                key=itemgetter('numero_estacion')
            )
            
            # Sort atajos by numero_atajo
            sorted_atajos = sorted(
                [
                    {
                        "id": atajo.id,
                        "nombre": atajo.nombre,
                        "dificultad": atajo.dificultad,
                        "lat": atajo.lat,
                        "lng": atajo.lng,
                        "img": atajo.img,
                        "description": atajo.description,
                        "numero_atajo": atajo.numero_atajo,
                        "coordenadas": [
                            {
                                "id": coord.id,
                                "cordenadas": coord.cordenadas
                            } for coord in atajo.coordenadas
                        ] if atajo.coordenadas else [],
                    } for atajo in ruta_coordenada.atajos
                ],
                key=itemgetter('numero_atajo')
            )
            
            return {
                "id": ruta_coordenada.id,
                "coordenadas_principales": [
                    {
                        "id": coord.id,
                        "cordenadas": coord.cordenadas
                    } for coord in ruta_coordenada.coordenadas_principales
                ],
                "estaciones": sorted_estaciones,
                "atajos": sorted_atajos,
                "emergencias": [
                    {
                        "id": emergencia.id,
                        "tipo": emergencia.tipo,
                        "numero": emergencia.numero
                    } for emergencia in ruta_coordenada.emergencias
                ]
            }
        except Exception as e:
            print(f"Error en get_coordenada_content: {str(e)}")
            raise