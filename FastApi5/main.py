from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todo")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "Message": "Todo added",
        "Data": todos
    }