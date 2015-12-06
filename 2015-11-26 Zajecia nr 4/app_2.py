# -*- coding: utf-8 -*-

import timeit

BENCH_NUM = 1000
REPEAT_NUM = 100


def range_test():
    for x in range(1000):
        pass

def xrange_test():
    for x in xrange(1000):
        pass


range_res_min = min(timeit.repeat(
    'range_test()', 
    setup='from __main__ import range_test',
    number=BENCH_NUM,
    repeat=REPEAT_NUM,
))

xrange_res_min = min(timeit.repeat(
    'xrange_test()', 
    setup='from __main__ import xrange_test',
    number=BENCH_NUM,
    repeat=REPEAT_NUM,
))

print 'Range min res: {}'.format(range_res_min)
print 'Xrange min res: {}'.format(xrange_res_min)
