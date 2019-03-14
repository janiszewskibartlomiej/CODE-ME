import random
import time


def ramka(funkcja):
    def wrapper():
        print('-----------------------------------')
        funkcja()
        print('-----------------------------------')

    return wrapper

def ramka2(funkcja):
    def wrapper():
        print('===================================')
        funkcja()
        print('===================================')

    return wrapper

@ramka
@ramka2
def obliczenia():
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    obliczenia()
    print()  # oddzielenie pustą linią
    obliczenia()
    print()
    obliczenia()
