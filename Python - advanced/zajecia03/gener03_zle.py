def trzy_liczby():
    for element in [13, 17, 19]:
        yield element

if __name__ == '__main__':

    print(next(trzy_liczby()))
    print(next(trzy_liczby()))
    print(next(trzy_liczby()))

    # Powyżej stworzyliśmy trzy odrębne generatory i z każdego wzięliśmy pierwszy element
