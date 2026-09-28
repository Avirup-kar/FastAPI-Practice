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
pwd_context = CryptContext(schemes=["bcrypt"])

#OAuth Setup
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

#Dummy_user_data
fake_user_db = {
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
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
    user = fake_user_db.get(form_data.username)
    if not user or not varify_password(form_data.password, user["hashed_password"]):
         raise HTTPException(
            status_code=400,
            detail="Invalid username or password"
        )
    access_token = create_token({"sub": form_data.username})
    
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
    
    
#Token verify
def verify_token(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRECT_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired Token"
        )
        
        
@app.get("/protected")
def protected_route(username: str = Depends(verify_token)):
    return {
        "message":"Hello you have access to this protected route!",
        "user":username
    }