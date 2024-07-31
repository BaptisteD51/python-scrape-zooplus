import re

import requests

from front.categories import Categories
from front.articles import Articles
from front.csvwrite import Csv
from back.scrape_back import scrape_back

magazine = input("Enter the magazine url:")

scrape_back()

cat_urls = Categories(magazine).get_urls()

all_pairs = []

for cat_url in cat_urls:
    articles = Articles()
    all_pairs.extend(articles.get_urls_ids(cat_url))

Csv(all_pairs)