import random
import time


def ramka(funkcja):
    def wrapper():
        print('-----------------------------------')
        funkcja()
        print('-----------------------------------\n')

    return wrapper


def obliczenia():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    udekorowane_obliczenia = ramka(obliczenia)
    udekorowane_obliczenia()

    udekorowane_obliczenia()

    udekorowane_obliczenia()
