class Prostokat:
    # zmienne klasy, współdzielone między wszsytkimi obiektami
    bok_a = 7
    bok_b = 13


p = Prostokat()
print(p)

pole = p.bok_a * p.bok_b
print(pole)

p.bok_a = 11
pole = p.bok_a * p.bok_b
print(pole)

