from fastapi import FastAPI, Path, Body
from typing import Optional, Annotated
from pydantic import BaseModel, Field

app=FastAPI()


# class Detail(BaseModel):
#     name: str
#     description: str |None = Field(default=None, title="user detail", description="the description length max. ten", max_length=10)
#     price: int
#     tax: Optional[float]

# class User(BaseModel):
#     username: str
#     address: Optional[str]

# @app.put("/user/{user_id}")
# async def read_detail(user_id: int, item: Detail, user: User, q: Annotated[int, Body(embed=False)]):
#     result={"user_id": user_id, "impotance": q}
#     if item:
#         result.update({"item": item})
#     if user:
#         result.update({"user": user})
#     return result

class Image(BaseModel):
    url: str |None=None
    name: str

class Detail(BaseModel):
    name: str
    price: int
    tag: list[str] = []
    image: list[Image] |None=None

@app.put("/user/{user_id}")
async def read_all(user_id: int, item:Detail):
    return {"usre_id": user_id, "Detail": item}