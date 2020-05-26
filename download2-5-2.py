from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 1) html 웹에서 다운 받아 retrieve로 가져 오는 방법
# 2) 하드디스크에 있는 것을 읽어오는 방법
# 3) 기본 명령어 통하여 읽어오는 방법


# 1) 직접 접근하여 string 값 가져오기
html = """
<html>
<body>
<h1>파이썬 BeautifulSoup 공부</h1>
<p>태그 선택자</p>
<p>CSS 선택자</p>
</body>
</html>
"""

print('html', html)

soup = BeautifulSoup(html, 'html.parser')
print('soup', type(soup))
print('prettify', soup.prettify())

# 직접 접근으로 순차적으로 접근할 수 있음. (direct로..)
h1 = soup.html.body.h1
print('h1', h1) # <h1>파이썬 BeautifulSoup 공부</h1>
print(h1.string) # 파이썬 BeautifulSoup 공부

p1 = soup.html.body.p   # p가 두 개인데 무엇을 가져오나?
print('p1', p1) # <p>태그 선택자</p>  -> 첫 번째꺼만 가져옴!
p2 = p1.next_sibling.next_sibling # 엔터도 고려해줘야 함. 그러므로 2번 이동해야 함.
print('p2', p2)
p3 = p1.previous_sibling.previous_sibling
print('p3', p3)
print()

print("h1 >> ", h1.string)
print("p >> ", p1.string)
print("p >> ", p2.string)

# 이렇게 접근하는 것은 사이트가 업데이트되면 처음부터 다시 설정해줘야 하기에 많이 사용하진 않음..
