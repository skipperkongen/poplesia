import sys
import time

from bs4 import BeautifulSoup
import requests

MAX_ARTICLES = 1

resp = requests.get('https://ekstrabladet.dk')
if resp.status_code == 200:
    html = resp.text
else:
    print('Could not read web page, exiting')
    sys.exit(0)

soup = BeautifulSoup(html, 'html.parser')
print(soup.title.text)

def get_front_links(soup):
    for art in soup.find_all('article'):
        # get first href
        yield art.find('a').attrs['href']

subpages = []
for i, href in enumerate(get_front_links(soup)):
    if i >= MAX_ARTICLES: break
    subresp = requests.get(href)
    if subresp.status_code == 200:
        html = subresp.text
        subsoup = BeautifulSoup(html, 'html.parser')
        print(subsoup.title.text)
        text = subsoup.find('div', class_='article-bodytext').getText()
        text = " ".join(text.split())
        print(text)
    else:
        continue
