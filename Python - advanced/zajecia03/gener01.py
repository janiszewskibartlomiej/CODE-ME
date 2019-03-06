def parzyste_liczby():
    liczba = 0
    while liczba < 100:
        liczba += 2
        yield liczba


if __name__ == '__main__':

    p_licz = parzyste_liczby()

    # print(type(p_licz))

    for liczba in p_licz:
        print(liczba)
