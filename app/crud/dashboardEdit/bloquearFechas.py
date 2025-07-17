from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from datetime import datetime
from typing import List, Optional
from ...models.destino import Reserva
from ...schemas.dashboardEdit.bloquearFechas import ReservaBloqueoCreate

def get_reserva(db: Session, reserva_id: int):
    return db.query(Reserva).filter(Reserva.id == reserva_id).all()

def get_reservas_by_alojamiento_y_tipo(
    db: Session,
    alojamiento_id: int,
    tipo_alojamiento_id: str
):
    return db.query(Reserva).filter(
        Reserva.alojamiento_id == alojamiento_id,
        Reserva.tipo_alojamiento_id == tipo_alojamiento_id
    ).all()

def check_disponibilidad(
        db: Session,
        alojamiento_id: int,
        tipo_alojamiento_id: str,
        fecha_inicio: datetime,
        fecha_fin: datetime
) -> bool:
    reservas_existentes = db.query(Reserva).filter(
        Reserva.alojamiento_id == alojamiento_id,
        Reserva.tipo_alojamiento_id == tipo_alojamiento_id,
        Reserva.estado.in_(['pendiente', 'confirmada', 'bloqueado']),
        or_(
            and_(
                Reserva.fecha_inicio <= fecha_fin,
                Reserva.fecha_fin >= fecha_inicio
            )
        )
    ).first()

    return reservas_existentes is None

def create_bloqueo(db: Session, bloqueo: ReservaBloqueoCreate):
    if not check_disponibilidad(
        db,
        bloqueo.alojamiento_id,
        bloqueo.tipo_alojamiento_id,
        bloqueo.fecha_inicio,
        bloqueo.fecha_inicio
    ):
        raise ValueError("Las fechas selecionadas no estan disponibles")
    
    bloqueo_dict = bloqueo.dict()
    bloqueo_dict.pop('estado', None)

    db_bloqueo = Reserva(
        **bloqueo_dict,  # Usar el dict después del pop
        estado='bloqueado',
        fecha_creacion=datetime.utcnow()
    )

    try:
        db.add(db_bloqueo)
        db.commit()
        db.refresh(db_bloqueo)
        return db_bloqueo
    except Exception as e:
        db.rollback()
        raise e
    
def get_fechas_bloqueadas(  
    db: Session,
    alojamiento_id: int,
    tipo_alojamiento_id: str
) -> List[dict]:
    reservas = db.query(Reserva).filter(
        Reserva.alojamiento_id == alojamiento_id,
        Reserva.tipo_alojamiento_id == tipo_alojamiento_id,
        Reserva.estado.in_(['bloqueado', 'confirmada', 'pendiente'])
    ).all()

    return [{
        'fecha_inicio': reserva.fecha_inicio,
        'fecha_fin': reserva.fecha_fin,
        'estado': reserva.estado,
        'reserva_id': reserva.id
    } for reserva in reservas]

def delete_bloqueo(db: Session, reserva_id: int):
    bloqueo = db.query(Reserva).filter(
        Reserva.id == reserva_id,
        Reserva.estado == 'bloqueado'
    ).first()
    
    if not bloqueo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bloqueo no encontrado"
        )
    
    try:
        db.delete(bloqueo)
        db.commit()
        return {"message": "Bloqueo eliminado correctamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al eliminar el bloqueo"
        )