from pydantic import BaseModel

class Request_Entry(BaseModel):
    title: str
    topic: str
    state: str
    country: str
    created_by: str
    updated_by: str |None = None


class Response_Entry(BaseModel):
    title: str
    topic: str
    state: str
    country: str

    class Config:
        orm_mode = True



