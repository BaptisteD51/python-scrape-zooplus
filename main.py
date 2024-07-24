import requests
import re

resp = requests.get("https://www.zooplus.fr/magazine")
source = resp.text

def getCategoriesUrls(source):    
    pattern = r'(?<=\"nav-main-flyout__link\" href=\").*(?=\")'
    matches = re.findall(pattern,source)

    def keep(link):
        pattern = r'/[\w-]*/[\w-]*/[\w-]*$'
        match = re.search(pattern, link)
        if match != None:
            return True
        else:
            return False
        
    matches = list(filter(keep,matches))
    return matches


caturls = getCategoriesUrls(source)

def getArticlesUrls(url):
    resp = requests.get(url)
    source = resp.text
    pattern = 'r' + url + '/[a-zA-Z-]+'
    