from fastapi import FastAPI, HTTPException, Header, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRECT_KEY = "my^%385683^3name5u47465#@&is758$fastapi"

ALGORITHM = "HS256"

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp": expire 
    })
    
    token = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    
    