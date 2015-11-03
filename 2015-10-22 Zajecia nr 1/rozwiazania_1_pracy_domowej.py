# -*- coding: utf-8 -*-
import requests
import hashlib
import time

import unicodecsv as csv

from bs4 import BeautifulSoup
from collections import OrderedDict
from lxml import html


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        method(*args, **kw)
        te = time.time()

        return '%2.2f sec' % (te - ts)

    return timed


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

response = requests.get('http://www.bankier.pl/fundusze/notowania/wszystkie')
response.encoding = 'utf-8'

@timeit
def balor(response, filename):
    html_doc = response.text  # that's the decoded content of the response

    # parse the contents as a HTML
    soup = BeautifulSoup(html_doc, 'html.parser')
    # look for tables with specified class. Take the first one (0-based
    # indices).
    table = soup.find_all('table', class_='sortTableMixedData')[0]

    data = list()  # we could also write: data = []

    for row in table.find_all('tr'):  # take the data from one row at a time
        # we will extract the row data into this dictionary
        tmp_dict = OrderedDict()

        for header, cell in zip(HEADERS, row.find_all('td', recursive=False)):
            # recursive=False means: don't look for nested td's
            # "  XYZ\n\n \t".strip() == "XYZ"
            tmp_dict[header] = cell.text.strip()
        data.append(tmp_dict)  # add just processed row to our resulting list

    # open the file in binary writing mode (or create if not existing yet)
    f = open(filename, 'wb')

    # that's the guy that knows how to translate python objects to csv files
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)  # the headers have to be written manually

    for x in data:  # take each computed row
        w.writerow(x.values())  # {'a': 5, 13: 'lol'}.values() == (5, 'lol')
    # we have to close the file handler to make sure that the write buffer is
    # flushed
    f.close()


@timeit
def webster58(response, filename):
    index1 = response.text.find('<tbody')
    index2 = response.text.find('</tbody>')
    soup = BeautifulSoup(response.text[index1:index2], 'lxml')

    def func(r):
        return map(lambda x: x.get('data-value', x.text).strip(),
                   r.find_all('td', recursive=0))

    trs = soup.find('tbody').find_all('tr', recursive=0)

    with open(filename, 'wb') as f:
        w = csv.writer(f, encoding='utf-8')
        w.writerow(HEADERS)
        w.writerows(map(func, filter(lambda x: x.attrs.get('class') is None,
                                     trs)))


@timeit
def grzeszczak_maciej(response, filename):
    soup = BeautifulSoup(response.text, 'html.parser')
    headers = [e.text[:e.text.find(" AD")].strip()
               for e in soup.find_all('th')]
    with open(filename, 'w') as f:
        w = csv.writer(f, encoding='utf-8')
        w.writerow(headers)
        for row in soup.find_all('table', 'sortTableMixedData')[0].find_all('tr'):
            r = row.find_all('td')
            if len(r) != len(headers):
                continue
            w.writerow([td.text.strip() if ind != len(
                headers) - 1 else td['data-value'] for ind, td in enumerate(r)])


@timeit
def guzek_jakub(response, filename):

    html_doc = response.text

    soup = BeautifulSoup(html_doc, 'html.parser')
    table = soup.find_all('table', class_='sortTableMixedData')[0]

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)

    for row in table.findAll('tr'):
        if row.get("class") != None:
            continue
        tmp_dict = OrderedDict()
        for header, cell in zip(HEADERS, row.findAll('td', recursive=False)):
            tmp_dict[header] = cell.text.strip()
            if (cell.get("data-value")) != None:
                tmp_dict[header] = cell.get("data-value")
        if tmp_dict.values():
            w.writerow(tmp_dict.values())

    f.close()


@timeit
def kwiecinski_mateusz(response, filename):

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    table = soup.find_all('table', class_='sortTableMixedData')[0]

    data2 = list()
    for row in table.find_all('tr'):
        rowData = list()
        for column in row.select('td[data-value]'):
            column.string = column['data-value']
        for cell in row.find_all('td', recursive=False):
            rowData.append(cell.text.strip())
        if len(rowData) == 11:
            data2.append(rowData)

    f = open(filename, 'wb')

    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)
    for x in data2:
        w.writerow(x)
    f.close()


@timeit
def plebanski_michal(response, filename):

    html_doc = response.text
    # wycinam z danych tylko tabele
    index1 = html_doc.find('<table class="sortTableMixedData')
    index2 = html_doc.find('</table>', index1)
    # parser zmieniony na szybszy
    soup = BeautifulSoup(html_doc[index1:index2], 'lxml')

    data = list()
    for row in soup.find_all('tr'):
        tmp_list = []  # lista jest szybsza
        tmp_data = row.find_all('td', recursive=False)
        if(len(tmp_data) == 11):  # usuwa puste pola w excelu
            for cell in tmp_data[0:10]:  # tak naprawde [0:9] -> pydoc
                tmp_list.append(cell.text.strip())
            tmp_list.append(tmp_data[10]['data-value'])
            data.append(tmp_list)
        else:
            continue

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)

    for x in data:
        w.writerow(x)  # usuwam .values() specyficzne dla slownika

    f.close()


@timeit
def wasniowska_magda(response, filename):
    soup = BeautifulSoup(response.text, 'html.parser')

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    table = soup.find_all('table', class_='sortTableMixedData')[0]
    ifHeader = True
    cells = []

    for row in table.findAll('tr', {'class': ''}):
        if(ifHeader):
            ifHeader = False
            for cell in row.find_all('th', recursive=False):
                s = cell.text.find('AD')
                cells.append(cell.text[:s - 1].strip())
        else:
            for cell in row.find_all('td', recursive=False):
                if(cell.has_attr('data-value')):
                    cells.append(cell['data-value'])
                else:
                    cells.append(cell.text.strip())
        w.writerow(cells)
        del cells[:]

    f.close()


@timeit
def puchalski_pawel_bs1(response, filename):

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    # We can do that because there are only one table at webpage
    td = soup.find_all('td')
    data = []
    temp_data = []

    for tag in td:  # We'll check every cell
        try:
            tempString = tag.string.strip()
            temp_data.append(tempString)
            # if tag.string.strip() == '-' then we know we're in rank section of
            # table and next cell should be in new row
            if tempString == '-':
                data.extend([temp_data])  # Now we have full row
                temp_data = []
        # if rank section has image in it we need will get AttributeError so we're
        # checking 'data-value' of this <td> tag
        except AttributeError:
            try:
                temp_data.append(tag['data-value'])  # We have full row now
                data.extend([temp_data])
                temp_data = []  # starting over and over again
            # Yup there's some weird <iframe> we want to ignore
            except KeyError:
                pass

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)
    w.writerows(data)
    f.close()


@timeit
def puchalski_pawel_bs2(response, filename):

    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # We can do that because there are only one table at webpage
    td = soup.find_all('td')

    # get Key of attribute 'default-key' if there's no attribute return string
    # of las child
    data = [cell.get('data-value', default=cell.get_text(strip=True))
            for cell in td]
    # There was one <iframe> tag that we need to clear
    data = filter(None, data)
    # chunk one big list into list of lists
    data = [data[x:x + 11] for x in xrange(0, len(data), 11)]

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)
    w.writerows(data)
    f.close()


@timeit
def puchalski_pawel_lxml(response, filename):

    tree = html.fromstring(response.text)  # Parse the html

    data = []
    # Search all nodes that ends with <td><a></a></td>
    data.extend([tree.xpath("//td/a/text()")])
    i = 2
    while i != 1:
        # Search every i'th <td> node
        path = "//td[position() mod 10 = %s]/text()" % (i)
        data.extend([tree.xpath(path)])
        i = (i + 1) % 10
    # Find values of attribute "data-value" in <td> node
    data.extend([tree.xpath("//td/@data-value")])

    data = zip(*data)  # Transpose our list

    f = open(filename, 'wb')
    w = csv.writer(f, encoding='utf-8')
    w.writerow(HEADERS)
    w.writerows(data)
    f.close()


reference_file = "reference.csv"
webster58(response, reference_file)

original_md5 = hashlib.md5(open(reference_file, 'rb').read()).hexdigest()


def chceck_validity(filename, reference_md5):
    with open(filename) as file_to_check:
        data = file_to_check.read()
        return reference_md5 == hashlib.md5(data).hexdigest()


def run(name):
    filename = '{}.csv'.format(name)
    time = getattr(__import__('__main__'), name)(response, filename)
    validity = chceck_validity(filename, original_md5)
    print time, '-', validity, '-', name


run('balor')
run('webster58')
run('grzeszczak_maciej')
run('guzek_jakub')
run('kwiecinski_mateusz')
run('plebanski_michal')
run('wasniowska_magda')
run('puchalski_pawel_bs1')
run('puchalski_pawel_bs2')
run('puchalski_pawel_lxml')
