# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# data = response.json()
#print(data[:2])

from fastapi import FastAPI
import requests

app = FastAPI()

#GET all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()