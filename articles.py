import re

import requests

class Articles:
    urls_ids = []

    def __init__(self, url):
        resp = requests.get(url)
        source = resp.text
        pattern = url + "/[a-zA-Z-]+"
        post_urls = re.findall(pattern,source)
        post_urls = list(set(post_urls))
        
        for url in post_urls:
            id = self.get_post_id(url)
            if id != None:
                url_id = {"url":url,"id":id}
                print(url_id)
                self.urls_ids.append(url_id)
        
    
    

    def get_post_id(self, url):
        resp = requests.get(url)
        source = resp.text
        regex = r"<body.*postid-([\d]+)"
        match = re.search(regex, source)
        if match != None:
            return match[1]
        else:
            return None