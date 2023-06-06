from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from  src.entry.model import Entry
from src.entry.schemas import Request_Entry, Response_Entry

entry = APIRouter()

#All entry details
@entry.get("/all_entry")
def show_entry(db: Session = Depends(get_db)):
    show_all_entry = db.query(Entry).all()

    return show_all_entry

#Create new entry
@entry.post("/create_entry", response_model=Response_Entry)
def create_entry(request: Request_Entry, db: Session = Depends(get_db)):
    new_entry = Entry(**request.dict())
    db.add(new_entry)
    db.commit()

    return new_entry

#Update entry by id
@entry.put("/update_entry/{id}")
def update_entry(id: str, request: Request_Entry, db:Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).update(request.dict())
    db.commit()

    return {"message": "Update Done"}

#Delete entry by id
@entry.delete("/delete_entry/{id}")
def delete_entry(id: str, db: Session = Depends(get_db)):
    db.query(Entry).filter(Entry.id == id).delete(synchronize_session=False)
    db.commit()

    return {"message": "Delete Done"}





