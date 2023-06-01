from fastapi import FastAPI,Query
from typing import Annotated
from pydantic import Required

app=FastAPI()

#regular expresion
# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3,max_length=10,regex="^fixedquery$")] = None):
#     results = {"items": [{"item_id": "laptop"}, {"item_id": "computer"}]}
#     if q:
#         results.update({"q": q})
#     return results

#default value
# @app.get("/items/")
# async def read_items(q: str = Query(default="fixedquery",min_length=3)):
#     results = {"items": [{"item_id": "laptop"}, {"item_id": "computer"}]}
#     if q:
#         results.update({"q": q})
#     return results

#Ellipsis
# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "laptop"}, {"item_id": "computer"}]}
#     if q:
#         results.update({"q": q})
#     return results

#multiple time use in q querys
# @app.get("/items")
# async def read_items(q: Annotated[list[str] |None, Query()]=None):
#     results = {"items": [{"item_id": "laptop"}, {"item_id": "computer"}]}
#     if q:
#         results.update({"q": q})
#     return results

#title
@app.get("/items")
async def read_items(q: Annotated[str |None, Query(title="laptop and computer store", description="All item is new")]=None):
    results = {"items": [{"item_id": "laptop"}, {"item_id": "computer"}]}
    if q:
        results.update({"q": q})
    return results

