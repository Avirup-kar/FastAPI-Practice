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

@app.get("/todos")
def get_todos():
    return {
        "Data": todos
    }    

@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"err": "todo not found"}        