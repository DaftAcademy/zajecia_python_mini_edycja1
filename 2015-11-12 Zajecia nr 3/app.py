# -*- coding: utf-8 -*-

import datetime
import requests

import matplotlib.pyplot as plt


BASE_URL = u'http://api.fixer.io/{0}'

BASE_CURRENCY = u'PLN'
CURRENCIES = u'EUR,USD'



def gather_data(start_date, tick):
    curr_date = start_date
    params = {
        'base': BASE_CURRENCY,
        'symbols': CURRENCIES,
    }

    today = datetime.date.today()
    data = dict()

    while curr_date <= today:
        url = BASE_URL.format(curr_date)
        res = requests.get(url, params=params)
        res_json = res.json()

        for k, v in res_json['rates'].items():
            if k not in data:
                data[k] = {
                    'x': list(),
                    'val': list(),
                }
            data[k]['x'].append(curr_date)
            data[k]['val'].append(v)
        curr_date += tick
    return data

def show_graph(data, rotation=None):
    lines = list()
    for currency, d in data.items():
        lines.append(plt.plot(d['x'], d['val'])[0])

    plt.legend(lines, data.keys(), loc='upper right', shadow=True)

    if rotation:
        plt.xticks(rotation=rotation)
    plt.xlabel('time')
    plt.ylabel('val')
    plt.title('Wykres nas piekny')

    plt.show()

data = gather_data(
    start_date=datetime.date(year=2015, month=1, day=1),
    tick=datetime.timedelta(days=14),
)
show_graph(data, rotation=45)

