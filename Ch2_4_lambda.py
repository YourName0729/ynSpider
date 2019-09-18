from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

twoTags = soup.findAll(lambda tags: len(tags.attrs) == 2)

for tag in twoTags:
    print(tag, '\n')