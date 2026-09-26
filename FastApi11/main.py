from fastapi import FastAPI, requests
import time

app = FastAPI()


@app.middleware("http")
async def log_middleware(request: requests, call_next):
    start_time = time.time()
    
    responce = await call_next(request)
    
    process_time = time.time()-start_time
    
    print(f"Path: {request.url.path} | Time: {process_time}")
    
    return responce

# @app.middleware("http")
# async def my_middleware(request: requests, call_next):
#     print("Request Received")
    
#     responce = await call_next(request)
    
#     print("Responce send")
    
#     return responce