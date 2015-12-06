# -*- coding: utf-8 -*-

import timeit

BENCH_NUM = 10000
COUNT = 1


def test_func():
    global COUNT
    print 'lol: {}'.format(COUNT)
    COUNT += 1


res = timeit.timeit(
    'test_func()', 
    setup='from __main__ import test_func',
    number=BENCH_NUM,
)

print res