from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

fp = open("cars.html", encoding='utf-8')
soup = BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

car_func("#gr") # id가 gr
car_func("li#gr") # list tag에 id가 gr
car_func("ul > li#gr") # ul tag의 자식 중에 list tag의 gr
car_func("#cars #gr")
car_func("#cars > #gr")
car_func("li[id='gr']")
car_func("li:nth-of-type(4)")
print()

print("car_func", soup.select("li")[3].string)
print("car_func", soup.find_all("li")[3].string)
print()

# select vs find_all

# 람다식

car_lambda = lambda q : print("car_lambda", soup.select_one(q).string)

car_lambda("#gr") # id가 gr
car_lambda("li#gr") # list tag에 id가 gr
car_lambda("ul > li#gr") # ul tag의 자식 중에 list tag의 gr
car_lambda("#cars #gr")
car_lambda("#cars > #gr")
car_lambda("li[id='gr']")
car_lambda("li:nth-of-type(4)")
