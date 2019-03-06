def fibo():
    a = 0
    b = 1

    yield a
    yield b

    while True:
        yield a + b
        a, b = b, a + b


if __name__ == '__main__':
    f = fibo()

    for _ in range(10):
        print(next(f))
