import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
print(soup.find("h1").get_text())
