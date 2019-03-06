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

    next(odl)  # to, że wywołanie next() daje nam kolejną wartość, to nie znaczy, że musimy ją wykorzystać
    next(odl)
    next(odl)
    next(odl)
    # next(odl)
