# funkcja, która nie przyjmuje parametrów i ale zwraca wartość


def odpowiedz_na_wielkie_pytanie():
    # https://pl.wikipedia.org/wiki/Wielkie_pytanie_o_%C5%BCycie,_wszech%C5%9Bwiat_i_ca%C5%82%C4%85_reszt%C4%99
    return 42


komunikat = 'Odpowiedź na "Wielkie pytanie o życie, wszechświat ' \
            'i całą resztę" to: {}'.format(odpowiedz_na_wielkie_pytanie())

print(komunikat)
