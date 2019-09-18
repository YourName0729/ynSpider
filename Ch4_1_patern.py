import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url, self.title, self.body = url, title, body

    def print(self):
        print("URL: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body: {}".format(self.body))

class Website:
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url, self.titleTag, self.bodyTag = url, titleTag, bodyTag

class Crawler:
    def getPage(self, url):
        try:
            html = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(html.text, 'html.parser')
    
    def safeGet(self, pageObj, selector):
        tar = pageObj.select(selector)
        if tar is None or len(tar) == 0:
            return ''
        return '\n'.join([ele.get_text() for ele in tar])
    def parse(self, site, url):
        soup = self.getPage(url)
        
        if soup is None:
            return
        title = self.safeGet(soup, site.titleTag)
        body = self.safeGet(soup, site.bodyTag)
        if title != '' and body != '':
            Content(url, title, body).print()

def main():
    websites = [Website('O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'),
                Website('Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'),
                Website('Brookings', 'http://www.brooking.edu', 'h1', 'div.post-body'),
                Website('New York Times', 'http://nytimes.com', 'h1', 'p.story-content')]

    crawler = Crawler()
    crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')


if __name__ == '__main__':
    main()