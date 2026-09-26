from fastapi import FastAPI, HTTPException, Requests
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name:str):
          self.name = name
          
@app.exception_handler(UserNotFoundException)      
def user_not_found_handler(reqquest: Requests, exe: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message": f"User {exe.name} not found"
        }
    )    
    
@app.get("/users/{name}")
def get_user(name:str):
    if name != "Avirup kar":
        raise UserNotFoundException(name)
    return {
        "name": name
    }
    