# -*- coding: utf-8 -*-

from collections import OrderedDict

import requests
from bs4 import BeautifulSoup
import unicodecsv as csv


FILENAME = 'results.csv'
URL = "http://www.bankier.pl/fundusze/notowania/wszystkie"
HEADERS = (
    u'Nazwa funduszu', 
    u'Kurs', 
    u'Waluta', 
    u'St. zw. 1D',
    u'St. zw. 7D',
    u'St. zw. 1M',
    u'St. zw. 3M',
    u'St. zw. 1R',
    u'St. zw. 3L',
    u'Data',
    u'Ranking 12M',
)

response = requests.get(URL)
response.encoding = 'utf-8'
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
table = soup.find_all('table', class_='sortTableMixedData')[0]


data = list()

for row in table.find_all('tr'):
	tmp_dict = OrderedDict()
	for header, cell in zip(HEADERS, row.find_all('td', recursive=False)):
		tmp_dict[header] = cell.text.strip()
	data.append(tmp_dict)

f = open(FILENAME, 'wb')

w = csv.writer(f, encoding='utf-8')
w.writerow(HEADERS)

for x in data:
	w.writerow(x.values())n
f.close()