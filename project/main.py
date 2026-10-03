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
def create_blog(blog: schemas.BlogCreate, db:Session = Depends(get_db)):
    new_blog = models.Blog(
        title = blog.title,
        content = blog.content
    )
    
    db.add(create_blog)
    db.commit()
    db.refresh()
    
    return new_blog