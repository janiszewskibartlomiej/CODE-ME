# Bartłomiej Janiszewski

from zaddom02_e1 import TaliaKart


def rozdaj_karty(talia, ile_kart=1):
    lista_kart = []

    if ile_kart <= 0:
        lista_kart

    if ile_kart == 1:
        lista_kart.append(talia)

    # if 53 > ile_kart > 1:
    #     for element in range(ile_kart):
    #         lista_kart.append(talia)

    if ile_kart > 1:

        try:
            for element in range(ile_kart):

                lista_kart.append(next(talia))

        except StopIteration:
            lista_kart

    return lista_kart


if __name__ == '__main__':
    talia = TaliaKart()

    gracz1 = rozdaj_karty(talia, 14)
    gracz2 = rozdaj_karty(talia, 14)
    gracz3 = rozdaj_karty(talia, 14)
    gracz4 = rozdaj_karty(talia, 14)

    print(gracz1)
    print(gracz2)
    print(gracz3)
    print(gracz4)
