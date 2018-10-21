from random import sample

def chybil_trafil():
    zbior = range(1, 20)
    cztery_liczby = sample(zbior, k=4)
    return sorted(cztery_liczby)


def dodaj_zaklad(zaklad, wszystkie_zaklady):
    wszystkie_zaklady.append(zaklad)
    return


def czy_jest_zwyciezca(zwycieskie_liczby, wszystkie_zaklady):
    if zwycieskie_liczby in wszystkie_zaklady:
        print('Mamy zwycięzcę I stopnia, który poprawnie skreślił liczby: ', zwycieskie_liczby)
    else:
        print('Tym razem nie ma zwycięzcy')


# print(chybil_trafil())
#
# dodaj_zaklad([1, 2, 3, 4])
# print(wszystkie_zaklady)
#
# czy_jest_zwyciezca([1, 2, 3, 4])
