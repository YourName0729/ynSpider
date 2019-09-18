from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
soup = BeautifulSoup(html, 'html.parser')

# for link in soup.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

bodycontent = soup.find('div', {'id':'bodyContent'})
links = bodycontent.findAll('a', {'href':re.compile('^(/wiki/)((?!:).)*$')})

for link in links:
    print(link.attrs['href'])