
"""
Flask Server
@author: pkugoodspeed
@date: 06/30/2018
@copyright: jogchat.com
"""
import newspaper
from termcolor import colored


NEWS_INFO = ['source_url', 'url', 'title', 'top_img', 'top_image', 'keywords', 'meta_keywords', 'tags', 'authors', 'publish_date', 'summary', 'meta_description', 'meta_data']


def extractFromSrc(src_url):
    data = []
    paper_src = newspaper.build(src_url)
    print(paper_src.articles)
    for article in paper_src.articles:
        article.download()
        if article.download_state != 2:
            print(colored("ERROR: Failed to download paper from " + article.url, "red", "on_white"))
            continue
        article.download()
        article.parse()
        article.nlp()
        a_data = vars(article)
        data.append(
            dict([(key, a_data[key]) for key in NEWS_INFO]))
        print("=" * 64)
        print(colored("Ariticle :" + article.title, 'cyan'))
        print(colored('\n' + article.summary, 'blue'))
        print("=" * 64 + "\n")
    return data


def extractFromUrl(url):
    article = newspaper.Article(url)
    article.download()
    if article.download_state != 2:
        print(colored("ERROR: Failed to download paper from " + url, "red", "on_white"))
        return
    article.parse()
    article.nlp()
    print("=" * 64)
    print(colored("Ariticle :" + article.title, 'cyan'))
    print(colored('\t' + article.summary, 'blue'))
    print("=" * 64 + "\n")
    a_data = vars(article)
    return dict([(key, a_data[key]) for key in NEWS_INFO])
