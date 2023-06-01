from typing import Annotated
from fastapi import Depends, FastAPI, Cookie, Header, HTTPException

app = FastAPI()

# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons

# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


#classes as dependencies
# fake_items_db = [{"item": "Foo"}, {"name": "Bar"}, {"item_name": "Baz"}]

# class CommonQueryParams:
#     def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit

# @app.get("/items/")
# async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response


#first dependencies
# def query_extractor(q: str | None = None):
#     return q

# def query_or_cookie_extractor(
#     q: Annotated[str, Depends(query_extractor)],
#     last_query: Annotated[str | None, Cookie()] = None):
#     if not q:
#         return last_query
#     return q

# @app.get("/items/")
# async def read_query(query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]):
#     return {"q_or_cookie": query_or_default}


#dependencies in path operation decoration
# async def verify_token(x_token: Annotated[str, Header()]):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header")
#     # return x_token
    

# async def verify_key(x_key: Annotated[str, Header()]):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key header invalid")
#     # return x_key

# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "Foo"}, {"item": "Bar"}]

# def sum(a:int=3, b:int=5):
#     s=a+b
#     try:  
#         return s
#     except:
#         return "value error"
# def mul(c: int= Depends(sum)):
#     # s = sum()
#     d=c*3
#     try:
#         return d
#     except:
#         return "value error"
    
# @app.get("/items")
# async def detai(z: Annotated[int,Depends(mul)]):
#     return z
