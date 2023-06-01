from sqlalchemy import Column, String, Integer
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), index=True)
    address = Column(String(250), index=True)
    state = Column(String(250))