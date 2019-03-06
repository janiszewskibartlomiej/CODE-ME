def trzy_liczby_z_vatem():
    for element in [13, 17, 19]:
        yield element * 1.23

if __name__ == '__main__':

    tl = trzy_liczby_z_vatem()

    print(type(tl))

    print(next(tl))
    print(next(tl))
    print(next(tl))
