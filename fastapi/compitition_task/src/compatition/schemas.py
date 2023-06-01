from pydantic import BaseModel

class Request_Competition(BaseModel):
    name: str
    status: str
    description: str
    created_by: str
    updated_by: str |None = None



class Response_Competition(BaseModel):
    name: str
    status: str
    description: str

    class Config:
        orm_mode = True

