from sqlalchemy import Column, String, Boolean, DateTime
from src.database import Base
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

class DBmodel():
    __tablename__ = "same_detail"

    id = Column(UUID, primary_key=True, default=uuid.uuid4())
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    updated_by = Column(String)
    is_active = Column(Boolean, default=True)