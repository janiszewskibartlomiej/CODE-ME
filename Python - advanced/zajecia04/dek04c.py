import random
import time


def ramka(funkcja):
    def wrapper(*args):
        print('-----------------------------------')
        funkcja(*args)
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


@ramka
def drukuj_argumenty(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    obliczenia(4)
    print()  # oddzielenie pustą linią

    drukuj_argumenty('dzień')
    drukuj_argumenty('dzień', 'dobry')
    drukuj_argumenty('dzień', 'dobry', 'Python!')
