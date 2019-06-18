import matplotlib.pyplot as plt


def funkcja_kwadratowa(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f1 = funkcja_kwadratowa(-1, 2, -10)

zbior_x = list(range(-10, 10))
print(zbior_x)

zbior_y = [f1(x) for x in zbior_x]
print(zbior_y)

plt.plot(zbior_x, zbior_y)

plt.show()
