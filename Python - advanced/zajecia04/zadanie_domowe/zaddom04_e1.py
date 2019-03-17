# Bartłomiej Janiszewski

import time
from datetime import datetime
import random


def timer(funkcja):
    t = datetime.now()
    funkcja()
    n = datetime.now()


    return print(f'\nCzas wykonania: {n - t}')


def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    # przykladowa_funkcja()
    timer(przykladowa_funkcja)
