"""
Flask Server
@author: pkugoodspeed
@date: 06/30/2018
@copyright: jogchat.com
"""


import json
import time
import newspaper
from .extractor import extractFromUrl


def queryFromSrc(src_url):
    paper_src = newspaper.build(src_url)
    urls = paper_src.article_urls()
    for u in urls:
        data = extractFromUrl(u)
        if not data["summary"]:
            time.sleep(3)
            continue
        author = "Chaoran Wang"
        if data["authors"]:
            author = data["authors"][0]
        paper_cfg = {
            "Timestamp": int(time.time()),
            "Author": author,
            "Title": data["title"],
            "URL": data["url"],
            "Summary": data["summary"]
        }
        for keyword in data['meta_keywords']:
            paper_cfg["Domain"] = keyword
            paper_str = json.dumps(paper_cfg, indent=4)
            print(paper_str)
        time.sleep(5)
    