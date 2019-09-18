from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

gifts = soup.find('table', {'id':'giftList'}).children

# print(len(gifts))
for gift in gifts:
    print(gift)

siblings = soup.find('table', {'id':'giftList'}).tr.next_siblings

for sibling in siblings:
    print(sibling)