import requests
from bs4 import BeautifulSoup

# url
blogos = requests.get("https://blogos.com/")

# set BueatifulSoup
soup2 = BeautifulSoup(blogos.text, "html.parser")

# get headlines
blogos_headlines = soup2.find("ul", attrs={"class", "side-dot"})

bH = blogos_headlines.get_text()

from autoEmail import Mailsend

Mailsend()
