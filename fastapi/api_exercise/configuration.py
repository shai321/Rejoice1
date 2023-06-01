from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from fastapi.encoders import jsonable_encoder

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model=Item, summary="Create an item")
# async def create_item(item: Item):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item

# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]

# @app.get("/users/", tags=["users"], deprecated=True)
# async def read_users():
#     return [{"username": "johndoe"}]



#using the jsonable_encoder
fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime |None = None
    description: str | None = None

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    return fake_db
