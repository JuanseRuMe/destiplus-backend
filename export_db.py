"""
Script para exportar datos usando la configuración existente de la aplicación
"""

import json
import os
from datetime import datetime
import sys

# Añadir el directorio actual al path
sys.path.append('.')

# Importar desde tu aplicación
from app.db.session import Base, engine
from app.core.config import settings
from sqlalchemy import MetaData

# Directorio donde se guardarán los archivos
EXPORT_DIR = "context_data"

def serialize_datetime(obj):
    """Función para serializar objetos datetime a JSON"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

def export_all_tables():
    """Exporta todas las tablas de la base de datos a archivos JSON"""
    # Crear directorio si no existe
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
    
    # Usar el engine existente de tu aplicación
    connection = engine.connect()
    
    try:
        # Obtener metadata
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        # Obtener todas las tablas
        all_tables = metadata.tables
        print(f"Se encontraron {len(all_tables)} tablas")
        
        # Diccionario para almacenar todos los datos
        all_data = {}
        
        # Exportar cada tabla
        for table_name, table in all_tables.items():
            print(f"Exportando tabla: {table_name}")
            
            # Consultar datos
            result = connection.execute(table.select())
            rows = result.fetchall()
            
            # Obtener nombres de columnas
            column_names = table.columns.keys()
            
            # Convertir a lista de diccionarios
            table_data = []
            for row in rows:
                # Convertir Row a dict
                row_dict = {column: value for column, value in zip(column_names, row)}
                table_data.append(row_dict)
            
            # Guardar tabla individual
            file_path = os.path.join(EXPORT_DIR, f"{table_name}.json")
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(table_data, f, default=serialize_datetime, ensure_ascii=False, indent=2)
            
            print(f"  - {len(table_data)} registros exportados a {file_path}")
            
            # Agregar al diccionario de todos los datos
            all_data[table_name] = table_data
        
        # Guardar todas las tablas en un único archivo
        combined_path = os.path.join(EXPORT_DIR, "all_tables.json")
        with open(combined_path, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, default=serialize_datetime, ensure_ascii=False, indent=2)
        
        print(f"\nTodos los datos combinados guardados en: {combined_path}")
        
    finally:
        connection.close()

if __name__ == "__main__":
    export_all_tables()
    print("\nProceso de exportación completado.")