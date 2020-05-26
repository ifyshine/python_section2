from bs4 import BeautifulSoup
import sys
import io
import re # regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
    <ul>
        <li><a id="naver" href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.daum.com">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="https://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

# id값이나 속성값으로도 가져올 수 있음.
soup = BeautifulSoup(html, 'html.parser')
print(soup.find(id="naver").string) # id가 naver 인 것을 바로 가져올 수도 있음.

# 정규표현식을 통해 받을 수 있음. -> 사용률이 떨어짐.. (CSS선택자를 주로 사용)
li = soup.find_all(href=re.compile(r"^https://")) # rawdata로 하고 시작은 http로 한다!
for e in li:
    print(e.attrs['href'])
