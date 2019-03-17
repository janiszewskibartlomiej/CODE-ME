# Bartłomiej Janiszewski

import time
from datetime import datetime
import random


def timer(funkcja):
    pass


def przykladowa_funkcja():
    t = datetime.now()
    print('\n',t)
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    n = datetime.now()
    print('\n',n)
    delta = n - t
    print(f'\nCzas wykonania: {delta}')


if __name__ == '__main__':
    timer(przykladowa_funkcja())


