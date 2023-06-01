from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# class Detail(BaseModel):
#     name: str
#     price: int
#     tax: float
#     tag: list[str] = []


# @app.post("/user")
# async def creat_detail(detail: Detail) -> Detail:
#     return detail

# @app.get("/user")
# async def read_detail() :
#     return [
#         {"name":"shailesh", "price":55},
#         {"name":"abhay", "price":32.0}
#         ]


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr

# @app.post("/user")
# async def creat_detail(user: UserIn):
#     return user


#add on output model
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


#return type and data filtering
# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
    
# class Base(BaseModel):
#     name:str |None=None

# class UserIn(BaseUser, Base):
#     password: str

# @app.post("/user/")
# async def create_user(user: UserIn) -> Base:
#     return user

#response model encoding
class Item(BaseModel):
    name: str
    price: float
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "price": 50.2, "tax": 10.5, "tags": ["shai","abhay"]},
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude={"name","tax"})
async def read_item(item_id: str):
    return items[item_id]
