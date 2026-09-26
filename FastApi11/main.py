from fastapi import FastAPI, requests

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: requests, call_next):
    print("Request Received")
    
    responce = await call_next(request)
    
    print("Responce send")
    
    return responce