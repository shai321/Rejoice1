from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated
from datetime import datetime, time, timedelta
from uuid import UUID

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: int
#     tax: float
 

# @app.put("/user/{user_id}")
# async def detail(user_id: int, item: Annotated[Item, Body(
#             example={
#                 "name": "Foo",
#                 "description": "A very nice Item",
#                 "price": 300,
#                 "tax": 333.2,
#             })]):
#     return {"user_id": user_id, "item": item}



@app.put("/user/{user_id}")
async def detail(user_id: int, start_datetime: datetime |None=None, end_datetime: datetime |None=None, repeat_at: time |None=None, process_after: timedelta |None=None):
    # start_process = start_datetime + process_after
    # duration = end_datetime - start_process
    return {
        "user_id": user_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        # "start_process": start_process,
        # "duration": duration
    }
