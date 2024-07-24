import re

import requests

from categories import Categories
from articles import Articles

magazine = "https://www.zooplus.no/magasin"

cat_urls = Categories(magazine).get_urls()

all_pairs = []

for cat_url in cat_urls:
    all_pairs.extend(Articles(cat_url).urls_ids)

print(all_pairs)