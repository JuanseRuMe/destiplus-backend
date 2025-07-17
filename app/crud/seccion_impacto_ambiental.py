from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List, Dict, Any, Optional

from ..models.destino import ArbolesPlantados, ArbolesDonados, Usuario
from ..models.listado_rutas_destino import ListadoRutas

def get_arboles_info_completa(db: Session, ruta_id: Optional[int] = None) -> Dict[str, Any]:
    """
    Obtiene información completa de árboles plantados con todos sus detalles relacionados.
    
    Args:
        db: Sesión de base de datos
        ruta_id: ID opcional de la ruta para filtrar árboles
        
    Returns:
        Diccionario con información completa de árboles y estadísticas
    """
    # Consulta base
    query = db.query(ArbolesPlantados)
    
    # Filtrar por ruta si se proporciona ID
    if ruta_id is not None:
        query = query.filter(ArbolesPlantados.ruta_id == ruta_id)
    
    # Ordenar por fecha de plantación descendente
    query = query.order_by(desc(ArbolesPlantados.fecha_plantacion))
    
    # Obtener todos los árboles
    arboles_db = query.all()
    
    # Preparar resultado
    arboles_info = []
    
    for arbol in arboles_db:
        # Información base del árbol
        arbol_data = {
            "id": arbol.id,
            "donacion_id": arbol.donacion_id,
            "plantador_id": arbol.plantador_id,
            "fecha_plantacion": arbol.fecha_plantacion,
            "ubicacion_geografica": arbol.ubicacion_geografica,
            "ruta_id": arbol.ruta_id,
            "nombre_ubicacion": arbol.nombre_ubicacion,
            "region": arbol.region,
            "pais": arbol.pais,
            "especie": arbol.especie,
            "estado_actual": arbol.estado_actual,
            "imagen_url": arbol.imagen_url,
            "descripcion": arbol.descripcion,
            "co2_estimado": arbol.co2_estimado or 5.0,  # Valor por defecto si es None
            "donante": None,
            "plantador": None,
            "ruta": None
        }
        
        # Obtener información del donante si existe
        if arbol.donacion_id:
            donacion = db.query(ArbolesDonados).filter(ArbolesDonados.id == arbol.donacion_id).first()
            if donacion:
                donante_data = {
                    "id": donacion.donante_id,
                    "nombre": donacion.donante_nombre,
                    "fecha_donacion": donacion.fecha_donacion,
                    "cantidad_total": donacion.cantidad_total,
                    "descripcion": donacion.descripcion,
                    "estado": donacion.estado,
                    "foto_perfil": None
                }
                
                # Agregar foto de perfil del donante si existe
                if donacion.donante_id:
                    donante = db.query(Usuario).filter(Usuario.id == donacion.donante_id).first()
                    if donante:
                        donante_data["foto_perfil"] = donante.foto_perfil
                
                arbol_data["donante"] = donante_data
        
        # Obtener información del plantador si existe
        if arbol.plantador_id:
            plantador = db.query(Usuario).filter(Usuario.id == arbol.plantador_id).first()
            if plantador:
                arbol_data["plantador"] = {
                    "id": plantador.id,
                    "nombre": plantador.nombre,
                    "foto_perfil": plantador.foto_perfil
                }
        
        # Obtener información de la ruta si existe
        if arbol.ruta_id:
            ruta = db.query(ListadoRutas).filter(ListadoRutas.id == arbol.ruta_id).first()
            if ruta:
                arbol_data["ruta"] = {
                    "id": ruta.id,
                    "nombre": ruta.nombre,
                    "img": ruta.img,
                    "calificacion": ruta.calificacion
                }
        
        arboles_info.append(arbol_data)
    
    # Calcular estadísticas
    total_arboles = len(arboles_info)
    co2_total = sum(arbol.get("co2_estimado", 0) or 0 for arbol in arboles_info)
    m2_reforestados = total_arboles * 2  # Estimación: 2m² por árbol
    
    # Construir respuesta completa
    respuesta = {
        "cantidad_total": total_arboles,
        "co2_total": co2_total,
        "m2_reforestados": m2_reforestados,
        "arboles": arboles_info
    }
    
    return respuesta