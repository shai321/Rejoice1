from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from  src.entry.model import Entry
from src.entry.schemas import Request_Entry, Response_Entry

router = APIRouter()

#All entry details
@router.get("/entry")
def show_entry(db: Session = Depends(get_db)):
    all_entry = db.query(Entry).all()

    return all_entry

#Create new entry
@router.post("/entry", response_model=Response_Entry)
def create_entry(request: Request_Entry, db: Session = Depends(get_db)):
    new_entry = Entry(**request.dict())
    db.add(new_entry)
    db.commit()

    return new_entry

#Update entry by id
@router.put("/entry/{id}")
def update_entry(id: str, request: Request_Entry, db:Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).update(request.dict())
    db.commit()

    return "Done"

#Delete entry by id
@router.delete("/entry/{id}")
def delete_entry(id: str, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    db.commit()

    return "Done"





