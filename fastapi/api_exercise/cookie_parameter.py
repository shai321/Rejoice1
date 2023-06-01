from fastapi import FastAPI, Cookie, Header
from typing import Annotated

app = FastAPI()


@app.get("/user")
async def detail(user_id: Annotated[str |None, Cookie()] = None):
    return {"user_id": user_id}