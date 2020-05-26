from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# CSS selector 사용하여 추출하기 (scrapying할 때 가장 많이 쓰임)
# 2-4에서 했던 'a' tag만 가져오는 방법은 복잡한 사이트에서 사용하기 힘듦
# -> 이곳 저곳 'a' tag가 있기에, 내가 원하는 것을 selection 및 필요없는 부분 delete해주는 과정이 추가로 필요하게 됨.
# 코드가 길어지고 유지보수가 힘들어짐... 정확히 필요한 것만 선택할 수 있는 것이 필요함!


html = """
<html><body>
<div id="main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java 초고수 되기</li>
        <li>파이썬 기초 프로그래밍</li>
        <li>파이썬 머신러닝 프로그래밍</li>
        <li>안드로이드 블루투스 프로그래밍</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

# h1 tag의 강의목록 가져오기
h1 = soup.select("div#main > h1")
print('h1', h1)

for z in h1:
    print(z.string)
# select는 하나만 가져와도 list 구조로 가져오기에, 이렇게 for문으로 분리해줘야 함 -> 번거로움...
print()

# so, select_one 사용!
h1_2 = soup.select_one("div#main > h1")
print('h1_2', h1_2.string)
# 가져올 게 하나라면 select_one으로 출력함..
print()


# ex2. ul tag의 list 가져오기
list_li = soup.select("div#main > ul.lecs > li")
for li in list_li:
    print("li >>>", li.string)
print()
