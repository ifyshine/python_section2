from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os
import time

#---------------------------------
opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)
#-------------------------------------

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = 'https://www.inflearn.com/tag-curation/tag/356'
res = req.urlopen(url)
savePath = 'D:\\imagedown\\' # D:\\imagedown\\

# 예외 처리 - 폴더 만들기 예제
try:
    if not (os.path.isdir(savePath)): # 그 폴더가 있는지 확인
        os.makedirs(os.path.join(savePath))
except OSError as e:  # 에러 살피기
    if e.errno != errno.EEXIT:
        print('폴더 만들기 실패')
        raise

soup = BeautifulSoup(res, 'html.parser')

img_list = soup.select("div.column.is-one-fifth-fullhd.is-3-widescreen.is-3-desktop.is-4-tablet.is-6-mobile")

#
# for i, e in enumerate(img_list, 1):
#     print(i, e)

for i,e in enumerate(img_list,1):
    with open(savePath+"text_"+str(i)+".txt","wt") as f:
        f.write(e.select_one("div.course_title").string)
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    src = e.select_one('img.swiper-lazy')['data-src']
    fileName =os.path.dirname(src)  + "/" + rep.quote_plus(os.path.basename(src))
    req.urlretrieve(fileName, fullFileName)
    time.sleep(0.5)

    # req.urlretrieve('https://cdn.inflearn.com/' + req.quote(e.select_one("figure.is_thumbnail > img")['src'][:25]),fullFileName)

print("다운로드 완료")
#

# -----------------------------------------------------------------
# recommand = soup.select("div.course_card_item")

# for i,e in enumerate(recommand,1):
#     with open(savePath+"title_"+str(i)+".txt", "wt") as f:
#         f.write(e.select_one("div.course_title").string)
#     fullfilename = os.path.join(savePath, savePath+'img_'+str(i)+'.png')
#     time.sleep(0.5)
#     req.urlretrieve('https://cdn.inflearn.com/' + req.quote(e.select_one("figure.is_thumbnail > img")['src'][25:]),fullfilename)
#
# print("강좌 정보 텍스트 출력 및 이미지 다운 완료!")
