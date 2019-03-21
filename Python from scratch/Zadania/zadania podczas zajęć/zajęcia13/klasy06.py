class Prostokat:
    def __init__(self, a, b):
        if a > 0 and b > 0:
            self.bok_a = a
            self.bok_b = b
        else:
            raise ValueError('Jeden z boków jest mniejszy lub równy zero.')

    def __repr__(self):
        return f'Prostokąt o bokach {self.bok_a} i {self.bok_b}'


if __name__ == '__main__':
    p = Prostokat(5, 6)
    print(p)

    p = Prostokat(3, -2)
    print(p)
