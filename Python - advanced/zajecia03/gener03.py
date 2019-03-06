def trzy_liczby():
    for element in [13, 17, 19]:
        yield element

if __name__ == '__main__':

    tl = trzy_liczby()

    print(type(tl))

    print(next(tl))
    print(next(tl))
    print(next(tl))
