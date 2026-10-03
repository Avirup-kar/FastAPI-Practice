from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Sessionlocal
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return{
      "message": "Blog API Started"
    }