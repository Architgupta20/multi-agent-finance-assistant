# scrapes new headlines

import requests
from bs4 import BeautifulSoup

def scrape_earnings_news(company: str):
    url = f"https://www.google.com/search?q={company}+earnings+news"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    headlines = [h.get_text() for h in soup.select("h3")]
    return headlines[:5]
