from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
     name: str
     age: int

@app.post("/users")
def create_user(user: User):
     users .append(user)   