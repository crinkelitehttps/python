#!/usr/bin/python3

# Scrape donedeal.ie

import requests
from bs4 import BeautifulSoup

url = "http://www.boards.ie/vbulletin/showthread.php?t=2057580480&page=3"
r = requests.get(url)

soup = BeautifulSoup(r.content, "lxml")

links = soup.find_all("a")

for link in links:
        print("<a href='%s'>%s</a>" %(link.get("href"), link.text))
