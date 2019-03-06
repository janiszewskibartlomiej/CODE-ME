# porównaj z gener04.py

if __name__ == '__main__':

    tl = (element * 1.23 for element in [13, 17, 19])

    print(type(tl))

    print(next(tl))
    print(next(tl))
    print(next(tl))
