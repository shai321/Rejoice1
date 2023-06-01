from pydantic import BaseModel

class Detail(BaseModel):
    id: int
    name: str
    address: str
    state: str
     
    class config:
        orm_mode = True

