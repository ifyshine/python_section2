import sys
import io
import urllib.request as req
from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


url = "http://www.encar.com/"

mem = req.urlopen(url)
# print(mem)   # <http.client.HTTPResponse object at 0x000002A438110128>
# print(type(mem)) # <class 'http.client.HTTPResponse'>
#
#
# print("geturl", mem.geturl())
# print("status", mem.status) # 200, 404, 403, 500
# # 200 정상 404 없음 403 reject 500 서버자체의 compile error
# print("hearders", mem.getheaders())
#

print("info", mem.info()) # getheaders보단 깔끔(줄바꿈 되어 있음)
print("code", mem.getcode()) # status랑 비슷함.
print("read", mem.read(50))   # 해당 정수만큼의 데이터만 불러옴.
print("read", mem.read(50).decode("utf-8")) #euc-kr....


print(urlparse(url)) # 하나하나 차근차근 parsing 해줌.
