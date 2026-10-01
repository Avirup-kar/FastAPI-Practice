# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup (requests.text, "html.parse")

# print(soup.title.text)

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/news")
def get_news():
    url = "https://indianexpress.com/"
    
    responce = requests.get(url)
    
    soup = BeautifulSoup(requests.text, "html.parse")
    
    title = []
    
    for item in soup.find_all("a", class_= "")