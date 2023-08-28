from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=226")

soup = BeautifulSoup(html, "html.parser")
news = soup.select("#main_content > div.list_body.newsflash_body > ul.type06_headline > li > dl > dt> a")
n=0
for new in news:
   url=new.get("href") 
   new=new.text.strip()
   if new !="" :
      n +=1
      print( "{:02d}".format(n), new)
      print( "  ", url)