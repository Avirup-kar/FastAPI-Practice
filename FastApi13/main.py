from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todod(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    complted = Column(String)
    
    
Base.metadata.create_all(bind=engine)    