from iter02 import ParzysteLiczby


p_licz = ParzysteLiczby()

print(next(p_licz))
print(next(p_licz))
print(p_licz.__next__())  # tak się raczej nie pisze kodu

print(list(p_licz))

# print(next(p_licz))  # to rzuci wyjątek
