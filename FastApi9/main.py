from fastapi import FastAPI, HTTPException, requests
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
          self.name = name
    
@app.get("/users/{name}")
def get_user(name:str):
    if name != "Avirup kar":
        raise UserNotFoundException(name)
    return {
        "name": name
    }
    