from fastapi import FastAPI

app = FastAPI()

# @app.post("/create_user")
# def create_user(name: str, age: int):
#     return {"name": name, "age": age}

@app.post("/create_user")
def create_user(user:dict):
    return {
        "Messaeg": "User created successfuly",
        "Data": user
    }