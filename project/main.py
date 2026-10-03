from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Sessionlocal
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#DB Dependency
def get_db():
    db = Sessionlocal()
    try:
      yield db
    finally:
      db.close()

#Home
@app.get("/")
def home():
    return{
      "message": "Blog API Started"
    }
    
#Create Blog
@app.post("/blog", response_model= schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate):
    