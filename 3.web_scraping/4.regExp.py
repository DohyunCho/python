from distutils.filelist import findall
import re

#ca?e
p = re.compile("ca.e") 
# . : 은 하나의 문자
# ^ : 은 문자열의 시작
# $ : 은 문자열의 끝

def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 매치되면 표시 않되면 오류발생
        print("m.string : ", m.string) # 입력 받은 문자열 표시
        print("m.start() : ", m.start()) # 일치하는 문자열 시작 인텍스
        print("m.end() : ", m.end()) # 일치하는 문자열 끝 인텍스
        print("m.span() : ", m.span()) # 일치하는 문자열 시작,끝 인텍스
    else:
        print("패턴일치 없음")

m = p.match("careless") # p.match("casfe") "care" "case"  "good care" "careless"  match 는 처음부터 일치하는지 확인
print_match(m)

m = p.search("good care") # search 는 일치하는 거 있는지 확인
print_match(m)

list = p.findall("good care cafe") # findall 는 일치하는 거 모두 확인
print(list)
