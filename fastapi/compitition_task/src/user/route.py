from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.user.schemas import Request_User, Response_User
from src.user.model import User

router = APIRouter()

#Get all user details
@router.get("/users")
def show_detail(user: Request_User, db: Session = Depends(get_db)):
    users = db.query(User).all()

    return {"users": users}

#Create new users
@router.post("/users", response_model=Response_User)
def user_detail(user: Request_User, db: Session = Depends(get_db)):
    user.password = user.password+"12354"
    users = User(**user.dict())
    db.add(users)
    db.commit()

    return users

#Update user detail by name
@router.put("/users/{name}")
def update_detail(name: str, user: Request_User, db: Session = Depends(get_db)):
    db.query(User).filter(User.name == name).update(user.dict())
    db.commit()

    return "Done"

#Delete user detail by name
@router.delete("/users/{name}")
def delete_detail(name: str, db: Session = Depends(get_db)):
    db.query(User).filter(User.name == name).delete(synchronize_session=False)
    db.commit()
    
    return "Done"





