# etap pierwszy

from random import sample


def chybil_trafil():
    liczby = sample(range(1, 20), k=4)
    return sorted(liczby)


x = chybil_trafil()
if __name__ == '__main__':
    print(x)

# etap drugi

wszystkie_zaklady = []


def dodaj_zaklad(zaklad, wszystkie_zaklady):
    wszystkie_zaklady.append(zaklad)

moj_zaklad = [1, 2, 3, 4]
dodaj_zaklad(moj_zaklad, wszystkie_zaklady)

if __name__ == '__main__':
    print(wszystkie_zaklady)

    print(wszystkie_zaklady)


#etap 3

for r in range(10):
    dodaj_zaklad(chybil_trafil(), wszystkie_zaklady)

if __name__ == '__main__':
    print(wszystkie_zaklady)


#etap 4

def czy_jest_zwyciezca(zwycieskie_liczby, wszystkie_zaklady):
    if zwycieskie_liczby in wszystkie_zaklady:
        print(f'Mamy zwycięzcę I stopnia, który poprawnie skreślił liczby: {zwycieskie_liczby}')
    else:
        print('Tym razem nie ma zwycięzcy')

if __name__ == '__main__':
    czy_jest_zwyciezca(moj_zaklad, wszystkie_zaklady)


