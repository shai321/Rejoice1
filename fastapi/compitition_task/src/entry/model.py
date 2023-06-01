from sqlalchemy import Column, String, Integer, ForeignKey
from src.database import Base
from src.utils.same_model import DBmodel
from src.user.model import User
from sqlalchemy.dialects.postgresql import UUID

class Entry(DBmodel, Base):
    __tablename__ = "entry"

    title = Column(String)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    created_by = Column(String, ForeignKey(User.id))