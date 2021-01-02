# Web scraping

When it comes to web scraping, there is a [trade-off](https://www.analyticsvidhya.com/blog/2020/04/5-popular-python-libraries-web-scraping/) between scraping static content fast (e.g. BeautifulSoup) and scraping dynamic content slow (e.g. Selenium).

Since most websites today are dynamic, it makes sense to use Selenium. However, for demo purposes I will use BeautifulSoup.

## Python demos

> Harvesting information from a news site

Here I will show you how to extract entities (e.g. names and places) from all the articles that appear on the front page of a news site.

First, install dependencies in virtual environment:

```
python3 -m venv venv
source venv/bin/activate
# Installing takes several minutes...
pip install -r requirements.txt
```

Run demo:

```
python ./demos/scraping_demo.py
```
