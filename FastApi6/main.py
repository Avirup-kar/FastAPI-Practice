from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
     name: str
     age: int

@app.post("/users")
def create_user(user: User):
     users.append(user) 
     return users


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = False):
     if user_id < len(users):
          users[user_id] = user       
          return {
               "Message": "User updated",
               "Notify": notify,
               "Data": user
          }
     return {"err": "User not found"} 