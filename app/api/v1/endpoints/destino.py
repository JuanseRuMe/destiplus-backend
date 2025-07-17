from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ....db.session import get_db
from ....crud.destino import DestinoCRUD
from ....schemas.destino import DestinoResponse

router = APIRouter()

@router.get("/destinos/{municipio}/content", response_model=DestinoResponse)
def get_destino_content(
    municipio: str,
    db: Session = Depends(get_db)
):
    destino = DestinoCRUD.get_destino_content(db, municipio)
    if not destino:
        raise HTTPException(status_code=404, detail="Destino not found")
    return destino