# tutaj wpisz swoje imię i nazwisko

import time
import random


def timer_dekorator(funkcja):
    pass


@timer_dekorator
def przykladowa_funkcja():
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()


if __name__ == '__main__':
    przykladowa_funkcja()
