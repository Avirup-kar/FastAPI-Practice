from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name: str
    age: int

# @app.post("/create_user")
# def create_user(name: str, age: int):
#     return {"name": name, "age": age}

@app.post("/create_user")
def create_user(user:user):
    return {
        "Messaeg": "User created successfuly",
        "Data": user
    }