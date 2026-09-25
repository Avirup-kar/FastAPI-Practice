from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "Message": "User created"
    }
    
    
@app.get("/get_users")
def get_users():
    return {
        "status": "Success",
        "message": "User created",
        "data": {
            "name": "Avirup kar",
            "age": 19
        }
    }
    
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id": 1,
        "name": "Mohit"
    }