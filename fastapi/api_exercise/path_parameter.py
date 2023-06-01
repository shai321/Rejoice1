from fastapi import FastAPI
from enum import Enum


app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(item_id: int):
#     c = item_id+4
#     return c

# @app.get("/items/me")
# async def read_items():
#     return {"all_item": "The current items"}


# @app.get("/data/me")
# def read_items():
#     return {"all_item": "The current items"}

class Name(str,Enum):
    shailesh="yash"
    abhay="sagar"
    vijay="vijay"

@app.get("/name/{name}")
async def get_name(name: Name):
    if name.value=="yash":
        return {"name": name, "message": "learning api"}
    if name is Name.abhay:
        return {"name": name, "message": "learning database"}
    return {"name": name, "message": "learning json"}
    

