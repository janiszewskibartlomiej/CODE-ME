class Kwadrat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __bool__(self):   # tu możemy żąglować True and False, możemy
        # tu przekazywać różne żeczy nawet zapisywanie do logów
        if self.a == self.b:
            return True
        else:
            print('ccccc')
            return False


if __name__ == '__main__':
    dobry_kwadrat = Kwadrat(7, 7)

    print(dobry_kwadrat)
    print(bool(dobry_kwadrat))

    zly_kwadrat = Kwadrat(3, 5)

    if zly_kwadrat:
        print('zrób coś z kwadratem')
    else:
        print('coś jest nie tak z twoim kwadratem :/')
