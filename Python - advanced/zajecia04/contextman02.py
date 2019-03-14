class Kultura:
    def __enter__(self):
        print('Dzień dobry')

    def __exit__(self, *args):
        print('Do widzenia')


with Kultura():
    a = 3
    b = 7
    print(a + b)
