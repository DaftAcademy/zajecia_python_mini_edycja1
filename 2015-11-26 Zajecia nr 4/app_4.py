# -*- coding: utf-8 -*-

import timeit
import random

import numpy as np


BENCH_NUM = 50
REPEAT_NUM = 10

SETUP = '''
from __main__ import native_test, numpy_test

x = 500
y = 500
'''

def native_test(x_size, y_size):
    qwe = [[random.random() for y in xrange(y_size)] for x in xrange(x_size)]
    qwe_multiplied = [[y*5. for y in x] for x in qwe]
    return qwe_multiplied


def numpy_test(x_size, y_size):
    qwe = np.random.random((x_size, y_size))
    qwe_multiplied = qwe * 5.
    return qwe_multiplied


def _run_test(command):
    min_test_time = min(timeit.repeat(
        command, 
        setup=SETUP,
        number=BENCH_NUM,
        repeat=REPEAT_NUM,
    ))

    print 'Time for {}: {}'.format(
        command, min_test_time)

_run_test('native_test(x,y)')
_run_test('numpy_test(x,y)')