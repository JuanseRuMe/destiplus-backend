# app/crud/crud_project.py
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List, Optional

# Ajusta la ruta de importación según tu estructura
from ..models.proyectosAndresPage import Project 

def get_projects_for_preview(
    db: Session, 
    skip: int = 0, 
    limit: int = 10, 
    featured: bool = False # Para determinar el orden para el home vs. página de proyectos
) -> List[Project]:
    """
    Obtiene una lista de proyectos para previsualización.
    Si 'featured' es True, ordena por 'priority' y luego por 'start_date' o 'created_at'.
    Si no, ordena solo por 'start_date' o 'created_at'.
    No filtra por 'is_active' según la solicitud.
    """
    query = db.query(Project)

    # Define el campo de fecha para ordenar por defecto (si start_date no está, usa created_at)
    # SQLAlchemy no permite usar OR directamente en order_by para campos,
    # así que priorizaremos start_date si existe, o created_at.
    # Para una lógica más compleja, se podría usar una expresión case o Coalesce.
    # Por simplicidad, si start_date es común, ordenamos por él.
    # Si muchos proyectos no tienen start_date, created_at sería mejor default.

    default_order_field = Project.start_date
    if not db.query(Project.start_date).first(): # Chequeo simple si el campo es usado
         default_order_field = Project.created_at


    if featured:
        # Para destacados: menor prioridad primero, luego los más recientes
        query = query.order_by(asc(Project.priority), desc(default_order_field))
    else:
        # Para listado general: los más recientes primero
        query = query.order_by(desc(default_order_field))
    
    return query.offset(skip).limit(limit).all()

# Aquí podrían ir otras funciones CRUD para proyectos completos en el futuro