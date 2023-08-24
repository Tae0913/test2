from bs4 import BeautifulSoup
from urllib.request import urlopen
#위 두개는 크롤링을 하기위해 사용하는 라이브러리 사이트에 있는 내용을 가져와 우리가 볼 수 있게 만듦.
html = urlopen("http://jeju-s.jje.hs.kr/jeju-s") #과학고 홈페이지
soup = BeautifulSoup(html, "html.parser")
#container > div.main_content > div.meal_menu > ul > li
bap = soup.select(".meal_menu ul li")
print("="*50)
print( bap)
print("-"*50)
menu=""
for m in bap:
   print( m.text.strip() ) 
   menu = m.text

print("="*50)
menu = menu.split(" ")
print(menu)
print("="*50)
i = 0
for m in menu:
   i = i + 1
   if m != "":
      print(i, m)
print("="*50)