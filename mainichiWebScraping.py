import requests
from bs4 import BeautifulSoup

# url
html = requests.get("http://www.mainichi.jp/")

# set BueatifulSoup
soup = BeautifulSoup(html.text, "html.parser")

# get headlines
mainnewsindex = soup.find("ul", attrs={"class", "list-typeA"})

print(mainnewsindex.get_text())



