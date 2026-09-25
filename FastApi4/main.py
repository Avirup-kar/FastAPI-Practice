from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/create_user")
def create_user(user: User):
    return {
        "Message": "User created",
        "data": user
    }


class address(BaseModel):
    