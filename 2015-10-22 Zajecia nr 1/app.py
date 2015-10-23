# -*- coding: utf-8 -*-

# import python core library modules first
from collections import OrderedDict  # import only interesting thing from module

# after one newline import 3rd party modules
import requests  # import whole module
from bs4 import BeautifulSoup
import unicodecsv as csv  # import whole module as a drop-in replacement for csv module

# after another newline import modules that we own
# from daftcode_utils import rock_that_workshop

# constants should be UPPERCASED and at the begginning of the app
FILENAME = 'results.csv'  # we can use both: single ' and double quotes "
URL = "http://www.bankier.pl/fundusze/notowania/wszystkie"
HEADERS = (  # this is a tuple, created as a literal
    u'Nazwa funduszu',  # see the u before the string? These can hold ąęćżł
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

response = requests.get(URL)  # a simple HTTP GET request will be used
response.encoding = 'utf-8'  # but the requests module incorrectly guesses the encoding here
html_doc = response.text  # that's the decoded content of the response

soup = BeautifulSoup(html_doc, 'html.parser')  # parse the contents as a HTML
# look for tables with specified class. Take the first one (0-based indices).
table = soup.find_all('table', class_='sortTableMixedData')[0]

data = list() # we could also write: data = []

for row in table.find_all('tr'):  # take the data from one row at a time
    tmp_dict = OrderedDict()  # we will extract the row data into this dictionary

    # zip(['a','b','c'], [666, 'X', -13]) ==  [('a',666), ('b','X'), ('c',-13)]
    for header, cell in zip(HEADERS, row.find_all('td', recursive=False)):
        # recursive=False means: don't look for nested td's
        tmp_dict[header] = cell.text.strip()  # "  XYZ\n\n \t".strip() == "XYZ"
    data.append(tmp_dict)  # add just processed row to our resulting list

f = open(FILENAME, 'wb')  # open the file in binary writing mode (or create if not existing yet)

# that's the guy that knows how to translate python objects to csv files
w = csv.writer(f, encoding='utf-8')
w.writerow(HEADERS)  # the headers have to be written manually

for x in data:  # take each computed row
    w.writerow(x.values())  # {'a': 5, 13: 'lol'}.values() == (5, 'lol')
f.close()  # we have to close the file handler to make sure that the write buffer is flushed
