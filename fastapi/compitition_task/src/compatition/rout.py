from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.compatition.model import Compatition
from src.compatition.schemas import Request_Competition, Response_Competition

router = APIRouter()

#All competition detail
@router.get("/competition")
def show_competition(db: Session = Depends(get_db)):
    all_competition = db.query(Compatition).all()

    return all_competition

#Create new competition
@router.post("/competition", response_model=Response_Competition)
def create_competition(request: Request_Competition, db: Session = Depends(get_db)):
    new_competition = Compatition(**request.dict())
    db.add(new_competition)
    db.commit()

    return new_competition

#Update competition detail by id 
@router.put("/competition/{id}")
def update_competition(id: str, request: Request_Competition, db: Session = Depends(get_db)):
    db.query(Compatition).filter(Compatition.id == id).update(request.dict())
    db.commit()

    return "Done"

#Delete competition detail by id
@router.delete("/competition/{id}")
def delete_competition(id: str, db:Session = Depends(get_db)):
    db.query(Compatition).filter(Compatition.id == id).delete(synchronize_session=False)
    db.commit()

    return "Done"
