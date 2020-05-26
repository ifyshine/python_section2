import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# 이미지 다운로드(via urlopen)
imgUrl = "https://siape.veta.naver.com/fxclick?eu=EU10041888&calp=-&oj=A4YjrwVVtw%2B3VyLQuD3ZS1SZisnjXWIojYzm%2Fj95uDN40LzGhlVOIfW1YEqVwubmCwqC6SiClbn9fM6Y%2BcPWlDso7nnmgYB5Ne22tgUa034&ac=8075870&src=4285675&br=3109382&evtcd=P901&x_ti=1276&tb=&oid=&sid1=&sid2=&rk=5036765e230ee2792201a3dc49034920&eltts=8Zz6UF6wlFzdSmGBRjLW8g%3D%3D&lu=&brs=Y&"
vidUrl = "https://b01-kr-naver-vod.pstatic.net/tveta/c/read/v2/VOD_ALPHA/X_COM_922/2020-04-24/BA76A40E07185DFB34404AE8C3AC028F_1D0DAF5CD6F97D7CC343972442CE114D_2020-04-24.mp4?_lsu_sa_=6dc5e9fd615d603651da45446c25fab6fec03038380a2f363c4767cc27ef3c65e3298a3a6905570c407936623634fb974a32d54367c70d199d0272ec9c91da351cdd74a284c80deb3551a8173516a4e3"

savePath1 = "d:/test1.png"
savePath2 = "d:/test2.mp4"


f = dw.urlopen(imgUrl).read() # 메모리에 할당만 함..
f2 = dw.urlopen(vidUrl).read() # with를 써볼 것!

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)   # 이걸 사용하는게 좋음. with 벗어나는 문장에선 자동으로 close 실행됨.



print("다운로드 완료")
