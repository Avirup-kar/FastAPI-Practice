from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

@app.post("/create_user", status_code = status.HTTP_201_CREATED)
def create_user():
    return {
        "Message": "User created"
    }