from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app=FastAPI()

class Detail(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]

# @app.post("/item")
# async def creat_detail(item: Detail):
#     # return {"name":item.name, "price":item.price}
#     return item

# @app.post("/item")
# async def creat_detail(item: Detail):
#     item_dict=item.dict()
#     if item.tax:
#         total_tax=item.price+item.tax
#         item_dict.update({"total_tex": total_tax})
#     return item_dict

@app.put("/item/{item_id}")
async def item_detail(item_id: int, item:Detail, q: str |None=None):
    item_dict=item.dict()
    result = {"item_id": item_id, **item_dict}
    if q:
        result.update({"q": q})
    return result
