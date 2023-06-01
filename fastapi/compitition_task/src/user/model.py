from sqlalchemy import Column, String
from src.database import Base
from src.utils.same_model import DBmodel

class User(DBmodel, Base):
    __tablename__ = "user"
    
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    role = Column(String)
