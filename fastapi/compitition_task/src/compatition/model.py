from sqlalchemy import Column, String, ForeignKey
from src.database import Base
from src.utils.same_model import DBmodel
from src.user.model import User
from sqlalchemy.dialects.postgresql import UUID


class Compatition(DBmodel, Base):
    __tablename__ = "compatition"

    name = Column(String)
    status = Column(String)
    description = Column(String)
    created_by = Column(String, ForeignKey(User.id))