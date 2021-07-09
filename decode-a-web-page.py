import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html)
h3_table = soup.find_all('h3')
for h3 in h3_table:
    title = h3.span
    if title != None:
        if title.get('class') is None:
            print(title.string)


