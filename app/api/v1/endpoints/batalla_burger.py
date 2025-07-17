from fastapi import FastAPI, Depends, HTTPException, Request, APIRouter
from sqlalchemy.orm import Session
from typing import List # Si vas a tener endpoints que devuelvan listas


from ....models.batalla_burguer import BurgerVote
from ....schemas.batalla_burger import VoteCreate, Vote, VoteCount
from ....crud.batalla_burger import create_vote, get_votes_by_burger
from ....db.session import SessionLocal, engine, get_db 

router = APIRouter()

@router.post("/votes/batalla", response_model= Vote, status_code=201) # Si usas app directamente
def create_new_vote(
    vote: VoteCreate, # Datos validados del cuerpo del request
    request: Request,         # Para obtener la IP del cliente
    db: Session = Depends(get_db) # Inyección de dependencia de la sesión de DB
):
    client_ip = request.client.host # Obtener la IP del cliente

    try:
        created_vote = create_vote(db=db, vote=vote, ip_address=client_ip)
        return created_vote
    except ValueError as e:
        # Capturar el error específico que lanzamos desde CRUD si hay duplicado
        raise HTTPException(status_code=409, detail=str(e)) # 409 Conflict
    except Exception as e:
        # Capturar cualquier otro error inesperado
        print(f"Error inesperado al crear voto: {e}")
        raise HTTPException(status_code=500, detail="Error interno al procesar el voto.")



@router.get("/votes/burger/{burger_id}/count", response_model=VoteCount)
def read_vote(burger_id: int, db: Session = Depends(get_db)):
    count = get_votes_by_burger(db=db, burger_id=burger_id)
    return VoteCount(burger_id=burger_id, vote_count=count)
