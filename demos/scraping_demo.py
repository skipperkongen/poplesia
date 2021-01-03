import sys
import time

from bs4 import BeautifulSoup
import requests
import spacy
nlp = spacy.load('da_core_news_md')

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

captures = []
for i, href in enumerate(get_front_links(soup)):
    if i >= MAX_ARTICLES: break
    subresp = requests.get(href)
    if subresp.status_code == 200:
        html = subresp.text
        subsoup = BeautifulSoup(html, 'html.parser')
        text = subsoup.find('div', class_='article-bodytext').getText()
        text = " ".join(text.split())
        ents = [e.text for e in nlp(text).ents]
        capture = {
            'type': 'poplesia/capture/scraping/v1',
            'timestamp': int(time.time()),
            'url': '',
            'title': '',
            'entities': ents
        }
        captures.append(capture)
    else:
        continue

with open('capture_scraping')
for capture in captures:
    print(capture)
