from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

#Allowed Origins (Front-end URL)
origin = [
   "http://localhost:5173"
]

app.add_middleware()