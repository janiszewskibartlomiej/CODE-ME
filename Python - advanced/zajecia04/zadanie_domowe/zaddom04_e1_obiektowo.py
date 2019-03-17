# Bartłomiej Janiszewski

import time
from datetime import datetime
import random


class Timer:
    def __enter__(self):
        self.t = datetime.now()
        timer(przykladowa_funkcja())
        return self.t

    def __exit__(self, *agr):
        self.n = datetime.now()
        delta = self.n - self.t
        return  print(f'Czas wykonania: {delta}')



def timer(funkcja):
    return



def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    with Timer() as t:
        print()


