from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from config import Settings

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def create_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITH)


def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms=Settings.ALGORITH)
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")