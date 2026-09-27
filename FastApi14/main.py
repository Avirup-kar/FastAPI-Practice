from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
       "message": "Async API"
    }

# async def task():
#     await time.sleep(3)
#     print("Print the data")
#     return

# task()