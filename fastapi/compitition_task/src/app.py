from fastapi import FastAPI
from src.user import route
from src.entry import routes
from src.compatition import rout

import uvicorn

app = FastAPI()

app.include_router(route.router)
app.include_router(routes.router)
app.include_router(rout.router)

