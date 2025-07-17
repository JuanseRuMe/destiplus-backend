import os
import sys
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Dict, Any
from ..models.destino import Restaurante, Bar, Actividad, Alojamiento

# Debugging imports
print("Current directory:", os.getcwd())
print("Python path:", sys.path)

try:
    print("Attempting to import models...")
    from app.models.destino import Restaurante, Bar, Actividad, Alojamiento
    print("Models imported successfully!")
except ImportError as e:
    print(f"Import error: {str(e)}")
    # Intentar importación alternativa
    try:
        print("Attempting alternative import...")
        from models.destino import Restaurante, Bar, Actividad, Alojamiento
        print("Alternative import successful!")
    except ImportError as e2:
        print(f"Alternative import error: {str(e2)}")
        try:
            print("Attempting relative import...")
            from ..models.destino import Restaurante, Bar, Actividad, Alojamiento
            print("Relative import successful!")
        except ImportError as e3:
            print(f"Relative import error: {str(e3)}")
            print("All import attempts failed")
            raise

def verify_user(email: str, type: str, db: Session) -> Dict[str, Any]:
    model_map = {
        'restaurante': Restaurante,
        'bares': Bar,
        'actividades': Actividad,
        'alojamientos': Alojamiento
    }
    
    model = model_map.get(type)
    if not model:
        raise HTTPException(400, "Tipo de negocio inválido")
        
    user = db.query(model).filter(model.usuario == email).first()
    
    return {
        "exists": True if user else False,
        "type": type,
        "message": "Usuario ya registrado" if user else "Usuario no encontrado"
    }

def register_user(email: str, type: str, db: Session) -> Dict[str, Any]:
    model_map = {
        'restaurante': Restaurante,
        'bares': Bar,
        'actividades': Actividad,
        'alojamientos': Alojamiento
    }
    
    model = model_map.get(type)
    if not model:
        raise HTTPException(400, "Tipo de negocio inválido")

    # Valores por defecto según el tipo de negocio
    default_values = {
        'restaurante': {
            'usuario': email,
            'name': 'Pendiente',
            'items': {'Tipo': 'Pendiente'},
            'calificacion': 0.0,
            'precio_promedio': 0,
            'img': '',
            'logo': '',
            'concepto': 'Pendiente',
            'horario': {'abren': '', 'cierran': ''},
            'contacto': 0,
            'metodosdepago': 'Pendiente',
            'servicios': {'delivery': 'No disponible', 'reservas': 'No disponible', 'parking': 'No disponible'},
            'destacados': [],
            'recurrentes': [],
            'antojos': [],
            'bebidas': [],
            'imgs': {'imagenes': []},
            'coordenadas': {'lat': 0, 'lng': 0},
            'destino_id': 1 # Valor por defecto
        },
        'bares': {
            'usuario': email,
            'name': 'Pendiente',
            'items': {'Tipo': 'Pendiente'},
            'calificacion': 0.0,
            'precio_promedio': 0,
            'img': '',
            'logo': '',
            'concepto': 'Pendiente',
            'horario': {'abren': '', 'cierran': ''},
            'contacto': 0,
            'metodos_de_pago': 'Pendiente',
            'servicios': {'delivery': 'No disponible', 'reservas': 'No disponible', 'parking': 'No disponible'},
            'destacados': [],
            'recurrente': [],
            'antojos': [],
            'bebidas': [],
            'imgs': {'imagenes': []},
            'coordenadas': {'lat': 0, 'lng': 0},
            'destino_id': 1
        },
        'actividades': {
            'usuario': email,
            'destino_id': 1,
            'logo': '',
            'oferente': 'Pendiente',
            'horario': {'abren': '', 'cierran': ''},
            'contacto': 0,
            'metodosDePago': 'Pendiente',
            'actividad': [],
            'coordenadas': {'lat': 0, 'lng': 0}
        },
        'alojamientos': {
            'usuario': email,
            'destino_id': 1,
            'oferente': 'Pendiente',
            'logo': '',
            'checkIn': '',
            'checkOut': '',
            'contacto': 0,
            'metodosDePago': 'Pendiente',
            'politicas': {},
            'coordenadas': {'lat': 0, 'lng': 0},
            'alojamiento': []
        }
    }

    try:
        # Crear nueva instancia con valores por defecto
        new_user = model(**default_values[type])
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {
            "exists": False,
            "type": type,
            "message": "Usuario registrado exitosamente"
        }
    except Exception as e:
        db.rollback()
        print(f"Error al registrar usuario: {str(e)}")
        raise HTTPException(500, f"Error al registrar usuario: {str(e)}")