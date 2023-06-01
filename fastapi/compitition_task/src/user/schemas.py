from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4,  UUID

from datetime import datetime


class Request_User(BaseModel):
    # id: UUID = Field(default_factory=uuid4)
    name: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    gender: str
    role: str
    updated_by: str |None = None

class Response_User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: EmailStr
    first_name: str
    last_name: str
    gender: str
    role: str
   

    class Config:
        orm_mode = True




