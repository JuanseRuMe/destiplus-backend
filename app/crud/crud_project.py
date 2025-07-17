# app/crud/crud_project.py
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from typing import List, Optional

from ..models.proyectosAndresPage import Project 

# --- NUEVA FUNCIÓN para obtener un proyecto completo por slug ---
def get_project_by_slug(db: Session, slug: str) -> Optional[Project]:
    """
    Obtiene un único proyecto por su slug.
    No filtra por 'is_active' ya que se asumió que la columna fue eliminada o no se usa.
    """
    return db.query(Project).filter(Project.slug == slug).first()