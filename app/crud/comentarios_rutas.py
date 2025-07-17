from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import List

from ..models.listado_rutas_destino import Comentarios_Rutas
from ..models.destino import Usuario

def get_comentarios_by_ruta(db: Session, ruta_id: int, skip: int = 0, limit: int = 100) -> List[dict]:
    """Obtiene todos los comentarios aprobados de una ruta específica con datos del usuario"""
    
    # Consulta que combina comentarios con datos del usuario
    comentarios = db.query(
        Comentarios_Rutas, 
        Usuario.nombre.label("nombre_usuario"),
        Usuario.foto_perfil.label("foto_usuario")
    ).join(
        Usuario, 
        Comentarios_Rutas.usuario_id == Usuario.id
    ).filter(
        Comentarios_Rutas.ruta_id == ruta_id,
        Comentarios_Rutas.estado == "aprobado"  # Solo comentarios aprobados
    ).order_by(
        desc(Comentarios_Rutas.fecha_creacion)
    ).offset(skip).limit(limit).all()
    
    # Formatear resultados para la respuesta
    resultado = []
    for comentario, nombre_usuario, foto_usuario in comentarios:
        comentario_dict = {
            "id": comentario.id,
            "ruta_id": comentario.ruta_id,
            "usuario_id": comentario.usuario_id,
            "comentario": comentario.comentario,
            "calificacion": comentario.calificacion,
            "fecha_creacion": comentario.fecha_creacion,
            "estado": comentario.estado,
            "imagen": comentario.imagen,
            "nombre_usuario": nombre_usuario,
            "foto_usuario": foto_usuario
        }
        resultado.append(comentario_dict)
    
    return resultado