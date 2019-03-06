def parzyste_liczby():
    liczba = 0
    while liczba < 100:
        yield liczba
        liczba += 2


if __name__ == '__main__':

    p_licz = parzyste_liczby()

    for liczba in p_licz:
        print(liczba)
