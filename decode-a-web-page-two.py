import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)

paragraphs_table = soup.find_all('p')
paragraphs_table = paragraphs_table[6:-6]
for paragraph in paragraphs_table:
    print(paragraph.text)