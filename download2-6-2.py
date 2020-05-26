from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 같은 경로에 있는 파일 불러들어오기
fp = open("food-list.html", encoding='utf-8')
soup = BeautifulSoup(fp, "html.parser")

# 리스트 태그의 8번째를 가져와서 바로 출력
# Select-one : 하나만 선택. 바로 출력가능(하나만 선택했기에)
print("1", soup.select("li:nth-of-type(4)")[1].string)

print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)
# # -> id

print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string)
# 조건에 맞는게 1개여도 index로 접근해야 함 -> list로 만들어지기 때문..

print("4", soup.select("#ac-list > li.alcohol.high")[0].string)
# . 은 class

param = {"data-lo": "cn", "class" : "alcohol"}
print("5", soup.find("li", param).string) # 태그선택자 이용
# "li" 중 param 조건에 맞는 것을 반환하도록!
# find에서 두 번째 칸(조건)도 dictionary 형태로 반환시킬 수 있음.

print("6", soup.find(id="ac-list").find("li", param).string)
# 5번 방법으로 하는 것이 더 가독성 높음..]

for ac in soup.find_all("li"):
    # 9개의 li tag 모두 긁어옴...
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
