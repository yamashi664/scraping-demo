import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
res = requests.get(url, timeout=10)
res.raise_for_status()  # エラー時は例外にして気づけるように
res.encoding = res.apparent_encoding  # 文字化け対策の一例

soup = BeautifulSoup(res.text, "lxml")
title = soup.find("h1").get_text(strip=True)
print("ページタイトル（h1）：", title)
