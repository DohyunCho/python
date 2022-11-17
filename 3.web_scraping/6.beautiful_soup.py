# pip install beautifulsoup4
# pip install lxml
import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(url, headers)
res = requests.get(url)
res.raise_for_status() # 문제있으면 바로 종료

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)   # title 태그 표시
# print(soup.title.get_text()) # title 태크의 text 표시
# print(soup.a)       # 첫번째 a 태그 표시
# print(soup.a.attrs) # 첫번째 a 의 속성 표시
# print(soup.a["href"]) # 첫번째 a 태그 href 속성 표시

# print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a 태그 중에서 속성 class 가 Nbtn_upload 인것 표시
# print(soup.find(attrs={"class":"Nbtn_upload"}))

rank01 = soup.find(attrs={"class":"rank01"})
# print(rank01.a)
print(rank01.a.get_text)
print(rank01.next_sibling.next_sibling)

rank02 = rank01.next_sibling.next_sibling
print(rank02.a.get_text)

