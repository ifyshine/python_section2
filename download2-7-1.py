
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 기본 ---------------?????? -------------------
# from bs4 import BeautifulSoup
# url = "http://finance.daum.net/domestic/market_cap"
# res = req.urlopen(url).read()
# soup = BeautifulSoup(res, "html.parser")

# print('soup', soup.prettify())

# top = soup.select("#boxMarketCap > div.box_contents > div > table > tbody > tr")
#
# print(top)
#
# for i, e in enumerate(top,1):
#     print(i, ",", e.find("a").string, " : ", e.find("span").string)
#


# -----------------------------------------------------#
from fake_useragent import UserAgent
import json

# Fake Header 정보
ua = UserAgent()

# 헤더 선언
headers = {
    'User-Agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"

# print(req.get_method())   #Post or Get 확인
# print(req.get_full_url()) #요청 Full Url 확인

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')


# 응답 데이터 확인(Json Data)
# print('res', res)

# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)['data']

# 중간 확인
print('중간 확인 : ', rank_json, '\n')

for elm in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )
