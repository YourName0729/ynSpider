from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

count = 0
visited = set()
def getLinks(url):
    global visited  
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    soup = BeautifulSoup(html, 'html.parser')

    
    for link in soup.findAll('a', {'href':re.compile('^(/wiki/)((?!:).)*$')}):
        global count
        if count > 20:
            return
        newPage = link.attrs['href']
        if newPage not in visited:          
            visited.add(newPage)
            print(newPage)
            count += 1 
            getLinks(newPage)


getLinks('')