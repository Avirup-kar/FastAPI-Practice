from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "Message": "User created"
    }
    
    
@app.get("/get_user")
def get_user():
    return {
        "status": "Success",
        "message": "User created",
        "data": {
            "name": "Avirup kar",
            "age": 19
        }
    }