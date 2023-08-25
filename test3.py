from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s") 
soup = BeautifulSoup(html, "html.parser")

with open("temp.html", "r", encoding="utf-8") as file:
    html = file.read()

    soup = BeautifulSoup(html, "html.parser")


    pp = soup.select("#blue2")
    for p in pp:
        print(p.text)