# -*- coding: utf-8 -*-

import psutil
import hurry.filesize



def get_cpu_stats():
    return psutil.cpu_percent(interval=1, percpu=True)


def get_memory_stats():
    _size = hurry.filesize.size

    virt = psutil.virtual_memory()
    swap = psutil.swap_memory()

    memory_data = {
        'virtual': {
            'avail': _size(virt.free),
            'total': _size(virt.total),
            'percent': virt.percent,
        },
        'swap': {
            'avail': _size(swap.free),
            'total': _size(swap.total),
            'percent': swap.percent,
        },
    }

    return memory_data


def get_process_list():
    process_list = list()
    for p in psutil.process_iter():
        try:
            process_list.append(
                [
                    p.pid,
                    p.name(),
                    p.status(),
                    p.username(),
                ]
            )
        except psutil.ZombieProcess:
            continue
    return process_list