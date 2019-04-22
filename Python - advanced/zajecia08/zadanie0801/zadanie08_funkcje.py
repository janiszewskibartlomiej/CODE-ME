def policz_linie(s):
    return len(s.split('\n'))


def policz_wyrazy(s):
    return sum([len(x.split()) for x in s.split('\n')])


def policz_bajty(s):
    return len(s)
