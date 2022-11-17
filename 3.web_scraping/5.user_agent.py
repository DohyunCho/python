from email import header
import requests

url = "https://nadocoding.tistory.com"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"}

res = requests.get(url, headers)
# res.raise_for_status() # 문제있으면 바로 종료

with open("nadocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)