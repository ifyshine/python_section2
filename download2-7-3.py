from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#--------------- 기본 -----------------------
url = "https://www.inflearn.com/tag-curation/tag/448"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")
#------------------------------------------------

#---------------- 유니코드 이용 ---------------#
# import urllib.parse as rep
# base= "https://www.inflearn.com/"
# quote = rep.quote_plus("courses/it-programming", safe='/')
# # quote : 유니코드로 생성됨.
#
# url = base + quote
# res = req.urlopen(url).read()
# soup = BeautifulSoup(res, "html.parser")
# --------------------------------------------


recommand = soup.select("div.course_title")

for i,e in enumerate(recommand,1):
    print(i,e.string)

#main > section.section.section_1 > div.container.course_list > div > div:nth-child(1) > div > a > div.card-image > figure > img
