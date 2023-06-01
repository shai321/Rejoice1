from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = []
class Detail(BaseModel):
    id: int
    name: str
    address: str
    dist: str
    state: str

@app.post("/user")
async def show_detail(detail: Detail):
    data.append(detail.dict())
    return data

@app.get("/user")
async def show_user_detail():
    return data

@app.get("/user/{user_id}")
async def show_user_detail(user_id: int):
    return data[user_id-1]

@app.put("/user/{user_id}")
async def show_user_detail(user_id: int, detail: Detail):
    data[user_id-1] = detail
    return data

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    data.pop(user_id-1)
    return data


    
