from random import sample


def chybil_trafil():
    zbior = range(1, 20)
    cztery_liczby = sample(zbior, k=4)
    return sorted(cztery_liczby)


wynik = chybil_trafil()

if __name__ == '__main__':
    print('Wylosowane liczby to: ', wynik)
