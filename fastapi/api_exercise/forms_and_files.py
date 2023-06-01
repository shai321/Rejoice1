from fastapi import FastAPI, Form, File, UploadFile
from typing import Annotated

app = FastAPI()

# @app.post("/login/")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username}


# @app.post("/files/")
# async def create_file(files: Annotated[list[bytes], File(description="A file read as bytes")]):
#     return {"file_size": [len(file) for file in files]}

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}  

@app.post("/files/")
async def create_file(
    file: Annotated[bytes, File()],
    files: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": files.content_type,
    }
