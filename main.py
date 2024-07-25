import re

import requests

from categories import Categories
from articles import Articles
from csvwrite import Csv

magazine = input("Enter the magazine url:")

cat_urls = Categories(magazine).get_urls()

all_pairs = []

for cat_url in cat_urls:
    articles = Articles()
    all_pairs.extend(articles.get_urls_ids(cat_url))

Csv(all_pairs)