from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os 
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

#Allowed Origins (Front-end URL)


app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ORIGIN"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return{
       "message": "CORS ENABLE API"
    }