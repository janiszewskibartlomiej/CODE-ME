# Bartłomiej Janiszewski

import time
import random
from datetime import datetime


def timer_dekorator(funkcja):
    def run():
        first = datetime.now()
        funkcja()
        second = datetime.now()
        print(f'Czas wykonania: {second - first}')

    return run


@timer_dekorator
def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    przykladowa_funkcja()
