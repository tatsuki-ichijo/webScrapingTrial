import requests
from bs4 import BeautifulSoup

# url
mainichi = requests.get("http://www.mainichi.jp/")

# set BueatifulSoup
soup = BeautifulSoup(mainichi.text, "html.parser")

# get headlines and links
div = soup.find_all("div")

headlines = []
links = []

for headline in div:
    for main_box in headline.find_all(class_="main-box"):
        for a in main_box.find_all("a"):
            headlines.append(a.get_text())
            links.append("http:" + a.get('href'))

new_links = links[0:10]
new_headlines = []
for stripping in headlines:
    stripped = stripping.strip('\n')
    new_headlines.append(stripped)

# results
results = []
for c, d in zip(new_headlines, new_links):
    ai = "\n" + c + "\n(" + d + ")" + "\n"
    results.append(ai)

url = "https://notify-api.line.me/api/notify"
token = "jee51ogSpbfBqYHHzBBtTypxTXRPlfqQFSVb17mnjaI"
headers = {"Authorization" : "Bearer "+ token}

payload = {"message": results}

r = requests.post(url, headers=headers, params=payload)
