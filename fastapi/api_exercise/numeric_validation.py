from fastapi import FastAPI, Path
from typing import  Annotated

app=FastAPI()



@app.get("/user/{user_id}")
async def detail(q=int,user_id: float= Path(title="The ID of the item to get", gt=0, lt=1)):
    result={"user_id": user_id}
    if q:
        result.update({"q": q})
    return result



