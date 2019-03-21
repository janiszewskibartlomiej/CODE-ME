class Prostokat:
    def __init__(self, a, b):
        self.bok_a = a
        self.bok_b = b


p = Prostokat(5, 6)
print(p)

pole = p.bok_a * p.bok_b
print(pole)

p.bok_a = 11
pole = p.bok_a * p.bok_b
print(pole)

