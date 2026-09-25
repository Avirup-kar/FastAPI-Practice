from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    password: str

class userResponce(BaseModel):
    name: str
    age: int  


@app.get("/user", response_model= userResponce)
def get_user():
    return {
        "name": "Avirup kar",
        "age": 19,
        "password": 1234567
    }