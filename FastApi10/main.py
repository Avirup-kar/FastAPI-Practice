from fastapi import FastAPI, Depends

app = FastAPI()

def get_current_user():
    return{
      "user": "Mohit"
    }