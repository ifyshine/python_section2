from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"
print(">>", urljoin(baseUrl, "b.html"))
# >> http://test.com/html/b.html

print(">>", urljoin(baseUrl, "sub/b.html"))
# >> http://test.com/html/sub/b.html
# urljoin : 절대경로는 묶어놓고 나머지 파일만 위치를 지정할 수 있음.

print(">>", urljoin(baseUrl, "../index.html"))
# >> http://test.com/index.html

print(">>", urljoin(baseUrl, "../img/img.jpg"))
# >> http://test.com/img/img.jpg

print(">>", urljoin(baseUrl, "../css/css.jpg"))
# >> http://test.com/css/css.jpg
