from fastapi import FastAPI, HTTPException, Depends
from jose import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext

app = FastAPI()

#JWT Config
SECRECT_KEY = "my^%385683^3name5u47465#@&is758$fastapi"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

#Password hashing setup
pwd_context = CryptContext(schemes=["bycrypt"])

#OAuth Setup
OAuth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy_user_data
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("12345")
    }
}

#Hash Password
def hash_password (password:str):
    return pwd_context.hash(password)

#varify Password
def varify_password(plain_password, hased_password):
    return pwd_context.verify(plain_password, hased_password)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp": expire 
    })
    
    token = jwt.encode(to_encode, SECRECT_KEY, algorithm=ALGORITHM)
    
    return token


#Login API (Token Genrate)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db(form_data:username)
    
    
#Token verify
def verify_token(token: str = Header(None)):
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=ALGORITHM)
        return payload
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )
        
@app.get("/secure")
def secure_data(user = Depends(verify_token)):
    return{
        "message": "Secure Data Accessed",
        "user": user
    }