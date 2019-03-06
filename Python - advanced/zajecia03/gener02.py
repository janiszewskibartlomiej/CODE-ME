def odliczanie():
    print('rozpoczynam odliczanie!')

    yield 3
    yield 2
    yield 1

    print('i ostatnie moje słowo...')

    yield 0

    print('odliczanie się już skończyło')


if __name__ == '__main__':
    odl = odliczanie()

    print(next(odl))
    print(next(odl))
    print(next(odl))
    print(next(odl))
    print(next(odl))
