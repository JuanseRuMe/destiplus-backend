# app/models/daily_learning.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

# Asegúrate de que Base se importe correctamente desde tu configuración de sesión de DB
# Ejemplo: from app.db.session import Base
# Si Base está en el mismo archivo que el engine:
# from ..db.session import Base

# Si estás definiendo Base aquí por primera vez para este módulo (ajusta según tu proyecto):
Base = declarative_base()

class DailyLearningContent(Base):
    __tablename__ = 'daily_learning_content'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    fun_fact = Column(Text, nullable=False)
    category = Column(String(100), nullable=False, index=True)
    icon_name = Column(String(50), nullable=True)  # Ej: "FaMicroscope"
    color_hex = Column(String(7), nullable=True)   # Ej: "#D4AF37"
    is_active = Column(Boolean, nullable=False, server_default=func.true()) # server_default en lugar de default para SQL puro

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self):
        return f"<DailyLearningContent(id={self.id}, question='{self.question[:20]}...', category='{self.category}')>"