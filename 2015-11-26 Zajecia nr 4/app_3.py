# -*- coding: utf-8 -*-

import timeit

BENCH_NUM = 1000
REPEAT_NUM = 100

input = [1,2,3,4]

SETUP = '''
from __main__ import test_iter, test_map, test_compr

words_list = u'Apply function to every item of iterable and return a list of the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel.'.split(' ')
'''

def test_iter(words):
    out = list()
    for word in words:
        out.append(word.capitalize())
    return out

def test_map(words):
    return map(unicode.capitalize, words)

def test_compr(words):
    return [ x.capitalize() for x in words ]



def _run_test(command):
    min_test_time = min(timeit.repeat(
        command, 
        setup=SETUP,
        number=BENCH_NUM,
        repeat=REPEAT_NUM,
    ))

    print 'Time for {}: {}'.format(
        command, min_test_time)


_run_test('test_iter(words_list)')
_run_test('test_map(words_list)')
_run_test('test_compr(words_list)')

