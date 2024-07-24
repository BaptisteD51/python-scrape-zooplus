import re

import requests

class Categories:
    urls = []

    def __init__(self, url):
        resp = requests.get(url)
        source = resp.text
        
        pattern = r'(?<=\"nav-main-flyout__link\" href=\").*(?=\")'
        matches = re.findall(pattern,source)
        matches = list(filter(self.keep,matches))
        self.urls = matches

    
    def keep(self, link):
        pattern = r'/[\w-]*/[\w-]*/[\w-]*$'
        match = re.search(pattern, link)
        if match != None:
            return True
        else:
            return False
        
    
    def get_urls(self):
        return self.urls
    