from fastapi import FastAPI
from src.user.route import user
from src.entry.route import entry
from src.compatition.route import compatition 

import uvicorn

app = FastAPI()
app.include_router(user)
app.include_router(entry)
app.include_router(compatition)


