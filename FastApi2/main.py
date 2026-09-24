from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/users")
def get_users(name: str = None):
    return {"Name":name}


@app.get("/products")
def get_users(item: int = 10):
    return {"Item": item}