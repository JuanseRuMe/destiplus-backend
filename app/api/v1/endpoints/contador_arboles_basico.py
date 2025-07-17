from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ....db.session import get_db
from ....crud.contador_arboles_basico import ArbolesCRUD
from ....schemas.contador_arboles_basico import DatosArbolesRuta

router = APIRouter()

@router.get("/contador/arboles/{ruta_id}", response_model=DatosArbolesRuta)
def get_arboles_info_ruta(
    ruta_id: int,
    db: Session = Depends(get_db)
):
    """
    Obtiene información completa sobre los árboles plantados en una ruta específica,
    incluyendo el total, CO2 ahorrado y los últimos plantadores.
    """
    try:
        resultado = ArbolesCRUD.get_arboles_info_por_ruta(db, ruta_id)
        return resultado
    except Exception as e:
        print(f"Error detallado: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener información de árboles: {str(e)}"
        )