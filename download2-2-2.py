import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# 이미지 다운로드(via urlopen)
imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130915_223%2Fwhdaud3373_1379254029536jhxD8_JPEG%2FUHQ_shutterstock_2522829.jpg&type=b400"
htmlURL = "http://google.com"

savePath1 = "d:/test1.jpg"
savePath2 = "d:/index.html"

f = dw.urlopen(imgUrl).read() # 메모리에 할당만 함..
f2 = dw.urlopen(htmlURL).read() # with를 써볼 것!

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)   # 이걸 사용하는게 좋음. with 벗어나는 문장에선 자동으로 close 실행됨.






print("다운로드 완료")
