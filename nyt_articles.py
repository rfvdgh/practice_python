#! usr/bin/env python3

import requests
from bs4 import BeautifulSoup

source = requests.get('http://nytimes.com').text
soup = BeautifulSoup(source, 'lxml')

section = soup.find('div', class_='css-jbmajz')
article1 = section.find('article').h2.text

for article in section.find_all('article'):
    try:
        headline = article.h2.text
        print(headline)
    except:
        pass