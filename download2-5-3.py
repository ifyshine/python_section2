from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 태그선택자 이용하여 string 가져오기

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

# <li> tag 아래에 있는 <a> tag의 속성 url 한 번에 가져오기
soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a") # a tag에 바로 접근해서 한 번에 받는 것.
print('links', type(links))
print(links)
print()


# ex1
# 이후 반복문을 통한 추출이 필요함.
for a in links:
    print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('txt >> ',txt, 'href >> ', href)
print()

# ex2 : string이 daum인 것을 가져 오기.
b = soup.find_all("a", string="daum")
print(b)
print()

# ex3 : find_all vs find
c = soup.find("a")
print(c) # 가장 위에 있는 거 하나만 가져옴
print()

# ex4 : limmit - 가져오는 갯수 설정
d = soup.find_all("a", limit=3)
print(d)
