# import requests
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup (requests.text, "html.parse")

# print(soup.title.text)

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

#Cache Storage
cache_data = []
last_fetch = 0

@app.get("/news")
def get_news(page: int = 1, limit:int = 5):
    global cache_data, last_fetch
    
    start = time.time()
    
    if start - last_fetch > 60:
        print("Fetching Fresh Data")
        
        url = "https://news.ycombinator.com/"
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, "html.parser")
            
        title = []
            
        cache_data = [    
            item.text for item in soup.find_all("span", class_="titleline"):
                title.append(item.text)
        ]
        
        last_fetch = time.time()
    
        