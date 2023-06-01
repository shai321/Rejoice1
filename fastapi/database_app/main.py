from fastapi import FastAPI, Request, Depends, HTTPException
from . import model, crud, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/{user_id}")
async def show_detail(user_id: int, user: schemas.Detail, db: Session = Depends(get_db)):
    return crud.show_detail(db=db, user = user)


@app.get("/user")
async def show_detail(user: schemas.Detail,db: Session = Depends(get_db)):
    items = crud.get_detail(db)
    return {"item":items}



