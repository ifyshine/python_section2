import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 특정 values를 주고 그에 맞는 response를 받는 방법...
API = "https://api.ipify.org"

values = {
    'format' : 'json'
}
print('before', values)

params = urlencode(values)
print('after', params)

url = API + "?" + params
print("요청 url", url)

reqData = req.urlopen(url).read().decode('utf-8')
print("출력", reqData)
