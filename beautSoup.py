#  imdb ye göre en iyi 20 film

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)

html = response.content
soup = BeautifulSoup(html, 'html.parser')

liste = soup.find('tbody', {"class":"lister-list"}).find_all("tr", limit=20)
count = 0

for tr in liste:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year =  tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text

    count += 1
    print(f"{count}. film: {title.ljust(45)} yıl: {year.ljust(6)} puanı: {rating}")


   # print(liste)







