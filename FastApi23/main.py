from fastapi import FastAPI, requests
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI

#Limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: requests, exc: RateLimitExceeded):
    return JSONResponse (
        status_code=429,
        content={"detail":"Too many Requests"}
        )
    

#Rate Limiter API
@app.get("/data")
def get_data(request: requests):
    return{
     "message": "Success"
    }