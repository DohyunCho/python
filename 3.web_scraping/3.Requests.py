import requests

#res = requests.get("http://www.naver.com/zzzz1")
#res = requests.get("http://www.naver.com")
#res = requests.get("http://cafe.naver.com/clover349111")
res = requests.get("https://nadocoding.tistory.com")
print("응답코드 : ", res.status_code)
res.raise_for_status() # 문제있으면 바로 종료
# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("응답에 문제가 있습니다. : ", res.status_code)

print(len(res.text))

with open("webcrolling.html", "w", encoding="utf-8") as f:
    f.write(res.text)