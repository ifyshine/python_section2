import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


# 이미지 다운로드(via urlretrieve)
imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20130915_223%2Fwhdaud3373_1379254029536jhxD8_JPEG%2FUHQ_shutterstock_2522829.jpg&type=b400"
htmlURL = "http://google.com"

savePath1 = "d:/test1.jpg"
savePath2 = "d:/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료")
