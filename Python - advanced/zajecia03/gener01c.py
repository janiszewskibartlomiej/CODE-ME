def co_druga_liczba(start=0):
    liczba = start
    while liczba < 100:
        yield liczba
        liczba += 2


if __name__ == '__main__':

    liczby = co_druga_liczba(29)

    print(list(liczby))
