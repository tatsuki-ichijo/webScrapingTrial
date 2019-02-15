import requests
from bs4 import BeautifulSoup

# url
blogos = requests.get("https://blogos.com/")

# set BueatifulSoup
soup = BeautifulSoup(blogos.text, "html.parser")

# get headlines
blogos_headlines = soup.find_all(class_ = "pickup-article-main-column-simple-0 pickup-box")

headlines = []
for headline in blogos_headlines:
    for side_dot in headline.find_all(class_ = 'side-dot'):
        for li in side_dot.find_all('li'):
            headlines.append(li.text)

# get links
blogos_headlines2 = soup.find_all("div")

links = []
for link in blogos_headlines2:
    for pickup in link.find_all(class_ = "pickup-article-main-column-simple-0"):
        for aa in pickup.find_all('a'):
            links.append("http://www.blogos.com"+aa.get('href'))

newlinks = links[0:10]

# Results
for c , d in zip(headlines, newlinks):
    print(c + ", " + d)


