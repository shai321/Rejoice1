from sqlalchemy.orm import Session
from . import model, schemas

def get_detail(db: Session):
    return db.query(model.User).all()

def show_detail(db: Session, user: schemas.Detail):
    db_item = model.User(**user.dict())
    db.add(db_item)
    db.commit()
    return db_item
