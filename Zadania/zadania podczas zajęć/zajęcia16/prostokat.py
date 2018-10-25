class Prostokat:
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError('Prostokat musi mieć dodatnie boki.')
        self.bok_a = a
        self.bok_b = b

    def __repr__(self):
        return f'Prostokąt o bokach: a={self.bok_a}, b={self.bok_b}'

    def pole(self):
        return self.bok_a * self.bok_b

    def czy_kwadrat(self):
        if self.bok_a == self.bok_b:
            return True
        else:
            return False
