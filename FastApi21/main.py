import requests
from bs4 import BeautifulSoup

url = "http://example.com"

response = requests.get(url)

soup = BeautifulSoup (requests.text, "html.parse")

print(soup.title.text)