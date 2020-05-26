from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

#---------------------------------
# opener = req.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# req.install_opener(opener)
#-------------------------------------

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('아이유')
url = base + quote

res = req.urlopen(url)
savePath = 'D:/imagedown/' # D:\\imagedown\\

# 예외 처리 - 폴더 만들기 예제
try:
    if not (os.path.isdir(savePath)): # 그 폴더가 있는지 확인
        os.makedirs(os.path.join(savePath))
except OSError as e:  # 에러 살피기
    if e.errno != errno.EEXIT:
        print('폴더 만들기 실패')
        raise

soup = BeautifulSoup(res, 'html.parser')
img_list = soup.select("div.img_area._item > a.thumb._thumb > img")


for i, img_list in enumerate(img_list, 1):
    print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg')
    print(fullFileName)
    # req.urlretrieve(img_list['data-source'], fullFileName)


print('다운로드 완료')
