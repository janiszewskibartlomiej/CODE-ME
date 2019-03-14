class Kultura:
    def __enter__(self):
        print('Dzień dobry')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Nastąpił wyjątek:')
            print('Nazwa:', exc_type.__name__)
            print('Przekazana wartość:', exc_val)
            print('Błąd w linii:', exc_tb.tb_lineno)
        print('Do widzenia')


with Kultura():
    a = 3
    b = 7
    raise NotImplementedError('Poważny błąd!')
    print(a + b)  # ta linia nie zostanie wykonana
