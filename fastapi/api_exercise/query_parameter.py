from fastapi import FastAPI

app=FastAPI()

# fack_item=[{"item": "laptop", "name": "computer", "item_name": "ipad"},
#            {"item_name": "laptop"},{ "item_name": "computer"}, {"item_name": "ipad"},
#            {"item_name": "laptop"},{ "item_name": "computer"}, {"item_name": "ipad"},
#            {"item_name": "laptop"},{ "item_name": "computer"}, {"item_name": "ipad"}]
# @app.get("/item/")
# async def read_item(skip:int=1, limit:int=2):
#     return fack_item[skip: skip+limit]

# @app.get("/item/{id_name}/")
# async def read_item(id_name: str, q: str |None=None):
#     if q:
#         return {"id_name": id_name, "q": q}
#     return {"id_name": id_name}


#query parameter type conversion
# @app.get("/item/{id_name}/")
# async def read_item(id_name: str, q: str |None=None, short: bool=True):
#     item={"id_name": id_name}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item


# Multiple path and query parameter
# @app.get("/item/{item_id}/user/{user_id}")
# async def read_item(item_id: str, user_id: str, q: str |None=None, short: bool=True):
#     item={"item_id": item_id, "user_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "This is an amazing item that has a long description"})
#     return item


#required query parameter
@app.get("/item/{item_id}")
async def read_item(item_id: str, needy: str, skip: int=0, limit: int |None=None):
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}