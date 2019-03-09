# Bartłomiej Janiszewski

liczby = [91111, -7108079251, 405883740, 7942725602, 345220, 2915371507, 30, 9438104, 5736286, 984, 0]


def ile_cyfr(liczby):
    liczby_rm = [rm for rm in liczby if rm >=0]
    points = [str(element) for element in liczby_rm]
    string_with_len = [i +' ({} cyfr)'.format(len(i)) for i in points]
    return string_with_len


if __name__ == '__main__':
    print(ile_cyfr(liczby))
