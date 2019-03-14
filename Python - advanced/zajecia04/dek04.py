import random
import time


def ramka(funkcja):
    def wrapper(trudnosc):
        print('-----------------------------------')
        funkcja(trudnosc)
        print('-----------------------------------')

    return wrapper

@ramka
def obliczenia(trudnosc=5):
    # ta funkcja nie robi nic pożytecznego
    print('liczę', end='')
    for _ in range(trudnosc):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('obliczyłem! wynik to: ', random.randint(10, 100))


if __name__ == '__main__':
    obliczenia(10)
    print()  # oddzielenie pustą linią
    obliczenia(7)
    print()
    obliczenia(2)
