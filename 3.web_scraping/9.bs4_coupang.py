# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup
# import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"}

# res = requests.get(url)
res = requests.get(url, headers)
# res.raise_for_status() # 문제있으면 바로 종료

print(res.text)
# soup = BeautifulSoup(res.text, "lxml")

# items = soup.find_all("dl", attrs={"class":"search-product-wrap"})
# print(items[0].find("div", attrs={"class":"name"}).get_text())
