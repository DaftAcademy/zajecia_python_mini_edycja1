#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

from app import db, app, CpuStats
from utils import get_cpu_stats


def gather_cpu_data():
    print 'Collecting CPU data...'
    cpu_loads = get_cpu_stats(app.config['CPU_SAMPLER_TIME'])
    cs = CpuStats(cpu_loads)
    db.session.add(cs)
    db.session.commit()
    db.session.flush()


def create_job(interval, func, *args, **kargs):
    stopped_e = threading.Event()

    def task_main_loop():
        while not stopped_e.wait(interval):
            func(*args, **kargs)

    t = threading.Thread(target=task_main_loop)
    t.start()

    return t, stopped_e

# CPU Gathering Job
cpu_thread, cpu_stop_e = create_job(
    app.config['CPU_GATHER_JOB_INTERVAL'], 
    gather_cpu_data)

print 'Our job started!'

try:
    while True:
        print '...'
        time.sleep(1)
except KeyboardInterrupt:
    cpu_stop_e.set()
    print '\nExiting...'