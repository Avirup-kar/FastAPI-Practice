from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastApi"}

@app.get("/about")
def home():
    return {"message": "Welcome to About"}