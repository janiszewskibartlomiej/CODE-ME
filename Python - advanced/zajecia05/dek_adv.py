import random
import time

def ustaw_znak(znak='-'):
    def ramka(funkcja):
        def wrapper():
            print(znak * 35)
            funkcja()
            print(znak * 35)

        return wrapper
    return ramka

@ustaw_znak('#')
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
