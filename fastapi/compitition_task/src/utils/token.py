import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends, HTTPException
from datetime import timedelta, time
import datetime
from jose import JWTError

key = '8bb918b556f55a605363726a12a198aad3301420240b8ef23c129c5c5aff440e'
ALGORITHM = "HS256"

class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="shailesh")

def create_access_token(data: dict, expire_time = datetime.datetime.utcnow()+datetime.timedelta(seconds=10)):
    payload = {"data": data, "exp": expire_time}
    encoder_jwt = jwt.encode(payload, key, algorithm=ALGORITHM)
    return encoder_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    
    try: 
        payload = jwt.decode(token, key, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return {"message": "Time expire"} 
    except jwt.InvalidTokenError:
        return "Invalide token. Please log in again"