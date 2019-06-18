# https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt


def funkcja_liniowa(a, b):
    return lambda x: a * x + b


def funkcja_kwadratowa(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f1 = funkcja_kwadratowa(1, 1, 1)

x = list(range(-10, 10))
y = [f1(x) for x in x]

# spróbuj wyrysować dwie funkcje na jednym wykresie
plt.plot(x, y, 'r--')
plt.plot(x, y, 'o')

plt.xlabel('x')
plt.ylabel('y')

plt.show()
