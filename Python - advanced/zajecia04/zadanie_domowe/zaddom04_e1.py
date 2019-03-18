# Bartłomiej Janiszewski

import time
from datetime import datetime
import random


def timer(funkcja):
    first = datetime.now()
    funkcja()
    second = datetime.now()
    print(f'Czas wykonania: {second - first}')


def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    # przykladowa_funkcja()
    timer(przykladowa_funkcja)
