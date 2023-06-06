from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.user.schemas import Request_User, Response_User, Login
from src.user.model import User
from src.utils.token import create_access_token, get_current_user
import json
from typing import Annotated

user = APIRouter()

#Get all user details
@user.get("/all_users")
def show_detail(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return {"users": users}

#Create new users
@user.post("/create_user", response_model=Response_User)
def user_detail(request: Request_User, db: Session = Depends(get_db)):
    request.password = request.password+"12354"
    create_user = User(**request.dict())
    db.add(create_user)
    db.commit()

    return create_user

@user.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    user_data = db.query(User).filter(User.email == request.email,
                                 User.password == request.password).first()

    if user_data:
        user_encode = create_access_token({"name": str(user_data.id), "email": user_data.email})
        return user_encode     
    else :
        return {"message": "email and password is wrong"}
    

@user.put("/update_user/{id}")
def update_detail(id: str, access_token: Annotated[User, Depends(get_current_user)], request: Request_User, db: Session = Depends(get_db)):
    """Update user detail by name"""
    

    db.query(User).filter(User.id == id).update()
    db.commit()

    return {"message": "Update Done"}

#Delete user detail by name
@user.delete("/delete_user/{id}")
def delete_detail(id: str, db: Session = Depends(get_db)):
    a=db.query(User).filter(User.id == id).delete(synchronize_session=False)
    db.commit()
    
    return {"message": "Delete Done"}





