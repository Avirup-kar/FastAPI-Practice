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

@app.put("/todo/update/{todo_id}") 
def update_todo(todo_id: int, updated_todo: Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return todos
    return {"err": "todo not found"}        

@app.delete("/todo/delet/{todo_id}")
def delet_todo(todo_id: int):
     for index,todo in enumerate(todos):
         if todo.id == todo_id:
            todos.pop(index)
            return todos
     return {"err": "todo not found"}          
