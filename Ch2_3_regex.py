from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

images = soup.findAll('img', {'src':re.compile('\.\.\/img\/gifts\/img.\.jpg')})

for image in images:
    print(image['src'])